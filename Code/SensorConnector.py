# todo refactor with BrickletConnector
from BrickletConnector import BaseConnector

from tinkerforge.bricklet_accelerometer import Accelerometer
from tinkerforge.bricklet_ambient_light import AmbientLight
from tinkerforge.bricklet_ambient_light_v2 import BrickletAmbientLightV2
from tinkerforge.bricklet_barometer import BrickletBarometer
from tinkerforge.bricklet_co2 import CO2
from tinkerforge.bricklet_color import Color
from tinkerforge.bricklet_current12 import Current12
from tinkerforge.bricklet_current25 import Current25
from tinkerforge.bricklet_distance_ir import DistanceIR
from tinkerforge.bricklet_distance_us import DistanceUS
from tinkerforge.bricklet_dust_detector import DustDetector
from tinkerforge.bricklet_gps import GPS
from tinkerforge.bricklet_gps_v2 import GPSV2
from tinkerforge.bricklet_hall_effect import HallEffect
from tinkerforge.bricklet_humidity import BrickletHumidity
from tinkerforge.bricklet_laser_range_finder import LaserRangeFinder
from tinkerforge.bricklet_linear_poti import LinearPoti
from tinkerforge.bricklet_load_cell import LoadCell
from tinkerforge.bricklet_moisture import BrickletMoisture
from tinkerforge.bricklet_motion_detector import MotionDetector
from tinkerforge.bricklet_ptc import PTC
from tinkerforge.bricklet_rotary_encoder import RotaryEncoder
from tinkerforge.bricklet_rotary_poti import RotaryPoti
from tinkerforge.bricklet_sound_intensity import SoundIntensity
from tinkerforge.bricklet_temperature import BrickletTemperature
from tinkerforge.bricklet_temperature_ir import TemperatureIR
from tinkerforge.bricklet_thermocouple import BrickletThermocouple
from tinkerforge.bricklet_tilt import Tilt
from tinkerforge.bricklet_uv_light import UVLight
from tinkerforge.bricklet_voltage import Voltage
from tinkerforge.bricklet_voltage_current import VoltageCurrent

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
