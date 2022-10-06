import requests as req
from bs4 import BeautifulSoup as DOM
from dbgid.utils.debug import dbgLogger
class BaseClient(dbgLogger):
  def __init__(self,url : str, verbose : bool = False):
    self._url = url
    self._verbose = dbgLogger().debug(verbose)
  def _get_text_element_by_class(self, element : bytes , tag : str, selector : str):
    self._sop = DOM(element,'html.parser')
    return self._sop.find(tag,attrs={'class':selector}).get_text()
  def _get_input_value_by_name(self,element : bytes, name : str):
    self._sop = DOM(element,'html.parser')
    return self._sop.findAll('input',attrs={'name':name})[0]['value']
  def _get_input_value_by_id(self,element : bytes, id : str):
    self._sop = DOM(element,'html.parser')
    return self._sop.findAll('input',attrs={'id':id})[0]['value']
  def _get(self,headers : dict):
    self._session = req.Session()
    self._res = self._session.get(self._url,headers=headers)
    return self._res.content
  def _post(self, headers : dict, data : dict, json : bool =False):
    self._session = req.Session()
    self._res = self._session.post(self._url,headers=headers,data=data)
    if json == True:
      return self._res.json()
    else:
      return self._res.content
  def _post_json(self, headers : dict, json : dict):
    self._session = req.Session()
    self._res = self._session.post(self._url,headers=headers,json=json).json()
    return self.res