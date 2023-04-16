import requests
from bs4 import BeautifulSoup

url = 'https://www.nytimes.com/'
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')

titles = soup.find_all('h2', {'class': 'css-1vvhd4r esl82me2'})

for title in titles:
    if title.text.strip():
        print(title.text.strip())
