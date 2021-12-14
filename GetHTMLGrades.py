import mechanize
import re
from bs4 import BeautifulSoup
from secret import passw

def GetGradesPage(row) :
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
    br['row'] = str(row)

    response = br.submit()
    soup = BeautifulSoup(response, 'lxml')

    with open("notes_vide.html", "w", encoding = 'utf-8') as file :
        file.write(str(soup))

    br.close()

def GetRowFormation(formation) :
    br = mechanize.Browser()
    br.open("https://ent.uca.fr")

    br.form = list(br.forms())[0]

    br["username"] = "maaudigie"
    br["password"] = passw

    br.submit()

    br.open("https://ent.uca.fr/scolarite/stylesheets/etu/welcome.faces")
    br.open("https://ent.uca.fr/scolarite/stylesheets/etu/notes.faces")

    link = br.find_link(text_regex=re.compile(formation))
    print(link)

    br.close()

    

f = "2ème année DI Informatique"
GetRowFormation(f)