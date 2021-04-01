from tkinter import *
from tkinter import messagebox
from string import ascii_uppercase
import random
import wordlist



window=Tk()
window.title("HANGMAN")
imgLabel=Label(window)
Label(window,text="HANGMAN(COVID-19 VERSION)",font=("Helvetica 18 bold"),fg='blue').grid(row=0,column=0,columnspan=13)
Label(window,text="Enter your choice",font=("Helvetica 15 bold"),fg='blue').grid(row=1,column=0,columnspan=13)
Button(window,text="Ramayan",command=lambda:ramayan(),font=("Helvetica 10",),fg='yellow',activeforeground='red',bg='black').grid(row=2,column=0,columnspan=8)
Button(window,text="Mahabharat",command=lambda:mahabharat(),font=("Helvetica 10",),fg='yellow',activeforeground='red',bg='black').grid(row=2,column=1,columnspan=15)



photos= [PhotoImage(file="C:\\Users\\SHWETA\\Desktop\\New folder\\images\\hang0.png"),PhotoImage(file="C:\\Users\\SHWETA\\Desktop\\New folder\\images\\hang1.png"),PhotoImage(file="C:\\Users\\SHWETA\\Desktop\\New folder\\images\\hang2.png"),PhotoImage(file="C:\\Users\\SHWETA\\Desktop\\New folder\\images\\hang3.png"),
         PhotoImage(file="C:\\Users\\SHWETA\\Desktop\\New folder\\images\\hang4.png"),PhotoImage(file="C:\\Users\\SHWETA\\Desktop\\New folder\\images\\hang5.png"),PhotoImage(file="C:\\Users\\SHWETA\\Desktop\\New folder\\images\\hang6.png"),PhotoImage(file="C:\\Users\\SHWETA\\Desktop\\New folder\\images\\hang7.png"),
         PhotoImage(file="C:\\Users\\SHWETA\\Desktop\\New folder\\images\\hang8.png"),PhotoImage(file="C:\\Users\\SHWETA\\Desktop\\New folder\\images\\hang9.png"),PhotoImage(file="C:\\Users\\SHWETA\\Desktop\\New folder\\images\\hang10.png"),PhotoImage(file="C:\\Users\\SHWETA\\Desktop\\New folder\\images\\hang11.png")]

def ramayan():
    words=[]
    hints=[]
    words=wordlist.ramayanWords()
    hints=wordlist.ramayanHints()
    
    
    the_word=random.choice(words)
    i=words.index(the_word)
    Label(window,text=hints[i],font=("Helvetica 12 bold")).grid(row=4,column=0,columnspan=13)
        
    startGame(the_word)

def mahabharat():
    words=[]
    hints=[]
    words=wordlist.mahabharatWords()
    hints=wordlist.mahabharatHints()
   
    
    the_word=random.choice(words)
    i=words.index(the_word)
    Label(window,text=hints[i],font=("Helvetica 12 bold")).grid(row=4,column=0,columnspan=13)
    
    startGame(the_word)
    


def startGame(list1):
    the_word=[]
    the_word=list1
    global the_word_withSpaces
    global numberofGuesses
    numberofGuesses=0
    imgLabel.config(image=photos[0])
    the_word_withSpaces=" ".join(the_word)
    lblWord.set(" ".join("_"*len(the_word)))

def newGame():
    Label(window,text="  ",font=("Helvetica 10 bold")).grid(row=4,column=0,columnspan=13)
    lblWord.set(" ".join(" "))

def guess(letter):
    global numberofGuesses
    if numberofGuesses<11:
        txt=list(the_word_withSpaces)
        guessed=list(lblWord.get())
        if the_word_withSpaces.count(letter)>0:
            for c in range(len(txt)):
                if txt[c]==letter:
                    guessed[c]=letter
                lblWord.set("".join(guessed))
                if lblWord.get()== the_word_withSpaces:
                    messagebox.showinfo("HANGMAN","You guessed it!")
                    window.mainloop()
                   
        else:
            numberofGuesses+=1
            imgLabel.config(image=photos[numberofGuesses])
            if numberofGuesses==11:
                    messagebox.showwarning("HANGMAN","GAME OVER!")
           
imgLabel=Label(window)
imgLabel.grid(row=3,column=0,columnspan=1,padx=10,pady=40)
imgLabel.config(image=photos[0])

lblWord=StringVar()
Label(window,textvariable=lblWord, font=('Consolas 24 bold')).grid(row=3,column=2,columnspan=7,padx=10)



n=89
for c in ascii_uppercase:
    Button(window,text=c, command=lambda c=c:guess(c), font=("Helvetica 18"),width=4,fg='purple',activeforeground='red').grid(row=(n+1)//9,column=(n+1)%9,sticky='E')
    n+=1



Button(window,text="New\nGame", command=lambda:newGame(), font=("Helvetica 10 bold"),activeforeground='black',fg='red').grid(row=1,column=7)
newGame()
window.mainloop()
