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

if __name__ == '_main_':
	config.ALL = '1'
	[rel_sensors, rel_uids] = Start.build_dictionaries()
	ipcon = IPConnection()
	

