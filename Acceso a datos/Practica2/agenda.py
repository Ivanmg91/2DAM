#Si el csv no existe, lo crea
import csv
import os.path

rutaDelCsv = "./agenda.csv"
opcionMenuAgenda = 0

if not os.path.exists(rutaDelCsv):

    print("No hay ninguna agenda, se creará una nueva")
    primeraFila = "nombre;apellidos;email;telefono1;telefono2;direccion"

    with open('agenda.csv', mode='w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(primeraFila.split(";"))
        print("Agenda creada")

    #Entrar en el bucle del menu de la agenda
    print("Bienvenido a la agenda\n1.Añadir contacto\n2.Modificar contacto\n3.Eliminar contacto\n4.Buscar contacto\n5.Mostrar lista de contactos ordenada\n6.Salir")
    opcionMenuAgenda = int(input("Introduce una opción: "))

    while opcionMenuAgenda != 6:
        if opcionMenuAgenda == 1:

            nombre = input("Introduce el nombre: ")
            apellidos = input("Introduce los apellidos: ")
            email = input("Introduce el email: ")
            telefono1 = input("Introduce el primer telefono: ")
            telefono2 = input("Introduce el segundo telefono: ")
            direccion = input("Introduce la dirección: ")

            with open('agenda.csv', mode='a', newline='') as file:
                writer = csv.writer(file, delimiter=';')
                writer.writerow([nombre, apellidos, email, telefono1, telefono2, direccion])
                print("Contacto añadido")

        elif opcionMenuAgenda == 2:

            # Guardar todos los contactos en una lista
            todosloscontactos = []
            with open('agenda.csv', mode='r', newline='') as file:
                reader = csv.reader(file, delimiter=';')
                for row in reader:
                    todosloscontactos.append(row)

            contactoAModificar = input("Introduce el nombre del contacto a modificar: ")
            contactoApellidoAEliminar = input("Introduce los apellidos del contacto a modificar: ")
            contactos = []

            # Bucle que recorre todos los contactos y si existe el contacto a modificar, hace algo
            for contacto in todosloscontactos:
                if contacto[0] == contactoAModificar and contacto[1] == contactoApellidoAEliminar:
                    # guardar todos los contactos menos el que se quiere modificar
                    with open('agenda.csv', mode='r', newline='') as file:
                        reader = csv.reader(file, delimiter=';')
                        for row in reader:
                            if row[0] != contactoAModificar or row[1] != contactoApellidoAEliminar:
                                contactos.append(row)

                    # borrar todo el contenido del csv y escribir los contactos menos el que se quiere modificar, para luego añadir el contacto modificado
                    with open('agenda.csv', mode='w', newline='') as file:
                        writer = csv.writer(file, delimiter=';')
                        writer.writerows(contactos)

                    nombreMod = input("Introduce el nuevo nombre: ")
                    apellidosMod = input("Introduce los nuevos apellidos: ")
                    emailMod = input("Introduce el nuevo email: ")
                    telefono1Mod = input("Introduce el nuevo primer telefono: ")
                    telefono2Mod = input("Introduce el nuevo segundo telefono: ")
                    direccionMod = input("Introduce la nueva dirección: ")

                    with open('agenda.csv', mode='a', newline='') as file:
                        writer = csv.writer(file, delimiter=';')
                        writer.writerow([nombreMod, apellidosMod, emailMod, telefono1Mod, telefono2Mod, direccionMod])

            # Si no existe el contacto a modificar, se muestra un mensaje. Si contactos esta vacio, es que no se ha encontrado el contacto
            if not contactos:
                print("El contacto no existe")



        elif opcionMenuAgenda == 3:

            contactoAEliminar = input("Introduce el nombre del contacto a eliminar: ")
            contactoApellidoAEliminar = input("Introduce los apellidos del contacto a eliminar: ")
            # Guardar todos los contactos en una lista
            todosloscontactos = []
            with open('agenda.csv', mode='r', newline='') as file:
                reader = csv.reader(file, delimiter=';')
                for row in reader:
                    todosloscontactos.append(row)

            # Filtrar el contacto a eliminar
            for contacto in todosloscontactos:
                if contacto[0] == contactoAEliminar and contacto[1] == contactoApellidoAEliminar:
                    todosloscontactos.remove(contacto)

            contactos = todosloscontactos

            # Borrar todo el contenido del csv y escribir los contactos actualizados
            with open('agenda.csv', mode='w', newline='') as file:
                writer = csv.writer(file, delimiter=';')
                writer.writerows(contactos)

        elif opcionMenuAgenda == 4:

            contactoABuscar = input("Introduce el nombre del contacto que quieres buscar: ")
            contactoImprimir = ""

            # Guardar todos los contactos en una lista
            todosloscontactos = []
            with open('agenda.csv', mode='r', newline='') as file:
                reader = csv.reader(file, delimiter=';')
                for row in reader:
                    todosloscontactos.append(row)

            for contacto in todosloscontactos:
                if contacto[0] == contactoABuscar:
                    contactoImprimir = contacto
                    print(contactoImprimir)

            if not contactoImprimir:
                print("El contacto no existe")


        elif opcionMenuAgenda == 5:

            # Guardar todos los contactos en una lista excepto la primera fila
            todosloscontactos = []
            with open('agenda.csv', mode='r', newline='') as file:
                reader = csv.reader(file, delimiter=';')
                next(reader)
                for row in reader:
                    todosloscontactos.append(row)

            # Ordenar la lista de contactos
            todosloscontactos.sort(key=lambda contacto: contacto[0].lower())

            # Imprimir la lista de contactos ordenada
            for contacto in todosloscontactos:
                print(contacto)

        else:
            print("Opción no válida")

        opcionMenuAgenda = int(input("Introduce una opción:\n1.Añadir contacto\n2.Modificar contacto\n3.Eliminar contacto\n4.Buscar contacto\n5.Mostrar lista de contactos ordenada\n6.Salir"))


else:
    #Entrar en el bucle del menu de la agenda
    print("Bienvenido a la agenda\n1.Añadir contacto\n2.Modificar contacto\n3.Eliminar contacto\n4.Buscar contacto\n5.Mostrar lista de contactos ordenada\n6.Salir")
    opcionMenuAgenda = int(input("Introduce una opción: "))

    while opcionMenuAgenda != 6:
        if opcionMenuAgenda == 1:

            nombre = input("Introduce el nombre: ")
            apellidos = input("Introduce los apellidos: ")
            email = input("Introduce el email: ")
            telefono1 = input("Introduce el primer telefono: ")
            telefono2 = input("Introduce el segundo telefono: ")
            direccion = input("Introduce la dirección: ")

            with open('agenda.csv', mode='a', newline='') as file:
                writer = csv.writer(file, delimiter=';')
                writer.writerow([nombre, apellidos, email, telefono1, telefono2, direccion])
                print("Contacto añadido")

        elif opcionMenuAgenda == 2:

            # Guardar todos los contactos en una lista
            todosloscontactos = []
            with open('agenda.csv', mode='r', newline='') as file:
                reader = csv.reader(file, delimiter=';')
                for row in reader:
                    todosloscontactos.append(row)

            contactoAModificar = input("Introduce el nombre del contacto a modificar: ")
            contactoApellidoAEliminar = input("Introduce los apellidos del contacto a modificar: ")
            contactos = []

            # Bucle que recorre todos los contactos y si existe el contacto a modificar, hace algo
            for contacto in todosloscontactos:
                if contacto[0] == contactoAModificar and contacto[1] == contactoApellidoAEliminar:
                    # guardar todos los contactos menos el que se quiere modificar
                    with open('agenda.csv', mode='r', newline='') as file:
                        reader = csv.reader(file, delimiter=';')
                        for row in reader:
                            if row[0] != contactoAModificar or row[1] != contactoApellidoAEliminar:
                                contactos.append(row)

                    # borrar todo el contenido del csv y escribir los contactos menos el que se quiere modificar, para luego añadir el contacto modificado
                    with open('agenda.csv', mode='w', newline='') as file:
                        writer = csv.writer(file, delimiter=';')
                        writer.writerows(contactos)

                    nombreMod = input("Introduce el nuevo nombre: ")
                    apellidosMod = input("Introduce los nuevos apellidos: ")
                    emailMod = input("Introduce el nuevo email: ")
                    telefono1Mod = input("Introduce el nuevo primer telefono: ")
                    telefono2Mod = input("Introduce el nuevo segundo telefono: ")
                    direccionMod = input("Introduce la nueva dirección: ")

                    with open('agenda.csv', mode='a', newline='') as file:
                        writer = csv.writer(file, delimiter=';')
                        writer.writerow([nombreMod, apellidosMod, emailMod, telefono1Mod, telefono2Mod, direccionMod])

            # Si no existe el contacto a modificar, se muestra un mensaje. Si contactos esta vacio, es que no se ha encontrado el contacto
            if not contactos:
                print("El contacto no existe")



        elif opcionMenuAgenda == 3:

            contactoAEliminar = input("Introduce el nombre del contacto a eliminar: ")
            contactoApellidoAEliminar = input("Introduce los apellidos del contacto a eliminar: ")
            # Guardar todos los contactos en una lista
            todosloscontactos = []
            with open('agenda.csv', mode='r', newline='') as file:
                reader = csv.reader(file, delimiter=';')
                for row in reader:
                    todosloscontactos.append(row)

            # Filtrar el contacto a eliminar
            for contacto in todosloscontactos:
                if contacto[0] == contactoAEliminar and contacto[1] == contactoApellidoAEliminar:
                    todosloscontactos.remove(contacto)

            contactos = todosloscontactos


            # Borrar todo el contenido del csv y escribir los contactos actualizados
            with open('agenda.csv', mode='w', newline='') as file:
                writer = csv.writer(file, delimiter=';')
                writer.writerows(contactos)

        elif opcionMenuAgenda == 4:

            contactoABuscar = input("Introduce el nombre del contacto que quieres buscar: ")
            contactoImprimir = ""

            # Guardar todos los contactos en una lista
            todosloscontactos = []
            with open('agenda.csv', mode='r', newline='') as file:
                reader = csv.reader(file, delimiter=';')
                for row in reader:
                    todosloscontactos.append(row)

            for contacto in todosloscontactos:
                if contacto[0] == contactoABuscar:
                    contactoImprimir = contacto
                    print(contactoImprimir)

            if not contactoImprimir:
                print("El contacto no existe")


        elif opcionMenuAgenda == 5:

            # Guardar todos los contactos en una lista excepto la primera fila
            todosloscontactos = []
            with open('agenda.csv', mode='r', newline='') as file:
                reader = csv.reader(file, delimiter=';')
                next(reader)
                for row in reader:
                    todosloscontactos.append(row)

            # Ordenar la lista de contactos
            todosloscontactos.sort(key=lambda contacto: contacto[0].lower())

            # Imprimir la lista de contactos ordenada
            for contacto in todosloscontactos:
                print(contacto)

        else:
            print("Opción no válida")

        opcionMenuAgenda = int(input("Introduce una opción:\n1.Añadir contacto\n2.Modificar contacto\n3.Eliminar contacto\n4.Buscar contacto\n5.Mostrar lista de contactos ordenada\n6.Salir"))

