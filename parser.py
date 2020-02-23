import urllib.request
from bs4 import BeautifulSoup

html = '<td id="td1" class="title">' \
       '  <div class="tit3">' \
       '    <a href="/movie/bi/mi/basic.nhn?code=161242" title="범죄도시">범죄도시</a>' \
       '  </div>' \
       '</td>'


# url = "https://wiki.jieunkim.site/"
# req = urllib.request.urlopen(url)
# res = req.read()
def ex1():
    bs = BeautifulSoup(html, 'html.parser')
    # keywords = soup.find_all('span')

    tag = bs.a
    print(tag, type(tag))


def ex2():
    bs = BeautifulSoup(html, 'html.parser')

    tag = bs.td
    print(tag['class'])
    print(tag['id'])
    print(tag.attrs)

    tag = bs.div
    print(tag['id'])


def ex3():
    bs = BeautifulSoup(html, 'html.parser')

    tag = bs.find('div', attrs={'class', 'tit3'})
    print(tag)

    tag = bs.find('td', attrs={'class': 'not_exist'})
    print(tag)

    tag = bs.find(attrs={'title': '범죄도시'})
    print(tag)


def ex4():
    bs = BeautifulSoup(html, 'html.parser')
    tag = bs.select('td div a')[0]
    print(tag)

    text = tag.contents[0]
    print(text)


def ex5():
    bs = BeautifulSoup(html, 'html.parser')
    tag = bs.select('td')[0]
    print(tag)

    div_elements = tag.find_all('div')
    for div in div_elements:
        div.extract()

    print(tag)


ex5()
