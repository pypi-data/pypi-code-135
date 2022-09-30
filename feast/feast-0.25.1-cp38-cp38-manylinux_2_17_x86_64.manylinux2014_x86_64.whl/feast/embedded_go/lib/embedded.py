
# python wrapper for package github.com/feast-dev/feast/go/embedded within overall package embedded
# This is what you import to use the package.
# File is generated by gopy. Do not edit.
# gopy build -output /project/build/lib.linux-x86_64-cpython-38/feast/embedded_go/lib -vm /opt/python/cp38-cp38/bin/python --build-tags cgo,ccalloc --dynamic-link=True -no-make github.com/feast-dev/feast/go/embedded

# the following is required to enable dlopen to open the _go.so file
import os,sys,inspect,collections
try:
	import collections.abc as _collections_abc
except ImportError:
	_collections_abc = collections

cwd = os.getcwd()
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
os.chdir(currentdir)
from . import _embedded
from . import go

os.chdir(cwd)

# to use this code in your end-user python file, import it as follows:
# from embedded import embedded
# and then refer to everything using embedded. prefix
# packages imported by this package listed below:




# ---- Types ---

# Python type for map map[string]int32
class Map_string_int32(go.GoClass):
	""""""
	def __init__(self, *args, **kwargs):
		"""
		handle=A Go-side object is always initialized with an explicit handle=arg
		otherwise parameter is a python list that we copy from
		"""
		self.index = 0
		if len(kwargs) == 1 and 'handle' in kwargs:
			self.handle = kwargs['handle']
			_embedded.IncRef(self.handle)
		elif len(args) == 1 and isinstance(args[0], go.GoClass):
			self.handle = args[0].handle
			_embedded.IncRef(self.handle)
		else:
			self.handle = _embedded.Map_string_int32_CTor()
			_embedded.IncRef(self.handle)
			if len(args) > 0:
				if not isinstance(args[0], _collections_abc.Mapping):
					raise TypeError('Map_string_int32.__init__ takes a mapping as argument')
				for k, v in args[0].items():
					_embedded.Map_string_int32_set(self.handle, k, v)
	def __del__(self):
		_embedded.DecRef(self.handle)
	def __str__(self):
		s = 'embedded.Map_string_int32 len: ' + str(len(self)) + ' handle: ' + str(self.handle) + ' {'
		if len(self) < 120:
			for k, v in self.items():
				s += str(k) + '=' + str(v) + ', '
		return s + '}'
	def __repr__(self):
		s = 'embedded.Map_string_int32({'
		for k, v in self.items():
			s += str(k) + '=' + str(v) + ', '
		return s + '})'
	def __len__(self):
		return _embedded.Map_string_int32_len(self.handle)
	def __getitem__(self, key):
		return _embedded.Map_string_int32_elem(self.handle, key)
	def __setitem__(self, key, value):
		_embedded.Map_string_int32_set(self.handle, key, value)
	def __delitem__(self, key):
		return _embedded.Map_string_int32_delete(self.handle, key)
	def keys(self):
		return go.Slice_string(handle=_embedded.Map_string_int32_keys(self.handle))
	def values(self):
		vls = []
		kys = self.keys()
		for k in kys:
			vls.append(self[k])
		return vls
	def items(self):
		vls = []
		kys = self.keys()
		for k in kys:
			vls.append((k, self[k]))
		return vls
	def __iter__(self):
		return iter(self.items())
	def __contains__(self, key):
		return _embedded.Map_string_int32_contains(self.handle, key)


#---- Enums from Go (collections of consts with same type) ---


#---- Constants from Go: Python can only ask that you please don't change these! ---


# ---- Global Variables: can only use functions to access ---


# ---- Interfaces ---


# ---- Structs ---

