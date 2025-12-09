import xmltodict

bookstore_xml = """
<bookstore>
    <book>
        <title>Harry Potter</title>
        <price>29.99</price>
    </book>
    <book>
        <title>Harry Potter 2</title>
        <price>39.99</price>
    </book>
</bookstore>"""

data = xmltodict.parse(bookstore_xml)
print(data)
