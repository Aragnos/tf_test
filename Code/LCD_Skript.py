import time
import sys
from subprocess import Popen, PIPE
from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_lcd_20x4 import BrickletLCD20x4
from ErrorClass import LCDError

sys.path.append('../')

UID_LCD = "BFX"
HOST = "localhost"
PORT = 4223


'''
Not working with current setup, connect LCD from beginning and disconnect later?
'''


def lcd_callback(button):
	print(button)
	if button == 1:
		get_ip()
	if button == 2:
		check_ip_connection()
	if button == 3:
		# kill this program
		unload()
		print("kill")


def connect_lcd():
	ipcon.connect(HOST, PORT)  # Connect to brickd
	return BrickletLCD20x4(UID_LCD, ipcon)


def check_lcd_connection():
	""" If LCD is not connected, an exception will be thrown"""
	try:
		lcd.is_backlight_on()
	except Exception as e:
		print(e)
		raise LCDError("LCD not reachable.")


def get_ip():
	"""" Prints the ip4 address of redbrick, if associated"""
	p1 = Popen(["iwconfig"], stdout=PIPE)
	iwconfig = p1.communicate()[0]
	if iwconfig.__contains__("unassociated"):
		lcd.write_line(0, 0, "unassociated")
	else:
		# change ipconfig to ifconfig
		p2 = Popen(["ipconfig"], stdout=PIPE)
		ifconfig = p2.communicate()[0]
		ifconfig = ifconfig.split("\n")
		for i in range(0, len(ifconfig)):
			temp = str(ifconfig[i])
			# working on windows, but will be wrong in Unix
			if temp.__contains__("IPv4"):
				print(temp)
				split = temp.split(":")
				print(split[len(split) - 1])
				break


def check_ip_connection():
	""" Checks if bricklet is connected to the internet/network"""
	# change -n to -c for use on linux
	p1 = Popen(["ping", "-n", "4", "google.de"], stdout=PIPE)
	output = p1.communicate()[0]
	if output.__contains__("nicht finden") or output.__contains__("not found"):
		print("Not reachable")
		lcd.write_line(1, 0, "Not reachable")


# Called before exiting
def unload():
	lcd.backlight_off()
	lcd.clear_display()
	ipcon.disconnect()
	raise LCDError("Process got killed.")


if __name__ == "__main__":
	ipcon = IPConnection()
	lcd = connect_lcd()
	while True:
		try:
			check_lcd_connection()
		except LCDError as e:
			print(e.msg)
			time.sleep(30)
		else:
			break
	lcd.register_callback(lcd.CALLBACK_BUTTON_PRESSED, lcd_callback)
	lcd.backlight_on()
	# testing
	p1 = Popen(["dir"], shell=True, stdout=PIPE)
	output = p1.communicate()[0]
	print(type(output))
	unload()
	while True:
		time.sleep(300)
