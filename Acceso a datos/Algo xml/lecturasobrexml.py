import xml.etree.ElementTree as ET

tree = ET.parse('items2.xml')
root = tree.getroot()

# Find the first 'item' object
for elem in root:
    print(elem.find('item').get('name'))

# Find all "item" objects and print their "name" attribute
for elem in root:
    for subelem in elem.findall('item'):
        # If we don't need to know the name of the attribute(s), get dict
        print(subelem.attrib)
        # If we know the name of the attribute, access it directly
        print(subelem.get('name'))