import mysql.connector
from MySQLdb.cursors import Cursor

class Centro:
    def __init__(self, id, regim_id, provincia_id, codi, centre, direccio, localitat, telefon, query):
        self.id = id
        self.regim_id = regim_id
        self.provincia_id = provincia_id
        self.codi = codi
        self.centre = centre
        self.direccio = direccio
        self.localitat = localitat
        self.telefon = telefon
        self.query = query

def conectar_bd():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        port="33006",
        database="centres_gva"
    )

def mostrar_opciones():
    print("╔═══════════════════════════╗")
    print("║ 1. Extracción de datos    ║")
    print("║ 2. Nuevos datos           ║")
    print("║ 3. Actualización de datos ║")
    print("║ 4. Borrado de datos       ║")
    print("║ 5. Salir                  ║")
    print("╚═══════════════════════════╝")

def mostrar_opciones_extraccion_datos():
    print("╔════════════════════════════════════════════════════════════════════╗")
    print("║ 1. Listar todos los nombres de centros.                            ║")
    print("║ 2. Listar todos los nombres de centros de la provincia de Valencia.║")
    print("║ 3. Listar todos los nombres y códigos de los ciclos.               ║")
    print("║ 4. Listar todos los centros donde se imparte el ciclo de DAM.      ║")
    print("║ 5. Obtener toda la información a cerca del centro con id = 18.     ║")
    print("║ 6. Salir                                                           ║")
    print("╚════════════════════════════════════════════════════════════════════╝")

def mostrar_opciones_nuevos_datos():
    print("╔══════════════════════════════════════╗")
    print("║ 1. Crear un nuevo centro por defecto.║")
    print("║ 2. Salir                             ║")
    print("╚══════════════════════════════════════╝")

def mostrar_opciones_actualizacion_datos():
    print("╔════════════════════════════════════════════╗")
    print("║ 1. Actualizar el teléfono del IES La Sénia.║")
    print("║ 2. Salir                                   ║")
    print("╚════════════════════════════════════════════╝")

def mostrar_opciones_borrado_de_datos():
    print("╔════════════════════════════════════════╗")
    print("║ 1. Borrar el centro público IES LA MAR.║")
    print("║ 2. Salir                               ║")
    print("╚════════════════════════════════════════╝")

mostrar_opciones()
opcion = input("Introduce una opción: ")

