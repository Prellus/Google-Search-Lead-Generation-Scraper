from search_engines import Google

engine = Google()

query = input("Search Query: ")
max_pages = int(input("Max pages: "))

output = engine.search(query, pages=max_pages)
text = output.text()
print(text)
engine.output(output='csv', path='results')