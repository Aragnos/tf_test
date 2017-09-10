from tinkerforge.ip_connection import IPConnection
from datetime import datetime
import sys
import Datenbank as DB
import ErrorClass as Error
import time
import config
import Sensor
import WLAN

# todo: connect sensors, PyToSh: root password, WLAN,
# Todo: test all
# todo opt: LCD Script

# Database stuff
database_host = config.DATABASE_HOST
database_port = config.DATABASE_PORT
user = config.DATABASE_USER
password = config.DATABASE_PASSWORD
database = config.DATABASE_NAME


def build_dictionaries():
	"""Build sensor dictionary from bricklet UIDS

		Run through each bricklet and check, if it should be connected
		Add these bricklets and corresponding uids to a dictionary, respectively.

		:returns: Two dictionaries with bricklets and uids
		"""
	rel_sensors = {}
	rel_uids = {}
	# not all sensors should be connected
	if config.ALL == '0':
		if config.AMBIENT == 1:
			rel_sensors.update({"ambient_light": 1})
			rel_uids.update({"ambient_light": config.UID_AMBIENT})
		if config.BAROMETER == 1:
			rel_sensors.update({"barometer": 1})
			rel_uids.update({"barometer": config.UID_BAROMETER})
		if config.HUMIDITY == 1:
			rel_sensors.update({"humidity": 1})
			rel_uids.update({"humidity": config.UID_HUMIDITY})
		if config.LCD == 1:
			rel_sensors.update({"lcd": 1})
			rel_uids.update({"lcd": config.UID_LCD})
		if config.MOISTURE == 1:
			rel_sensors.update({"moisture": 1})
			rel_uids.update({"moisture": config.UID_MOISTURE})
		if config.TEMPERATURE == 1:
			rel_sensors.update({"temperature": 1})
			rel_uids.update({"temperature": config.UID_TEMPERATURE})
		if config.THERMOCOUPLE == 1:
			rel_sensors.update({"thermocouple": 1})
			rel_uids.update({"thermocouple": config.UID_THERMOCOUPLE})
	else:
		rel_sensors = {
			"ambient_light": 1,
			"barometer": 1,
			"humidity": 1,
			"lcd": 1,
			"moisture": 1,
			"temperature": 1,
			"thermocouple": 1}
		rel_uids.update({"ambient_light": config.UID_AMBIENT})
		rel_uids.update({"barometer": config.UID_BAROMETER})
		rel_uids.update({"humidity": config.UID_HUMIDITY})
		rel_uids.update({"lcd": config.UID_LCD})
		rel_uids.update({"moisture": config.UID_MOISTURE})
		rel_uids.update({"temperature": config.UID_TEMPERATURE})
		rel_uids.update({"thermocouple": config.UID_THERMOCOUPLE})
	return [rel_sensors, rel_uids]


# --------------------------------------------------
# Main program procedure
# --------------------------------------------------

# Build dictionary from bricklet UIDS
[relevant_sensors, relevant_uids] = build_dictionaries()
# connect to daemon via ipconnection
ipcon = IPConnection()
# connect sensors
connected_sensors = Sensor.connect_sensors(relevant_sensors, relevant_uids, ipcon)
# quit()

# LCD connected?
# 	Success: Wait for user input, Failure: continue
# Loop forever
while True:
	# get sensor values
	sensor_values = {}
	for sensor in connected_sensors:
		#new_value = Sensor.get_value(connected_sensors[sensor])
		new_value = 0
		sensor_values.update({sensor: new_value})
	# WLAN configured # todo later
	# WLAN available?
	db_available = False
	db_conn = []

	try:
		WLAN.check_interface()
	except WindowsError:
		print('Wrong system.')
	except Error.InterfaceError:
		WLAN.restart_interface(config.INTERFACE_NAME)
		try:
			WLAN.check_interface()
		except WindowsError:
			print('Wrong system.')
		except Error.InterfaceError:
			db_available = False
	finally:
		# Try to ping database host
		try:
			WLAN.check_connection(database_host, 4)
		except Error.InterfaceError:
			db_available = False
		except Error.ConnectionError:
			db_available = False
		else:
			# Try to connect to database
			try:
				db_conn = DB.connect_database(host=database_host, port=database_port, user=user, passwd=password,
											db=database)
			except Error.DatabaseError:
				db_available = False
			else:
				db_available = True

	# current time
	timestamp = "{:%Y-%m-%d %H:%M:%S}".format(datetime.now())
	quit()
	if db_available:
		#
		# Success: Save sensor values to DB
		"""db_statement = "INSERT INTO `" + sensor + "` (`wert`) VALUES ('" + str(get_value(sensor)) + "')"
			cur.execute(db_statement)
			conn.commit()
		"""
		pass
	else:
		# Failure: Save sensor values to SD Card
		"""
		ambient_file = open('Ambientlight.txt', 'a')
		timestamp = "{:%Y/%m/%d %H:%M:%S}" % (local_time[0], local_time[1], local_time[2], local_time[3], local_time[4])
		write_str = "%s\t%d\n" % (timestamp, illuminance)
		ambient_file.write(write_str)
		ambient_file.close()
		"""
		pass
	# 	Sleep
	if db_conn == '[ ]':
		# todo delete
		break

"""
try:
	conn = DB.connect_database(host=database_host, port=database_port, user=user, passwd=password, db=database)
	# any sensor data in files? Yes: Save these to db. No: continue.
	# save sensor data to database
except ErrorClass.DatabaseError as e:
	print(e.message)
	# save sensor data to file

# LCD.connect_lcd()


sensor_file = open('Test.txt', 'a')
for i in range(0, 10):
	timestamp = "{:%Y-%m-%d %H:%M:%S}".format(datetime.datetime.now())
	write_str = "%s \t %d\n" % (timestamp, i)
	sensor_file.write(write_str)
	#print(write_str)
	time.sleep(1)
sensor_file.close()
"""
