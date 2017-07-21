from subprocess import Popen, PIPE
from ErrorClass import ConnError

try:
	x = 1.0/2
	raise ConnError("Test Error Raise")
	y = 2/1
	#proc = Popen('dir', stdout=PIPE, shell=True)
	#proc.wait()
	#print proc.returncode
	#print (proc.communicate()[1])
except ConnError as e:
	print(e.msg)
else:
	print(x)
finally: 
	print('Finally')