import os
import sys
import logging
import pkgutil
import importlib.machinery
import importlib.util
import types
import shutil
import traceback
import platform
from pathlib import Path
from subprocess import Popen
from subprocess import PIPE
from subprocess import STDOUT
from abc import ABC
from abc import abstractmethod
import argparse
import requests
import jsonpickle
from tqdm import tqdm
from zipfile import ZipFile
from distutils.dir_util import mkpath
import operator
import re

######## START CONTENT ########
class ActualType(type):
    def __repr__(self):
        return self.__name__



class MissingArgumentError(Exception, metaclass=ActualType):
    pass



class UserFunctorError(Exception, metaclass=ActualType):
    pass
    
class CommandUnsuccessful(UserFunctorError, metaclass=ActualType):
    pass



class ErrorResolutionError(Exception, metaclass=ActualType):
    pass

class FailedErrorResolution(ErrorResolutionError, metaclass=ActualType):
    pass



class SelfRegisteringError(Exception, metaclass=ActualType):
    pass

class ClassNotFound(SelfRegisteringError, metaclass=ActualType):
    pass



class HelpWanted(Exception, metaclass=ActualType):
    pass

class HelpWantedWithRegistering(HelpWanted, metaclass=ActualType):
    pass



class Fatal(Exception, metaclass=ActualType):
    pass

class FatalCannotExecute(Fatal, metaclass=ActualType):
    pass



class PackageError(Exception, metaclass=ActualType):
    pass

#Self registration for use with json loading.
#Any class that derives from SelfRegistering can be instantiated with:
#   SelfRegistering("ClassName")
#Based on: https://stackoverflow.com/questions/55973284/how-to-create-this-registering-factory-in-python/55973426
class SelfRegistering(object):

    class ClassNotFound(Exception): pass

    def __init__(this, *args, **kwargs):
        #ignore args.
        super().__init__()

    @classmethod
    def GetSubclasses(cls):
        for subclass in cls.__subclasses__():
            # logging.info(f"Subclass dict: {subclass.__dict__}")
            yield subclass
            for subclass in subclass.GetSubclasses():
                yield subclass

    @classmethod
    def GetClass(cls, classname):
        for subclass in cls.GetSubclasses():
            if subclass.__name__ == classname:
                return subclass

        # no subclass with matching classname found (and no default defined)
        raise ClassNotFound(f"No known SelfRegistering class: {classname}")            

    #TODO: How do we pass args to the subsequently called __init__()?
    def __new__(cls, classname, *args, **kwargs):
        toNew = cls.GetClass(classname)
        logging.debug(f"Creating new {toNew.__name__}")

        # Using "object" base class method avoids recursion here.
        child = object.__new__(toNew)

        #__dict__ is always blank during __new__ and only populated by __init__.
        #This is only useful as a negative control.
        # logging.debug(f"Created object of {child.__dict__}")

        return child

    @staticmethod
    def RegisterAllClassesInDirectory(directory):
        logging.debug(f"Loading SelfRegistering classes in {directory}")
        logging.debug(f"Available modules: {os.listdir(directory)}")
        for file in os.listdir(directory):
            if (file.startswith('_') or not file.endswith('.py')):
                continue

            moduleName = file.split('.')[0]

            # logging.debug(f"Attempting to registering classes in {moduleName}.")
            loader = importlib.machinery.SourceFileLoader(moduleName, os.path.join(directory, file))
            module = types.ModuleType(loader.name)
            loader.exec_module(module)

            # NOTE: the module is not actually imported in that it is available through sys.modules.
            # However, this appears to be enough to get both inheritance and SelfRegistering functionality to work.
            sys.modules[moduleName] = module #But just in case...
            logging.debug(f"{moduleName} imported.")

            #### Other Options ####
            # __import__(module)
            # OR
            # for importer, module, _ in pkgutil.iter_modules([directory]):
            #     importer.find_module(module).exec_module(module) #fails with "AttributeError: 'str' object has no attribute '__name__'"
            #     importer.find_module(module).load_module(module) #Deprecated

        # enable importing and inheritance for SelfRegistering classes
        if (directory not in sys.path):
            sys.path.append(directory)

def INVALID_NAME():
    return "INVALID_NAME"


# A Datum is a base class for any object-oriented class structure.
# This class is intended to be derived from and added to.
# The members of this class are helpful labels along with the ability to invalidate a datum.
class Datum(SelfRegistering):

    # Don't worry about this.
    # If you really want to know, look at SelfRegistering.
    def __new__(cls, *args, **kwargs):
        return object.__new__(cls)

    def __init__(this, name=INVALID_NAME(), number=0):
        # logging.debug("init Datum")

        # Names are generally useful.
        this.name = name

        # Storing validity as a member makes it easy to generate bad return values (i.e. instead of checking for None) as well as manipulate class (e.g. each analysis step invalidates some class and all invalid class are discarded at the end of analysis).
        this.valid = True 

    # Override this if you have your own validity checks.
    def IsValid(this):
        return this.valid == True

    # Sets valid to true
    # Override this if you have members you need to handle with care.
    def MakeValid(this):
        this.valid = True

    # Sets valid to false.
    def Invalidate(this):
        this.valid = False

#from .Executor import Executor # don't import this, it'll be circular!

