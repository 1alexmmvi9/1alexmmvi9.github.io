import sqlite3

conexion = sqlite3.connect('empresa.db')

cursor = conexion.cursor()

cursor.execute('''
    CREATE TABLE 
    IF NOT EXISTS clientes
    (
        Identificador INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT,
        apellidos TEXT,
        email TEXT,
        direccion TEXT
    )
''')

cursor.execute('''
    INSERT INTO clientes
    VALUES (
        NULL,
        'Andrés',
        'Ruiz',
        'andresruiztorres782@gmail.com.com',
        'La calle de Andrés'
    );
''')

conexion.commit()

cursor.execute('''
    SELECT * FROM clientes
''')

filas = cursor.fetchall()

for fila in filas:
    print(fila)

conexion.close()
