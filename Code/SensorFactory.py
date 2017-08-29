from abc import ABCMeta, abstractmethod
"""  Try to create dummy sensors, sending data if asked. Use this to emulate sensors. Necessary, possible? """
# TODO


class Sensor:
	__metaclass__ = ABCMeta
	# Base class for sensors

	@abstractmethod
	def __init__(self):
		pass

	@abstractmethod
	def get_value(self):
		pass


class AmbientLight(Sensor):

	def __init__(self):
		super(AmbientLight, self).__init__()
		pass

	def get_value(self):
		return 10.

ab = AmbientLight()
x = ab.get_value()
print(x)
sensors = { "ambient_light" : ab}

y = sensors["ambient_light"].get_value()
print(y)