# @recoverable
# Decorating another function with this method will engage the error recovery system provided by *this.
# To use this, you must define a GetExecutor() method in your class and decorate the functions you want to recover from.
# For more info, see Executor.ResolveError and the README.md
def recoverable(function):
    def method(obj, *args, **kwargs):
        return RecoverableImplementation(obj, obj.GetExecutor(), function, *args, **kwargs)
    return method


# This needs to be recursive, so rather than having the recoverable decorator call or decorate itself, we just break the logic into this separate method.
def RecoverableImplementation(obj, executor, function, *args, **kwargs):
    try:
        return function(obj, *args, **kwargs)
    except FailedErrorResolution as fatal:
        raise fatal
    except Exception as e:
        if (not executor.resolveErrors):
            raise e

        logging.warning(f"Got error '{e}' from function ({function}) by {obj.name}.")

        # We have to use str(e) instead of pointers to Exception objects because multiple Exceptions will have unique addresses but will still be for the same error, as defined by string comparison.
        if (str(e) not in executor.errorResolutionStack.keys()):
            executor.errorResolutionStack.update({str(e):[]})

        # ResolveError should be the only method which adds to executor.errorResolutionStack.
        # ResolveError is itself @recoverable.
        # So, each time we hit this point, we should also hit a corresponding ClearErrorResolutionStack() call. 
        # If we do not, an exception is passed to the caller; if we do, the stack will be cleared upon the last resolution.
        executor.errorRecursionDepth = executor.errorRecursionDepth + 1

        if (executor.errorRecursionDepth > len(executor.errorResolutionStack.keys())+1):
            raise FailedErrorResolution(f"Hit infinite loop trying to resolve errors. Recursion depth: {executor.errorRecursionDepth}; STACK: {executor.errorResolutionStack}.")

        for i, res in enumerate(executor.resolveErrorsWith):

            logging.debug(f"Checking if {res} can fix '{e}'.")
            if (not executor.ResolveError(e, i)): # attempt to resolve the issue; might cause us to come back here with a new error.
                # if no resolution was attempted, there's no need to re-run the function.
                continue
            try:
                logging.debug(f"Trying function ({function}) again after applying {res}.")
                ret = function(obj, *args, **kwargs)
                executor.ClearErrorResolutionStack() # success!
                logging.info(f"{res} successfully resolved '{e}'!")
                return ret
            except Exception as e2:
                logging.debug(f"{res} failed with '{e2}'; will ignore and see if we can use another ErrorResolution to resolve '{e}'.")
                # Resolution failed. That's okay. Let's try the next.
                # Not all ErrorResolutions will apply to all errors, so we may have to try a few before we get one that works.
                pass

        #  We failed to resolve the error. Die
        raise FailedErrorResolution(f"Tried and failed to resolve: {e} STACK: {executor.errorResolutionStack}.")

