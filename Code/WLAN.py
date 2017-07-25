import PyToSh
from ErrorClass import InterfaceError, ConnectionError


""" Modify os to work without sudo password. Otherwise hardcoded password required. """


def check_connection(host, count=4):
	""" If wlan interface is up, try to ping the host for count times """
	command = ["ping", "-c", count, host]
	output = PyToSh.popen_comm(command)
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
	output = PyToSh.popen_comm(command)
	if output.__contains__("unassociated"):
		raise InterfaceError("Interface not properly configured")
	return


def restart_interface(iface):
	""" Restarts the Interface called iface """
	# see comment above about sudo
	# Todo check -f option
	command_down = ["ifdown", "-f", iface]
	command_up = ["ifup", iface]
	PyToSh.sudo_popen_wait(command_down)
	PyToSh.sudo_popen_wait(command_up)
	return


""" Configuration of the RED Brick to use WLAN """


def wpa_supplicant():
	""" Creates the wpa_supplicant configuration"""
	# Todo
	config_string = ""
	supplicant_file = "/etc/wpa_supplicant/wpa_supplicant.conf"
	cmd_one = ["echo", config_string]
	cmd_two = ["tee", "sudo", "nano", supplicant_file]
	PyToSh.popoen_pipe(cmd_one, cmd_two)
	return


def interfaces():
	""" Extends the interface file"""
	# Todo
	return
