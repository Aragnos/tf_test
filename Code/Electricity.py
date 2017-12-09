from tinkerforge.ip_connection import IPConnection
from datetime import datetime
import time
import config
import Sensor
import FileConnector
from tinkerforge.brick_master import BrickMaster


def build_dictionaries():
	"""Build sensor dictionary from bricklet UIDS

		Run through each bricklet and check, if it should be connected
		Add these bricklets and corresponding uids to a dictionary, respectively.

		:returns: Two dictionaries with bricklets and uids
		"""
	rel_uids = {}
	rel_sensors = {
		"ambient_light": 1,
		"barometer": 1,
		"humidity": 1,
		"lcd": 1,
		"moisture": 1,
		"temperature": 1,
		"thermocouple": 1}
	rel_uids.update({"ambient_light": config.UID_AMBIENT})
	rel_uids.update({"barometer": config.UID_BAROMETER})
	rel_uids.update({"humidity": config.UID_HUMIDITY})
	rel_uids.update({"lcd": config.UID_LCD})
	rel_uids.update({"moisture": config.UID_MOISTURE})
	rel_uids.update({"temperature": config.UID_TEMPERATURE})
	rel_uids.update({"thermocouple": config.UID_THERMOCOUPLE})
	return [rel_sensors, rel_uids]


# --------------------------------------------------
# Main program procedure
# --------------------------------------------------

def print_verbrauch(info):
	# master 1
	# Spannung in mv
	voltage = str(master_1.get_stack_voltage())
	# Verbrauch in ma
	current = str(master_1.get_stack_current())
	out_str = 'Master_1\n{}\nSpannung:\t{}\tVerbrauch:\t{}'.format(info, voltage, current)
	print(out_str)

	# master 2
	# Spannung in mv
	voltage = str(master_2.get_stack_voltage())
	# Verbrauch in ma
	current = str(master_2.get_stack_current())
	out_str = 'Master_2\n{}\nSpannung:\t{}\tVerbrauch:\t{}'.format(info, voltage, current)
	print(out_str)


if __name__ == "__main__":
	# Build dictionary from bricklet UIDS
	[relevant_sensors, relevant_uids] = build_dictionaries()
	# connect to daemon via ipconnection
	ipcon = IPConnection()

	uid_master_1 = ''
	uid_master_2 = ''
	master_1 = BrickMaster(uid_master_1, ipcon)
	master_2 = BrickMaster(uid_master_2, ipcon)

	ipcon.connect('localhost', 4223)
	# Stromverbrauch vor allen Sensoren
	print_verbrauch('Master alleine')
	# connect rest of sensors
	ipcon.disconnect()
	connected_sensors = Sensor.connect_sensors(relevant_sensors, relevant_uids, ipcon)
	ipcon.connect('localhost', 4223)
	# Stromverbrauch mit allen Sensoren
	print_verbrauch('Alle Sensoren')
	while True:
		# get sensor values
		sensor_values = {}
		for sensor in connected_sensors:
			try:
				new_value = Sensor.get_value(connected_sensors[sensor])
				print_verbrauch('Wert geholt von {}'.format(sensor))
				new_value = 0
				sensor_values.update({sensor: new_value})
			except Exception as e:
				print(e)
				pass
		time.sleep(60)
		break
