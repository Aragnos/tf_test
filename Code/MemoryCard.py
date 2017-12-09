import FileConnector


class MemoryCard:

	def __init__(self, connected_sensors, path):
		"""

		:param connected_sensors: sensors connected as a list
		:param path: path the values should be saved
		"""
		self.connected_sensors = connected_sensors
		self.path = path

	def save_sd(self, sensor_values, timestamp):
		"""Saves sensor values to sd card"""
		opened_files = FileConnector.open_files(self.connected_sensors, self.path, 'a')
		FileConnector.write_files(sensor_values, opened_files, timestamp)
		FileConnector.close_files(opened_files)

	def save_sd_to_db(self, save_db_method):
		"""Save temporary value from SD to database"""
		# Get values saved on sd
		open_files = []
		try:
			open_files = FileConnector.open_files(self.connected_sensors, self.path, 'r')
		except Exception as e:
			print(e)
			pass
		for f in open_files:
			values = FileConnector.check_and_return(open_files[f])
			for value in values:
				# timestamp on 0, sensor value on 1
				splitted_value = value.split('\t')
				tmp_dic = {f: splitted_value[1]}
				# save values to database
				save_db_method(tmp_dic, splitted_value[0])
		FileConnector.close_files(open_files)
		FileConnector.delete_files(self.path)
