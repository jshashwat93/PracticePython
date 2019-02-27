import requests
from bs4 import BeautifulSoup


url = "https://www.nytimes.com/"
r = requests.get(url)
r_html = r.text
soup = BeautifulSoup(r_html, features="html.parser")
# headlines = soup.find_all("div", {"class": "css-1j836f9 esl82me3"})
headlines = soup.find_all(class_="css-1j836f9 esl82me3")

for item in headlines:
    if len(item.contents) == 1:
        print(item.text)
    elif len(item.contents) == 2:
        print(item.contents[1].text)
