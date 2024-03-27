import requests
from bs4 import BeautifulSoup as bs
import pickle


letters = ['Г','К','Н','П','С','Т','Ч','Ш','Д','В']
s = {}

for letter in letters:

    print(letter)

    page = 1
    w = []

    r = requests.get(f"https://synonymonline.ru/{letter}")
    html = bs(r.content, 'html.parser')

    while r.ok:
        print(page)
        row = html.find_all("div", class_="row")[1]
        words = row.select(".words-list")
        for k in words:
            w += k.text.split()
        page += 1
        r = requests.get(f"https://synonymonline.ru/{letter}?page={page}")
        html = bs(r.content, 'html.parser')

    s[letter] = w

with open('words.txt', 'wb') as out:
    pickle.dump(s, out)