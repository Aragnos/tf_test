from subprocess import Popen, PIPE
from ErrorClass import InterfaceError, ConnectionError


""" Modify os to work without sudo password. Otherwise hardcoded. """


def check_connection(host, count=4):
	""" If wlan interface is up, try to ping the host for count times"""
	command = ["ping", "-c", count, host]
	process = Popen(command, stdout=PIPE)
	output = process.communicate()[0]
	if output.__contains__("not found"):
		raise InterfaceError("Host not found")
	# Todo
	elif output.__contains__(""):
		raise ConnectionError("Destination host not reachable")
	return


def check_interface():
	""" Checks if the interface is configured"""
	command = ["iwconfig"]
	proces = Popen(command, stdout=PIPE)
	output = proces.communicate()[0]
	if output.__contains__("unassociated"):
		raise InterfaceError("Interface not properly configured")
	return


def restart_interface():
	""" Restarts the Interface """
	# Todo
	return
