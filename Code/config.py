# --------------------------------------------------
# WLAN Settings
# --------------------------------------------------
WLAN_CONFIGURED = '0'
WLAN_USER = ""
WLAN_PASSWORD = ""
# --------------------------------------------------
# Database Settings
# --------------------------------------------------
DATABASE_HOST = "localhost"
DATABASE_PORT = "3306"
DATABASE_NAME = "tf"
DATABASE_USER = "Red"
DATABASE_PASSWORD = "red-brick42"
# --------------------------------------------------
# Linux Settings
# --------------------------------------------------
ROOT_PASSWORD = "tf"
# --------------------------------------------------
# Bricklet UIDS
# --------------------------------------------------
UID_AMBIENT = "yBG"  # UID of Ambient Light Bricklet 2.0
UID_BAROMETER = "ytN"  # UID for Barometer Bricklet
UID_HUMIDITY = "Cd7"  # UID for Humidity Bricklet
UID_LCD = "BFX"  # UID of LCD Display
UID_MOISTURE = "zSG"  # UID for Moisture Bricklet
UID_TEMPERATURE = "zbS"  # UID for Temperature Bricklet
UID_THERMOCOUPLE = "B8k"  # UID for Thermocouple Bricklet
# --------------------------------------------------
# Connected Sensors
# If ALL is set to 1 the program tries to connect to all sensors:
# Ambient, Barometer, Humidity, LCD, Moisture, Temperature and Thermocouple.
# If it can't find a sensos, this one will be left out.
# If relevant is set to 1, only sensors with '1' will be connected.
# --------------------------------------------------
ALL = '1'

AMBIENT = '1'
BAROMETER = '1'
HUMIDITY = '1'
LCD = '1'
MOISTURE = '1'
TEMPERATURE = '1'
THERMOCOUPLE = '1'
# --------------------------------------------------
