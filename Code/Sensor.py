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
""" Connect to sensors and get sensor data"""
""" 
use instance of (isinatance()) to get the corresponding sensor, so only one generic method is called from main program,
set uid from config file
"""
# TODO delete dependencies: Factory, sys, IP_Error?


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
	if sensors["thermocouple"] == 1:
		thermo = BrickletThermocouple(uids["thermocouple"], ipcon)
		con_sensors.update({"thermocouple": thermo})
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
	return
