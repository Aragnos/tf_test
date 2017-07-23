import sys

sys.path.append('../')
import Datenbank as DB
import ErrorClass
import LCD_Skript as LCD
import time
import datetime

database_host = "localhost"
database_port = 3306
user = "Red"
passwd = "red-brick42"
database = "tf"

try:
	conn = DB.connect_database(database_host, database_port, user, passwd, database)
except ErrorClass.DatabaseError as e:
	print(e.msg)

# LCD.connect_lcd()


file = open('Test.txt', 'a')
for i in range(0, 10):
	timestamp = "{:%Y-%m-%d %H:%M:%S}".format(datetime.datetime.now())
	write_str = "%s \t %d\n" % (timestamp, i)
	file.write(write_str)
	#print(write_str)
	time.sleep(1)
file.close()
