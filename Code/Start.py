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


def build_dictionary():
	# todo no need
	"""Build sensor dictionary from bricklet UIDS"""
	rel_sens = {}
	if config.RELEVANT == '1':
		if config.AMBIENT == 1:
			rel_sens.update({"ambient_light": 1})
		if config.BAROMETER == 1:
			rel_sens.update({"barometer": 1})
		if config.HUMIDITY == 1:
			rel_sens.update({"humidity": 1})
		if config.LCD == 1:
			rel_sens.update({"lcd": 1})
		if config.MOISTURE == 1:
			rel_sens.update({"moisture": 1})
		if config.TEMPERATURE == 1:
			rel_sens.update({"temperature": 1})
		if config.THERMOCOUPLE == 1:
			rel_sens.update({"thermocouple": 1})
		return rel_sens
	else:
		sensors = {
			"ambient_light": 1,
			"barometer": 1,
			"humidity": 1,
			"lcd": 1,
			"moisture": 1,
			"temperature": 1,
			"thermocouple": 1}
	return sensors


# --------------------------------------------------
# Main program procedure
# --------------------------------------------------

# Build dictionary from bricklet UIDS
relevant_sensors = build_dictionary()


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
