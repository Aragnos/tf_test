"""
Connects all Bricklets
"""
from tinkerforge.bricklet_lcd_20x4 import BrickletLCD20x4


class BaseConnector:

	def __init__(self, uid, ipcon):
		self.bricklet = self.create_instance(uid, ipcon)

	def create_instance(self, uid, ipcon):
		"""
		Returns bricklet object
		:param uid: bricklet uid
		:param ipcon: ipconnection from tinkerforge
		:return: object of given bricklet
		"""
		raise NotImplementedError('create_instance has to be overwritten by subclasses')


class LCDConnector(BaseConnector):
	def create_instance(self, uid, ipcon):
		return BrickletLCD20x4(uid, ipcon)

	def get_value(self):
		pass
