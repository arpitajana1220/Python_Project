'''
Hello Everyone!
Today we are going to play Number guessing game
Its going to be You vs Computer 
'''
#Importing required library
import random
from tkinter import *
from tkinter import ttk, Label,Entry,Button,Variable


app = Tk()

app.title("Guess the Number!")
app.configure(background="light pink")
app.geometry("800x600")
app.resizable(width=FALSE,height=False)
a=ttk.Label(app,text='Hey there, Lets Play!')

#Create a LabelFrame
labelframe= LabelFrame(app, text= "Guess the Number", font= ('Century 20 bold'),labelanchor= "n",bd=5,bg= "pink",width= 600, height= 450, cursor= "target")
labelframe.grid(column=20,row=55,pady=60,padx=90)

#Label for Player
l1= Label(labelframe, text="Player Guess", font= ('Helvetica 18 bold'))
l1.place(relx= .12, rely= .1)

#Label for Player guess
l1= Label(labelframe, text="Guess a number between 1 and 100:")
l1.place(relx= .10, rely= .3)


#Label for VS
l2= Label(labelframe, text="VS", font= ('Helvetica 18 bold'), bg="khaki3")
l2.place(relx= .45, rely= .1)

#Label for Computer
l3= Label(labelframe, text="Computer Guess", font= ('Helvetica 18 bold'))
l3.place(relx= .58, rely= .1)

#Label for Computer Guess
l3= Label(labelframe, text="Is guess too high (H), too low (L), or correct (C)??")
l3.place(relx= .54, rely= .3)

#Label for winner
l2= Label(labelframe, text="Yay!", font= ('Helvetica 18 bold'), bg="khaki3")
l2.place(relx= .45, rely= .8)


app.mainloop()


