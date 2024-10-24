import xml.etree.ElementTree as ET

# Create the file structure
data = ET.Element('data')
items = ET.SubElement(data, 'items')
item1 = ET.SubElement(items, 'item')
item2 = ET.SubElement(items, 'item')
item1.set('name', 'item1')
item2.set('name', 'item2')
item1.text = 'item1abc'
item2.text = 'item2abc'

# Convert the ElementTree to a bytes object
mydata = ET.tostring(data)

# Open the file in binary mode and write the bytes
with open("items2.xml", "wb") as myfile:
    myfile.write(mydata)