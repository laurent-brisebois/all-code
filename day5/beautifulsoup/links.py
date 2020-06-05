from bs4 import BeautifulSoup
import requests

page = requests.get("https://laurent-brisebois.github.io/python-week-docs/course/day4/theory.html")

soup = BeautifulSoup(page.content, 'html.parser')

# loop across all <anchor> tags and find the addresses they link to
for link in soup.find_all('a'):
    link = link.get('href')
    # print(type(link))
    
    if link[0] == 'h':
        print(link)
