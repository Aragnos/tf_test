"""
Connects all Sensors, using BrickletConnector
Stores sensor object and get_value() method
"""
# todo integrate into Sensor
import config_test


def create_objects(ipcon):
	"""

	:param ipcon: IPConnection from Tinkerforge
	:return: bricklet class objects, as dictionary
	"""
	bricklet_classes = {}
	connector = __import__("BrickletConnector")
	# create class objects for every bricklet uid in config file
	# if uid is empty, skip
	for bricklet in config_test.bricklet_uids:
		uid = config_test.bricklet_uids[bricklet]
		if uid == "":
			continue
		class_string = "{}Connector".format(bricklet)
		class_reference = getattr(connector, class_string)
		brick_object = class_reference(uid, ipcon)
		bricklet_classes.update({bricklet: brick_object})
	return bricklet_classes
