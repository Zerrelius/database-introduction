import sqlite3

# Verbindung zur SQLite-Datenbank herstellen (Datei wird erstellt, falls nicht vorhanden)
conn = sqlite3.connect('studenten.db')

# Cursor-Objekt zum Ausführen von SQL-Befehlen
cursor = conn.cursor()

# Erstellt in der Datenbank die Tabelle students
cursor.execute('''
               CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name VARCHAR(32) NOT NULL,
                age INTEGER NOT NULL,
                course VARCHAR(32) NOT NULL
               )
''')

# Erstellung der Create oder eher insert into Funktion
def student_hinzufuegen(name, age, course):
    cursor.execute('''
    INSERT INTO students (name, age, course)
    VALUES (?, ?, ?)
    ''', (name, age, course))
    conn.commit()
    print(f"Student {name} hinzugefügt.")

# Erstellung der Read Funktion
def show_students():
    cursor.execute('SELECT * FROM students')
    students = cursor.fetchall()
    for x in students:
        print(x)

# Erstellung der Update Funktion
def update_students(stud_id, stud_name, stud_age, stud_course):
    cursor.execute('''
    UPDATE students SET name = ?, age = ?, course = ? 
    WHERE id = ? 
    ''', (stud_name, stud_age, stud_course, stud_id)
    )
    conn.commit()
    print(f"Student {stud_name} mit der Nummer {stud_id} wurde erfolgreich geupdatet.")

# Erstellung der Delete Funktion
def delete_students(stud_id):
    cursor.execute('''
    DELETE FROM students WHERE id = ?
    ''', (stud_id)
    )
    conn.commit()
    print(f"Student mit der ID: {stud_id} wurde entfernt.")

# Main Programm
while True:
    print("----- Die Studenten Datenbank -----")
    print("1. Student hinzufügen")
    print("2. Studenten Anzeigen lassen")
    print("3. Studenten Aktualisieren")
    print("4. Studenten entfernen")
    print("5. Das Programm beenden")
    print("-----")
    choose = input("Was möchten Sie tun?\n")

    if choose == "1":
        print("----- Student hinzufügen -----")
        stud_name = input("Wie lautet der Name des Studenten?\n")
        stud_age = int(input("Wie alt ist der Student?\n"))
        stud_course = input("Welchen Kurs hat der Student belegt?\n")
        student_hinzufuegen(stud_name, stud_age, stud_course)

    elif choose == "2":
        print("----- Liste der Studenten -----")
        show_students()

    elif choose == "3":
        print("----- Studeten Aktualisieren -----")
        stud_id = input("Welchen Studenten möchten Sie verändern?\n")
        new_stud_name = input("Wie lautet der neue Name des Studenten?\n")
        new_stud_age = int(input("Wie ist das neue Alter des Studenten?\n"))
        new_stud_course = input("Wie lautet der neue Kurs des Studenten?\n")
        update_students(new_stud_name, new_stud_age, new_stud_course, stud_id)
    
    elif choose == "4":
        print("----- Studenten löschen -----")
        del_stud_id = input("Welchen Studenten möchten Sie löschen? Bitte geben Sie die ID an.\n")
        delete_students(del_stud_id)

    elif choose == "5":
        print("Das Programm wird beendet. Auf wiedersehen!")
        break

    else:
        print("Bitte geben Sie nur die Auswahl Möglichkeiten an.")