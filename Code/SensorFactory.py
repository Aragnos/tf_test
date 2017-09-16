"""  Try to create dummy sensors, sending data if asked. Use this to emulate sensors. Necessary, possible? """
from abc import ABCMeta, abstractmethod
from tinkerforge.bricklet_ambient_light_v2 import BrickletAmbientLightV2
from tinkerforge.bricklet_barometer import BrickletBarometer
from tinkerforge.bricklet_humidity import BrickletHumidity
from tinkerforge.bricklet_lcd_20x4 import BrickletLCD20x4
from tinkerforge.bricklet_moisture import BrickletMoisture
from tinkerforge.bricklet_temperature import BrickletTemperature
from tinkerforge.bricklet_thermocouple import BrickletThermocouple

# TODO two methods for barometer


class Sensor:

	def __init__(self):
		pass
# 	metaclass__ = ABCMeta
	# Base class for sensors

# 	@abstractmethod
	def get_value(self):
		pass

	"""Dummy method for returning values"""
	def get_val(self, sensor):
		if isinstance(sensor, BrickletAmbientLightV2):
			return 100
		if isinstance(sensor, BrickletBarometer):
			# second barometer value
			return 200
		# altitude = barometer.get_altitude()
		if isinstance(sensor, BrickletHumidity):
			return 300
		if isinstance(sensor, BrickletMoisture):
			return 400
		if isinstance(sensor, BrickletTemperature) or isinstance(sensor, BrickletThermocouple):
			return 500


class AmbientLight(Sensor):

	def get_value(self):
		return 10


class Barometer(Sensor):

	def get_value(self):
		return 100


class Humidity(Sensor):

	def get_value(self):
		return 200


class Moisture(Sensor):
	def get_value(self):
		return 300


class Temperature(Sensor):
	def get_value(self):
		return 400


class Thermocouple(Sensor):
	def get_value(self):
		return 1000
