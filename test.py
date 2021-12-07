import re
import mechanize
from bs4 import BeautifulSoup
from secret import passw

br = mechanize.Browser()
br.open("https://ent.uca.fr")

br.form = list(br.forms())[0]

br["username"] = "maaudigie"
br["password"] = passw

response = br.submit()
soup = BeautifulSoup(response, 'lxml')

response2 = br.open("https://ent.uca.fr/scolarite/stylesheets/etu/welcome.faces")
soup2 = BeautifulSoup(response2, 'lxml')

response3 = br.open("https://ent.uca.fr/scolarite/stylesheets/etu/notes.faces")
soup3 = BeautifulSoup(response3, 'lxml')

br.form = list(br.forms())[3]
br.form.set_all_readonly(False)
br["_id74:_idcl"] = "_id74:tableetp:0:_id128"
br["_id74:_link_hidden_"] = "null"
br['row'] = '4'

response4 = br.submit()
soup4 = BeautifulSoup(response4, 'lxml')
print(soup4.prettify())

with open("ziggy.html", "w", encoding = 'utf-8') as file :
    file.write(str(soup4))
