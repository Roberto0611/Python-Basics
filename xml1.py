#Import XML library
import xml.etree.ElementTree as ET

#Create XML
data = '''
<person>
 <name> Chuck </name>
 <phone type="intl">
  +1 734 303 4456
 </phone>
 <email hide="yes"/>
</person>
'''

#Search for the data.
tree = ET.fromstring(data);
print('name:', tree.find('name').text);
print('Attr:',tree.find('email').get('hide'));