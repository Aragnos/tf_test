import time
from datetime import datetime

from tinkerforge.ip_connection import IPConnection
import ErrorClass as Error
import Sensor
import WLAN
import config_test
import SensorBuilder
from Database import Database
from MemoryCard import MemoryCard

# todo: WLAN,
# Todo: test all
# todo opt: LCD Script
# todo change hardcoded strings to variables
# Database stuff
database_host = config_test.DATABASE_HOST
database_port = config_test.DATABASE_PORT
user = config_test.DATABASE_USER
password = config_test.DATABASE_PASSWORD
database = config_test.DATABASE_NAME
path = 'Werte'

def check_and_connect_database():
	# todo refac
	db = None
	try:
		db = Database(host=database_host, port=database_port, user=user, password=password, database=database)
	except Error.DatabaseError:
		# db not available. If WLAN should be configured, try to get it back up
		if config_test.WLAN_CONFIGURED == '1':
			try:
				WLAN.check_interface()
			except WindowsError:
				print('Wrong system.')
			except Error.InterfaceError:
				# try to restart WLAN three times
				for x in range(0, 3):
					WLAN.restart_interface(config_test.INTERFACE_NAME)
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
	ipcon = IPConnection()
	# connect sensors
	connected_sensors = SensorBuilder.create_sensor_objects(ipcon)
	# connect to daemon via ipconnection
	ipcon.connect('localhost', 4223)

	# Loop forever
	while True:
		# get sensor values
		sensor_values = SensorBuilder.poll_values(connected_sensors)
		# extract list of connected sensors for MemoryCard Object
		con_sensors_list = []
		for sen in connected_sensors:
			con_sensors_list.append(sen)
		# create MemoryCard Instance
		memo = MemoryCard(con_sensors_list, path)
		# WLAN configured
		# Connection to database possible
		db_obj = check_and_connect_database()
		# current time
		timestamp = "{:%Y-%m-%d %H:%M:%S}".format(datetime.now())

		# Evaluates to True, if db_obj is not None
		if db_obj:
			# function is used in memo, to save things to database
			# -> MemoryCard needs no knowledge about the actual method
			save_db_method = db_obj.save_db
			# Write previous sensor values from SD to DB
			memo.save_sd_to_db(save_db_method)
			# Save sensor values to DB
			db_obj.save_db(sensor_values, timestamp)
		else:
			# Save sensor values to SD Card
			memo.save_sd(sensor_values, timestamp)
		# Sleep
		time.sleep(10)
