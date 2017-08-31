""" Test file. If DB-connection is lost,  save sensor data to file """


import Datenbank as DB
import ErrorClass

database_host = "localhost"
database_port = 3306
user = "Red"
passwd = "red-brick42"
database = "tf"

"""
try:
	conn = DB.connect_database(database_host, database_port, user, passwd, database)
	# any sensor data in files? Yes: Save these to db. No: continue.
	# TODO
	sensor_file = open('Test.txt', 'a')
	# save sensor data to database
except ErrorClass.DatabaseError as e:
	print(e.msg)
	# TODO
	# save sensor data to file
	sensor_file = open('Test.txt', 'a')
	sensor_file.close()
"""

from TestProperties import Celsius

c = Celsius(-200)
print(c.temperature)
