"""Code for the first test run of tinkerforge system.
	Main Goal: runtime with powerbank, stability of wireless connection"""

from tinkerforge.ip_connection import IPConnection
from datetime import datetime
import ErrorClass as Error
import config
import Sensor
import WLAN
import FileConnector
import Start
import config
import time
from datetime import datetime

if __name__ == '__main__':
	config.ALL = '1'
	# todo
	wlan_user = ''
	wlan_password = ''
	#WLAN.wpa_supplicant(wlan_user, wlan_password)
	#WLAN.interfaces('wlan0')
	counter = 0
	wlan_status = '+'
	while True:
		counter = counter + 1
		try:
			WLAN.check_interface()
			WLAN.check_connection('google.de')
		except:
			wlan_status = '-'
		try_file = open('TryRun.txt', 'a')
		timestamp = "{:%Y-%m-%d %H:%M:%S}".format(datetime.now())
		write_str = '%d \t %s \t WLAN: %s \n' % (counter, timestamp, wlan_status)
		try_file.write(write_str)
		try_file.close()
		time.sleep(10)
