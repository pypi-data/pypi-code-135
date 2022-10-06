from faker import Faker
import random,string
class dbgFaker():
  def __init__(self,locale : str = 'id_ID'):
    self._db=Faker(locale)
  def getData(self) -> dict:
    self._username = self._db.user_name()
    self._password = self._db.password()
    self._name = self._db.name()
    self._phone = '+62'+str(random.choice([812,813,857,878,895,896]))+''.join(random.choice(string.digits) for _ in range(8))
    self._ua = self._db.user_agent()
    return {'name': self._name, 'username': self._username, 'password': self._password, 'phone': self._phone, 'useragent': self._ua}