"""
  CTA extended class to submit jobs locally
"""

__RCSID__ = "$Id$"

import glob
import os
import shlex
import shutil
import tarfile
import tempfile
import six
from six.moves.urllib.parse import unquote as urlunquote

# DIRAC imports
import DIRAC
from DIRAC import gConfig, gLogger, S_OK, S_ERROR
from DIRAC.Interfaces.API.Dirac import Dirac
from DIRAC.ConfigurationSystem.Client.Helpers.Operations import Operations
from DIRAC.Core.Utilities.ModuleFactory import ModuleFactory
from DIRAC.Core.Utilities.PrettyPrint import printTable, printDict
from DIRAC.Core.Utilities.Subprocess import systemCall


class Submission(Dirac):
    """CTA extension class to submit jobs locally
    """

    def __init__(self):
        """Constructor"""
        """Constructor"""
        Dirac.__init__(self)

    def runLocalJob(self, job):
        """Execute jobs locally.
        These can be either:

         - Instances of the Job Class
            - VO Application Jobs
            - Inline scripts
            - Scripts as executables
            - Scripts inside an application environment

         - JDL File

        Example usage:

        >>> print submission.runLocalJob(job)
        {'OK': True, 'Value': '12345'}

        :param job: Instance of Job class
        :type job: ~DIRAC.Interfaces.API.Job.Job
        :returns: S_OK,S_ERROR
        """

        try:
            formulationErrors = job.errorDict
        except AttributeError as x:
            self.log.verbose("Could not obtain job errors:%s" % (x))
            formulationErrors = {}

        if formulationErrors:
            for method, errorList in formulationErrors.items():  # can be an iterator
                self.log.error(">>>> Error in %s() <<<<\n%s" % (method, "\n".join(errorList)))
            return S_ERROR(formulationErrors)

        # Run any VO specific checks if desired prior to submission, this may or may not be overridden
        # in a derived class for example
        try:
            result = self.preSubmissionChecks(job, "local")
            if not result["OK"]:
                self.log.error('Pre-submission checks failed for job with message: "%s"' % (result["Message"]))
                return result
        except Exception as x:
            msg = 'Error in VO specific function preSubmissionChecks: "%s"' % (x)
            self.log.error(msg)
            return S_ERROR(msg)

        result = self.runLocal(job)

        return result

    def runLocal(self, job):
        """Internal function.  This method is called by Submit API function submitLocalJob.
            All output files are written to the local directory.

            This is a method for running local tests. It skips the creation of a JobWrapper,
            but preparing an environment that mimics it.

        :param job: a job object
        :type job: ~DIRAC.Interfaces.API.Job.Job
        """
        self.log.notice("Executing workflow locally")
        curDir = os.getcwd()
        self.log.info("Executing from %s" % curDir)

        jobDir = tempfile.mkdtemp(suffix="_JobDir", prefix="Local_", dir=curDir)
        os.chdir(jobDir)
        self.log.info("Executing job at temp directory %s" % jobDir)

        tmpdir = tempfile.mkdtemp(prefix="DIRAC_")
        self.log.verbose("Created temporary directory for submission %s" % (tmpdir))
        jobXMLFile = tmpdir + "/jobDescription.xml"
        self.log.verbose("Job XML file description is: %s" % jobXMLFile)
        with open(jobXMLFile, "w+") as fd:
            fd.write(job._toXML())  # pylint: disable=protected-access

        shutil.copy(jobXMLFile, "%s/%s" % (os.getcwd(), os.path.basename(jobXMLFile)))

        res = self.__getJDLParameters(job)
        if not res["OK"]:
            self.log.error("Could not extract job parameters from job")
            return res
        parameters = res["Value"]
        self.log.debug("Extracted job parameters from JDL", parameters)

        arguments = parameters.get("Arguments", "")

        # Replace argument placeholders for parametric jobs
        # if we have Parameters then we have a parametric job
        if "Parameters" in parameters:
            for par, value in parameters.items():  # can be an iterator
                if par.startswith("Parameters."):
                    # we just use the first entry in all lists to run one job
                    parameters[par[len("Parameters.") :]] = value[0]
            arguments = arguments % parameters

        self.log.verbose("Job parameters: %s" % printDict(parameters))
        inputDataRes = self._getLocalInputData(parameters)
        if not inputDataRes["OK"]:
            return inputDataRes
        inputData = inputDataRes["Value"]

        if inputData:
            self.log.verbose("Job has input data: %s" % inputData)
            localSEList = gConfig.getValue("/LocalSite/LocalSE", "")
            if not localSEList:
                return self._errorReport("LocalSite/LocalSE should be defined in your config file")
            localSEList = localSEList.replace(" ", "").split(",")
            self.log.debug("List of local SEs: %s" % localSEList)
            inputDataPolicy = Operations().getValue("InputDataPolicy/InputDataModule")
            if not inputDataPolicy:
                return self._errorReport("Could not retrieve DIRAC/Operations/InputDataPolicy/InputDataModule for VO")

            self.log.info("Job has input data requirement, will attempt to resolve data for %s" % DIRAC.siteName())
            self.log.verbose("\n".join(inputData if isinstance(inputData, (list, tuple)) else [inputData]))
            replicaDict = self.getReplicasForJobs(inputData)
            if not replicaDict["OK"]:
                return replicaDict
            guidDict = self.getLfnMetadata(inputData)
            if not guidDict["OK"]:
                return guidDict
            for lfn, reps in replicaDict["Value"]["Successful"].items():  # can be an iterator
                guidDict["Value"]["Successful"][lfn].update(reps)
            resolvedData = guidDict
            diskSE = gConfig.getValue(self.section + "/DiskSE", ["-disk", "-DST", "-USER", "-FREEZER"])
            tapeSE = gConfig.getValue(self.section + "/TapeSE", ["-tape", "-RDST", "-RAW"])
            configDict = {"JobID": None, "LocalSEList": localSEList, "DiskSEList": diskSE, "TapeSEList": tapeSE}
            self.log.verbose(configDict)
            argumentsDict = {
                "FileCatalog": resolvedData,
                "Configuration": configDict,
                "InputData": inputData,
                "Job": parameters,
                "InputDataDirectory" : "CWD",
            }
            self.log.verbose(argumentsDict)
            moduleFactory = ModuleFactory()
            moduleInstance = moduleFactory.getModule(inputDataPolicy, argumentsDict)
            if not moduleInstance["OK"]:
                self.log.warn("Could not create InputDataModule")
                return moduleInstance

            module = moduleInstance["Value"]
            result = module.execute()
            if not result["OK"]:
                self.log.warn("Input data resolution failed")
                return result

        softwarePolicy = Operations().getValue("SoftwareDistModule")
        if softwarePolicy:
            moduleFactory = ModuleFactory()
            moduleInstance = moduleFactory.getModule(softwarePolicy, {"Job": parameters})
            if not moduleInstance["OK"]:
                self.log.warn("Could not create SoftwareDistModule")
                return moduleInstance

            module = moduleInstance["Value"]
            result = module.execute()
            if not result["OK"]:
                self.log.warn("Software installation failed with result:\n%s" % (result))
                return result
        else:
            self.log.verbose("Could not retrieve SoftwareDistModule for VO")

        self.log.debug("Looking for resolving the input sandbox, if it is present")
        sandbox = parameters.get("InputSandbox")
        if sandbox:
            self.log.verbose("Input Sandbox is %s" % sandbox)
            if isinstance(sandbox, six.string_types):
                sandbox = [isFile.strip() for isFile in sandbox.split(",")]
            for isFile in sandbox:
                self.log.debug("Resolving Input Sandbox %s" % isFile)
                if isFile.lower().startswith("lfn:"):  # isFile is an LFN
                    isFile = isFile[4:]
                # Attempt to copy into job working directory, unless it is already there
                if os.path.exists(os.path.join(os.getcwd(), os.path.basename(isFile))):
                    self.log.debug("Input Sandbox %s found in the job directory, no need to copy it" % isFile)
                else:
                    if os.path.isabs(isFile) and os.path.exists(isFile):
                        self.log.debug("Input Sandbox %s is a file with absolute path, copying it" % isFile)
                        shutil.copy(isFile, os.getcwd())
                    elif os.path.isdir(isFile):
                        self.log.debug(
                            "Input Sandbox %s is a directory, found in the user working directory, copying it" % isFile
                        )
                        shutil.copytree(isFile, os.path.basename(isFile), symlinks=True)
                    elif os.path.exists(os.path.join(curDir, os.path.basename(isFile))):
                        self.log.debug("Input Sandbox %s found in the submission directory, copying it" % isFile)
                        shutil.copy(os.path.join(curDir, os.path.basename(isFile)), os.getcwd())
                    elif os.path.exists(os.path.join(tmpdir, isFile)):  # if it is in the tmp dir
                        self.log.debug("Input Sandbox %s is a file, found in the tmp directory, copying it" % isFile)
                        shutil.copy(os.path.join(tmpdir, isFile), os.getcwd())
                    else:
                        self.log.verbose("perhaps the file %s is in an LFN, so we attempt to download it." % isFile)
                        getFile = self.getFile(isFile)
                        if not getFile["OK"]:
                            self.log.warn("Failed to download %s with error: %s" % (isFile, getFile["Message"]))
                            return S_ERROR("Can not copy InputSandbox file %s" % isFile)

                isFileInCWD = os.getcwd() + os.path.sep + isFile

                basefname = os.path.basename(isFileInCWD)
                if tarfile.is_tarfile(basefname):
                    try:
                        with tarfile.open(basefname, "r") as tf:
                            for member in tf.getmembers():
                                tf.extract(member, os.getcwd())
                    except (tarfile.ReadError, tarfile.CompressionError, tarfile.ExtractError) as x:
                        return S_ERROR("Could not untar or extract %s with exception %s" % (basefname, repr(x)))

        self.log.info("Attempting to submit job to local site: %s" % DIRAC.siteName())

        # DIRACROOT is used for finding dirac-jobexec in python2 installations
        # (it is normally set by the JobWrapper)
        # We don't use DIRAC.rootPath as we assume that a DIRAC installation is already done at this point
        # DIRAC env variable is only set for python2 installations
        if "DIRAC" in os.environ:
            os.environ["DIRACROOT"] = os.environ["DIRAC"]
            self.log.verbose("DIRACROOT = %s" % (os.environ["DIRACROOT"]))

        if "Executable" in parameters:
            executable = os.path.expandvars(parameters["Executable"])
        else:
            return self._errorReport('Missing job "Executable"')

        if "-o LogLevel" in arguments:
            dArguments = arguments.split()
            logLev = dArguments.index("-o") + 1
            dArguments[logLev] = "LogLevel=DEBUG"
            arguments = " ".join(dArguments)
        else:
            arguments += " -o LogLevel=DEBUG"
        command = "%s %s" % (executable, arguments)

        self.log.info("Executing: %s" % command)
        executionEnv = dict(os.environ)
        variableList = parameters.get("ExecutionEnvironment")
        if variableList:
            self.log.verbose("Adding variables to execution environment")
            if isinstance(variableList, six.string_types):
                variableList = [variableList]
            for var in variableList:
                nameEnv = var.split("=")[0]
                valEnv = urlunquote(var.split("=")[1])  # this is needed to make the value contain strange things
                executionEnv[nameEnv] = valEnv
                self.log.verbose("%s = %s" % (nameEnv, valEnv))

        result = systemCall(0, cmdSeq=shlex.split(command), env=executionEnv, callbackFunction=self.__printOutput)
        if not result["OK"]:
            return result

        status = result["Value"][0]
        self.log.verbose("Status after execution is %s" % (status))

        # FIXME: if there is an callbackFunction, StdOutput and StdError will be empty soon
        outputFileName = parameters.get("StdOutput")
        errorFileName = parameters.get("StdError")

        if outputFileName:
            stdout = result["Value"][1]
            if os.path.exists(outputFileName):
                os.remove(outputFileName)
            self.log.info("Standard output written to %s" % (outputFileName))
            with open(outputFileName, "w") as outputFile:
                print(stdout, file=outputFile)
        else:
            self.log.warn("Job JDL has no StdOutput file parameter defined")

        if errorFileName:
            stderr = result["Value"][2]
            if os.path.exists(errorFileName):
                os.remove(errorFileName)
            self.log.verbose("Standard error written to %s" % (errorFileName))
            with open(errorFileName, "w") as errorFile:
                print(stderr, file=errorFile)
            sandbox = None
        else:
            self.log.warn("Job JDL has no StdError file parameter defined")
            sandbox = parameters.get("OutputSandbox")

        if sandbox:
            if isinstance(sandbox, six.string_types):
                sandbox = [osFile.strip() for osFile in sandbox.split(",")]
            for i in sandbox:
                globList = glob.glob(i)
                for osFile in globList:
                    if os.path.isabs(osFile):
                        # if a relative path, it is relative to the user working directory
                        osFile = os.path.basename(osFile)
                    # Attempt to copy back from job working directory
                    if os.path.isdir(osFile):
                        shutil.copytree(osFile, curDir, symlinks=True)
                    elif os.path.exists(osFile):
                        shutil.copy(osFile, curDir)
                    else:
                        return S_ERROR("Can not copy OutputSandbox file %s" % osFile)

        os.chdir(curDir)

        if status:  # if it fails, copy content of execution dir in current directory
            destDir = os.path.join(curDir, os.path.basename(os.path.dirname(tmpdir)))
            self.log.verbose("Copying outputs from %s to %s" % (tmpdir, destDir))
            if os.path.exists(destDir):
                shutil.rmtree(destDir)
            shutil.copytree(tmpdir, destDir)

        self.log.verbose("Cleaning up %s..." % tmpdir)
        self.__cleanTmp(tmpdir)

        if status:
            return S_ERROR("Execution completed with non-zero status %s" % (status))

        return S_OK("Execution completed successfully")
