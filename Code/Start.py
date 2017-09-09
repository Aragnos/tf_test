import sys
import Datenbank as DB
import ErrorClass
import time
import datetime
import config
# todo: connect sensors, PyToSh: root password, WLAN,
# Todo: test all
# todo opt: LCD Script

# Database stuff
database_host = config.DATABASE_HOST
database_port = config.DATABASE_PORT
user = config.DATABASE_USER
password = config.DATABASE_PASSWORD
database = config.DATABASE_NAME
# Build dictionary from bricklet UIDS


# connect sensors
# LCD connected?
# 	Success: Wait for user input, Failure: continue
# WLAN available?
# Loop forever
# 	get sensor values
# 	Try to connect to DB
# 		Success: Save sensor values to DB, Failure: Save sensor values to SD Card
# 	Sleep
try:
	conn = DB.connect_database(host=database_host, port=database_port, user=user, passwd=password, db=database)
	# any sensor data in files? Yes: Save these to db. No: continue.
	# save sensor data to database
except ErrorClass.DatabaseError as e:
	print(e.message)
	# save sensor data to file

# LCD.connect_lcd()

"""
sensor_file = open('Test.txt', 'a')
for i in range(0, 10):
	timestamp = "{:%Y-%m-%d %H:%M:%S}".format(datetime.datetime.now())
	write_str = "%s \t %d\n" % (timestamp, i)
	sensor_file.write(write_str)
	#print(write_str)
	time.sleep(1)
sensor_file.close()
"""
