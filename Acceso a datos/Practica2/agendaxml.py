#Si el csv no existe, lo crea
import csv
import os.path
import csv
import xml.etree.ElementTree as ET

rutaDelXml = "./agenda.xml"
opcionMenuAgenda = 0

if not os.path.exists(rutaDelXml):

    print("No hay ninguna agenda, se creará una nueva")
    # Craer el xml con la raiz
    raiz = ET.Element('agenda')
    tree = ET.ElementTree(raiz)
    tree.write(rutaDelXml, encoding='utf-8', xml_declaration=True)

else:
    tree = ET.parse(rutaDelXml)
    raiz = tree.getroot()

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


            contactos = raiz.find("contactos")
            if contactos is None:
                contactos = ET.SubElement(raiz, 'contactos')

            contacto = ET.SubElement(contactos, 'contacto')
            ET.SubElement(contacto, 'nombre').text = nombre
            ET.SubElement(contacto, 'apellidos').text = apellidos
            ET.SubElement(contacto, 'email').text = email
            ET.SubElement(contacto, 'telefono1').text = telefono1
            ET.SubElement(contacto, 'telefono2').text = telefono2
            ET.SubElement(contacto, 'direccion').text = direccion

            tree.write(rutaDelXml, encoding='utf-8', xml_declaration=True)
            print("Contacto añadido")

        elif opcionMenuAgenda == 2:

            # Guardar datos del contacto a modificar
            nombre = input("Introduce el nombre del contacto a modificar: ")
            apellidos = input("Introduce los apellidos del contacto a modificar: ")

            # Buscar el contacto y modificarlo
            contacto_encontrado = False
            for contacto in raiz.findall(".//contacto"): # .//contacto busca en todos los niveles del arbol
                nombre_element = contacto.find('nombre')
                apellidos_element = contacto.find('apellidos')

                if nombre_element is not None and apellidos_element is not None:
                    if nombre_element.text == nombre and apellidos_element.text == apellidos:
                        contacto_encontrado = True
                        print("Contacto encontrado. Introduce los nuevos datos.")

                        nuevo_nombre = input("Introduce el nuevo nombre: ")
                        nuevo_apellidos = input("Introduce los nuevos apellidos: ")
                        nuevo_email = input("Introduce el nuevo email: ")
                        nuevo_telefono1 = input("Introduce el nuevo primer telefono: ")
                        nuevo_telefono2 = input("Introduce el nuevo segundo telefono: ")
                        nueva_direccion = input("Introduce la nueva dirección: ")

                        nombre_element.text = nuevo_nombre
                        apellidos_element.text = nuevo_apellidos
                        contacto.find('email').text = nuevo_email
                        contacto.find('telefono1').text = nuevo_telefono1
                        contacto.find('telefono2').text = nuevo_telefono2
                        contacto.find('direccion').text = nueva_direccion

                        tree.write(rutaDelXml, encoding='utf-8', xml_declaration=True)
                        print("Contacto modificado")
                        break

            if not contacto_encontrado:
                print("Contacto no encontrado")

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


