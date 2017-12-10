""" Test file"""
import config_test as ct
import BrickletConnector as BC
dic = ct.bricklet_uids

from tinkerforge.ip_connection import IPConnection

al = BC.AmbientLightConnector("xdy", IPConnection())

print(al.bricklet)
print(al.get_value())

al_str = 'AmbientLight'
connector_str = al_str + 'Connector'
m = __import__("BrickletConnector")
m = getattr(m, connector_str)
al_obj = m("xyz", IPConnection())
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