while opcion != "5":
    if opcion == "1":
        while True:
            mostrar_opciones_extraccion_datos()
            opcion = input("Introduce una opción: ")

            if opcion == "1":
                conexion = conectar_bd()
                cursor = conexion.cursor()
                cursor.execute("SELECT id, regim_id, provincia_id, codi, centre, direccio, localitat, telefon FROM centre")
                almacenar_centros = cursor.fetchall()

                for i in almacenar_centros:
                    centro = Centro(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], "SELECT id, regim_id, provincia_id, codi, centre, direccio, localitat, telefon FROM centre")
                    print(f"Centre: {centro.centre}")

                cursor.close()
                conexion.close()


            elif opcion == "2":
                conexion = conectar_bd()
                cursor = conexion.cursor()
                cursor.execute("SELECT id, regim_id, provincia_id, codi, centre, direccio, localitat, telefon FROM centre WHERE provincia_id = 2")
                almacenar_centros = cursor.fetchall()

                for i in almacenar_centros:
                    centro = Centro(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], "SELECT id, regim_id, provincia_id, codi, centre, direccio, localitat, telefon FROM centre WHERE provincia_id = 2")
                    print(f"Centre: {centro.centre}")

                cursor.close()
                conexion.close()

            elif opcion == "3":
                conexion = conectar_bd()
                cursor = conexion.cursor()
                cursor.execute("SELECT id, regim_id, provincia_id, codi, centre, direccio, localitat, telefon FROM centre")
                almacenar_centros = cursor.fetchall()

                for i in almacenar_centros:
                    centro = Centro(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], "SELECT id, regim_id, provincia_id, codi, centre, direccio, localitat, telefon FROM centre")
                    print(f"Centre: {centro.centre} i Codi: {centro.codi}")

                cursor.close()
                conexion.close()

            elif opcion == "4":
                conexion = conectar_bd()
                cursor = conexion.cursor()
                cursor.execute("SELECT c.id, c.regim_id, c.provincia_id, c.codi, c.centre, c.direccio, c.localitat, c.telefon FROM centre c JOIN cicle_centre cc ON c.id = cc.centre_id JOIN cicle ci ON ci.id = cc.cicle_id WHERE ci.nom = 'DESENVOLUPAMENT D''APLICACIONS MULTIPLATAFORMA'")
                almacenar_centros = cursor.fetchall()

                for i in almacenar_centros:
                    centro = Centro(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], "SELECT c.id, c.regim_id, c.provincia_id, c.codi, c.centre, c.direccio, c.localitat, c.telefon FROM centre c JOIN cicle_centre cc ON c.id = cc.centre_id JOIN cicle ci ON ci.id = cc.cicle_id WHERE ci.nom = 'DESENVOLUPAMENT D''APLICACIONS MULTIPLATAFORMA'")
                    print(f"Centre: {centro.centre}")


                cursor.close()
                conexion.close()

            elif opcion == "5":
                conexion = conectar_bd()
                cursor = conexion.cursor()
                cursor.execute("SELECT id, regim_id, provincia_id, codi, centre, direccio, localitat, telefon FROM centre WHERE id = 18")
                almacenar_centros = cursor.fetchall()

                for i in almacenar_centros:
                    centro = Centro(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], "SELECT id, regim_id, provincia_id, codi, centre, direccio, localitat, telefon FROM centre WHERE id = 18")
                    print(f"Centre: {centro.centre} i Codi: {centro.codi} i Direcció: {centro.direccio} i Localitat: {centro.localitat} i Telèfon: {centro.telefon}")

                cursor.close()
                conexion.close()

            elif opcion == "6":
                break

    elif opcion == "2":
        while True:
            mostrar_opciones_nuevos_datos()
            opcion = input("Introduce una opción: ")

            if opcion == "1":
                conexion = conectar_bd()
                cursor = conexion.cursor()

                #NO me deja poner el codigo del pdf porq empieza por 0, he puesto un 1 delante.
                centro_default = Centro(99, 1, 3, "03013339", "IES LA MAR", "Av. AUGUSTA, 2", "03730 - XABIA", "966428205", "INSERT INTO centre (id, regim_id, provincia_id, codi, centre, direccio, localitat, telefon) VALUES (99, 1, 3, 03013339, 'IES LA MAR', 'C/ LA MAR', 'ALZIRA', '962400000')")
                cursor.execute("INSERT INTO centre (id, regim_id, provincia_id, codi, centre, direccio, localitat, telefon) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (centro_default.id, centro_default.regim_id, centro_default.provincia_id, centro_default.codi, centro_default.centre, centro_default.direccio, centro_default.localitat, centro_default.telefon))
                cursor.execute("INSERT INTO cicle_centre (centre_id, cicle_id) VALUES (99, 1)")
                cursor.execute("INSERT INTO cicle_centre (centre_id, cicle_id) VALUES (99, 3)")
                cursor.execute("INSERT INTO cicle_centre (centre_id, cicle_id) VALUES (99, 4)")

                print("Centro creado correctamente")

                conexion.commit()
                cursor.close()
                conexion.close()

            elif opcion == "2":
                break

    elif opcion == "3":
        while True:
            mostrar_opciones_actualizacion_datos()
            opcion = input("Introduce una opción: ")

            if opcion == "1":
                conexion = conectar_bd()
                cursor = conexion.cursor()
                cursor.execute("UPDATE centre SET telefon = '964000000' WHERE centre = 'IES LA SÉNIA'")

                print("Teléfono actualizado correctamente")

                conexion.commit()
                cursor.close()
                conexion.close()

            elif opcion == "2":
                break

    elif opcion == "4":
        while True:
            mostrar_opciones_borrado_de_datos()
            opcion = input("Introduce una opción: ")

            if opcion == "1":
                conexion = conectar_bd()
                cursor = conexion.cursor()
                cursor.execute("DELETE FROM cicle_centre WHERE centre_id = (SELECT id FROM centre WHERE centre = 'IES LA MAR')")
                cursor.execute("DELETE FROM centre WHERE centre = 'IES LA MAR'")

                print("Centro borrado correctamente")

                conexion.commit()
                cursor.close()
                conexion.close()

            elif opcion == "2":
                break

    mostrar_opciones()
    opcion = input("Introduce una opción: ")