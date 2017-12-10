import time
from datetime import datetime

from tinkerforge.ip_connection import IPConnection
import ErrorClass as Error
import Sensor
import WLAN
import config
from Database import Database
from MemoryCard import MemoryCard

# todo: WLAN,
# Todo: test all
# todo opt: LCD Script
# todo change hardcoded strings to variables
# Database stuff
database_host = config.DATABASE_HOST
database_port = config.DATABASE_PORT
user = config.DATABASE_USER
password = config.DATABASE_PASSWORD
database = config.DATABASE_NAME
path = 'Werte'


def build_dictionaries():
	# todo refactor to new module
	"""Build sensor dictionary from bricklet UIDS

		Run through each bricklet and check, if it should be connected
		Add these bricklets and corresponding uids to a dictionary, respectively.

		:returns: Two dictionaries with bricklets and uids
		"""
	rel_sensors = {}
	rel_uids = {}
	# not all sensors should be connected
	if config.ALL == '0':
		if config.AMBIENT == '1':
			rel_sensors.update({"ambient_light": 1})
			rel_uids.update({"ambient_light": config.UID_AMBIENT})
		if config.BAROMETER == '1':
			rel_sensors.update({"barometer": 1})
			rel_uids.update({"barometer": config.UID_BAROMETER})
		if config.HUMIDITY == '1':
			rel_sensors.update({"humidity": 1})
			rel_uids.update({"humidity": config.UID_HUMIDITY})
		if config.LCD == '1':
			rel_sensors.update({"lcd": 1})
			rel_uids.update({"lcd": config.UID_LCD})
		if config.MOISTURE == '1':
			rel_sensors.update({"moisture": 1})
			rel_uids.update({"moisture": config.UID_MOISTURE})
		if config.TEMPERATURE == '1':
			rel_sensors.update({"temperature": 1})
			rel_uids.update({"temperature": config.UID_TEMPERATURE})
		if config.THERMOCOUPLE == '1':
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


def check_and_connect_database():
	db = None
	try:
		db = Database(host=database_host, port=database_port, user=user, password=password, database=database)
	except Error.DatabaseError:
		# db not available. If WLAN should be configured, try to get it back up
		if config.WLAN_CONFIGURED == '1':
			try:
				WLAN.check_interface()
			except WindowsError:
				print('Wrong system.')
			except Error.InterfaceError:
				# try to restart WLAN three times
				for x in range(0, 3):
					WLAN.restart_interface(config.INTERFACE_NAME)
					try:
						WLAN.check_interface()
					except WindowsError:
						print('Wrong system.')
					except Error.InterfaceError:
						pass
					else:
						# WLAN is back up -> one more try to connect to database
						try:
							db = Database(
								host=database_host, port=database_port, user=user, password=password, database=database
							)
						except Error.DatabaseError:
							pass
	return db


# --------------------------------------------------
# Main program procedure
# --------------------------------------------------

if __name__ == "__main__":
	# Build dictionary from bricklet UIDS
	[relevant_sensors, relevant_uids] = build_dictionaries()
	# connect to daemon via ipconnection
	ipcon = IPConnection()
	# connect sensors
	connected_sensors = Sensor.connect_sensors(relevant_sensors, relevant_uids, ipcon)

	ipcon.connect('localhost', 4223)

	# extract list of connected sensors
	con_sensors_list = []
	for sen in connected_sensors:
		con_sensors_list.append(sen)
	# create MemoryCard Instance
	memo = MemoryCard(con_sensors_list, path)
	# Loop forever
	while True:
		# get sensor values
		sensor_values = {}
		for sensor in connected_sensors:
			try:
				new_value = Sensor.get_value(connected_sensors[sensor])
				sensor_values.update({sensor: new_value})
			except Exception as e:
				print(e)
		# WLAN configured
		# Connection to database possible
		db_obj = check_and_connect_database()
		# current time
		timestamp = "{:%Y-%m-%d %H:%M:%S}".format(datetime.now())

		# Evaluates to True, if db_obj is not None
		if db_obj:
			# function is used in memo, to save things to database -> MemoryCard needs no knowledge about the
			# actual method
			save_db_method = db_obj.save_db
			# Write previous sensor values from SD to DB?
			memo.save_sd_to_db(save_db_method)
			# Save sensor values to DB
			db_obj.save_db(sensor_values, timestamp)
		else:
			# Save sensor values to SD Card
			memo.save_sd(sensor_values, timestamp)
		# Sleep
		time.sleep(10)
