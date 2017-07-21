#!/usr/bin/env python
# -*- coding: utf-8 -*-
# all import stuff is done here, e.g. Bricklet API
import sys
import time
import os
from datetime import datetime
import pymysql
from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_ambient_light_v2 import BrickletAmbientLightV2
from tinkerforge.bricklet_barometer import BrickletBarometer
from tinkerforge.bricklet_humidity import BrickletHumidity
from tinkerforge.bricklet_lcd_20x4 import BrickletLCD20x4
from tinkerforge.bricklet_moisture import BrickletMoisture
from tinkerforge.bricklet_temperature import BrickletTemperature
from tinkerforge.bricklet_thermocouple import BrickletThermocouple

sys.path.append('../')

# host and port this programm should connect to
# keep localhost while connceted to PC
HOST = "localhost"
PORT = 4223

# collection of our bricklets UIDs
UID_AMBIENT = "yBG"  # UID of Ambient Light Bricklet 2.0
UID_BAROMETER = "ytN"  # UID for Barometer Bricklet
UID_HUMIDITY = "Cd7"  # UID for Humidity Bricklet
UID_LCD = "BFX"  # UID of LCD Display
UID_MOISTURE = "zSG"  # UID for Moisture Bricklet
UID_TEMPERATURE = "zbS"  # UID for Temperature Bricklet
UID_THERMO = "B8k"  # UID for Termocouple Bricklet

# bricklet objects
# Attention: These are global variables and may not be set to the expected
# connections but strings, so use them very carefully
al = ""
barometer = ""
humidity = ""
lcd = ""
moisture = ""
temperature = ""
thermo = ""


# Handles interrupt signal and exit gracefully
def signal_handler(signal, frame):
	print('Caught Keyboard Interrupt')
	unload()


def connect_sensors():
	global al
	global barometer
	global humidity
	global lcd
	global moisture
	global temperature
	global thermo

	if sensors["ambient_light"] == 1:
		al = BrickletAmbientLightV2(UID_AMBIENT, ipcon)
	if sensors["barometer"] == 1:
		barometer = BrickletBarometer(UID_BAROMETER, ipcon)
	if sensors["humidity"] == 1:
		humidity = BrickletHumidity(UID_HUMIDITY, ipcon)
	if sensors["lcd"] == 1:
		lcd = BrickletLCD20x4(UID_LCD, ipcon)
	if sensors["moisture"] == 1:
		moisture = BrickletMoisture(UID_MOISTURE, ipcon)
	if sensors["temperature"] == 1:
		temperature = BrickletTemperature(UID_TEMPERATURE, ipcon)
	if sensors["thermo_couple"] == 1:
		thermo = BrickletThermocouple(UID_THERMO, ipcon)


def get_value(sensor):
	if sensor == "ambient_light":
		return al.get_illuminance() / 100.0
	if sensor == "barometer":
		# zweiter Barometer Wert
		return barometer.get_air_pressure() / 1000.0
	# altitude = barometer.get_altitude()
	if sensor == "humidity":
		return humidity.get_humidity() / 10.0
	if sensor == "moisture":
		return moisture.get_moisture_value()
	if sensor == "temperature":
		return temperature.get_temperature() / 100.0
	if sensor == "thermo_couple":
		return thermo.get_temperature() / 100.0


# Called before exiting the script
def unload():
	# tear down db and brick connection and exit script
	# cur.close()
	# conn.close()
	ipcon.disconnect()
	os._exit(0)


if __name__ == "__main__":
	ipcon = IPConnection()  # Create IP connection
	# Create device objects for bricklets given in list sensors
	sensors = {
		"ambient_light": 1,
		"barometer": 0,
		"humidity": 0,
		"lcd": 0,
		"moisture": 0,
		"temperature": 0,
		"thermo_couple": 0}

	# connect to the sensors
	connect_sensors()

	ipcon.connect(HOST, PORT)  # Connect to brickd
	# Don't use device before ipcon is connected

	# set Ambient Light configuration to avoid saturation
	if sensors["ambient_light"] == 1:
		al.set_configuration(0, 2)

	# Connect to database
	"""
	conn = pymysql.connect(host="192.168.0.20", port=3306, user='Red', passwd='red-brick42', db='tf')
	cur = conn.cursor()
	
	# activate signal handler
	signal.signal(signal.SIGINT, signal_handler)

	# write values to database
	
	for sensor in sensors:
		if sensors[sensor] == 1 and sensor != "lcd":
			# Fallunterscheidung barometer
			db_statement = "INSERT INTO `" + sensor + "` (`wert`) VALUES ('" + str(get_value(sensor)) + "')"
			cur.execute(db_statement)
	conn.commit()
	"""
	# ambient_file = open('Ambientlight.txt', 'a')
	illuminance = al.get_illuminance() / 100.0

	timestamp = "{:%Y-%m-%d %H:%M:%S}".format(datetime.now())
	print(timestamp)
	# timestamp = "{:%Y/%m/%d %H:%M:%S}" % (local_time[0], local_time[1], local_time[2], local_time[3], local_time[4])
	# write_str = "%s\t%d\n" % (timestamp, illuminance)
	# ambient_file.write(write_str)
	# ambient_file.close()
	# on exit
	unload()
