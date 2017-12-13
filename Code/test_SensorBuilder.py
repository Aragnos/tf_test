from unittest import TestCase
from SensorBuilder import create_sensor_objects, poll_values
from tinkerforge.ip_connection import IPConnection
import config_test as ct


class TestSensorBuilder(TestCase):
	def setUp(self):
		self.ipcon = IPConnection()
		self.assertErrors = []
		for bricklet in ct.bricklet_uids:
			ct.bricklet_uids[bricklet] = "abc"
			ct.sensors_in_use.append(bricklet)
		self.bricklets = create_sensor_objects(self.ipcon)
		self.values = poll_values(self.bricklets)

	def tearDown(self):
		self.assertEqual([], self.assertErrors)

	def test_create_sensor_objects_not_none(self):

		for brick in self.bricklets:
			try:
				self.assertNotEqual(self.bricklets[brick], None)
			except AssertionError as e:
				self.assertErrors.append(e)

	def test_create_sensor_objects(self):
		for brick in self.bricklets:
			brick_str = str(self.bricklets[brick])
			try:
				self.assertTrue(brick_str.__contains__(brick))
			except AssertionError as e:
				self.assertErrors.append(e)

	def test_poll_value(self):
		for val in self.values:
			self.assertIsNotNone(val)