# UserFunctor is a base class for any function-oriented class structure or operation.
# This class derives from Datum, primarily, to give it a name but also to allow it to be stored and manipulated, should you so desire.
class UserFunctor(ABC, Datum):

    def __init__(this, name=INVALID_NAME()):
        super().__init__(name)

        # All necessary args that *this cannot function without.
        this.requiredKWArgs = []

        # Static arguments are Fetched when *this is first called and never again.
        # All static arguments are required.
        this.staticKWArgs = []
        this.staticKWArgsValid = False

        # Because values can be Fetched from *this, values that should be provided in arguments will be ignored in favor of those Fetched by a previous call to *this.
        # Thus, we can't enableThis when Fetching required or optional KWArgs (this is done for you in ValidateArgs)
        # If you want an arg to be populated by a child's member, make it static.

        # For optional args, supply the arg name as well as a default value.
        this.optionalKWArgs = {}

        # All external dependencies *this relies on (binaries that can be found in PATH).
        # These are treated as static args (see above).
        this.requiredPrograms = []

        # For converting config value names.
        # e.g. "type": "projectType" makes it so that when calling Set("projectType", ...),  this.type is changed.
        this.configNameOverrides = {}

        # Rolling back can be disabled by setting this to False.
        this.enableRollback = True

        # Numerical result indication the success or failure of *this.
        # Set automatically.
        # 0 is invalid; 1 is best; higher numbers are usually worse.
        this.result = 0

        # Whether or not we should pass on exceptions when calls fail.
        this.raiseExceptions = True

        # Ease of use members
        # These can be calculated in UserFunction and Rollback, respectively.
        this.functionSucceeded = False
        this.rollbackSucceeded = False

    # Override this and do whatever!
    # This is purposefully vague.
    @abstractmethod
    def UserFunction(this):
        raise NotImplementedError 

    # Undo any changes made by UserFunction.
    # Please override this too!
    def Rollback(this):
        pass

    # Override this to check results of operation and report on status.
    # Override this to perform whatever success checks are necessary.
    def DidUserFunctionSucceed(this):
        return this.functionSucceeded

    # RETURN whether or not the Rollback was successful.
    # Override this to perform whatever success checks are necessary.
    def DidRollbackSucceed(this):
        return this.rollbackSucceeded

    # Grab any known and necessary args from this.kwargs before any Fetch calls are made.
    def ParseInitialArgs(this):
        this.os = platform.system()
        if (not isinstance(this, Executor)):
            if ('executor' in this.kwargs):
                this.executor = this.kwargs.pop('executor')
            else:
                logging.warning(f"{this.name} was not given an 'executor'. Some features will not be available.")

    # Convert Fetched values to their proper type.
    # This can also allow for use of {this.val} expression evaluation.
    def EvaluateToType(this, value, evaluateExpression = False):
        if (value is None or value == "None"):
            return None

        if (isinstance(value, dict)):
            ret = {}
            for key, value in value.items():
                ret[key] = this.EvaluateToType(value)
            return ret

        elif (isinstance(value, list)):
            ret = []
            for value in value:
                ret.append(this.EvaluateToType(value))
            return ret

        else:
            if (evaluateExpression):
                evaluatedvalue = eval(f"f\"{value}\"")
            else:
                evaluatedvalue = str(value)

            # Check original type and return the proper value.
            if (isinstance(value, (bool, int, float)) and evaluatedvalue == str(value)):
                return value

            # Check resulting type and return a casted value.
            # TODO: is there a better way than double cast + comparison?
            if (evaluatedvalue.lower() == "false"):
                return False
            elif (evaluatedvalue.lower() == "true"):
                return True

            try:
                if (str(float(evaluatedvalue)) == evaluatedvalue):
                    return float(evaluatedvalue)
            except:
                pass

            try:
                if (str(int(evaluatedvalue)) == evaluatedvalue):
                    return int(evaluatedvalue)
            except:
                pass

            # The type must be a string.
            return evaluatedvalue

    # Wrapper around setattr
    def Set(this, varName, value):
        value = this.EvaluateToType(value)
        for key, var in this.configNameOverrides.items():
            if (varName == key):
                varName = var
                break
        logging.debug(f"Setting ({type(value)}) {varName} = {value}")
        setattr(this, varName, value)


    # Will try to get a value for the given varName from:
    #    first: this
    #    second: the local config file
    #    third: the executor (args > config > environment)
    # RETURNS the value of the given variable or default.
    def Fetch(this,
        varName,
        default=None,
        enableThis=True,
        enableExecutor=True,
        enableArgs=True,
        enableExecutorConfig=True,
        enableEnvironment=True):

        if (enableThis and hasattr(this, varName)):
            logging.debug(f"...got {varName} from self ({this.name}).")
            return getattr(this, varName)

        if (enableArgs):
            for key, val in this.kwargs.items():
                if (key == varName):
                    logging.debug(f"...got {varName} from argument.")
                    return val

        if (not hasattr(this, 'executor')):
            logging.debug(f"... skipping remaining Fetch checks, since 'executor' was not supplied in this.kwargs.")
            return default

        return this.executor.Fetch(varName, default, enableExecutor, enableArgs, enableExecutorConfig, enableEnvironment)
        

    # Override this with any additional argument validation you need.
    # This is called before PreCall(), below.
    def ValidateArgs(this):
        # logging.debug(f"this.kwargs: {this.kwargs}")
        # logging.debug(f"required this.kwargs: {this.requiredKWArgs}")

        if (not this.staticKWArgsValid):
            for prog in this.requiredPrograms:
                if (shutil.which(prog) is None):
                    errStr = f"{prog} required but not found in path."
                    logging.error(errStr)
                    raise UserFunctorError(errStr)

            for skw in this.staticKWArgs:
                if (hasattr(this, skw)): # only in the case of children.
                    continue

                fetched = this.Fetch(skw)
                if (fetched is not None):
                    this.Set(skw, fetched)
                    continue

                # Nope. Failed.
                errStr = f"{skw} required but not found."
                logging.error(errStr)
                raise MissingArgumentError(f"argument {skw} not found in {this.kwargs}")

            this.staticKWArgsValid = True

        for rkw in this.requiredKWArgs:
            # required kwargs must always be fetched in order to allow *this to be called multiple times.
            # if (hasattr(this, rkw)):
            #     continue

            fetched = this.Fetch(rkw, enableThis=False)
            if (fetched is not None):
                this.Set(rkw, fetched)
                continue

            # Nope. Failed.
            errStr = f"{rkw} required but not found."
            logging.error(errStr)
            raise MissingArgumentError(f"argument {rkw} not found in {this.kwargs}")

        for okw, default in this.optionalKWArgs.items():
            # optional kwargs must always be fetched in order to allow *this to be called multiple times.
            # if (hasattr(this, okw)):
            #     continue

            this.Set(okw, this.Fetch(okw, default=default, enableThis=False))

    # Override this with any logic you'd like to run at the top of __call__
    def PreCall(this):
        pass

    # Override this with any logic you'd like to run at the bottom of __call__
    def PostCall(this):
        pass

    # Make functor.
    # Don't worry about this; logic is abstracted to UserFunction
    def __call__(this, **kwargs) :
        logging.debug(f"<---- {this.name} ---->")

        this.kwargs = kwargs
        
        logging.debug(f"{this.name}({this.kwargs})")

        ret = None
        try:
            this.ParseInitialArgs()
            this.ValidateArgs()
            this.PreCall()
            
            ret = this.UserFunction()

            if (this.DidUserFunctionSucceed()):
                    this.result = 1
                    logging.info(f"{this.name} successful!")
            elif (this.enableRollback):
                logging.warning(f"{this.name} failed. Attempting Rollback...")
                this.Rollback()
                if (this.DidRollbackSucceed()):
                    this.result = 2
                    logging.info(f"Rollback succeeded. All is well.")
                else:
                    this.result = 3
                    logging.error(f"Rollback FAILED! SYSTEM STATE UNKNOWN!!!")
            else:
                this.result = 4
                logging.error(f"{this.name} failed.")
            
            this.PostCall()

        except Exception as e:
            if (this.raiseExceptions):
                raise e
            else:
                logging.error(f"ERROR: {e}")
                traceback.print_exc()

        if (this.raiseExceptions and this.result > 2):
            raise UserFunctorError(f"{this.name} failed with result {this.result}")

        logging.debug(f">---- {this.name} complete ----<")
        return ret

    # Adapter for @recoverable.
    # See Recoverable.py for details
    def GetExecutor(this):
        return this.executor

    ######## START: UTILITIES ########

    # RETURNS: an opened file object for writing.
    # Creates the path if it does not exist.
    def CreateFile(this, file, mode="w+"):
        Path(os.path.dirname(os.path.abspath(file))).mkdir(parents=True, exist_ok=True)
        return open(file, mode)

    # Copy a file or folder from source to destination.
    # This really shouldn't be so hard...
    # root allows us to interpret '/' as something other than the top of the filesystem.
    def Copy(this, source, destination, root='/'):
        if (source.startswith('/')):
            source = str(Path(root).joinpath(source[1:]).resolve())
        else:
            source = str(Path(source).resolve())
        
        destination = str(Path(destination).resolve())
        
        Path(os.path.dirname(os.path.abspath(destination))).mkdir(parents=True, exist_ok=True)

        if (os.path.isfile(source)):
            logging.debug(f"Copying file {source} to {destination}")
            try:
                shutil.copy(source, destination)
            except shutil.Error as exc:
                errors = exc.args[0]
                for error in errors:
                    src, dst, msg = error
                    logging.debug(f"{msg}")
        elif (os.path.isdir(source)):
            logging.debug(f"Copying directory {source} to {destination}")
            try:
                shutil.copytree(source, destination)
            except shutil.Error as exc:
                errors = exc.args[0]
                for error in errors:
                    src, dst, msg = error
                    logging.debug(f"{msg}")
        else:
            logging.error(f"Could not find source to copy: {source}")

    # Delete a file or folder
    def Delete(this, target):
        if (not os.path.exists(target)):
            logging.debug(f"Unable to delete nonexistent target: {target}")
            return
        if (os.path.isfile(target)):
            logging.debug(f"Deleting file {target}")
            os.remove(target)
        elif (os.path.isdir(target)):
            logging.debug(f"Deleting directory {target}")
            try:
                shutil.rmtree(target)
            except shutil.Error as exc:
                errors = exc.args[0]
                for error in errors:
                    src, dst, msg = error
                    logging.debug(f"{msg}")

    # Run whatever.
    # DANGEROUS!!!!!
    # RETURN: Return value and, optionally, the output as a list of lines.
    # per https://stackoverflow.com/questions/803265/getting-realtime-output-using-subprocess
    def RunCommand(this, command, saveout=False, raiseExceptions=True):
        logging.debug(f"================ Running command: {command} ================")
        p = Popen(command, stdout=PIPE, stderr=STDOUT, shell=True)
        output = []
        while p.poll() is None:
            line = p.stdout.readline().decode('utf8')[:-1]
            if (saveout):
                output.append(line)
            if (line):
                logging.debug(f"| {line}")  # [:-1] to strip excessive new lines.

        if (p.returncode is not None and p.returncode):
            raise CommandUnsuccessful(f"Command returned {p.returncode}")
        
        logging.debug(f"================ Completed command: {command} ================")
        if (saveout):
            return p.returncode, output
        
        return p.returncode
    ######## END: UTILITIES ########


