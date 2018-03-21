import re
from html import unescape

with open('dp.html') as f:
    html = f.read()

for partial_html in re.findall(r'<a itemprop="url".*?</ul>\s*</a></li>', html, re.DOTALL):
    url = re.search(r'<a itemprop="url" href="(.*?)">', partial_html, re.DOTALL).group(1)
    url = 'html://sample.scraping-book.com' + url

    title = re.search(r'<p itemprop="name".*?</p>', partial_html).group(0)
    title = re.sub(r'<br/>', ' ', title)
    title = re.sub(r'<.*?>', '', title)
    title = unescape(title)

    print(url, title)
