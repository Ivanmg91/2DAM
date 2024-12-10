import xml.etree.ElementTree as ET

data = ET.Element('data')
items = ET.SubElement(data, 'items')

item1 = ET.SubElement(items, 'item', name='item1')
item1.text = 'item1abc'

item2 = ET.SubElement(items, 'item', name='item2')
item2.text = 'item2abc'

item3 = ET.SubElement(items, 'item', name='item3')
item3.text = 'item3abc'

# Convertir el objeto Elementtree a cadena
tree = ET.ElementTree(data)

with open("data.xml", "wb") as file:
    tree.write(file, encoding='utf-8', xml_declaration=True)

print("XML creado")