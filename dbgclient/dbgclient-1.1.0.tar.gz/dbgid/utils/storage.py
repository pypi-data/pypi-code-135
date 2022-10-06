import json
class dbgStorage():
  def save(file : str, flag : str, content : str):
    with open(file,flag) as fh:
      fh.write(content)
      fh.close()
  def read(file : str, flag : str = 'r'):
    return open(file,flag).read()
  def readBinary(file : str, flag : str = 'rb'):
    return open(file,flag).read()
  def readLine(file : str, flag : str = 'r') -> list:
    return open(file,flag).readlines()
  def readJson(file : str, flag : str = 'r') -> dict:
    return json.loads(open(file,flag).read())