# Python type for struct embedded.DataTable
class DataTable(go.GoClass):
	""""""
	def __init__(self, *args, **kwargs):
		"""
		handle=A Go-side object is always initialized with an explicit handle=arg
		otherwise parameters can be unnamed in order of field names or named fields
		in which case a new Go object is constructed first
		"""
		if len(kwargs) == 1 and 'handle' in kwargs:
			self.handle = kwargs['handle']
			_embedded.IncRef(self.handle)
		elif len(args) == 1 and isinstance(args[0], go.GoClass):
			self.handle = args[0].handle
			_embedded.IncRef(self.handle)
		else:
			self.handle = _embedded.embedded_DataTable_CTor()
			_embedded.IncRef(self.handle)
			if  0 < len(args):
				self.DataPtr = args[0]
			if "DataPtr" in kwargs:
				self.DataPtr = kwargs["DataPtr"]
			if  1 < len(args):
				self.SchemaPtr = args[1]
			if "SchemaPtr" in kwargs:
				self.SchemaPtr = kwargs["SchemaPtr"]
	def __del__(self):
		_embedded.DecRef(self.handle)
	def __str__(self):
		pr = [(p, getattr(self, p)) for p in dir(self) if not p.startswith('__')]
		sv = 'embedded.DataTable{'
		first = True
		for v in pr:
			if callable(v[1]):
				continue
			if first:
				first = False
			else:
				sv += ', '
			sv += v[0] + '=' + str(v[1])
		return sv + '}'
	def __repr__(self):
		pr = [(p, getattr(self, p)) for p in dir(self) if not p.startswith('__')]
		sv = 'embedded.DataTable ( '
		for v in pr:
			if not callable(v[1]):
				sv += v[0] + '=' + str(v[1]) + ', '
		return sv + ')'
	@property
	def DataPtr(self):
		return _embedded.embedded_DataTable_DataPtr_Get(self.handle)
	@DataPtr.setter
	def DataPtr(self, value):
		if isinstance(value, go.GoClass):
			_embedded.embedded_DataTable_DataPtr_Set(self.handle, value.handle)
		else:
			_embedded.embedded_DataTable_DataPtr_Set(self.handle, value)
	@property
	def SchemaPtr(self):
		return _embedded.embedded_DataTable_SchemaPtr_Get(self.handle)
	@SchemaPtr.setter
	def SchemaPtr(self, value):
		if isinstance(value, go.GoClass):
			_embedded.embedded_DataTable_SchemaPtr_Set(self.handle, value.handle)
		else:
			_embedded.embedded_DataTable_SchemaPtr_Set(self.handle, value)

