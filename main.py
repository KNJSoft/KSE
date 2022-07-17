#importation
from subprocess import call
from tkinter import *
from tkinter import messagebox
from tkinter import ttk,Tk
#fonction de connection
def connexion():
    usersname=userenter.get()
    usermdp=mdpenter.get()
    if(usersname=="" and usermdp==""):
        messagebox.showerror("","entrer les données")
        mdpenter.delete("0","end")
        userenter.delete("0","end")

    elif(usersname=="admin"and usermdp=="admin"):
        messagebox.showinfo("","Bienvenue")
        mdpenter.delete("0", "end")
        userenter.delete("0", "end")
        root.destroy()
        call(["python","page2.py"])
    else:
        messagebox.showwarning("","Erreur de connexion")
        mdpenter.delete("0", "end")
        userenter.delete("0", "end")
#ma fenêtre
root=Tk()
root.title("FENÊTRE DE CONNECTION")
root.geometry("400x300+450+200")
root.resizable(False,False)
root.configure(background="#091821")

#ajout du titre
titre=Label(root,borderwidth=3,relief=SUNKEN
            ,text="Formulaire de connexion",font=("sans serif",23),background="#091821",fg="white")
titre.place(x=0,y=0,width=400)
#user
username=Label(root,text="Nom d'utilisateur:",font=("Arial",14),bg="#091821",fg="white")
username.place(x=5,y=100,width=150)
userenter=Entry(root,bd=4,font=("Arial",13))
userenter.place(x=150,y=100,width=200,height=30)
#mot de passe
mdp=Label(root,text="Mot de passe:",font=("Arial",14),bg="#091821",fg="white")
mdp.place(x=5,y=150,width=150)
mdpenter=Entry(root,show="*",bd=4,font=("Arial",13))
mdpenter.place(x=150,y=150,width=200,height=30)

#bouton connecter
btn=Button(root,text="Connexion",font=("Arial",16),bg="#FF4500",fg="white",command=connexion)
btn.place(x=150,y=200,width=200)
#execution
root.mainloop()