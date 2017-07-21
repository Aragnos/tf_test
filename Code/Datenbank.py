import pymysql
from ErrorClass import ConnectionError


def connect_database(host, port, user, passwd, db):
	""" Tries to connect to the databse. 
		Raises Connection Eroor """
	try:
		conn = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db)
		cur = conn.cursor()
		return [conn, cur]
	except:
		raise ConnectionError("Connection to Database failed")