# Python type for struct embedded.LoggingOptions
class LoggingOptions(go.GoClass):
	"""LoggingOptions is a public (embedded) copy of logging.LoggingOptions struct.\nSee logging.LoggingOptions for properties description\n"""
	def __init__(self, *args, **kwargs):
		"""
		handle=A Go-side object is always initialized with an explicit handle=arg
		otherwise parameters can be unnamed in order of field names or named fields
		in which case a new Go object is constructed first
		"""
		if len(kwargs) == 1 and 'handle' in kwargs:
			self.handle = kwargs['handle']
			_embedded.IncRef(self.handle)
		elif len(args) == 1 and isinstance(args[0], go.GoClass):
			self.handle = args[0].handle
			_embedded.IncRef(self.handle)
		else:
			self.handle = _embedded.embedded_LoggingOptions_CTor()
			_embedded.IncRef(self.handle)
			if  0 < len(args):
				self.ChannelCapacity = args[0]
			if "ChannelCapacity" in kwargs:
				self.ChannelCapacity = kwargs["ChannelCapacity"]
			if  1 < len(args):
				self.EmitTimeout = args[1]
			if "EmitTimeout" in kwargs:
				self.EmitTimeout = kwargs["EmitTimeout"]
			if  2 < len(args):
				self.WriteInterval = args[2]
			if "WriteInterval" in kwargs:
				self.WriteInterval = kwargs["WriteInterval"]
			if  3 < len(args):
				self.FlushInterval = args[3]
			if "FlushInterval" in kwargs:
				self.FlushInterval = kwargs["FlushInterval"]
	def __del__(self):
		_embedded.DecRef(self.handle)
	def __str__(self):
		pr = [(p, getattr(self, p)) for p in dir(self) if not p.startswith('__')]
		sv = 'embedded.LoggingOptions{'
		first = True
		for v in pr:
			if callable(v[1]):
				continue
			if first:
				first = False
			else:
				sv += ', '
			sv += v[0] + '=' + str(v[1])
		return sv + '}'
	def __repr__(self):
		pr = [(p, getattr(self, p)) for p in dir(self) if not p.startswith('__')]
		sv = 'embedded.LoggingOptions ( '
		for v in pr:
			if not callable(v[1]):
				sv += v[0] + '=' + str(v[1]) + ', '
		return sv + ')'
	@property
	def ChannelCapacity(self):
		return _embedded.embedded_LoggingOptions_ChannelCapacity_Get(self.handle)
	@ChannelCapacity.setter
	def ChannelCapacity(self, value):
		if isinstance(value, go.GoClass):
			_embedded.embedded_LoggingOptions_ChannelCapacity_Set(self.handle, value.handle)
		else:
			_embedded.embedded_LoggingOptions_ChannelCapacity_Set(self.handle, value)
	@property
	def EmitTimeout(self):
		return _embedded.embedded_LoggingOptions_EmitTimeout_Get(self.handle)
	@EmitTimeout.setter
	def EmitTimeout(self, value):
		if isinstance(value, go.GoClass):
			_embedded.embedded_LoggingOptions_EmitTimeout_Set(self.handle, value.handle)
		else:
			_embedded.embedded_LoggingOptions_EmitTimeout_Set(self.handle, value)
	@property
	def WriteInterval(self):
		return _embedded.embedded_LoggingOptions_WriteInterval_Get(self.handle)
	@WriteInterval.setter
	def WriteInterval(self, value):
		if isinstance(value, go.GoClass):
			_embedded.embedded_LoggingOptions_WriteInterval_Set(self.handle, value.handle)
		else:
			_embedded.embedded_LoggingOptions_WriteInterval_Set(self.handle, value)
	@property
	def FlushInterval(self):
		return _embedded.embedded_LoggingOptions_FlushInterval_Get(self.handle)
	@FlushInterval.setter
	def FlushInterval(self, value):
		if isinstance(value, go.GoClass):
			_embedded.embedded_LoggingOptions_FlushInterval_Set(self.handle, value.handle)
		else:
			_embedded.embedded_LoggingOptions_FlushInterval_Set(self.handle, value)

