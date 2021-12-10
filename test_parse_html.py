from bs4 import BeautifulSoup

with open("notes_complet.html") as file :
    soup = BeautifulSoup(file, 'lxml')

liste1 = []
liste2 = []
tag = soup.tbody

for balise in tag.contents :
    if(balise.name == "tr") :
        ligne = balise.contents
        matiere = ligne[2]
        note = ligne[3]
        if(len(matiere.contents) == 1) :
            if(len(note.contents) == 1) :
                liste1.append(matiere.string)

for mat in liste1 :
    liste2.append(mat.strip())

print(liste2)
