""" Execution of shell commands """
from subprocess import Popen, PIPE
# Todo refactor WLAN.py


def popen_comm(command):
	""" Popen with communicate, returns output """
	check_type(command)
	process = Popen(command, stdout=PIPE)
	output = process.communicate()[0]
	return output


def popen_wait(command):
	""" Popen with wait, no output """
	check_type(command)
	process = Popen(command)
	process.wait()
	return


def sudo_popen_comm(command):
	""" Popen with communicate, returns output """
	check_type(command)
	command.insert(0, "sudo")
	process = Popen(command, stdout=PIPE)
	output = process.communicate()[0]
	return output


def sudo_popen_wait(command):
	""" Popen with wait and sudo, no output """
	check_type(command)
	command.insert(0, "sudo")
	process = Popen(command)
	process.wait()
	return


def check_type(command):
	if type(command) == 'list':
		return
	else:
		raise # Todo new error