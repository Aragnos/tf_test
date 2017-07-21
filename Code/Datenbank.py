import pymysql
from ErrorClass import DatabaseError


def connect_database(host="localhost", port=3306, user="Red", passwd="red-brick42", db="tf"):
	""" Tries to connect to the databse. 
		Raises Connection Erorr """
	try:
		conn = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db)
		cur = conn.cursor()
		return [conn, cur]
	except:
		raise DatabaseError("Connection to Database failed")
