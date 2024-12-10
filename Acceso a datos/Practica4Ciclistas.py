import mysql.connector

def conectar_bd():
    return mysql.connector.connect(
        host="edu-dbms",
        user="root",
        password="dbrootpass",
        database="ciclistas"
    )

def mostrar_opciones():
    print("╔═══════════════════════════╗")
    print("║ 1. Extracción de datos    ║")
    print("║ 2. Nuevos datos           ║")
    print("║ 3. Salir                  ║")
    print("╚═══════════════════════════╝")

def mostrar_opciones_extraccion_datos():
    print("╔══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗")
    print("║ 1. Obtener el nombre y la categoría de los puertos ganados por ciclistas del equipo ‘Banesto’                                                                        ║")
    print("║ 2. Obtener el nombre de cada puerto indicando el número (netapa) y los kilómetros de la etapa en la que se encuentra el puerto.                                      ║")
    print("║ 3. Obtener el nombre y el director de los equipos a los que pertenezca algún ciclista mayor de 33 años.                                                              ║")
    print("║ 4. Obtener el nombre de los ciclistas con el color de cada maillot que hayan llevado.                                                                                ║")
    print("║ 5. Obtener pares de nombre de ciclista y número de etapa tal que ese ciclista haya ganado esa etapa habiendo llevado el maillot de color ‘Amarillo’ al menos una vez.║")
    print("║ 6. Obtener el valor del atributo netapa de las etapas que no comienzan en la misma ciudad en que acabó la anterior etapa.                                            ║")
    print("║ 7. Obtener el nombre de los equipos que tengan ciclistas indicando cuántos tiene cada uno.                                                                           ║")
    print("║ 8. Salir                                                                                                                                                             ║")
    print("╚══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝")

def mostrar_opciones_nuevos_datos():
    print("╔═════════════════════════════════════════════════════════════════════════════════════════════════════╗")
    print("║ 1. Crear un equipo                                                                                  ║")
    print("║ 2. Crear 5 ciclistas y asociados al equipo creado                                                   ║")
    print("║ 3. Crea 3 etapas y asociales como ciclista ganador alguno de los 5 ciclistas creados anteriormente  ║")
    print("║ 4. Salir                                                                                            ║")
    print("╚═════════════════════════════════════════════════════════════════════════════════════════════════════╝")

mostrar_opciones()
opcion = input("Introduce una opción: ")

