
from tkinter import *
from tkinter import filedialog,ttk
from words_in_proteome import *
from tkinter import messagebox


root = Tk()
root.title("Words In Proteome")
root.geometry("350x500")
root.pack_propagate(False)

myLabel = Label(root,text="Words In Proteome")
myLabel.pack()

def clickText():
    global txt
    txt = filedialog.askopenfilename(filetypes=(("text Files", "*.txt"),))
    print (txt," ||||| ")
    txt = read_words(txt)
    print("la nombre des mots selectioné est = ", len(txt))
    sec1 = Label(root, text=" succes",fg="green")
    sec1.pack()
    myButton2.pack()

def clickSeq():
    global seq
    seq = filedialog.askopenfilename(filetypes=(("seq Files", "*.fasta"),))
    print (seq," ||||| ")
    seq = read_sequences(seq)
    print("la nombre des mots selectioné est = ", len(seq))
    print("----------------------------------------------")
    sec2 = Label(root, text=" succes",fg="green")
    sec2.pack()
    myButton3.pack()

def start():
    global mot_trouve
    mot_trouve = search_words_in_proteome(txt,seq)
    t.pack()
    for word in mot_trouve:
        t.insert(parent='', index='end', values=(word, mot_trouve[word]))

    
    myButton4 = Button(root, text="close", command=root.destroy,bg="red")
    myButton4.pack()


t = ttk.Treeview(root)
t['columns'] = ("mot","nombre")
t.column("#0",width=0)
t.column("mot",width=80)
t.column("nombre",width=200)
t.heading("#0")
t.heading("mot",text="Mot")
t.heading("nombre",text="nombre d'apperation")



myButton1 = Button(root,text="select txt file",command=clickText)
myButton1.pack()
myButton2 = Button(root,text="select fasta file",command=clickSeq)
myButton3 = Button(root,text="Start",command=start ,fg="white", bg="black")
root.mainloop()