import pymysql
from ErrorClass import DatabaseError


class Database:

	def __init__(self, host, port, user, password, database):
		"""
		:param host: host name of database
		:param port: port of database
		:param user: name of the user for database
		:param password: password for database
		:param database: specific name of the database to use
		"""
		self.host = host
		self.port = port
		self.user = user
		self.password = password
		self.db = database
		self.connection = None
		self.cursor = None
		self.connect_database()

	def connect_database(self):
		""" Tries to connect to the database.
			Raises Database Error """
		try:
			self.connection = pymysql.connect(
				host=self.host, port=int(self.port), user=self.user, passwd=self.password, db=self.db
			)
			self.cursor = self.connection.cursor()
		except Exception as e:
			print(e)
			raise DatabaseError("Connection to Database failed")

	def save_db(self, sen_values, timestamp):
		"""
		Save sensor values to database
		:param sen_values: dictionary like {sensor_name: value}
		:param timestamp: time which should be put in the database
		"""

		for sensor in sen_values:
			if sensor == 'lcd':
				continue
			# Write data to database
			db_statement = "INSERT INTO `" + sensor + "` (`datum`, `wert`) VALUES ('" + timestamp + "', '" + str(
				sen_values[sensor]) + "')"
			self.cursor.execute(db_statement)
		# Commit changes onto the database
		self.connection.commit()
