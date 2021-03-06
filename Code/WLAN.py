import PyToSh
from ErrorClass import InterfaceError, ConnectionError


""" Modify os to work without sudo password. Otherwise hardcoded password required. """


def check_connection(host, count=4):
	""" If wlan interface is up, try to ping the host for count times """
	command = ["ping", "-c", str(count), str(host)]
	#command = ["ping", str(host)]
	output = PyToSh.popen_comm(command)
	# Todo more generic way?
	if output.__contains__('not found') or output.__contains__('unknown'):
		raise InterfaceError('Host not found.')
	# Todo check ping output
	elif output.__contains__('nicht finden'):
		raise ConnectionError('Destination host not reachable.')
	print(output)
	return


def check_interface():
	""" Checks if the interface is configured """
	command = ['iwconfig']
	output = PyToSh.popen_comm(command)
	if output.__contains__('unassociated'):
		raise InterfaceError('Interface not properly configured.')
	return


def restart_interface(iface):
	""" Restarts the Interface called iface """
	# see comment above about sudo
	# Todo check -f option
	command_down = ['ifdown', '-f', iface]
	command_up = ['ifup', iface]
	PyToSh.sudo_popen_wait(command_down)
	PyToSh.sudo_popen_wait(command_up)
	return


""" Configuration of the RED Brick to use WLAN """


def wpa_supplicant(username, password):
	""" Creates the wpa_supplicant configuration"""
	# Todo
	preemble_string = '''ctrl_interface=/var/run/wpa_supplicant
ctrl_interface_group=tf
eapol_version=1
ap_scan=1\n\n'''

	config_string = '''network={{
	ssid="RZUWsec"
	mode=0
	proto=WPA2
	key_mgmt=WPA-EAP
	pairwise=CCMP
	group=CCMP
	eap=TTLS
	phase2="auth=PAP"
	ca_cert="/etc/ssl/certs/Deutsche_Telekom_Root_CA_2.pem"
	anonymous_identity="anonymous@uni-wuerzburg.de"
	identity="{0}@uni-wuerzburg.de"
	password="{1}"
	priority=10
	}}'''.format(username, password)

	complete_config = preemble_string + config_string
	supplicant_file = '/etc/wpa_supplicant/wpa_supplicant.conf'
	cmd_one = ['echo', complete_config]
	cmd_two = ['sudo', 'tee', supplicant_file]
	PyToSh.sudo_popen_pipe(cmd_one, cmd_two)
	return


def interfaces(iface_name):
	""" Extends the interface file"""
	# Todo
	config_string = '''auto {0}	
	iface {0} inet dhcp
	wpa-conf /etc/wpa_supplicant/wpa_supplicant.conf'''.format(iface_name)
	interfaces_file = '/etc/network/interfaces'
	cmd_one = ['echo', config_string]
	cmd_two = ['sudo', 'tee', '-a', interfaces_file]
	PyToSh.sudo_popen_pipe(cmd_one, cmd_two)
	return

