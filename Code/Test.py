""" Test file"""
import config_test as ct
import BrickletConnector as BC
from tinkerforge.ip_connection import IPConnection
dic = ct.bricklet_uids
al = BC.AmbientLightConnector("xdy", IPConnection())

print(al.bricklet)
print(al.get_value())

al_str = ct.AMBIENTLIGHT
connector_str = "{}Connector".format(al_str)
m = __import__("BrickletConnector")
al_obj = al
m_obj = getattr(m, connector_str)
al_obj = m_obj("xyz", IPConnection())
print(al_obj.bricklet)
print(al_obj.get_value())
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
"""
