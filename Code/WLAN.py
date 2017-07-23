from subprocess import Popen, PIPE
from ErrorClass import InterfaceError, ConnectionError


""" Modify os to work without sudo password. Otherwise hardcoded password required. """


def check_connection(host, count=4):
	""" If wlan interface is up, try to ping the host for count times """
	command = ["ping", "-c", count, host]
	process = Popen(command, stdout=PIPE)
	output = process.communicate()[0]
	# Todo more generic way?
	if output.__contains__("not found"):
		raise InterfaceError("Host not found")
	# Todo check ping output
	elif output.__contains__(""):
		raise ConnectionError("Destination host not reachable")
	return


def check_interface():
	""" Checks if the interface is configured """
	command = ["iwconfig"]
	process = Popen(command, stdout=PIPE)
	output = process.communicate()[0]
	if output.__contains__("unassociated"):
		raise InterfaceError("Interface not properly configured")
	return


def restart_interface(iface):
	""" Restarts the Interface called iface """
	# see comment above about sudo
	# Todo check -f option
	command_down = ["sudo", "ifdown", "-f", iface]
	command_up = ["sudo", "ifup", iface]
	if_down = Popen(command_down)
	if_down.wait()
	if_up = Popen(command_up)
	if_up.wait()
	return
