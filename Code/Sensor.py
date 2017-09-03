from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_ambient_light_v2 import BrickletAmbientLightV2
from tinkerforge.bricklet_barometer import BrickletBarometer
from tinkerforge.bricklet_humidity import BrickletHumidity
from tinkerforge.bricklet_lcd_20x4 import BrickletLCD20x4
from tinkerforge.bricklet_moisture import BrickletMoisture
from tinkerforge.bricklet_temperature import BrickletTemperature
from tinkerforge.bricklet_thermocouple import BrickletThermocouple
from tinkerforge.ip_connection import Error as IP_Error
import SensorFactory
import sys
""" Connect to sensors and get sensor data"""
""" 
use instance of (isinatance()) to get the corresponding sensor, so only one generic method is called from main program,
set uid from config file
"""
# TODO delete dependencies: Factory, sys, IP_Error?
# TODO set uids?


def connect_sensors(sensors, uids, ipcon):
	# Dictionary with all connected sensors
	con_sensors = {}
	if sensors["ambient_light"] == 1:
		al = BrickletAmbientLightV2(uids["ambient_light"], ipcon)
		con_sensors.update({"ambient_light": al})
	if sensors["barometer"] == 1:
		barometer = BrickletBarometer(uids["barometer"], ipcon)
		con_sensors.update({"barometer": barometer})
	if sensors["humidity"] == 1:
		humidity = BrickletHumidity(uids["humidity"], ipcon)
		con_sensors.update({"humidity": humidity})
	if sensors["lcd"] == 1:
		lcd = BrickletLCD20x4(uids["lcd"], ipcon)
		con_sensors.update({"lcd": lcd})
	if sensors["moisture"] == 1:
		moisture = BrickletMoisture(uids["moisture"], ipcon)
		con_sensors.update({"moisture": moisture})
	if sensors["temperature"] == 1:
		temperature = BrickletTemperature(uids["temperature"], ipcon)
		con_sensors.update({"temperature": temperature})
	if sensors["thermo_couple"] == 1:
		thermo = BrickletThermocouple(uids["thermo_couple"], ipcon)
		con_sensors.update({"thermo_couple": thermo})
	return con_sensors


def get_value(sensor):
	if isinstance(sensor, BrickletAmbientLightV2):
		return sensor.get_illuminance()
	if isinstance(sensor, BrickletBarometer):
		# zweiter Barometer Wert
		return sensor.get_air_pressure() / 1000.0
	# altitude = barometer.get_altitude()
	if isinstance(sensor, BrickletHumidity):
		return sensor.get_humidity() / 10.0
	if isinstance(sensor, BrickletMoisture):
		return sensor.get_moisture_value()
	if isinstance(sensor, BrickletTemperature) or isinstance(sensor, BrickletThermocouple):
		return sensor.get_temperature() / 100.0


if __name__ == "__main__":
	# sensor with 1 are connected, with 0 not
	_sensors = {
		"ambient_light": 1,
		"barometer": 1,
		"humidity": 1,
		"lcd": 0,
		"moisture": 1,
		"temperature": 1,
		"thermo_couple": 1}

	# bricklet UIDs
	UID_AMBIENT = "yBG"  # UID of Ambient Light Bricklet 2.0
	UID_BAROMETER = "ytN"  # UID for Barometer Bricklet
	UID_HUMIDITY = "Cd7"  # UID for Humidity Bricklet
	UID_LCD = "BFX"  # UID of LCD Display
	UID_MOISTURE = "zSG"  # UID for Moisture Bricklet
	UID_TEMPERATURE = "zbS"  # UID for Temperature Bricklet
	UID_THERMO = "B8k"  # UID for Thermocouple Bricklet

	# dictionary with sensor UIDs
	_sensor_uid = {
		"ambient_light": UID_AMBIENT,
		"barometer": UID_BAROMETER,
		"humidity": UID_HUMIDITY,
		"lcd": UID_LCD,
		"moisture": UID_MOISTURE,
		"temperature": UID_TEMPERATURE,
		"thermo_couple": UID_THERMO}

	# Create IP connection
	_ipcon = IPConnection()

	attached_sensors = connect_sensors(_sensors, _sensor_uid, _ipcon)
	fac_sen = SensorFactory.Sensor()
	for sen in attached_sensors:
		try:
			print(get_value(attached_sensors[sen]))
		except IP_Error:
			sensor_val = fac_sen.get_val(attached_sensors[sen])
			output = "%s \t %s" % (sen, sensor_val)
			print(output)