while opcion != "3":
    if opcion == "1":
        mostrar_opciones_extraccion_datos()
        opcion = input("Introduce una opción: ")
        if opcion == "1":
            conexion = conectar_bd()
            cursor = conexion.cursor()
            cursor.execute("SELECT puerto.nompuerto, puerto.categoria FROM puerto JOIN ciclista ON puerto.dorsal = ciclista.dorsal JOIN equipo ON ciclista.nomeq = equipo.nomeq WHERE equipo.nomeq = 'Banesto'")

            for puerto in cursor:
                print("Nombre del puerto: ", puerto[0], " y Categoría: ", puerto[1])

            cursor.close()
            conexion.close()

            mostrar_opciones()
            opcion = input("Introduce una opción: ")

        elif opcion == "2":
            conexion = conectar_bd()
            cursor = conexion.cursor()
            cursor.execute("SELECT puerto.nompuerto, puerto.netapa, etapa.km FROM puerto JOIN etapa ON puerto.netapa = etapa.netapa")

            for puerto in cursor:
                print("Nombre del puerto: ", puerto[0], " y Número de etapa: ", puerto[1], " y Kilómetros: ", puerto[2])

            cursor.close()
            conexion.close()

            mostrar_opciones()
            opcion = input("Introduce una opción: ")

        elif opcion == "3":
            conexion = conectar_bd()
            cursor = conexion.cursor()
            cursor.execute("SELECT equipo.nomeq, equipo.director FROM equipo JOIN ciclista ON equipo.nomeq = ciclista.nomeq WHERE ciclista.edad > 33")

            for equipo in cursor:
                print("Nombre del equipo: ", equipo[0], " y Director: ", equipo[1])

            cursor.close()
            conexion.close()

            mostrar_opciones()
            opcion = input("Introduce una opción: ")

        elif opcion == "4":
            conexion = conectar_bd()
            cursor = conexion.cursor()
            cursor.execute("SELECT ciclista.nombre, maillot.color FROM ciclista JOIN llevar ON ciclista.dorsal = llevar.dorsal JOIN maillot ON llevar.codigo = maillot.codigo")

            for ciclista in cursor:
                print("Nombre del ciclista: ", ciclista[0], " y Color del maillot: ", ciclista[1])

            cursor.close()
            conexion.close()

            mostrar_opciones()
            opcion = input("Introduce una opción: ")

        elif opcion == "5":
            conexion = conectar_bd()
            cursor = conexion.cursor()
            cursor.execute("SELECT ciclista.nombre, etapa.netapa FROM ciclista JOIN etapa ON ciclista.dorsal = etapa.dorsal JOIN llevar ON ciclista.dorsal = llevar.dorsal JOIN maillot ON llevar.codigo = maillot.codigo WHERE maillot.color = 'Amarillo'")

            for ciclista in cursor:
                print("Nombre del ciclista: ", ciclista[0], " y Número de etapa: ", ciclista[1])

            cursor.close()
            conexion.close()

            mostrar_opciones()
            opcion = input("Introduce una opción: ")

        elif opcion == "6":
            conexion = conectar_bd()
            cursor = conexion.cursor()
            cursor.execute("SELECT netapa FROM etapa WHERE llegada <> salida")

            for etapa in cursor:
                print("Número de etapa: ", etapa[0])

            cursor.close()
            conexion.close()

            mostrar_opciones()
            opcion = input("Introduce una opción: ")

        elif opcion == "7":
            conexion = conectar_bd()
            cursor = conexion.cursor()
            cursor.execute("SELECT nomeq, COUNT(nomeq) FROM ciclista GROUP BY nomeq")

            for equipo in cursor:
                print("Nombre del equipo: ", equipo[0], " y Número de ciclistas: ", equipo[1])

            cursor.close()
            conexion.close()

            mostrar_opciones()
            opcion = input("Introduce una opción: ")

    if opcion == "2":
        mostrar_opciones_nuevos_datos()
        opcion = input("Introduce una opción: ")
        if opcion == "1":
            conexion = conectar_bd()
            cursor = conexion.cursor()

            cursor.execute("INSERT INTO equipo (nomeq, director) VALUES ('EquipoPrueba', 'DirectorPrueba')")
            conexion.commit()
            cursor.close()
            conexion.close()

            print("Equipo creado correctamente")

            mostrar_opciones()
            opcion = input("Introduce una opción: ")

        elif opcion == "2":
            conexion = conectar_bd()
            cursor = conexion.cursor()

            cursor.execute("SELECT COUNT(dorsal) FROM ciclista")
            for ciclista in cursor:
                dorsal = ciclista[0]

            cursor.close()
            cursor = conexion.cursor()

            for i in range(5):
                cursor.execute("INSERT INTO ciclista (dorsal, nombre, edad, nomeq) VALUES (" + str(dorsal + i + 1) + ", 'Ciclista" + str(i + 1) + "', 25, 'EquipoPrueba')")
                conexion.commit()

            cursor.close()
            conexion.close()

            print("Ciclistas creados correctamente")

            mostrar_opciones()
            opcion = input("Introduce una opción: ")

        elif opcion == "3":
            conexion = conectar_bd()
            cursor = conexion.cursor()

            cursor.execute("SELECT COUNT(netapa) FROM etapa")
            for etapa in cursor:
                netapa = etapa[0]

            cursor.close()
            cursor = conexion.cursor()

            for i in range(3):
                cursor.execute("INSERT INTO etapa (netapa, salida, llegada, dorsal) VALUES (" + str(netapa + i + 1) + ", 'Salida" + str(i + 1) + "', 'Llegada" + str(i + 1) + "', " + str(i + 1) + ")")
                conexion.commit()

            cursor.close()
            conexion.close()

            print("Etapas creadas correctamente")

            mostrar_opciones()
            opcion = input("Introduce una opción: ")


    else:
        mostrar_opciones()
        opcion = input("Introduce una opción: ")
