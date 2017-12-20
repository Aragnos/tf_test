# todo: add missing Bricklets in UID and mapping section
# --------------------------------------------------
# Mapping Bricklet name to internal name
# written in caps, as these are CONSTANTS
# useful to eliminate errors due to misspelling in other modules
# --------------------------------------------------
ACCELEROMETER = "Accelerometer"
AMBIENT_LIGHT = "AmbientLight"
AMBIENT_LIGHT_V2 = "AmbientLightV2"
BAROMETER = "Barometer"
CO2 = "CO2"
COLOR = "Color"
CURRENT12 = "Current12"
CURRENT25 = "Current25"
DISTANCE_IR = "DistanceIR"
DISTANCE_US = "DistanceUS"
DUST_DETECTOR = "DustDetector"
GPS = "GPS"
GPS_V2 = "GPSV2"
HALL_EFFECT = "HallEffect"
HUMIDITY = "Humidity"
LASER_RANGE_FINDER = "LaserRangeFinder"
LINEAR_POTI = "LinearPoti"
LOAD_CELL = "LoadCell"
MOISTURE = "Moisture"
MOTION_DETECTOR = "MotionDetector"
PTC = "PTC"
ROTARY_ENCODER = "RotaryEncoder"
ROTARY_POTI = "RotaryPoti"
SOUND_INTENSITY = "SoundIntensity"
TEMPERATURE = "Temperature"
TEMPERATURE_IR = "TemperatureIR"
THERMOCOUPLE = "Thermocouple"
TILT = "Tilt"
UV_LIGHT = "UVLight"
VOLTAGE = "Voltage"
VOLTAGE_CURRENT = "VoltageCurrent"
# --------------------------------------------------
# Bricklet UIDS
# --------------------------------------------------
bricklet_uids = {
	ACCELEROMETER: "",
	AMBIENT_LIGHT: "",
	AMBIENT_LIGHT_V2: "yBG",
	BAROMETER: "ytN",
	CO2: "",
	COLOR: "",
	CURRENT12: "",
	CURRENT25: "",
	DISTANCE_IR: "",
	DISTANCE_US: "",
	DUST_DETECTOR: "",
	GPS: "",
	GPS_V2: "",
	HALL_EFFECT: "",
	HUMIDITY: "Cd7",
	LASER_RANGE_FINDER: "",
	LINEAR_POTI: "",
	LOAD_CELL: "",
	# LCD: "BFX",
	MOISTURE: "zSG",
	MOTION_DETECTOR: "",
	PTC: "",
	ROTARY_ENCODER: "",
	ROTARY_POTI: "",
	SOUND_INTENSITY: "",
	TEMPERATURE: "zbS",
	TEMPERATURE_IR: "",
	THERMOCOUPLE: "B8k",
	TILT: "",
	UV_LIGHT: "",
	VOLTAGE: "",
	VOLTAGE_CURRENT: ""
}

# todo description
sensors_in_use = [
	AMBIENT_LIGHT_V2,
	ACCELEROMETER,
	AMBIENT_LIGHT,
	AMBIENT_LIGHT_V2,
	BAROMETER,
	CO2,
	COLOR,
	CURRENT12,
	CURRENT25,
	DISTANCE_IR,
	DISTANCE_US,
	DUST_DETECTOR,
	GPS,
	GPS_V2,
	HALL_EFFECT,
	HUMIDITY,
	LASER_RANGE_FINDER,
	LINEAR_POTI,
	LOAD_CELL,
	MOISTURE,
	MOTION_DETECTOR,
	PTC,
	ROTARY_ENCODER,
	ROTARY_POTI,
	SOUND_INTENSITY,
	TEMPERATURE,
	TEMPERATURE_IR,
	THERMOCOUPLE,
	TILT,
	UV_LIGHT,
	VOLTAGE,
	VOLTAGE_CURRENT
]

bricklets_in_use = [
	None
]
