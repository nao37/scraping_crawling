import re
from urllib.request import urlopen
import sqlite3
from html import unescape


def main():
    base_url = 'http://sample.scraping-book.com/dp'
    html = fetch(base_url)
    books = scrape(html)
    save('books.db', books)


def fetch(base_url):
    base_url = base_url
    f = urlopen(base_url)
    encoding = f.info().get_content_charset(failobj='utf-8')
    html = f.read().decode(encoding)

    return html


def scrape(html):
    books = []
    for partial_html in re.findall(r'<a itemprop="url" href=".*?</ul>\s*</a></li>', html, re.DOTALL):
        title = re.search(r'<p itemprop="name" class="title">.*?</p>', partial_html, re.DOTALL).group(0)
        title = re.sub(r'<[^>].*?>', '', title)
        title = unescape(title)

        url = re.search(r'<a itemprop="url" href="(.*?)">', partial_html, re.DOTALL).group(1)
        url = 'http://sample.scraping-book.com' + url

        books.append({'title': title, 'url': url})

    return books


def save(db_path, books):
    conn = sqlite3.connect(db_path)

    c = conn.cursor()

    c.execute('DROP TABLE IF EXISTS books')
    c.execute('''
        CREATE TABLE books (
            title text,
            url text
        )
    ''')
    c.executemany('INSERT INTO books VALUES (:title, :url)', books)

    conn.commit()
    conn.close()


if __name__ == '__main__':
    main()
