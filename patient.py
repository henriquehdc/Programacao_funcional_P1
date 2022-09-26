import sqlite3
conn = sqlite3.connect('Prova_Parcial_1.db')
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Patient(
    PatientID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL,
    LastName TEXT NOT NULL
)
""")
conn.commit()
conn.close()