# Python type for struct embedded.OnlineFeatureService
class OnlineFeatureService(go.GoClass):
	""""""
	def __init__(self, *args, **kwargs):
		"""
		handle=A Go-side object is always initialized with an explicit handle=arg
		otherwise parameters can be unnamed in order of field names or named fields
		in which case a new Go object is constructed first
		"""
		if len(kwargs) == 1 and 'handle' in kwargs:
			self.handle = kwargs['handle']
			_embedded.IncRef(self.handle)
		elif len(args) == 1 and isinstance(args[0], go.GoClass):
			self.handle = args[0].handle
			_embedded.IncRef(self.handle)
		else:
			self.handle = _embedded.embedded_OnlineFeatureService_CTor()
			_embedded.IncRef(self.handle)
	def __del__(self):
		_embedded.DecRef(self.handle)
	def __str__(self):
		pr = [(p, getattr(self, p)) for p in dir(self) if not p.startswith('__')]
		sv = 'embedded.OnlineFeatureService{'
		first = True
		for v in pr:
			if callable(v[1]):
				continue
			if first:
				first = False
			else:
				sv += ', '
			sv += v[0] + '=' + str(v[1])
		return sv + '}'
	def __repr__(self):
		pr = [(p, getattr(self, p)) for p in dir(self) if not p.startswith('__')]
		sv = 'embedded.OnlineFeatureService ( '
		for v in pr:
			if not callable(v[1]):
				sv += v[0] + '=' + str(v[1]) + ', '
		return sv + ')'
	def GetEntityTypesMap(self, featureRefs):
		"""GetEntityTypesMap([]str featureRefs) object, str"""
		return Map_string_int32(handle=_embedded.embedded_OnlineFeatureService_GetEntityTypesMap(self.handle, featureRefs.handle))
	def GetEntityTypesMapByFeatureService(self, featureServiceName):
		"""GetEntityTypesMapByFeatureService(str featureServiceName) object, str"""
		return Map_string_int32(handle=_embedded.embedded_OnlineFeatureService_GetEntityTypesMapByFeatureService(self.handle, featureServiceName))
	def CheckForInstantiationError(self):
		"""CheckForInstantiationError() str"""
		return _embedded.embedded_OnlineFeatureService_CheckForInstantiationError(self.handle)
	def GetOnlineFeatures(self, featureRefs, featureServiceName, entities, requestData, fullFeatureNames, output):
		"""GetOnlineFeatures([]str featureRefs, str featureServiceName, object entities, object requestData, bool fullFeatureNames, object output) str"""
		return _embedded.embedded_OnlineFeatureService_GetOnlineFeatures(self.handle, featureRefs.handle, featureServiceName, entities.handle, requestData.handle, fullFeatureNames, output.handle)
	def StartGprcServer(self, host, port):
		"""StartGprcServer(str host, int port) str
		
		StartGprcServer starts gRPC server with disabled feature logging and blocks the thread
		"""
		return _embedded.embedded_OnlineFeatureService_StartGprcServer(self.handle, host, port)
	def StartGprcServerWithLoggingDefaultOpts(self, host, port, writeLoggedFeaturesCallback):
		"""StartGprcServerWithLoggingDefaultOpts(str host, int port, callable writeLoggedFeaturesCallback) str
		
		StartGprcServerWithLoggingDefaultOpts starts gRPC server with enabled feature logging but default configuration for logging
		Caller of this function must provide Python callback to flush buffered logs
		"""
		return _embedded.embedded_OnlineFeatureService_StartGprcServerWithLoggingDefaultOpts(self.handle, host, port, writeLoggedFeaturesCallback)
	def StartGprcServerWithLogging(self, host, port, writeLoggedFeaturesCallback, loggingOpts):
		"""StartGprcServerWithLogging(str host, int port, callable writeLoggedFeaturesCallback, object loggingOpts) str
		
		StartGprcServerWithLogging starts gRPC server with enabled feature logging
		Caller of this function must provide Python callback to flush buffered logs as well as logging configuration (loggingOpts)
		"""
		return _embedded.embedded_OnlineFeatureService_StartGprcServerWithLogging(self.handle, host, port, writeLoggedFeaturesCallback, loggingOpts.handle)
	def StartHttpServer(self, host, port):
		"""StartHttpServer(str host, int port) str
		
		StartHttpServer starts HTTP server with disabled feature logging and blocks the thread
		"""
		return _embedded.embedded_OnlineFeatureService_StartHttpServer(self.handle, host, port)
	def StartHttpServerWithLoggingDefaultOpts(self, host, port, writeLoggedFeaturesCallback):
		"""StartHttpServerWithLoggingDefaultOpts(str host, int port, callable writeLoggedFeaturesCallback) str
		
		StartHttpServerWithLoggingDefaultOpts starts HTTP server with enabled feature logging but default configuration for logging
		Caller of this function must provide Python callback to flush buffered logs
		"""
		return _embedded.embedded_OnlineFeatureService_StartHttpServerWithLoggingDefaultOpts(self.handle, host, port, writeLoggedFeaturesCallback)
	def StartHttpServerWithLogging(self, host, port, writeLoggedFeaturesCallback, loggingOpts):
		"""StartHttpServerWithLogging(str host, int port, callable writeLoggedFeaturesCallback, object loggingOpts) str
		
		StartHttpServerWithLogging starts HTTP server with enabled feature logging
		Caller of this function must provide Python callback to flush buffered logs as well as logging configuration (loggingOpts)
		"""
		return _embedded.embedded_OnlineFeatureService_StartHttpServerWithLogging(self.handle, host, port, writeLoggedFeaturesCallback, loggingOpts.handle)
	def StopHttpServer(self, goRun=False):
		"""StopHttpServer() """
		_embedded.embedded_OnlineFeatureService_StopHttpServer(self.handle, goRun)
	def StopGrpcServer(self, goRun=False):
		"""StopGrpcServer() """
		_embedded.embedded_OnlineFeatureService_StopGrpcServer(self.handle, goRun)

