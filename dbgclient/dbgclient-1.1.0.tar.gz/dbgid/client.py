from dbgid.core.httpclient import BaseClient
import sys
class DbgHttp:
  def __init__(self, url : str, verbose : bool =False):
    self._url = url
    self._verbose = verbose
  def __enter__(self):
    return BaseClient(self._url,verbose=self._verbose)
  def __exit__(self,exc_type, exc_value, traceback):
    return