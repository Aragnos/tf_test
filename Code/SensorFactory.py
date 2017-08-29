from abc import ABCMeta, abstractmethod
"""  Try to create dummy sensors, sending data if asked. Use this to emulate sensors. Necessary, possible? """
# TODO
# TODO two methods for barometer

class Sensor:
	__metaclass__ = ABCMeta
	# Base class for sensors

	@abstractmethod
	def get_value(self):
		pass


class AmbientLight(Sensor):

	def get_value(self):
		return 10


class Barometer(Sensor):

	def get_value(self):
		return 100


class Humidity(Sensor):

	def get_value(self):
		return 200


class Moisture(Sensor):
	def get_value(self):
		return 300


class Temperature(Sensor):
	def get_value(self):
		return 400


class ThermoCouple(Sensor):
	def get_value(self):
		return 1000

ambient = AmbientLight()
barometer = Barometer()
humidity = Humidity()
moisture = Moisture()
temperature = Temperature()
thermo = ThermoCouple()


sensors = {
		"ambient_light": ambient,
		"barometer": barometer,
		"humidity": humidity,
		"moisture": moisture,
		"temperature": temperature,
		"thermo_couple": thermo}

y = sensors["ambient_light"].get_value()
print(y)

for sensor in sensors:
	print(sensors[sensor].get_value())
