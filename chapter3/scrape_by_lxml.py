from urllib.request import urlopen
import lxml.html

# HTMLファイルを読み込み、getroot()メソッドでHtmlElementオブジェクトを得る
tree = lxml.html.parse('index.html')
html = tree.getroot()

for anchor in html.cssselect('a'):
    # textがない場合はNoneが帰ってくる
    print(anchor.get('href'), anchor.text)
