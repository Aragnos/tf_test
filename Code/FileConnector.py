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
	"""Open files on SD for the connected connected_sensors and return file handles"""
	# Dictionary with all connected connected_sensors
	opened_files = {}
	if connected_sensors["ambient_light"] is not None:
		al = open('Ambientight.txt', 'a')
		opened_files.update({"ambient_light": al})
	if connected_sensors["barometer"] is not None:
		barometer = open('Barometer.txt', 'a')
		opened_files.update({"barometer": barometer})
	if connected_sensors["humidity"] is not None:
		humidity = open('Humidity.txt', 'a')
		opened_files.update({"humidity": humidity})
	if connected_sensors["lcd"] is not None:
		# lcd = BrickletLCD20x4(uids["lcd"], ipcon)
		# open_files.update({"lcd": lcd})
		pass
	if connected_sensors["moisture"] is not None:
		moisture = open('Moisture.txt', 'a')
		opened_files.update({"moisture": moisture})
	if connected_sensors["temperature"] is not None:
		temperature = open('Temperature.txt', 'a')
		opened_files.update({"temperature": temperature})
	if connected_sensors["thermocouple"] is not None:
		thermo = open('Thermocouple.txt', 'a')
		opened_files.update({"thermocouple": thermo})
	return opened_files


def close_files(opened_files):
	"""Close all given files"""
	for f in opened_files:
		opened_files[f].close()
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


def check_and_return(file_name):
	"""Checks if a file is present and returns its lines"""
	values = []
	try:
		opened_file = open(file_name, 'r')
		for line in opened_file:
			values.append(line)
	except IOError:
		pass
	return values
