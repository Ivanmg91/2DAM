import csv
import xml.etree.ElementTree as ET

csvA = 'agenda.csv'
xml = 'agenda.xml'

# Crear la raiz
raiz = ET.Element('agenda')
contactos = ET.SubElement(raiz, 'contactos')

with open(csvA, mode='r', newline='') as file:
    reader = csv.reader(file, delimiter=';')
    encabezado = next(reader)

    for linea in reader:
        contacto = ET.SubElement(contactos, 'contacto')
        for i in range(len(encabezado)):
            elemento = ET.SubElement(contacto, encabezado[i])
            elemento.text = linea[i]

# El element tree a cadena
xml_cadena = ET.tostring(raiz, encoding='utf-8', method='xml').decode('utf-8')

with open(xml, 'w') as file:
    file.write(xml_cadena)
print("CSV transformado a XML")