from bs4 import BeautifulSoup

with open('index.html') as f:
    soup = BeautifulSoup(f, 'html.parser')

for a in soup.select('a'):
    print(a.text, a.attrs['href'])

for a in soup.find_all('a'):
    print(a.get('href'))