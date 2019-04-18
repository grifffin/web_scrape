#!/usr/bin/env python3

from bs4 import BeautifulSoup
import requests
import json

#  get beautifulsoup object for the link
page_link = 'https://en.wikipedia.org/wiki/List_of_Latin_phrases_(full)'
page_response = requests.get(page_link, timeout=5)
page_content = BeautifulSoup(page_response.content, 'html.parser')

#  there's a table for each letter. this combines them into a list called rows
tables = page_content.find_all('table', class_='wikitable')
rows = []
for table in tables:
    table_body = table.find('tbody')
    rows += table_body.find_all('tr')

#  define the list 
phrases = []
for row in rows:
    #  normally, the phrase is the first col, and the translation is the second
    cols = row.find_all('td')
    if len(cols) > 1:
        dict = {}
        dict['phrase'] = cols[0].text
        dict['translation'] = cols[1].text
        phrases.append(dict)

#  use the other line for pretty print
#  print(json.dumps(phrases, indent=4))
print(json.dumps(phrases))
