import xmltodict

bookstore_xml = """
<bookstore>
    <book>
        <title>Harry Potter</title>
        <price>29.99</price>
    </book>
</bookstore>"""

data = xmltodict.parse(bookstore_xml)
print(data)
