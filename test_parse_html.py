from bs4 import BeautifulSoup

with open("notes_complet.html") as file :
    soup = BeautifulSoup(file, 'lxml')

tag = soup.tbody

for balise in tag.contents :
    if(balise.name == "tr") :
        ligne = balise.contents
        matiere = ligne[2]
        note = ligne[3]
        if(len(matiere.contents) == 1) :
            print(matiere.string)
            print("note ? long : ", len(note.contents))