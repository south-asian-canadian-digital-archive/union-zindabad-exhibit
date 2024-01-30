import json
from bs4 import BeautifulSoup

import requests

with open('urls.json', 'r') as f:
    urls: list[dict] = json.load(f)


for page in urls:

    html = requests.get(page['link'])
    soup = BeautifulSoup(html.text, 'html.parser')

    page['content'] = str(soup.find('div', {'id': 'content'}))

    if 'chapters' in page.keys():
        for chapter in page['chapters']:
            html = requests.get(chapter['link'])
            soup = BeautifulSoup(html.text, 'html.parser')

            chapter['content'] = str(soup.find('div', {'id': 'content'}))

# print(urls[0])

with open('content.json', 'w') as f:
    json.dump(urls, f, indent=4)
