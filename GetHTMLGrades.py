import mechanize
import re
import os
from bs4 import BeautifulSoup

def GetGradesPage(username, password, row) :
    br = mechanize.Browser()
    br.open("https://ent.uca.fr")

    br.form = list(br.forms())[0]

    br["username"] = username
    br["password"] = password

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

    with open("notes.html", "w", encoding = 'utf-8') as file :
        file.write(str(soup))

    br.close()

def GetRowFormation(username, password, formation) :
    br = mechanize.Browser()
    br.open("https://ent.uca.fr")

    br.form = list(br.forms())[0]

    br["username"] = username
    br["password"] = password

    br.submit()

    br.open("https://ent.uca.fr/scolarite/stylesheets/etu/welcome.faces")
    br.open("https://ent.uca.fr/scolarite/stylesheets/etu/notes.faces")

    link = br.find_link(text_regex=re.compile(formation))
    lien = str(link)
    lien = re.sub(r'([ -î])+row\',\'', '', lien)
    lien = re.sub(r'\']]\)([ -î])+', '', lien)
    br.close()

    return(lien)

def ManageFiles() :
    os.remove("old_notes.html")
    os.rename("notes.html", "old_notes.html")

def InitFiles(username, password, formation) :
    row = GetRowFormation(username, password, formation)
    GetGradesPage(username, password, row)
    ManageFiles()
    GetGradesPage(username, password, row)

def GetGradesTest() :
    br = mechanize.Browser()
    response = br.open("https://maxime-audigie.com/notes_vide.html")

    soup = BeautifulSoup(response, 'lxml')
    with open("notes.html", "w", encoding = 'utf-8') as file :
        file.write(str(soup))

    br.close()

def InitFilesTest() :
    GetGradesTest()
    ManageFiles()
    GetGradesTest()