# todo refactor with BrickletConnector
# todo add classes
from BrickletConnector import BaseConnector

from tinkerforge.bricklet_accelerometer import BrickletAccelerometer
from tinkerforge.bricklet_ambient_light import BrickletAmbientLight
from tinkerforge.bricklet_ambient_light_v2 import BrickletAmbientLightV2
from tinkerforge.bricklet_barometer import BrickletBarometer
from tinkerforge.bricklet_co2 import BrickletCO2
from tinkerforge.bricklet_color import BrickletColor
from tinkerforge.bricklet_current12 import BrickletCurrent12
from tinkerforge.bricklet_current25 import BrickletCurrent25
from tinkerforge.bricklet_distance_ir import BrickletDistanceIR
from tinkerforge.bricklet_distance_us import BrickletDistanceUS
from tinkerforge.bricklet_dust_detector import BrickletDustDetector
from tinkerforge.bricklet_gps import BrickletGPS
from tinkerforge.bricklet_gps_v2 import BrickletGPSV2
from tinkerforge.bricklet_hall_effect import BrickletHallEffect
from tinkerforge.bricklet_humidity import BrickletHumidity
from tinkerforge.bricklet_laser_range_finder import BrickletLaserRangeFinder
from tinkerforge.bricklet_linear_poti import BrickletLinearPoti
from tinkerforge.bricklet_load_cell import BrickletLoadCell
from tinkerforge.bricklet_moisture import BrickletMoisture
from tinkerforge.bricklet_motion_detector import BrickletMotionDetector
from tinkerforge.bricklet_ptc import BrickletPTC
from tinkerforge.bricklet_rotary_encoder import BrickletRotaryEncoder
from tinkerforge.bricklet_rotary_poti import BrickletRotaryPoti
from tinkerforge.bricklet_sound_intensity import BrickletSoundIntensity
from tinkerforge.bricklet_temperature import BrickletTemperature
from tinkerforge.bricklet_temperature_ir import BrickletTemperatureIR
from tinkerforge.bricklet_thermocouple import BrickletThermocouple
from tinkerforge.bricklet_tilt import BrickletTilt
from tinkerforge.bricklet_uv_light import BrickletUVLight
from tinkerforge.bricklet_voltage import BrickletVoltage
from tinkerforge.bricklet_voltage_current import BrickletVoltageCurrent


class BaseSensorConnector(BaseConnector):
	"""
	Encapsulation for all Sensor bricklets, or rather for all bricklets capable of returning measurements
	"""
	def create_instance(self, uid, ipcon):
		raise NotImplementedError('create_instance has to be overwritten by subclasses')

	def get_value(self):
		"""
		Get the value, if Bricklet is a sensor
		:return: sensor value
		"""
		raise NotImplementedError('create_instance has to be overwritten by subclasses')


class NotConnectedConnector(BaseSensorConnector):
	"""
	Dummy Class. If a sensors fails to return a value, the bricklet object will be swapped with this dummy.
	With this, the program does not have to wait for the response of the sensor (which will fail) in subsequent call and
	gets instead a dummy response
	Necessary if list in config is not up-to-date
	"""
	def create_instance(self, uid, ipcon):
		return None

	def get_value(self):
		return None


class AccelerometerConnector(BaseSensorConnector):
	def create_instance(self, uid, ipcon):
		return BrickletAccelerometer(uid, ipcon)

	def get_value(self):
		pass


class AmbientLightConnector(BaseSensorConnector):
	def create_instance(self, uid, ipcon):
		return BrickletAmbientLight(uid, ipcon)

	def get_value(self):
		pass


class AmbientLightV2Connector(BaseSensorConnector):
	def create_instance(self, uid, ipcon):
		return BrickletAmbientLightV2(uid, ipcon)

	def get_value(self):
		pass


class BarometerConnector(BaseSensorConnector):
	def create_instance(self, uid, ipcon):
		return BrickletBarometer(uid, ipcon)

	def get_value(self):
		pass


class CO2Connector(BaseSensorConnector):
	def create_instance(self, uid, ipcon):
		return BrickletCO2(uid, ipcon)

	def get_value(self):
		pass


class ColorConnector(BaseSensorConnector):
	def create_instance(self, uid, ipcon):
		return BrickletColor(uid, ipcon)

	def get_value(self):
		pass


class Current12Connector(BaseSensorConnector):
	def create_instance(self, uid, ipcon):
		return BrickletCurrent12(uid, ipcon)

	def get_value(self):
		pass


