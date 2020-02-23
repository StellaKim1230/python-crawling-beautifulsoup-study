import urllib.request
from bs4 import BeautifulSoup

url = "https://wiki.jieunkim.site/2019-memoirs.html"
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

codeTags = soup.find_all('code')

for codeTag in codeTags:
    print(codeTag.contents[0])

# print(codeTags)
