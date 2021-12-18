from bs4 import BeautifulSoup
import subprocess

def GetNewNotes() :
    with open("old_notes.html") as file :
        soup = BeautifulSoup(file, 'lxml')

    with open("notes.html") as file2 :
        soup2 = BeautifulSoup(file2, 'lxml')

    liste1 = []
    liste2 = []
    tbody1 = soup.tbody
    tbody2 = soup2.tbody

    for balise in tbody1.contents :
        if(balise.name == "tr") :
            ligne = balise.contents
            matiere = ligne[2]
            note = ligne[3]
            if(len(matiere.contents) == 1) :
                if(len(note.contents) == 1) :
                    liste1.append(matiere.string)

    for balise in tbody2.contents :
        if(balise.name == "tr") :
            ligne = balise.contents
            matiere = ligne[2]
            note = ligne[3]
            if(len(matiere.contents) == 1) :
                if(len(note.contents) == 1) :
                    liste2.append(matiere.string)

    for i in range (0, len(liste1)) :
        liste1[i] = liste1[i].strip()

    for i in range (0,len(liste2)) :
        liste2[i] = liste2[i].strip()

    if(len(liste1) <= len(liste2)) :
        for e in liste2 :
            if(e in liste1) :
                liste2.remove(e)

    return liste2

def CheckDiff() :
    proc = subprocess.run(["diff", "notes.html", "old_notes.html"])
    return(0 if proc.returncode == 0 else 1)

#InitFiles('maaudigie', passw, '3è année DI Informatique et modélisation')
#print()