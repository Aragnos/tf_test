import pymysql
from ErrorClass import DatabaseError


def connect_database(host="localhost", port=3306, user="Red", passwd="red-brick42", db="tf"):
	""" Tries to connect to the database.
		Raises Connection Error """
	try:
		conn = pymysql.connect(host=host, port=3306, user=user, passwd=passwd, db=db)
		cur = conn.cursor()
		return [conn, cur]
	except Exception as e:
		print(e)
		raise DatabaseError("Connection to Database failed")
