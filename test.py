'''from urllib import response
import requests
from twill.commands import *
'''
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
#print(soup.prettify())

response2 = br.open("https://ent.uca.fr/scolarite/stylesheets/etu/welcome.faces")
soup2 = BeautifulSoup(response2, 'lxml')
#print(soup2.prettify())
'''
print("\n")
print("Les forms \n")
for form in br.forms() :
    print("Form name:", form.name)
    #print(form)

print("\n")
br.form = list(br.forms())[1]
print("Les controles du form \n")
for control in br.form.controls:
    #print(control)
    print ("type=%s, name=%s value=%s" % (control.type, control.name, br[control.name]))
'''
#lien1 = br.find_link(text_regex=re.compile("Notes"))
#print(lien1)
response3 = br.open("https://ent.uca.fr/scolarite/stylesheets/etu/notes.faces")
soup3 = BeautifulSoup(response3, 'lxml')
#print(soup3.prettify())
'''
print("Les liens \n")
for link in br.links():
    print(link.text, link.url)
print("\n")
print("Les forms \n")
for form in br.forms() :
    print("Form name:", form.name)
    #print(form)

print("\n")
br.form = list(br.forms())[1]
print("Les controles du form \n")
for control in br.form.controls:
    #print(control)
    print ("type=%s, name=%s value=%s" % (control.type, control.name, br[control.name]))
'''
lien1 = list(br.links())[12]
print(lien1)
request4 = br.click_link(lien1)
response4 = br.follow_link(lien1)
soup4 = BeautifulSoup(response4)
print(soup4.prettify())

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