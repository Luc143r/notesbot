import pymysql

conn = pymysql.connect(
host = 'localhost',
user = 'root',
password = 'kjkszpj11',
db = 'notesbot',
)

cursor = conn.cursor(pymysql.cursors.DictCursor)

deleteincrement = """SELECT MAX(idnotes) as id FROM notes"""
cursor.execute(deleteincrement)
result = cursor.fetchone()
print(result['id'])
conn.commit()

cursor.close()
conn.close()