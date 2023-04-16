import requests
from bs4 import BeautifulSoup

url = 'https://www.nytimes.com/'
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')

titles = soup.find_all('h2', {'class': 'css-1vvhd4r esl82me2'})

with open('nyt_titles.txt', 'w') as f:
    for title in titles:
        f.write(title.text + '\n')
