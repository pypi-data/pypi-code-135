import eons
import os
import logging
import shutil
import jsonpickle
from pathlib import Path
from flask import request
from flask import Response
import traceback
from flask import Flask
from waitress import serve

######## START CONTENT ########
# All APIer errors
class APIError(Exception): pass


# Exception used for miscellaneous API errors.
class OtherAPIError(APIError): pass

# APIE Functors extend Eons Functors in order to:
# 1. Improve Fetch() behavior when cascading multiple Functor executions.
# 2. Allow Fetching from a http request.
class Functor(eons.UserFunctor):
    def __init__(this, name=eons.INVALID_NAME()):
        super().__init__(name)

        this.enableRollback = False

        # If you'd like to only check for your values in certain places, adjust this list.
        # These will call the corresponding methods as described in the docs: https://flask.palletsprojects.com/en/2.2.x/api/#flask.Request.args
        this.fetchFromRequest = [
            'args',
            'form',
            'json',
            'files'
        ]

    #Grab any known and necessary args from this.kwargs before any Fetch calls are made.
    # This is executed first when calling *this.
    def ParseInitialArgs(this):
        super().ParseInitialArgs()

        this.request = this.kwargs.pop('request')

        if ('predecessor' in this.kwargs):
            this.predecessor = this.kwargs.pop('predecessor')
        else:
            this.predecessor = None



    # Will try to get a value for the given varName from:
    #    first: this
    #    second: the Functor preceding *this
    #    third: the executor (args > config > environment)
    # RETURNS the value of the given variable or None.
    def Fetch(this,
        varName,
        default=None,
        enableThis=True,
        enableExecutor=True,
        enableArgs=True,
        enableExecutorConfig=True,
        enableEnvironment=True,
        enablePredecessor=True,
        enableRequest=True):
            
        # Duplicate code from eons.UserFunctor in order to establish precedence.
        if (enableThis and hasattr(this, varName)):
            logging.debug(f"...got {varName} from {this.name}.")
            return getattr(this, varName)

        if (enablePredecessor and this.predecessor is not None):
            # enableThis is hardcoded as True of enablePredecessor but only for the predecessor.
            val = this.predecessor.Fetch(varName, default, True, enableExecutor, enableArgs, enableExecutorConfig, enableEnvironment, enablePredecessor, enableRequest)
            if (val is not None):
                # logging.debug(f"...got {varName} from predecessor.") # Too many logs.
                return val

        # Checking this when the predecessor already did is wasteful but we don't know what they're looking at or looking for, so let's do it again.
        if (enableRequest):
            for field in this.fetchFromRequest:
                if (field == 'json' and this.request.content_type != "application/json"):
                    continue
                if (field == 'forms' and not this.request.data):
                    continue
                if (field == 'files' and not this.request.files):
                    continue
                
                # TODO: there's a better way to do this. You can pass the field arg to this.request somehow...
                val = getattr(this.request, field).get(varName)
                if (val is not None):
                    logging.debug(f"...got {varName} from request.")
                    return val

            return super().Fetch(varName, default, enableThis, enableExecutor, enableArgs, enableExecutorConfig, enableEnvironment)



