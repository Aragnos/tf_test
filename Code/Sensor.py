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


def connect_sensors(sensors, uids, ipcon):
	"""
	Creates Bricklet Instances
	:param sensors: connected sensors, as dictionary
	:param uids: bricklets uids, as dictionary
	:param ipcon: ipconnection from tinkerforge
	:return: Dictionary with all instances from connected sensors
	"""
	# Dictionary with all connected sensors
	con_sensors = {}
	for sensor in sensors:
		if sensor == "ambient_light":
			al = BrickletAmbientLightV2(uids["ambient_light"], ipcon)
			con_sensors.update({"ambient_light": al})
		if sensor == "barometer":
			barometer = BrickletBarometer(uids["barometer"], ipcon)
			con_sensors.update({"barometer": barometer})
		if sensor == "humidity":
			humidity = BrickletHumidity(uids["humidity"], ipcon)
			con_sensors.update({"humidity": humidity})
		if sensor == "lcd":
			lcd = BrickletLCD20x4(uids["lcd"], ipcon)
			con_sensors.update({"lcd": lcd})
		if sensor == "moisture":
			moisture = BrickletMoisture(uids["moisture"], ipcon)
			con_sensors.update({"moisture": moisture})
		if sensor == "temperature":
			temperature = BrickletTemperature(uids["temperature"], ipcon)
			con_sensors.update({"temperature": temperature})
		if sensor == "thermocouple":
			thermo = BrickletThermocouple(uids["thermocouple"], ipcon)
			con_sensors.update({"thermocouple": thermo})
	return con_sensors


def get_value(sensor):
	"""
	Gets the value from given sensor
	:param sensor: sensor which value should be read
	:return: current sensor value
	"""
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