# Python type for struct embedded.OnlineFeatureServiceConfig
class OnlineFeatureServiceConfig(go.GoClass):
	""""""
	def __init__(self, *args, **kwargs):
		"""
		handle=A Go-side object is always initialized with an explicit handle=arg
		otherwise parameters can be unnamed in order of field names or named fields
		in which case a new Go object is constructed first
		"""
		if len(kwargs) == 1 and 'handle' in kwargs:
			self.handle = kwargs['handle']
			_embedded.IncRef(self.handle)
		elif len(args) == 1 and isinstance(args[0], go.GoClass):
			self.handle = args[0].handle
			_embedded.IncRef(self.handle)
		else:
			self.handle = _embedded.embedded_OnlineFeatureServiceConfig_CTor()
			_embedded.IncRef(self.handle)
			if  0 < len(args):
				self.RepoPath = args[0]
			if "RepoPath" in kwargs:
				self.RepoPath = kwargs["RepoPath"]
			if  1 < len(args):
				self.RepoConfig = args[1]
			if "RepoConfig" in kwargs:
				self.RepoConfig = kwargs["RepoConfig"]
	def __del__(self):
		_embedded.DecRef(self.handle)
	def __str__(self):
		pr = [(p, getattr(self, p)) for p in dir(self) if not p.startswith('__')]
		sv = 'embedded.OnlineFeatureServiceConfig{'
		first = True
		for v in pr:
			if callable(v[1]):
				continue
			if first:
				first = False
			else:
				sv += ', '
			sv += v[0] + '=' + str(v[1])
		return sv + '}'
	def __repr__(self):
		pr = [(p, getattr(self, p)) for p in dir(self) if not p.startswith('__')]
		sv = 'embedded.OnlineFeatureServiceConfig ( '
		for v in pr:
			if not callable(v[1]):
				sv += v[0] + '=' + str(v[1]) + ', '
		return sv + ')'
	@property
	def RepoPath(self):
		return _embedded.embedded_OnlineFeatureServiceConfig_RepoPath_Get(self.handle)
	@RepoPath.setter
	def RepoPath(self, value):
		if isinstance(value, go.GoClass):
			_embedded.embedded_OnlineFeatureServiceConfig_RepoPath_Set(self.handle, value.handle)
		else:
			_embedded.embedded_OnlineFeatureServiceConfig_RepoPath_Set(self.handle, value)
	@property
	def RepoConfig(self):
		return _embedded.embedded_OnlineFeatureServiceConfig_RepoConfig_Get(self.handle)
	@RepoConfig.setter
	def RepoConfig(self, value):
		if isinstance(value, go.GoClass):
			_embedded.embedded_OnlineFeatureServiceConfig_RepoConfig_Set(self.handle, value.handle)
		else:
			_embedded.embedded_OnlineFeatureServiceConfig_RepoConfig_Set(self.handle, value)


# ---- Slices ---


# ---- Maps ---


# ---- Constructors ---
def NewOnlineFeatureService(conf, transformationCallback):
	"""NewOnlineFeatureService(object conf, callable transformationCallback) object"""
	return OnlineFeatureService(handle=_embedded.embedded_NewOnlineFeatureService(conf.handle, transformationCallback))


# ---- Functions ---


