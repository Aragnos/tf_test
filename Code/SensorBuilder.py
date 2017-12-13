"""
Connects all Sensors, using BrickletConnector
Stores sensor object and get_value() method
"""
# todo integrate into Sensor (or SensorConnector?)
from config_test import bricklet_uids, sensors_in_use


def create_sensor_objects(ipcon):
	"""

	:param ipcon: IPConnection from Tinkerforge
	:return: bricklet class objects, as dictionary
	"""
	bricklet_classes = {}
	connector = __import__("BrickletConnector")
	# create class objects for every bricklet uid in config file
	# if uid is empty, skip
	for sensor in sensors_in_use:
		uid = bricklet_uids[sensor]
		if uid == "":
			continue
		class_string = "{}Connector".format(sensor)
		class_reference = getattr(connector, class_string)
		brick_object = class_reference(uid, ipcon)
		bricklet_classes.update({sensor: brick_object})
	return bricklet_classes
