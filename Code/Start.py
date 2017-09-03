import sys

sys.path.append('../')
import Datenbank as DB
import ErrorClass
import LCD_Skript as LCD
import time
import datetime

# todo: connect sensors, PyToSh: root password, WLAN
# Todo: test all
# todo: konfig file
# todo opt: use config file, LCD Script



database_host = "localhost"
database_port = 3306
user = "Red"
passwd = "red-brick42"
database = "tf"

try:
	conn = DB.connect_database(database_host, database_port, user, passwd, database)
	# any sensor data in files? Yes: Save these to db. No: continue.
	# save sensor data to database
except ErrorClass.DatabaseError as e:
	print(e.message)
	# save sensor data to file

# LCD.connect_lcd()


sensor_file = open('Test.txt', 'a')
for i in range(0, 10):
	timestamp = "{:%Y-%m-%d %H:%M:%S}".format(datetime.datetime.now())
	write_str = "%s \t %d\n" % (timestamp, i)
	sensor_file.write(write_str)
	#print(write_str)
	time.sleep(1)
sensor_file.close()
