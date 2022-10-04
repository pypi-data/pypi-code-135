import logging
import pymysql

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class MyMysql:
	def __init__(self, db_host, db_port, db_user, db_password, db_name):
		self.host = db_host
		self.port = db_port
		self.username = db_user
		self.password = db_password
		self.db_name = db_name
		self.conn = None

	def open_connection(self):
		try:
			if self.conn is None:
				self.conn = pymysql.connect(
					host=self.host,
					port=self.port,
					user=self.username,
					password=self.password,
					database=self.db_name,
					charset='utf8mb4',
					cursorclass=pymysql.cursors.DictCursor,
					connect_timeout=5
				)
		except Exception as e:
			logging.error(str(e))

	def run_query(self, query):
		try:
			self.open_connection()
			with self.conn.cursor() as cur:
				if 'SELECT' in query or 'select' in query:
					cur.execute(query)
					result = cur.fetchall()
					cur.close()
					return result
				else:
					cur.execute(query)
					self.conn.commit()
					cur.close()
		except Exception as e:
			logging.error(str(e))
		finally:
			if self.conn is not None:
				self.conn.close()
				self.conn = None