# A DataContainer allows Data to be stored and worked with.
# This class is intended to be derived from and added to.
# Each DataContainer is comprised of multiple Data (see Datum.py for more).
# NOTE: DataContainers are, themselves Data. Thus, you can nest your child classes however you would like.
class DataContainer(Datum):
    def __init__(this, name=INVALID_NAME()):
        super().__init__(name)
        this.data = []

    # RETURNS: an empty, invalid Datum.
    def InvalidDatum(this):
        ret = Datum()
        ret.Invalidate()
        return ret

    # Sort things! Requires by be a valid attribute of all Data.
    def SortData(this, by):
        this.data.sort(key=operator.attrgetter(by))

    # Adds a Datum to *this
    def AddDatum(this, datum):
        this.data.append(datum)

    # RETURNS: a Datum with datumAttribute equal to match, an invalid Datum if none found.
    def GetDatumBy(this, datumAttribute, match):
        for d in this.data:
            try: # within for loop 'cause maybe there's an issue with only 1 Datum and the rest are fine.
                if (str(getattr(d, datumAttribute)) == str(match)):
                    return d
            except Exception as e:
                logging.error(f"{this.name} - {e.message}")
                continue
        return this.InvalidDatum()

    # RETURNS: a Datum of the given name, an invalid Datum if none found.
    def GetDatum(this, name):
        return this.GetDatumBy('name', name)

    # Removes all Data in toRem from *this.
    # RETURNS: the Data removed
    def RemoveData(this, toRem):
        # logging.debug(f"Removing {toRem}")
        this.data = [d for d in this.data if d not in toRem]
        return toRem

    # Removes all Data which match toRem along the given attribute
    def RemoveDataBy(this, datumAttribute, toRem):
        toRem = [d for d in this.data if str(getattr(d, datumAttribute)) in list(map(str, toRem))]
        return this.RemoveData(toRem)

    # Removes all Data in *this except toKeep.
    # RETURNS: the Data removed
    def KeepOnlyData(this, toKeep):
        toRem = [d for d in this.data if d not in toKeep]
        return this.RemoveData(toRem)

    # Removes all Data except those that match toKeep along the given attribute
    # RETURNS: the Data removed
    def KeepOnlyDataBy(this, datumAttribute, toKeep):
        # logging.debug(f"Keeping only class with a {datumAttribute} of {toKeep}")
        # toRem = []
        # for d in this.class:
        #     shouldRem = False
        #     for k in toKeep:
        #         if (str(getattr(d, datumAttribute)) == str(k)):
        #             logging.debug(f"found {k} in {d.__dict__}")
        #             shouldRem = True
        #             break
        #     if (shouldRem):
        #         toRem.append(d)
        #     else:
        #         logging.debug(f"{k} not found in {d.__dict__}")
        toRem = [d for d in this.data if str(getattr(d, datumAttribute)) not in list(map(str, toKeep))]
        return this.RemoveData(toRem)

    # Removes all Data with the name "INVALID NAME"
    # RETURNS: the removed Data
    def RemoveAllUnlabeledData(this):
        toRem = []
        for d in this.data:
            if (d.name =="INVALID NAME"):
                toRem.append(d)
        return this.RemoveData(toRem)

    # Removes all invalid Data
    # RETURNS: the removed Data
    def RemoveAllInvalidData(this):
        toRem = []
        for d in this.data:
            if (not d.IsValid()):
                toRem.append(d)
        return this.RemoveData(toRem)

    # Removes all Data that have an attribute value relative to target.
    # The given relation can be things like operator.le (i.e. <=)
    #   See https://docs.python.org/3/library/operator.html for more info.
    # If ignoreNames is specified, any Data of those names will be ignored.
    # RETURNS: the Data removed
    def RemoveDataRelativeToTarget(this, datumAttribute, relation, target, ignoreNames = []):
        try:
            toRem = []
            for d in this.data:
                if (ignoreNames and d.name in ignoreNames):
                    continue
                if (relation(getattr(d, datumAttribute), target)):
                    toRem.append(d)
            return this.RemoveData(toRem)
        except Exception as e:
            logging.error(f"{this.name} - {e.message}")
            return []

    # Removes any Data that have the same datumAttribute as a previous Datum, keeping only the first.
    # RETURNS: The Data removed
    def RemoveDuplicateDataOf(this, datumAttribute):
        toRem = [] # list of Data
        alreadyProcessed = [] # list of strings, not whatever datumAttribute is.
        for d1 in this.data:
            skip = False
            for dp in alreadyProcessed:
                if (str(getattr(d1, datumAttribute)) == dp):
                    skip = True
                    break
            if (skip):
                continue
            for d2 in this.data:
                if (d1 is not d2 and str(getattr(d1, datumAttribute)) == str(getattr(d2, datumAttribute))):
                    logging.info(f"Removing duplicate Datum {d2} with unique id {getattr(d2, datumAttribute)}")
                    toRem.append(d2)
                    alreadyProcessed.append(str(getattr(d1, datumAttribute)))
        return this.RemoveData(toRem)

    # Adds all Data from otherDataContainer to *this.
    # If there are duplicate Data identified by the attribute preventDuplicatesOf, they are removed.
    # RETURNS: the Data removed, if any.
    def ImportDataFrom(this, otherDataContainer, preventDuplicatesOf=None):
        this.data.extend(otherDataContainer.data);
        if (preventDuplicatesOf is not None):
            return this.RemoveDuplicateDataOf(preventDuplicatesOf)
        return []



