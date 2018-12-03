from bs4 import BeautifulSoup

with open("HTMLWiki.html") as fp:
    soup = BeautifulSoup(fp, 'html.parser')

#soup = BeautifulSoup("<html>data</html>")

soup.name