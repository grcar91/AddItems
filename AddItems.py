import sqlite3
import tkinter as tk
import tkinter.messagebox
from tkinter import *


windo = tk.Tk()
windo.geometry("550x350")
windo.title("Popis materijala")

tabela = sqlite3.connect("Popis_izdelkov.db")
conc = tabela.cursor()
conc.execute(''' CREATE TABLE IF NOT EXISTS Popis_izdelkov(id INTEGER PRIMARY KEY AUTOINCREMENT, 
             Koda izdelka INTEGER,
             Ime izdelka TEXT,
             Proizvajalec TEXT,
             Letnik INEGER)''')

tabela.commit()



napis1 = tk.Label(windo, text="Pazi pri vnosu podatkov!",font="arial,10" ,justify= "center")
napis1.grid(row=0,column=3, sticky=tk.E)

napis_koda = tk.Label(windo, font=7,text="Koda izdelka:")
napis_koda.grid(row=1,column=0)

vnos_koda = tk.Entry(windo, width=30, justify="center")
vnos_koda.grid(row=2, column=0)

napis_zaloga = tk.Label(windo, font=7,text="Zaloga izdelka:")
napis_zaloga.grid(row=2,column=3)

vnos_zaloga = tk.Entry(windo, width=30, justify="center")
vnos_zaloga.grid(row=3, column=3)

napis_ime =tk.Label(windo,font=7 , text="Ime izdelka:")
napis_ime.grid(row=1, column=5)

vnos_ime = tk.Entry(windo, width=30, justify="center")
vnos_ime.grid(row=2, column=5)

napis_proizvajalec = tk.Label(windo,font=7 ,text="Prozvajalec:")
napis_proizvajalec.grid(row=3,column=0)

vnos_proizvajalec = tk.Entry(windo, width=30, justify= "center")
vnos_proizvajalec.grid(row=4, column=0)

napis_letnik = tk.Label(windo,font=7 , text="Letnik izdelave:")
napis_letnik.grid(row=3, column=5)

vnos_letnik = tk.Entry(windo, width=30, justify="center")
vnos_letnik.grid(row=4, column=5)

def shranjevanje():
    koda = vnos_koda.get()
    ime = vnos_ime.get()
    proizvajalec = vnos_proizvajalec.get()
    letnik = vnos_letnik.get()
    zaloga = vnos_zaloga.get()

    sql = "INSERT INTO Popis_izdelkov(Koda, Ime, Proizvajalec, Letnik,Zaloga) VALUES(?,?,?,?,?)"
    podatki = (koda,ime, proizvajalec, letnik,zaloga)
    conc= tabela.cursor()
    conc.execute(sql,podatki)
    tabela.commit()
    conc.close()

    oknoshrani = tk.Toplevel(windo)
    oknoshrani.geometry("200x100")
    oknoshrani.title(NONE)

    napisshrani = tk.Label(oknoshrani,text="SHRANJENO",font=3)
    napisshrani.pack()

    tipka = tk.Button(oknoshrani,width=10, text="OK", command=oknoshrani.destroy)
    tipka.pack()

def brisanje():
    vnos_koda.delete(0,tk.END)
    vnos_ime.delete(0,tk.END)
    vnos_proizvajalec.delete(0,tk.END)
    vnos_letnik.delete(0,tk.END)
    vnos_zaloga.delete(0,tk.END)

def shrani_brisi():
    shranjevanje()
    brisanje()  

def prikazi():
    
    conc=tabela.cursor()
    conc.execute("SELECT * FROM Popis_izdelkov") 
    podatki=conc.fetchall()
    print(podatki)    
    
    novo = tk.Toplevel(windo)
    novo.geometry("400x400")
    novo.title("List ") 
    prikazano = tk.Listbox(novo,width=40,border=3)
    prikazano.grid(row=2,column=2)
    
    for podatek in podatki:
        prikazano.insert(0,podatek)
    tabela.commit()    
    conc.close ()

    def delete():
        try:
          deletindex = prikazano.curselection()[0]
          delet = prikazano.get(deletindex)
          prikazano.delete(deletindex)
          con = tabela.cursor()
          con.execute("DELETE FROM Popis_izdelkov WHERE id=?",(delet,))
          tabela.commit()
          con.close()
        except :
            pass

    def save():
        pass

     
    
    delet = tk.Button(novo,width=20,text="Delete",justify="center",command= delete)
    delet.grid(row=1,column=3) 

def jump_next(x,next_field):
    next_field.focus()

vnos_koda.bind("<Return>",lambda x:jump_next(x,vnos_ime))
vnos_ime.bind("<Return>",lambda x:jump_next(x,vnos_proizvajalec))
vnos_proizvajalec.bind("<Return>",lambda x:jump_next(x,vnos_letnik))
vnos_letnik.bind("<Return>",lambda x:jump_next(x,vnos_zaloga))






shrani = tk.Button(windo,width=20, text="Shrani",fg="red",bg="lightgreen", justify="center", command=shrani_brisi)
shrani.grid(row=5, column=3)

prikaz = tk.Button(windo,width=20, text="Prikazi izdelke",fg="red" ,bg="lightgreen", justify="center", command=prikazi)
prikaz.grid(row=7, column=3)

prikaz1 = tk.Button(windo,width=20, text="Brisi",fg="white" ,bg="red", justify="center", command=brisanje)
prikaz1.grid(row=8, column=3)




windo.mainloop()