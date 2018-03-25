import lxml.html
from urllib.request import urlopen

tree = lxml.html.parse('index.html')
tree = lxml.html.parse(urlopen('http://example.com/'))
print(tree)
html = tree.getroot()
print(html.cssselect('h1')[0].text)
print(html.cssselect('h1')[0].getparent().getparent().tag)