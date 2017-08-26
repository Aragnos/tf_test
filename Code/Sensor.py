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
	return


# global Data
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
