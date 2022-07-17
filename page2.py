#importation
import tkinter
from cProfile import label
from subprocess import call
from tkinter import *
from tkinter import messagebox
from tkinter import ttk,Tk
import mysql.connector


def ajout():
    #recuperation des valeurs
    Matricule=matriculeenter.get()
    Nom=nomenter.get()
    Prenom=prenomenter.get()
    Sexe=sexe.get()
    Classe=classedispo.get()
    Matiere=matiereenter.get()
    Note=noteenter.get()
    #connection a la base de données
    bd = mysql.connector.connect(host='127.0.0.1', user='root', password='', database='note_eleve')
    connexion = bd.cursor()
    #insertion des valeurs si possible
    try:
        sql="insert into note(mat,nom,prenom,sexe,classe,matiere,note) values (%s,%s,%s,%s,%s,%s,%s) "
        val=(Matricule,Nom,Prenom,Sexe,Classe,Matiere,Note)
        connexion.execute(sql,val)
        bd.commit()
        dernierematricule=connexion.lastrowid
        messagebox.showinfo("information","Note ajouter")
        root.destroy
        call(['python','page2.py'])
    except Exception as e:
        print(e)
        #retour
        bd.rollback()
        bd.close()
def modifier():
    # recuperation des valeurs
    Matricule = matriculeenter.get()
    Nom = nomenter.get()
    Prenom = prenomenter.get()
    Sexe = sexe.get()
    Classe = classedispo.get()
    Matiere = matiereenter.get()
    Note = noteenter.get()
    # connection a la base de données
    bd = mysql.connector.connect(host='localhost', user='root', password='', database='note_eleve')
    connexion = bd.cursor()
    # mise a jour des valeurs si possible
    try:
        sql="update note set nom=%s,prenom=%s,sexe=%s,classe=%s,matiere=%s,note=%s"
        val=(Matricule,Nom,Prenom,Sexe,Classe,Matiere,Note)
        connexion.execute(sql,val)
        bd.commit()
        dernierematricule=connexion.lastrowid
        messagebox.showinfo("information","Note modifier")
        root.destroy
        call(['python','page2.py'])
    except Exception as e:
        print(e)
        #retour
        bd.rollback()
        bd.close()

def supprimer():
    Matricule=matriculeenter.get()
    # connection a la base de données
    bd = mysql.connector.connect(host='127.0.0.1', user='root', password='', database='note_eleve')
    connexion = bd.cursor()
    try:
        sql="delete from note where code=%s"
        val=(Matricule)
        connexion.execute(sql,val)
        bd.commit()
        dernierematricule=connexion.lastrowid
        messagebox.showinfo("information","Note supprimer")
        root.destroy
        call(['python','page2.py'])
    except Exception as e:
        print(e)
        #retour
        bd.rollback()
        bd.close()

root=Tk()
root.title("MENU PRINCIPAL")
root.geometry("1350x700+0+0")
root.resizable(False,False)
root.configure(background="#091821")
#ajout du titre
titre=Label(root,borderwidth=3,relief=SUNKEN
            ,text="GESTION NOTES DES ETUDIANTS",font=("sans serif",25),background="#2F4F4F",fg="#FFFAFA")
titre.place(x=0,y=0,width=1350,height=100)
#details des eleves

#matricule
matricule=Label(root,text="MATRICULE",font=("Arial",18),bg="#091821",fg="white")
matricule.place(x=70,y=150,width=150)
matriculeenter=Entry(root,bd=4,font=("Arial",14))
matriculeenter.place(x=250,y=150,width=150)

#Nom
nom=Label(root,text="NOM",font=("Arial",18),bg="#091821",fg="white")
nom.place(x=70,y=200,width=150)
nomenter=Entry(root,bd=4,font=("Arial",14))
nomenter.place(x=250,y=200,width=300)

#Prenom
prenom=Label(root,text="PRENOM",font=("Arial",18),bg="#091821",fg="white")
prenom.place(x=70,y=250,width=150)
prenomenter=Entry(root,bd=4,font=("Arial",14))
prenomenter.place(x=250,y=250,width=300)

#sexe
sexe=StringVar()
sexemas=Radiobutton(root,text="MASCULIN",value="M",variable=sexe,indicatoron=0,font=("Arial",18),bg="#091821",fg="#696969")
sexemas.place(x=250,y=300,width=130)
sexefem=Radiobutton(root,text="FEMININ",value="F",variable=sexe,indicatoron=0,font=("Arial",18),bg="#091821",fg="#696969")
sexefem.place(x=420,y=300,width=130)

#CLASSE
classe=Label(root,text="CLASSE",font=("Arial",18),bg="#091821",fg="white")
classe.place(x=70,y=350,width=150)
classedispo=ttk.Combobox(root,font=("Arial",14))
classedispo['values']=['CP','CE1','CE2','CM1','CM2','6e','5e','4e','3e','2nd','p','Tle']
classedispo.place(x=250,y=350,width=130)

#matiere
matiere=Label(root,text="MATIERE",font=("Arial",18),bg="#091821",fg="white")
matiere.place(x=70,y=400,width=150)
matiereenter=Entry(root,bd=4,font=("Arial",14))
matiereenter.place(x=250,y=400,width=300)

#Note
note=Label(root,text="NOTE",font=("Arial",18),bg="#091821",fg="white")
note.place(x=70,y=450,width=150)
noteenter=Entry(root,bd=4,font=("Arial",14))
noteenter.place(x=250,y=450,width=200)

#Enregistrer
enregist=Button(root,text="Enregistrer",font=("Arial",16),bg="#D2691E",fg="white",command=ajout)
enregist.place(x=250,y=500,width=200)

#Modifier
modifier=Button(root,text="Modifier",font=("Arial",16),bg="#D2691E",fg="white",command=modifier)
modifier.place(x=250,y=550,width=200)

#Supprimer
supprimer=Button(root,text="Supprimer",font=("Arial",16),bg="#D2691E",fg="white",command=supprimer)
supprimer.place(x=250,y=600,width=200)

#table
table=ttk.Treeview(root,columns=(1,2,3,4,5,6,7),height=5,show="headings")
table.place(x=560,y=150,width=790,height=450)
#entete
table.heading(1,text="MAT")
table.heading(2,text="NOM")
table.heading(3,text="PRENOM")
table.heading(4,text="SEXE")
table.heading(5,text="CLASSE")
table.heading(6,text="MATIERE")
table.heading(7,text="NOTE")
#dimensions des colonnes
table.column(1,width=50)
table.column(2,width=150)
table.column(3,width=150)
table.column(4,width=100)
table.column(5,width=50)
table.column(6,width=100)
table.column(7,width=50)

#intraction dans les tables
bd=mysql.connector.connect(host='127.0.0.1',user='root',password='',database='note_eleve')
connexion=bd.cursor()
connexion.execute("select * from note")
for row in connexion:
    table.insert('',END,values=row)
bd.close()
#execution
root.mainloop()