"""Opens, closes and writes to file"""
import PyToSh
# todo test all


def open_files(file_list, path, use):
	"""
	Open all files given in file list and returns the opened file handlers
	:param file_list: files, which should be opened, as list
	:param path: path to the file location, as string
	:param use: 'a' for appending, 'r' for reading a file, as string
	:return: file handlers to the opened files, as dictionary
	"""
	# Dictionary with all opened files
	opened_files = {}
	for file_name in file_list:
		# a lcd can be connected, but has no file
		if file_name == "lcd":
			continue
		file_path = "{0}/{1}.txt".format(path, file_name)
		new_file = open(file_path, use)
		opened_files.update({file_name: new_file})
	return opened_files


def close_files(opened_files):
	"""
	Closes the given files
	:param opened_files: currently opened files, which should be closed, as dictionary
	"""
	for f in opened_files:
		opened_files[f].close()


def write_files(sensor_values, opened_files, timestamp):
	"""
	Write the sensor values to the opened files
	:param sensor_values: the values from sensors, as dictionary
	:param opened_files: currently opened files, as dictionary
	:param timestamp: timestamp
	:return:
	"""
	for sensor in opened_files:
		try:
			value = sensor_values[sensor]
			write_str = "%s \t %d\n" % (timestamp, value)
			opened_files[sensor].write(write_str)
		except Exception as e:
			print(e)
			continue
	return


def check_and_return(opened_file):
	"""Checks if a file is present and returns its lines
	:param opened_file: file, wich should be checked
	:return: lines of the file
	"""
	values = []
	try:
		for line in opened_file:
			values.append(line)
	except IOError as e:
		print(e)
		pass
	return values


def delete_files(path):
	"""
	Deletes the directory given in path, and therefore the files in the directory as well
	Then create a fresh directory with same name
	"""
	PyToSh.popen_comm(["rm", "-r", path])
	PyToSh.popen_comm(["mkdir", path])