# Endpoints are what is run when a given request is successfully authenticated.
# Put all your actual API logic in these!
# Keep in mind that Endpoints will be made available in a just-in-time, as-needed basis. There is no need to preload logic, etc.
# That also means that each Endpoint should operate in isolation and not require any other Endpoint to function.
# The exception to this isolation is when Endpoints are intended to be called in sequence.
# Any number of Endpoints can be chained together in any order. The behavior of the first affects the behavior of the last.
# This allows you to create generic "upload" Endpoints, where what is uploaded is determined by the preceding Endpoint.
# For example, you might have 3 Endpoints: "package", "photo", and "upload"; both package and photo set a member called "file_data"; upload Fetches "file_data" and puts it somewhere; you can thus use upload with either predecessor (e.g. .../package/upload and .../photo/upload).
# What is returned by an Endpoint is the very last Endpoint's return value. All intermediate values are skipped (so you can throw errors if calling things like .../package without a further action).
# NOTE: Endpoints should be published as api_s (i.e. projectType="api")
class Endpoint(Functor):
    def __init__(this, name=eons.INVALID_NAME()):
        super().__init__(name)

        this.enableRollback = False

        this.supportedMethods = [
            'POST',
            'GET',
            'PUT',
            'DELETE',
            'PATCH'
        ]

        # Only the items listed here will be allowed as next Endpoints.
        # If this list is empty, all endpoints are allowed.
        # When creating your endpoints, make sure to adjust this!
        # Also, please keep 'help'. It helps.
        this.allowedNext = ['help']

        this.next = []

        # Hop-by-hop headers are forbidden by WSGI.
        this.forbidden_headers = [
            'Keep-Alive',
            'Transfer-Encoding',
            'TE',
            'Connection',
            'Trailer',
            'Upgrade',
            'Proxy-Authorization',
            'Proxy-Authenticate',
        ]

        # What should the return type of *this be?
        this.mime = 'application/json'

        # If the client can store the result of *this locally, let them know.
        # When querying this, it is best to use the IsCachable() method.
        this.cacheable = False

        # If compiling data, from this.response['content_data'] for example, the response['content_string'] of *this will be overwritten.
        # You can override this behavior and force the compiled data to be lost by setting clobberContent to False.
        # This is useful if you are forwarding json requests and don't want to parse then recompile the content.
        this.clobberContent = True

        # The 'help' Endpoint will print this text.
        # Setting this will inform users on how to use your Endpoint.
        # Help will automatically print the name of *this for you, along with optional and required args, supported methods, and allowed next
        this.helpText = '''\
I'm just a generic endpoint. Not much I can do for ya. :\
'''

    # Call things!
    # Override this or die.
    def Call(this):
        pass


    # Override this to perform whatever success checks are necessary.
    # Override of eons.Functor method. See that class for details
    def DidCallSucceed(this):
        return True


    # If an error is thrown while Call()ing *this, APIE will attempt to return this method.
    def HandleBadRequest(this, request, error):
        message = f"Bad request for {this.name}: {str(error)}. "
        if ('help' in this.allowedNext):
            message += "Try appending /help."
        return message, 400


    # Hook for any pre-call configuration
    # Override of eons.Functor method. See that class for details
    def PreCall(this):
        pass


    # Hook for any post-call configuration
    # Override of eons.Functor method. See that class for details
    def PostCall(this):
        pass

    # Because APIE caches endpoints, the last response given will be stored in *this.
    # Call this method to clear the stale data.
    def ResetResponse(this):
        this.response = {}
        this.response['code'] = 200
        this.response['headers'] = {}
        this.response['content_data'] = {}
        this.response['content_string'] = ""

    # Called right before *this returns.
    # Handles json pickling, etc.
    def ProcessResponse(this):
        if (this.clobberContent):
            if(this.mime == 'application/json'):
                if (len(this.response['content_string'])):
                    logging.info(f"Clobbering content_string ({this.response['content_string']})")

                this.response['content_data'].update({'cacheable': this.cacheable})
                this.response['content_string'] = jsonpickle.encode(this.response['content_data'])

        if ('Content-Type' not in this.response['headers']):
            this.response['headers'].update({'Content-Type': this.mime})

        for header in this.forbidden_headers:
            try:
                this.response['headers'].pop(header)
            except KeyError:
                pass

        return Response(
            response = this.response['content_string'],
            status = this.response['code'],
            headers = this.response['headers'].items(),
            mimetype = this.mime, #This one is okay, I guess???
            content_type = None, #why is this here, we set it in the header. This is a problem in Flask.
            direct_passthrough = True # For speed??
        )


    # Override of eons.Functor method. See that class for details
    def UserFunction(this):
        # Skip execution when the user is asking for help.
        if (this.next and this.next[-1] == 'help'):
            return this.CallNext()

        this.ResetResponse()
        
        this.Call()
        
        if (not this.DidCallSucceed()):
            raise OtherAPIError(f"{this.name} failed.")
        
        if (not this.next):
            return this.ProcessResponse()
        
        return this.CallNext()


    def CallNext(this):
        return this.executor.ProcessEndpoint(this.next.pop(0), this.request, predecessor=this, next=this.next)


    #### SPECIALIZED OVERRIDES. IGNORE THESE ####

    # API compatibility shim
    def DidUserFunctionSucceed(this):
        return this.DidCallSucceed()


    #Grab any known and necessary args from this.kwargs before any Fetch calls are made.
    # This is executed first when calling *this.
    def ParseInitialArgs(this):
        super().ParseInitialArgs()

        # We want to let the executor know who we are as soon as possible, in case any errors come up in validation.
        this.executor.lastEndpoint = this

        if ('next' in this.kwargs):
            this.next = this.kwargs.pop('next')
        else:
            this.next = []

    def ValidateMethod(this):
        if (this.request.method not in this.supportedMethods):
            raise OtherAPIError(f"Method not supported: {this.request.method}")

    def ValidateNext(this):
        if (this.next and this.next[0] not in this.allowedNext):
            if (this.next[0] in ['hack'] and not this.executor.dev):
                raise OtherAPIError(f"Hacking is forbidden on production servers.")
            else:
                raise OtherAPIError(f"Next Endpoint not allowed: {this.next[0]}")

    def ValidateArgs(this):
        try:
            super().ValidateArgs()
        except eons.MissingArgumentError as e:
            # It doesn't matter if *this isn't valid if the user is asking for help.
            if (this.next and this.next[-1] == 'help'):
                return
            raise e

        this.ValidateMethod()
        this.ValidateNext()
        