class Current25Connector(BaseSensorConnector):
	def create_instance(self, uid, ipcon):
		return BrickletCurrent25(uid, ipcon)

	def get_value(self):
		pass


class DistanceIRConnector(BaseSensorConnector):
	def create_instance(self, uid, ipcon):
		return BrickletDistanceIR(uid, ipcon)

	def get_value(self):
		pass


class DistanceUSConnector(BaseSensorConnector):
	def create_instance(self, uid, ipcon):
		return BrickletDistanceUS(uid, ipcon)

	def get_value(self):
		pass


class DustDetectorConnector(BaseSensorConnector):
	def create_instance(self, uid, ipcon):
		return BrickletDustDetector(uid, ipcon)

	def get_value(self):
		pass


class GPSConnector(BaseSensorConnector):
	def create_instance(self, uid, ipcon):
		return BrickletGPS(uid, ipcon)

	def get_value(self):
		pass


class ConnectorGPSV2(BaseSensorConnector):
	def create_instance(self, uid, ipcon):
		return BrickletGPSV2(uid, ipcon)

	def get_value(self):
		pass


class HallEffectConnector(BaseSensorConnector):
	def create_instance(self, uid, ipcon):
		return BrickletHallEffect(uid, ipcon)

	def get_value(self):
		pass


class HumidityConnector(BaseSensorConnector):
	def create_instance(self, uid, ipcon):
		return BrickletHumidity(uid, ipcon)

	def get_value(self):
		pass


class LaserRangeFinderConnector(BaseSensorConnector):
	def create_instance(self, uid, ipcon):
		return BrickletLaserRangeFinder(uid, ipcon)

	def get_value(self):
		pass


class LinearPotiConnector(BaseSensorConnector):
	def create_instance(self, uid, ipcon):
		return BrickletLinearPoti(uid, ipcon)

	def get_value(self):
		pass


class LoadCellConnector(BaseSensorConnector):
	def create_instance(self, uid, ipcon):
		return BrickletLoadCell(uid, ipcon)

	def get_value(self):
		pass


class MoistureConnector(BaseSensorConnector):
	def create_instance(self, uid, ipcon):
		return BrickletMoisture(uid, ipcon)

	def get_value(self):
		pass


class MotionDetectorConnector(BaseSensorConnector):
	def create_instance(self, uid, ipcon):
		return BrickletMotionDetector(uid, ipcon)

	def get_value(self):
		pass


class PTCConnector(BaseSensorConnector):
	def create_instance(self, uid, ipcon):
		return BrickletPTC(uid, ipcon)

	def get_value(self):
		pass


class RotaryEncoderConnector(BaseSensorConnector):
	def create_instance(self, uid, ipcon):
		return BrickletRotaryEncoder(uid, ipcon)

	def get_value(self):
		pass


class RotaryPotiConnector(BaseSensorConnector):
	def create_instance(self, uid, ipcon):
		return BrickletRotaryPoti(uid, ipcon)

	def get_value(self):
		pass


class SoundIntensityConnector(BaseSensorConnector):
	def create_instance(self, uid, ipcon):
		return BrickletSoundIntensity(uid, ipcon)

	def get_value(self):
		pass


class TemperatureConnector(BaseSensorConnector):
	def create_instance(self, uid, ipcon):
		return BrickletTemperature(uid, ipcon)

	def get_value(self):
		return self.bricklet.get_temperature()


class TemperatureIRConnector(BaseSensorConnector):
	def create_instance(self, uid, ipcon):
		return BrickletTemperatureIR(uid, ipcon)

	def get_value(self):
		pass


class ThermocoupleConnector(BaseSensorConnector):
	def create_instance(self, uid, ipcon):
		return BrickletThermocouple(uid, ipcon)

	def get_value(self):
		pass


class TiltConnector(BaseSensorConnector):
	def create_instance(self, uid, ipcon):
		return BrickletTilt(uid, ipcon)

	def get_value(self):
		pass


class UVLightConnector(BaseSensorConnector):
	def create_instance(self, uid, ipcon):
		return BrickletUVLight(uid, ipcon)

	def get_value(self):
		pass


class VoltageConnector(BaseSensorConnector):
	def create_instance(self, uid, ipcon):
		return BrickletVoltage(uid, ipcon)

	def get_value(self):
		pass


class VoltageCurrentConnector(BaseSensorConnector):
	def create_instance(self, uid, ipcon):
		return BrickletVoltageCurrent(uid, ipcon)

	def get_value(self):
		pass

