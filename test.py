from urllib import response
import requests
from bs4 import BeautifulSoup
from twill.commands import *
from secret import passw
import mechanize

br = mechanize.Browser()
br.open("https://ent.uca.fr")
for form in br.forms() :
    print("Form name:", form.name)
    #print(form)

br.form = list(br.forms())[0]

for control in br.form.controls:
    #print(control)
    print ("type=%s, name=%s value=%s" % (control.type, control.name, br[control.name]))
'''
go('https://ent.uca.fr')
showforms()
fv("1", "username", "maaudigie")
fv("1", "password", passw)
submit()
go('https://ent.uca.fr/scolarite/stylesheets/etu/welcome.faces')
save_html('menu_notes.html')
showlinks()
show()


response = requests.get('https://ent.uca.fr/scolarite/stylesheets/etu/notes.faces')
print (response.status_code)

soup = BeautifulSoup(response.content, 'lxml')
print(soup.prettify())
'''