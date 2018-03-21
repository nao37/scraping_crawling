import sys
import re
from urllib.request import urlopen

f = urlopen('http://sample.scraping-book.com/dp')
byte_content = f.read()

scanned_text = byte_content[:1024].decode('ascii', errors='replace')

match = re.search(r'charset=["\']?([\w-]+)', scanned_text)
if match:
    encoding = match.group(1)
else:
    encoding = 'utf-8'
print('encoding:', encoding, file=sys.stderr)

text = byte_content.decode(encoding)
print(text)