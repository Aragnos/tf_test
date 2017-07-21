import Datenbank as DB

conn, cur = DB.connect_database("localhost", 3306, "Red", "red-brick42", "tf")
with open("Ambientlight.txt", 'r') as ambient_file:
	data = ambient_file.read()
	data = data.split("\n")
	for d in data:
		d = d.split("\t")
		statement = "INSERT INTO ambient_light (datum, wert) VALUES (\'{}\',\'{}\') ".format(d[0], d[1])
		cur.execute(statement)
	conn.commit()
