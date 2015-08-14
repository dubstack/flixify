import MySQLdb

def writeToDb(store):
	db = MySQLdb.connect("10.5.18.68","12CS30010","dual12","12CS30010")
	cursor = db.cursor()
	sql = """ SET FOREIGN_KEY_CHECKS=0 """
	cursor.execute(sql)
	cursor.execute("DROP TABLE IF EXISTS scriptData")
	db.commit()
	sql = """CREATE TABLE scriptData (
     typ varchar(100),
     speaker varchar(100),
     content varchar(100000),
     scenenum varchar(100),
     inde varchar(100) )"""
	print sql
	cursor.execute(sql)
	db.commit()
	for i  in range(0,len(store)):
		I=str(i+1)
		X=store[i]
		typ=X["type"]
		speaker=X["speaker"]
		content=X["content"]
		scenenum=X["scenenum"]
		content=content.replace("'"," ")
		sql = "insert into scriptData values('"+typ+"','"+speaker+"','"+content+"','"+scenenum+"','"+I+"');"
		print sql
		cursor.execute(sql)
		db.commit()


