﻿class Error(Exception):
	# Base Class for exceptions
	pass


class DatabaseError(Error):
	""" Raised if no connection to db possible """

	def __init__(self, msg):
		self.message = msg


class LCDError(Error):
	""" Raised if LCD_Bricklet is not connected """

	def __init__(self, msg):
		self.message = msg


class InterfaceError(Error):
	""" Raised if the interface is not correctly configured """

	def __init__(self, msg):
		self.message = msg


class ConnectionError(Error):
	""" Raised if connection to host not possible"""

	def __init__(self, msg):
		self.message = msg


class PopenFormatError(Error):
	""" Raised if command given to popen method is not a list"""

	def __init__(self):
		self.message = "Command should be a list"


class NotConnectedError(Error):
	"""Raised if sensor is not connected, but attempt to get values is made"""

	def __init__(self):
		self.message = "Not Connected"