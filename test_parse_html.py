from bs4 import BeautifulSoup

with open("notes_complet.html") as file :
    soup = BeautifulSoup(file, 'lxml')

tag = soup.tbody
for i in range (0, len(tag.contents)) :
    print("item n°", i, tag.contents[i])

