""" Test file"""
import config_test as ct
import BrickletConnector as BC
import SensorConnector as SC
from tinkerforge.ip_connection import IPConnection
dic = ct.bricklet_uids
al = SC.AmbientLightConnector("xdy", IPConnection())

print(al.bricklet)
print(al.get_value())

al_str = ct.AMBIENTLIGHT
connector_str = "{}Connector".format(al_str)
m = __import__("SensorConnector")
al_obj = al
m_obj = getattr(m, connector_str)
al_obj = m_obj("xyz", IPConnection())
print(al_obj.bricklet)
print(al_obj.get_value())
fail_obj = SC.BaseSensorConnector("xyz", IPConnection())
"""
def x():
	print(5)


def ambi():
	print("ambi")


c = {}
c2 = {"func": x}
c.update(c2)
print(c)
c.update({"al": ambi})
print(c)
c["al"]()

def change_premissions(password):
	# Changes the permissions so sudo can be used without password
	# Todo required? No
	command = ['sudo', 'visudo']
	add = 'tf ALL=(ALL) NOPASSWD: ALL'
	p = Popen(command, stdout=PIPE, stdin=PIPE)
	output = p.communicate(password)[0]
	# Todo Test in Linux environment
	return
"""
