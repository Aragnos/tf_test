# todo refactor with BrickletConnector
from BrickletConnector import BaseConnector

from tinkerforge.bricklet_ambient_light_v2 import BrickletAmbientLightV2
from tinkerforge.bricklet_barometer import BrickletBarometer
from tinkerforge.bricklet_humidity import BrickletHumidity
from tinkerforge.bricklet_moisture import BrickletMoisture
from tinkerforge.bricklet_temperature import BrickletTemperature
from tinkerforge.bricklet_thermocouple import BrickletThermocouple


class BaseSensorConnector(BaseConnector):

	def create_instance(self, uid, ipcon):
		raise NotImplementedError('create_instance has to be overwritten by subclasses')

	def get_value(self):
		"""
		Get the value, if Bricklet is a sensor
		:return: sensor value
		"""
		raise NotImplementedError('create_instance has to be overwritten by subclasses')


class AmbientLightConnector(BaseSensorConnector):
	def create_instance(self, uid, ipcon):
		return BrickletAmbientLightV2(uid, ipcon)

	def get_value(self):
		pass


class BarometerConnector(BaseSensorConnector):
	def create_instance(self, uid, ipcon):
		return BrickletBarometer(uid, ipcon)

	def get_value(self):
		pass


class HumidityConnector(BaseSensorConnector):
	def create_instance(self, uid, ipcon):
		return BrickletHumidity(uid, ipcon)

	def get_value(self):
		pass


class MoistureConnector(BaseSensorConnector):
	def create_instance(self, uid, ipcon):
		return BrickletMoisture(uid, ipcon)

	def get_value(self):
		pass


class TemperatureConnector(BaseSensorConnector):
	def create_instance(self, uid, ipcon):
		return BrickletTemperature(uid, ipcon)

	def get_value(self):
		return self.bricklet.get_temperature()


class ThermocoupleConnector(BaseSensorConnector):
	def create_instance(self, uid, ipcon):
		return BrickletThermocouple(uid, ipcon)

	def get_value(self):
		pass
