"""
Connects all Bricklets
"""

from tinkerforge.bricklet_ambient_light_v2 import BrickletAmbientLightV2
from tinkerforge.bricklet_barometer import BrickletBarometer
from tinkerforge.bricklet_humidity import BrickletHumidity
from tinkerforge.bricklet_lcd_20x4 import BrickletLCD20x4
from tinkerforge.bricklet_moisture import BrickletMoisture
from tinkerforge.bricklet_temperature import BrickletTemperature
from tinkerforge.bricklet_thermocouple import BrickletThermocouple


class BaseConnector:

	def __init__(self, uid, ipcon):
		self.bricklet = self.create_instance(uid, ipcon)

	def create_instance(self, uid, ipcon):
		"""
		Returns bricklet object
		:param uid: bricklet uid
		:param ipcon: ipconnection from tinkerforge
		:return: object of given bricklet
		"""
		raise NotImplementedError('create_instance has to be overwritten by subclasses')

	def get_value(self):
		"""
		Get the value, if Bricklet is a sensor
		:return: sensor value
		"""
		raise NotImplementedError('get_value has to be overwritten by subclasses')


class AmbientLightConnector(BaseConnector):

	def create_instance(self, uid, ipcon):
		return BrickletAmbientLightV2(uid, ipcon)

	def get_value(self):
		pass


class BarometerConnector(BaseConnector):

	def create_instance(self, uid, ipcon):
		return BrickletBarometer(uid, ipcon)

	def get_value(self):
		pass


class HumidityConnector(BaseConnector):

	def create_instance(self, uid, ipcon):
		return BrickletHumidity(uid, ipcon)

	def get_value(self):
		pass


class LCDConnector(BaseConnector):

	def create_instance(self, uid, ipcon):
		return BrickletLCD20x4(uid, ipcon)

	def get_value(self):
		pass


class MoistureConnector(BaseConnector):

	def create_instance(self, uid, ipcon):
		return BrickletMoisture(uid, ipcon)

	def get_value(self):
		pass


class TemperatureConnector(BaseConnector):

	def create_instance(self, uid, ipcon):
		return BrickletTemperature(uid, ipcon)

	def get_value(self):
		return self.bricklet.get_temperature()


class ThermocoupleConnector(BaseConnector):

	def create_instance(self, uid, ipcon):
		return BrickletThermocouple(uid, ipcon)

	def get_value(self):
		pass
