import requests
from bs4 import BeautifulSoup


url = "http://www.washingtonpost.com/wp-dyn/content/article/2010/08/29/AR2010082902749.html"
url_page2 = 'http://www.washingtonpost.com/wp-dyn/content/article/2010/08/29/AR2010082902749_2.html?sid=ST2010082902923'
r = requests.get(url)
r2 = requests.get(url_page2)
r_html = r.text + r2.text
soup = BeautifulSoup(r_html, features="html.parser")
content = soup.find_all("div", {"id": "body_after_content_column"})
for item in content:
    print(item.text)
