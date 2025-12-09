'''
Use xmltodict to parse the bookstore_xml string below.
Print the value of the attribute @category for the first book. 
(Note: xmltodict stores attributes with an @ symbol prefix, e.g., @id).
Print the text of the author for the second book.
'''

import xmltodict
bookstore_xml = """
<bookstore>
    <book category="cooking">
        <title lang="en">Everyday Italian</title>
        <author>Giada De Laurentiis</author>
        <price>30.00</price>
    </book>
    <book category="children">
        <title lang="en">Harry Potter</title>
        <author>J.K. Rowling</author>
        <price>29.99</price>
    </book>
</bookstore>
"""
data  = xmltodict.parse(bookstore_xml)
print(data['bookstore']['book'][0]['@category'])
print(data['bookstore']['book'][1]['title']['#text'])
