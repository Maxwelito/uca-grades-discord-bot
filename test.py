import requests
from bs4 import BeautifulSoup
from twill.commands import *
from secret import passw

go('https://ent.uca.fr')
showforms()
fv("1", "username", "maaudigie")
fv("1", "password", passw)
submit()
go('https://ent.uca.fr/scolarite/stylesheets/etu/notes.faces')
show()

'''
response = requests.get('https://ent.uca.fr/scolarite/stylesheets/etu/notes.faces')
print (response.status_code)

soup = BeautifulSoup(response.content, 'lxml')
print(soup.prettify())
'''