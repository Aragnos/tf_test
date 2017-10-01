"""Opens, closes and writes to file"""

# todo all
#todo two files for barometer
'''
sensor_file = open('Test.txt', 'a')
	for i in range(0, 10):
		timestamp = "{:%Y-%m-%d %H:%M:%S}".format(datetime.datetime.now())
		write_str = "%s \t %d\n" % (timestamp, i)
		sensor_file.write(write_str)
		#print(write_str)
		time.sleep(1)
	sensor_file.close()
'''


def open_files(connected_sensors):
	"""Open files on SD for the connected sensors and return file handles"""
	# Dictionary with all connected sensors
	open_files = {}
	if sensors["ambient_light"] == 1:
		al = open('Ambientight.txt', 'a')
		open_files.update({"ambient_light": al})
	if sensors["barometer"] == 1:
		barometer = open('Barometer.txt', 'a')
		open_files.update({"barometer": barometer})
	if sensors["humidity"] == 1:
		humidity = open('Humidity.txt', 'a')
		open_files.update({"humidity": humidity})
	if sensors["lcd"] == 1:
		#lcd = BrickletLCD20x4(uids["lcd"], ipcon)
		#open_files.update({"lcd": lcd})
	if sensors["moisture"] == 1:
		moisture = open('Moisture.txt', 'a')
		open_files.update({"moisture": moisture})
	if sensors["temperature"] == 1:
		temperature = open('Temperature.txt', 'a')
		open_files.update({"temperature": temperature})
	if sensors["thermocouple"] == 1:
		thermo = open('Thermocouple.txt', 'a')
		open_files.update({"thermocouple": thermo})
	return open_files


def close_files(opened_files):
	"""Close all given files"""
	for file in opened_files:
		file.close()
	return


def write_files(sensor_values, opened_files, timestamp):
	"""Write the sensor values to the opened files"""
	for sensor in opened_files:
		try:
			value = sensor_values[sensor]
			write_str = "%s \t %d\n" % (timestamp, value)
			opened_files[sensor].write(write_str)
		except:
			continue
	return
