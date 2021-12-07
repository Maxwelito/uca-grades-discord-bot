import mechanize
from bs4 import BeautifulSoup
from secret import passw

br = mechanize.Browser()
br.open("https://ent.uca.fr")

br.form = list(br.forms())[0]

br["username"] = "maaudigie"
br["password"] = passw

br.submit()

br.open("https://ent.uca.fr/scolarite/stylesheets/etu/welcome.faces")

br.open("https://ent.uca.fr/scolarite/stylesheets/etu/notes.faces")

br.form = list(br.forms())[3]
br.form.set_all_readonly(False)
br["_id74:_idcl"] = "_id74:tableetp:0:_id128"
br["_id74:_link_hidden_"] = "null"
br['row'] = '4'

response = br.submit()
soup = BeautifulSoup(response, 'lxml')
print(soup.prettify())

'''with open("ziggy.html", "w", encoding = 'utf-8') as file :
    file.write(str(soup4))'''