# Executor: a base class for user interfaces.
# An Executor is a functor and can be executed as such.
# For example
#    class MyExecutor(Executor):
#        def __init__(this):
#            super().__init__()
#    . . .
#    myprogram = MyExecutor()
#    myprogram()
# NOTE: Diamond inheritance of Datum.
class Executor(DataContainer, UserFunctor):
            

    def __init__(this, name=INVALID_NAME(), descriptionStr="eons python framework. Extend as thou wilt."):
        this.SetupLogging()

        super().__init__(name)

        this.resolveErrors = True
        this.errorRecursionDepth = 0
        this.errorResolutionStack = {}
        this.resolveErrorsWith = [ # order matters: first is first.
            'install_from_repo',
            'install_with_pip'
        ]

        this.cwd = os.getcwd()
        this.syspath = sys.path  # not used atm.

        this.Configure()
        this.argparser = argparse.ArgumentParser(description = descriptionStr)
        this.args = None
        this.extraArgs = None
        this.AddArgs()

    # Adapter for @recoverable.
    # See Recoverable.py for details
    def GetExecutor(this):
        return this

    # this.errorResolutionStack are whatever we've tried to do to fix whatever our problem is.
    # This method resets our attempts to remove stale data.
    def ClearErrorResolutionStack(this):
        if (this.errorRecursionDepth):
            this.errorRecursionDepth = this.errorRecursionDepth - 1
        
        if (not this.errorRecursionDepth):
            this.errorResolutionStack = {}

    # Configure class defaults.
    # Override this to customize your Executor.
    def Configure(this):
        this.defaultRepoDirectory = os.path.abspath(os.path.join(this.cwd, "./eons/"))
        this.registerDirectories = []
        this.defualtConfigFile = None

        # Usually, Executors shunt work off to other UserFunctors, so we leave these True unless a child needs to check its work.
        this.functionSucceeded = True
        this.rollbackSucceeded = True


    # Add a place to search for SelfRegistering classes.
    # These should all be relative to the invoking working directory (i.e. whatever './' is at time of calling Executor())
    def RegisterDirectory(this, directory):
        this.registerDirectories.append(os.path.abspath(os.path.join(this.cwd,directory)))


    # Global logging config.
    # Override this method to disable or change.
    def SetupLogging(this):
        logging.basicConfig(level = logging.INFO, format = '%(asctime)s [%(levelname)s] %(message)s (%(filename)s:%(lineno)s)', datefmt = '%H:%M:%S')


    # Adds command line arguments.
    # Override this method to change. Optionally, call super().AddArgs() within your method to simply add to this list.
    def AddArgs(this):
        this.argparser.add_argument('--verbose', '-v', action='count', default=0)
        this.argparser.add_argument('--quiet', '-q', action='count', default=0)
        this.argparser.add_argument('--config', '-c', type=str, default=None, help='Path to configuration file containing only valid JSON.', dest='config')
        this.argparser.add_argument('--no-repo', action='store_true', default=False, help='prevents searching online repositories', dest='no_repo')

    # Create any sub-class necessary for child-operations
    # Does not RETURN anything.
    def InitData(this):
        pass

    # Register included files early so that they can be used by the rest of the system.
    # If we don't do this, we risk hitting infinite loops because modular functionality relies on these modules.
    def RegisterIncludedClasses(this):
        this.RegisterAllClassesInDirectory(str(Path(__file__).resolve().parent.joinpath("resolve")))

    # Register all classes in each directory in this.registerDirectories
    def RegisterAllClasses(this):
        for d in this.registerDirectories:
            this.RegisterAllClassesInDirectory(os.path.join(os.getcwd(), d))
        this.RegisterAllClassesInDirectory(this.repo['store'])


    # Something went wrong, let's quit.
    # TODO: should this simply raise an exception?
    def ExitDueToErr(this, errorStr):
        #  logging.info("#################################################################\n")
        logging.error(errorStr)
        #  logging.info("\n#################################################################")
        this.argparser.print_help()
        sys.exit()


    # Populate the configuration details for *this.
    def PopulateConfig(this):
        this.config = None

        if (this.args.config is None):
            this.args.config = this.defualtConfigFile

        if (this.args.config is not None and os.path.isfile(this.args.config)):
            configFile = open(this.args.config, "r")
            this.config = jsonpickle.decode(configFile.read())
            configFile.close()
            logging.debug(f"Got config contents: {this.config}")


    #  Get information for how to download packages.
    def PopulateRepoDetails(this):
        details = {
            "store": this.defaultRepoDirectory,
            "url": "https://api.infrastructure.tech/v1/package",
            "username": None,
            "password": None
        }
        this.repo = {}

        if (this.args.no_repo is not None and this.args.no_repo):
            for key, default in details.items():
                this.repo[key] = None
            this.repo['store'] = this.Fetch("repo_store", default=this.defaultRepoDirectory)
        else:
            for key, default in details.items():
                this.repo[key] = this.Fetch(f"repo_{key}", default=default)


    # Do the argparse thing.
    # Extra arguments are converted from --this-format to this_format, without preceding dashes. For example, --repo-url ... becomes repo_url ...
    # NOTE: YOU CANNOT USE @recoverable METHODS HERE!
    def ParseArgs(this):
        this.args, extraArgs = this.argparser.parse_known_args()

        if (this.args.verbose > 0):
            logging.getLogger().setLevel(logging.DEBUG)

        if (this.args.quiet > 0):
            logging.getLogger().setLevel(logging.WARNING)
        elif (this.args.quiet > 1):
            logging.getLogger().setLevel(logging.ERROR)

        extraArgsKeys = []
        for index in range(0, len(extraArgs), 2):
            keyStr = extraArgs[index]
            keyStr = keyStr.replace('--', '').replace('-', '_')
            extraArgsKeys.append(keyStr)

        extraArgsValues = []
        for index in range(1, len(extraArgs), 2):
            extraArgsValues.append(extraArgs[index])

        this.extraArgs = dict(zip(extraArgsKeys, extraArgsValues))
        logging.debug(f"Got extra arguments: {this.extraArgs}") # has to be after verbosity setting


    #  Will try to get a value for the given varName from:
    #     first: this.
    #     second: extra arguments provided to *this.
    #     third: the config file, if provided.
    #     fourth: the environment (if enabled).
    #  RETURNS the value of the given variable or default.
    @recoverable
    def Fetch(this, varName, default=None, enableThis=True, enableArgs=True, enableConfig=True, enableEnvironment=True):
        logging.debug(f"Fetching {varName}...")

        if (enableThis and hasattr(this, varName)):
            logging.debug(f"...got {varName} from {this.name}.")
            return getattr(this, varName)

        if (enableArgs and this.extraArgs):
            for key, val in this.extraArgs.items():
                if (key == varName):
                    logging.debug(f"...got {varName} from argument.")
                    return val

        if (enableConfig and this.config):
            for key, val in this.config.items():
                if (key == varName):
                    logging.debug(f"...got {varName} from config.")
                    return val

        if (enableEnvironment):
            envVar = os.getenv(varName)
            if (envVar is not None):
                logging.debug(f"...got {varName} from environment")
                return envVar

        logging.debug(f"...could not find {varName}; using default ({default})")
        return default


    # UserFunctor method.
    # We have to ParseArgs() here in order for other Executors to use ____KWArgs...
    def ParseInitialArgs(this):
        this.ParseArgs() # first, to enable debug and other such settings.
        this.RegisterIncludedClasses()
        this.PopulateConfig()
        this.PopulateRepoDetails()
        
    # UserFunctor required method
    # Override this with your own workflow.
    def UserFunction(this):
        this.RegisterAllClasses()
        this.InitData()


    # Attempts to download the given package from the repo url specified in calling args.
    # Will refresh registered classes upon success
    # RETURNS whether or not the package was downloaded. Will raise Exceptions on errors.
    # Does not guarantee new classes are made available; errors need to be handled by the caller.
    @recoverable
    def DownloadPackage(this,
        packageName,
        registerClasses=True,
        createSubDirectory=False):

        if (this.args.no_repo is not None and this.args.no_repo):
            logging.debug(f"Refusing to download {packageName}; we were told not to use a repository.")
            return False

        logging.debug(f"Trying to download {packageName} from repository ({this.repo['url']})")

        if (not os.path.exists(this.repo['store'])):
            logging.debug(f"Creating directory {this.repo['store']}")
            mkpath(this.repo['store'])

        packageZipPath = os.path.join(this.repo['store'], f"{packageName}.zip")    

        url = f"{this.repo['url']}/download?package_name={packageName}"

        auth = None
        if this.repo['username'] and this.repo['password']:
            auth = requests.auth.HTTPBasicAuth(this.repo['username'], this.repo['password'])   

        headers = {
            "Connection": "keep-alive",
        }     

        packageQuery = requests.get(url, auth=auth, headers=headers, stream=True)

        if (packageQuery.status_code != 200):
            raise PackageError(f"Unable to download {packageName}")
            # let caller decide what to do next.

        packageSize = int(packageQuery.headers.get('content-length', 0))
        chunkSize = 1024 # 1 Kibibyte

        logging.debug(f"Writing {packageZipPath} ({packageSize} bytes)")
        packageZipContents = open(packageZipPath, 'wb+')
        
        progressBar = None
        if (not this.args.quiet):
            progressBar = tqdm(total=packageSize, unit='iB', unit_scale=True)

        for chunk in packageQuery.iter_content(chunkSize):
            packageZipContents.write(chunk)
            if (not this.args.quiet):
                progressBar.update(len(chunk))
        
        if (not this.args.quiet):
            progressBar.close()

        if (packageSize and not this.args.quiet and progressBar.n != packageSize):
            raise PackageError(f"Package wrote {progressBar.n} / {packageSize} bytes")
        
        packageZipContents.close()

        if (not os.path.exists(packageZipPath)):
            raise PackageError(f"Failed to create {packageZipPath}")

        logging.debug(f"Extracting {packageZipPath}")
        openArchive = ZipFile(packageZipPath, 'r')
        extractLoc = this.repo['store']
        if (createSubDirectory):
            extractLoc = os.path.join(extractLoc, packageName)
        openArchive.extractall(f"{extractLoc}")
        openArchive.close()
        os.remove(packageZipPath)
        
        if (registerClasses):
            this.RegisterAllClassesInDirectory(this.repo['store'])

        return True
            
    # RETURNS and instance of a Datum, UserFunctor, etc. (aka modules) which has been discovered by a prior call of RegisterAllClassesInDirectory()
    # Will attempt to register existing modules if one of the given name is not found. Failing that, the given package will be downloaded if it can be found online.
    # Both python modules and other eons modules of the same prefix will be installed automatically in order to meet all required dependencies of the given module.
    @recoverable
    def GetRegistered(this,
        registeredName,
        prefix=""):

        try:
            registered = SelfRegistering(registeredName)
        except Exception as e:
            # We couldn't get what was asked for. Let's try asking for help from the error resolution machinery.
            packageName = registeredName
            if (prefix):
                packageName = f"{prefix}_{registeredName}"
            logging.error(f"While trying to instantiate {packageName}, got: {e}")
            raise HelpWantedWithRegistering(f"Trying to get SelfRegistering {packageName}")

        # NOTE: UserFunctors are Data, so they have an IsValid() method
        if (not registered or not registered.IsValid()):
            logging.error(f"No valid object: {registeredName}")
            raise FatalCannotExecute(f"No valid object: {registeredName}") 

        return registered

    
    # Non-static override of the SelfRegistering method.
    # Needed for errorObject resolution.
    @recoverable
    def RegisterAllClassesInDirectory(this, directory):
        path = Path(directory)
        if (not path.exists()):
            logging.debug(f"Making path for SelfRegitering classes: {str(path)}")
            path.mkdir(parents=True, exist_ok=True)

        if (directory not in this.syspath):
            this.syspath.append(directory)

        SelfRegistering.RegisterAllClassesInDirectory(directory)


    # Utility method. may not be useful.
    @staticmethod
    def SplitNameOnPrefix(name):
        splitName = name.split('_')
        if (len(splitName)>1):
            return splitName[0], splitName[1]
        return "", name


    # Uses the ResolveError UserFunctors to process any errors.
    @recoverable
    def ResolveError(this, error, attemptResolution):
        if (attemptResolution >= len(this.resolveErrorsWith)):
            raise FailedErrorResolution(f"{this.name} does not have {attemptResolution} resolutions to fix this error: {error} (it has {len(this.resolveErrorsWith)})")

        resolution = this.GetRegistered(this.resolveErrorsWith[attemptResolution], "resolve") # Okay to ResolveErrors for ErrorResolutions.
        this.errorResolutionStack, errorMightBeResolved = resolution(executor=this, error=error)
        if (errorMightBeResolved):
            logging.debug(f"Error might have been resolved by {resolution.name}.")
        return errorMightBeResolved




