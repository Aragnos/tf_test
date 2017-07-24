""" Configuration of the RED Brick to use WLAN """
import PyToSh

def wpa_supplicant():
	""" Creates the wpa_supplicant configuration"""
	# Todo
	config_string = ""
	file = "/etc/wpa_supplicant/wpa_supplicant.conf"
	cmd_one = ["echo", config_string]
	cmd_two = ["tee", "sudo", "nano", file]
	PyToSh.popoen_pipe(cmd_one, cmd_two)
	return


def interfaces():
	""" Extends the interface file"""
	# Todo
	return

