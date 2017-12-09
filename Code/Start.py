﻿from tinkerforge.ip_connection import IPConnection
from datetime import datetime
import sys
from Database import Database
import ErrorClass as Error
import time
import config
import Sensor
import WLAN
from tinkerforge.ip_connection import Error as IP_Error
import FileConnector

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


def save_sd():
	"""Saves sensor values to sd card"""
	opened_files = FileConnector.open_files(connected_sensors, 'a')
	FileConnector.write_files(sensor_values, opened_files, timestamp)
	FileConnector.close_files(opened_files)
	return


def save_sd_to_db():
	"""Save temporary value from SD to database"""
	# Get values saved on sd
	open_files = []
	try:
		open_files = FileConnector.open_files(connected_sensors, 'r')
	except Exception as e:
		print(e)
		pass
	for f in open_files:
		values = FileConnector.check_and_return(open_files[f])
		print(len(values))
		for value in values:
			# timestamp on 0, sensor value on 1
			splitted_value = value.split('\t')
			tmp_dic = {f: splitted_value[1]}
			# save values to database
			db_obj.save_db(tmp_dic, splitted_value[0])
	FileConnector.close_files(open_files)
	FileConnector.delete_files()
	return

	
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

	# Loop forever
	while True:
		# get sensor values
		sensor_values = {}
		for sensor in connected_sensors:
			try:
				# todo for test reasons use try structure
				new_value = Sensor.get_value(connected_sensors[sensor])
				sensor_values.update({sensor: new_value})
			except Exception as e:
				print(e)
				pass
		# WLAN configured
		# Connection to database possible
		db_obj = check_and_connect_database()
		# current time
		timestamp = "{:%Y-%m-%d %H:%M:%S}".format(datetime.now())

		# Evaluates to True, if db_obj is not None
		if db_obj:
			#
			# Success:
			# Sensor values  written in files on SD?
			# Save sensor values to DB
			save_sd_to_db()
			db_obj.save_db(sensor_values, timestamp)
		else:
			# Failure: Save sensor values to SD Card
			save_sd()
		# Sleep
		time.sleep(10)