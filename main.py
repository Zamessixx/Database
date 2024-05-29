import sqlite3


conn = sqlite3.connect('student.dp')

cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS students( 
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    grade REAL
)
''')

cursor.execute('''
INSERT INTO students (name, grade)
VALUES ('Masha',162.8), ('Artem',190), ('Maksim',195.5), ('Bael',164.5)
''')

conn.commit()

cursor.execute('SELECT * FROM students')
rows = cursor. fetchall()


for row in rows:
    print(row)

conn.close()

