""" Execution of shell commands """
from subprocess import Popen, PIPE
from ErrorClass import PopenFormatError
import types
import config



def popen_comm(command):
	""" Popen with communicate, returns output """
	check_type(command)
	p = Popen(command, stdout=PIPE)
	output = p.communicate()[0]
	return output


def popen_wait(command):
	""" Popen with wait, no output """
	check_type(command)
	p = Popen(command)
	p.wait()
	return


def sudo_popen_comm(command):
	""" Popen with communicate, returns output """
	check_type(command)
	command.insert(0, "sudo")
	p = Popen(command, stdout=PIPE)
	output = p.communicate()[0]
	return output


def sudo_popen_wait(command):
	""" Popen with wait and sudo, no output """
	check_type(command)
	command.insert(0, "sudo")
	p = Popen(command)
	p.wait()
	return


def popen_pipe(command_one, command_two):
	""" Popen with pipelining """
	check_type(command_one)
	check_type(command_two)
	p1 = Popen(command_one, stdout=PIPE)
	p2 = Popen(command_two, stdin=p1.stdout, stdout=PIPE)
	p1.stdout.close()
	output = p2.communicate()[0]
	return output


def sudo_popen_pipe(command_one, command_two):
	""" Popen with pipelining and sudo"""
	pwd = config.ROOT_PASSWORD+"\n"
	# echos password to sudo
	echo_cmd = ["echo", pwd]
	sudo_cmd = ["sudo", "-S", "echo", "Root"]
	# Sudo acquired, process initial commands
	popen_pipe(echo_cmd, sudo_cmd)
	popen_pipe(command_one, command_two)
	return


def check_type(command):
	if isinstance(command, types.ListType):
		return
	else:
		raise PopenFormatError()



