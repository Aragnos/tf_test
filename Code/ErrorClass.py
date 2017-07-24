class Error(Exception):
	# Base Class for exceptions
	pass


class DatabaseError(Error):
	""" Raised if no connection to db possible """

	def __init__(self, msg):
		self.msg = msg


class LCDError(Error):
	""" Raised if LCD_Bricklet is not connected """

	def __init__(self, msg):
		self.msg = msg


class InterfaceError(Error):
	""" Raised if the interface is not correctly configured """

	def __init__(self, msg):
		self.msg = msg


class ConnectionError(Error):
	""" Raised if connection to host not possible"""

	def __init__(self, msg):
		self.msg = msg


class PopenFormatError(Error):
	""" Raised if command given to popen method is not a list"""

	def __init__(self):
		self.msg = "Command should be a list"