# Use an ErrorStringParser for each "parsers" in order to avoid having to override the GetObjectFromError method and create a new class for every error you want to handle.
# ErrorStringParsers enable ErrorResolutions to be created on a per-functionality, rather than per-error basis, reducing the total amount of duplicate code.
# Each error has a different string. In order to get the object of the error, we have to know where the object starts and ends.
# NOTE: this assumes only 1 object per string. Maybe fancier parsing logic can be added in the future.
#
# startPosition is always positive
# endPosition is always negative
class ErrorStringParser:
    def __init__(this, applicableError, startPosition, endPosition):
        this.applicableError = applicableError
        this.startPosition = startPosition
        this.endPosition = endPosition

    def Parse(this, errorString):
        end = this.endPosition
        if (not end):
            end = len(errorString)
        return errorString[this.startPosition:end]


# ErrorResolution is a UserFunctor which can be executed when an Exception is raised.
# The goal of this class is to do some kind of work that will fix the problem on the second try of whatever generated the error.
class ErrorResolution(UserFunctor):

    def __init__(this, name=INVALID_NAME()):
        super().__init__(name)

        # What errors, as ErrorStringParser objects, is *this prepared to handle?
        this.parsers = []

        this.error = None
        this.errorType = ""
        this.errorString = ""
        this.errorObject = ""
        this.errorResolutionStack = {}

        # We do want to know whether or not we should attempt to run whatever failed again.
        # So, let's store that in functionSucceeded. Meaning if this.functionSucceeded, try the original method again.
        # No rollback, by default and definitely don't throw Exceptions.
        this.enableRollback = False
        this.functionSucceeded = True
        this.raiseExceptions = False

        this.errorShouldBeResolved = False


    # Put your logic here!
    def Resolve(this):
        # You get the following members:
        # this.error (an Exception)
        # this.errorString (a string cast of the Exception)
        # this.errorType (a string)
        # this.errorObjet (a string or whatever you return from GetObjectFromError())

        # You get the following guarantees:
        # *this has not been called on this particular error before.
        # the error given is applicable to *this per this.parsers

        ###############################################
        # Please throw errors if something goes wrong #
        # Otherwise, set this.errorShouldBeResolved   #
        ###############################################
        
        pass



    # Helper method for creating ErrorStringParsers
    # To use this, simply take an example output and replace the object you want to extract with "OBJECT"
    def ApplyTo(this, error, exampleString):
        match = re.search('OBJECT', exampleString)
        this.parsers.append(ErrorStringParser(error, match.start(), match.end() - len(exampleString)))

    # Get the type of this.error as a string.
    def GetErrorType(this):
        return type(this.error).__name__

    # Get an actionable object from the error.
    # For example, if the error is 'ModuleNotFoundError', what is the module?
    def GetObjectFromError(this):
        for parser in this.parsers:
            if (parser.applicableError != this.errorType):
                continue

            this.errorObject = parser.Parse(this.errorString)
            return

        raise ErrorResolutionError(f"{this.name} cannot parse error object from ({this.errorType}): {str(this.error)}.")

    # Determine if this resolution method is applicable.
    def CanProcess(this):
        return this.GetErrorType() in [parser.applicableError for parser in this.parsers]

    # Grab any known and necessary args from this.kwargs before any Fetch calls are made.
    def ParseInitialArgs(this):
        super().ParseInitialArgs()
        if ('error' in this.kwargs):
            this.error = this.kwargs.pop('error')
            # Just assume the error is an actual Exception object.
        else:
            raise ErrorResolutionError(f"{this.name} was not given an error to resolve.")

        this.errorString = str(this.error)
        this.errorType = this.GetErrorType()

        # Internal member to avoid processing duplicates
        this.errorResolutionStack = this.executor.errorResolutionStack

    # Override of UserFunctor method.
    # We'll keep calling this until an error is raised.
    def UserFunction(this):
        this.functionSucceeded = True
        this.errorShouldBeResolved = True
        
        if (not this.CanProcess()):
            this.errorShouldBeResolved = False
            return this.errorResolutionStack, this.errorShouldBeResolved

        if (not this.errorString in this.errorResolutionStack.keys()):
            this.errorResolutionStack.update({this.errorString:[]})
        
        if (this.name in this.errorResolutionStack[this.errorString]):
            raise FailedErrorResolution(f"{this.name} already tried and failed to resolve {this.errorType}: {this.errorString}.")

        this.GetObjectFromError()

        try:
            this.Resolve()
        except:
            this.functionSucceeded = False
        
        this.errorResolutionStack[this.errorString].append(this.name)
        return this.errorResolutionStack, this.errorShouldBeResolved
        
