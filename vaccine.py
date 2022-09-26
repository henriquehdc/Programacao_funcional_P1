import sqlite3
conn = sqlite3.connect('Prova_Parcial_1.db')
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Vaccine(
    VaccineID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    PatientID INTEGER NOT NULL,
    VaccineName TEXT NOT NULL,
    DoseDate datetime NOT NULL,
    DoseNumber INTEGER,
    VaccineType TEXT NOT NULL,
    FOREIGN KEY(PatientID) REFERENCES Patient(PatientID)
)
""")
conn.commit()
conn.close()



name = input('Digite o primeiro nome do paciente: ')
lastName = input('Digite o sobrenome do paciente: ')

cursor.execute('INSERT INTO Patient(Name,LastName) VALUES (?,?)', (name,lastName))
conn.commit()

nome =  input('Digite o nome e o sobrenome do paciente que deseja adicionar a vacina: ')
vaccineName =  input('Digite o nome da vacina: ')
doseDate =  input('Digite a data da dose: ')
doseNumber = int(input('Digite o numero da dose: '))
vaccineType =  input('Digite o tipo da vacina: ')

autorid = cursor.execute('SELECT (authorID) from Author WHERE name = ?',[(nome)]).fetchone()
cursor.execute('INSERT INTO Post(author,title,created) VALUES (?,?,DateTime("now"))', (autorid[0],titulo))

conn.commit()
conn.close()