# Authenticator is a Functor which validates whether or not a request is valid.
# The inputs will be the path of the request and the request itself.
# If you need to check whether the request parameters, data, files, etc. are valid, please do so in your Endpoint.
# Because this class will be invoked often, we have made some performant modifications to the default UserFunctor methods.
# NOTE: All logic for *this should be in UserFunction. There are no extra functions called (e.g. PreCall, PostCall, etc.)
# UserFunction should either return False or raise an exception if the provided request is invalid and should return True if it is.
class Authenticator(Functor):
    def __init__(this, name="Authenticator"):
        super().__init__(name)

    # Override of eons.Functor method. See that class for details
    # NOTE: All logic for *this should be in UserFunction. There are no extra functions called (e.g. PreCall, PostCall, etc.)
    # UserFunction should either return False or raise an exception if the provided request is invalid and should return True if it is.
    def UserFunction(this):
        return True

    # This will be called whenever an unauthorized request is made.
    def Unauthorized(this, path):
        logging.debug(f"Unauthorized: {this.name} on {path}")
        return "Unauthorized", 401

    # Override of eons.Functor method. See that class for details
    def ParseInitialArgs(this):
        super().ParseInitialArgs()

        this.path = this.kwargs.pop('path')

    # Override of eons.Functor method. See that class for details
    # Slimmed down for performance
    def __call__(this, **kwargs):
        this.kwargs = kwargs
        
        this.ParseInitialArgs()
        this.ValidateArgs()
        return this.UserFunction()


class APIE(eons.Executor):

    def __init__(this):
        super().__init__(name="Application Program Interface with Eons", descriptionStr="A readily extensible take on APIs.")

        # this.RegisterDirectory("ebbs")

        this.optionalKWArgs['host'] = "0.0.0.0"
        this.optionalKWArgs['port'] = 80
        this.optionalKWArgs['dev'] = False
        this.optionalKWArgs['clean_start'] = True
        this.optionalKWArgs['authenticator'] = "noauth"
        this.optionalKWArgs['preprocessor'] = ""

        this.supportedMethods = [
            'POST',
            'GET',
            'PUT',
            'DELETE',
            'PATCH'
        ]

        # *this is single-threaded. If we want parallel processing, we can create replicas.
        this.lastEndpoint = None

        # TODO: is it actually faster to keep instances in RAM?
        # This is required for staticKWArgs to be effective.
        this.cachedEndpoints = {}


    # Configure class defaults.
    # Override of eons.Executor method. See that class for details
    def Configure(this):
        super().Configure()

        this.defualtConfigFile = "apie.json"

    # Override of eons.Executor method. See that class for details
    def RegisterIncludedClasses(this):
        super().RegisterIncludedClasses()
        this.RegisterAllClassesInDirectory(str(Path(__file__).resolve().parent.joinpath("api")))
        this.RegisterAllClassesInDirectory(str(Path(__file__).resolve().parent.joinpath("auth")))
        

    # Override of eons.Executor method. See that class for details
    def RegisterAllClasses(this):
        super().RegisterAllClasses()

    # Acquire and run the given endpoint with the given request.
    def ProcessEndpoint(this, endpointName, request, **kwargs):
        if (endpointName in this.cachedEndpoints):
            return this.cachedEndpoints[endpointName](executor=this, request=request, **kwargs)
        
        endpoint = this.GetRegistered(endpointName, "api")
        this.cachedEndpoints.update({endpointName: endpoint})
        return endpoint(executor=this, request=request, **kwargs)


    # What to do when a request causes an exception to be thrown.
    def HandleBadRequest(this, request, error):
        message = f"Bad request: {str(error)}"
        return message, 400


    # Override of eons.Executor method. See that class for details
    def UserFunction(this):
        super().UserFunction()

        if (this.clean_start):
            this.Clean()

        this.auth = this.GetRegistered(this.authenticator, "auth")

        this.flask = Flask(this.name)

        @this.flask.route("/", defaults={"path": ""}, methods = this.supportedMethods)
        def root(path):
            return "It works!", 200

        @this.flask.route("/<string:path>", methods = this.supportedMethods)
        @this.flask.route("/<path:path>", methods = this.supportedMethods)
        def handler(path):
            try:
                if (this.auth(executor=this, path=path, request=request)):
                    endpoints = []
                    if (this.preprocessor):
                        endpoints.append(this.preprocessor)
                    if (path.endswith('/')):
                        path = path[:-1]
                    endpoints.extend(path.split('/'))
                    this.lastEndpoint = None
                    logging.debug(f"Responding to request for {path}; request: {request}")
                    response = this.ProcessEndpoint(endpoints.pop(0), request, next=endpoints)
                    logging.debug(f"Got headers: {response.headers}")
                    logging.debug(f"Got response: {response}")
                    return response
                else:
                    return this.auth.Unauthorized(path)
            except Exception as error:
                traceback.print_exc()
                logging.error(str(error))
                if (this.lastEndpoint):
                    try:
                        return this.lastEndpoint.HandleBadRequest(request, error)
                    except Exception:
                        pass
                return this.HandleBadRequest(request, error) #fine. We'll do it ourselves.

        options = {}
        options['app'] = this.flask
        options['host'] = this.host
        options['port'] = this.port

        # Only applicable if using this.flask.run(**options)
        # if (this.args.verbose > 0):
        #     options['debug'] = True
        #     options['use_reloader'] = False

        serve(**options)


    # Remove possibly stale modules.
    def Clean(this):
        repoPath = Path(this.repo['store'])
        if (repoPath.exists()):
            shutil.rmtree(this.repo['store'])
        repoPath.mkdir(parents=True, exist_ok=True)

