from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_ambient_light_v2 import BrickletAmbientLightV2
from tinkerforge.bricklet_barometer import BrickletBarometer
from tinkerforge.bricklet_humidity import BrickletHumidity
from tinkerforge.bricklet_lcd_20x4 import BrickletLCD20x4
from tinkerforge.bricklet_moisture import BrickletMoisture
from tinkerforge.bricklet_temperature import BrickletTemperature
from tinkerforge.bricklet_thermocouple import BrickletThermocouple

""" Connect to sensors and get sensor data"""
""" 
use instance of (isinatance()) to get the corresponding sensor, so only one generic method is called from main program,
set uid from config file
"""
# TODO all
# TODO set  uids?


def connect_sensors(sensors, uids, ipcon):
	connected_sensors = []
	if sensors["ambient_light"] == 1:
		al = BrickletAmbientLightV2(UID_AMBIENT, ipcon)
		connected_sensors.append(al)
	if sensors["barometer"] == 1:
		barometer = BrickletBarometer(UID_BAROMETER, ipcon)
		connected_sensors.append(barometer)
	if sensors["humidity"] == 1:
		humidity = BrickletHumidity(UID_HUMIDITY, ipcon)
		connected_sensors.append(humidity)
	if sensors["lcd"] == 1:
		lcd = BrickletLCD20x4(UID_LCD, ipcon)
		connected_sensors.append(lcd)
	if sensors["moisture"] == 1:
		moisture = BrickletMoisture(UID_MOISTURE, ipcon)
		connected_sensors.append(moisture)
	if sensors["temperature"] == 1:
		temperature = BrickletTemperature(UID_TEMPERATURE, ipcon)
		connected_sensors.append(temperature)
	if sensors["thermo_couple"] == 1:
		thermo = BrickletThermocouple(UID_THERMO, ipcon)
		connected_sensors.append(thermo)
	return connected_sensors


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
	sensors = {
		"ambient_light": 1,
		"barometer": 0,
		"humidity": 0,
		"lcd": 0,
		"moisture": 0,
		"temperature": 0,
		"thermo_couple": 0}

	# bricklet UIDs
	UID_AMBIENT = "yBG"  # UID of Ambient Light Bricklet 2.0
	UID_BAROMETER = "ytN"  # UID for Barometer Bricklet
	UID_HUMIDITY = "Cd7"  # UID for Humidity Bricklet
	UID_LCD = "BFX"  # UID of LCD Display
	UID_MOISTURE = "zSG"  # UID for Moisture Bricklet
	UID_TEMPERATURE = "zbS"  # UID for Temperature Bricklet
	UID_THERMO = "B8k"  # UID for Thermocouple Bricklet

	# dictionary with sensor UIDs
	sensor_uid = {
		"ambient_light": UID_AMBIENT,
		"barometer": UID_BAROMETER,
		"humidity": UID_HUMIDITY,
		"lcd": UID_LCD,
		"moisture": UID_MOISTURE,
		"temperature": UID_TEMPERATURE,
		"thermo_couple": UID_THERMO}

	# Create IP connection
	ipcon = IPConnection()

	connected_sensors = connect_sensors(sensors, ipcon)
	for sensor in connected_sensors:
		print(get_value(sensor))
