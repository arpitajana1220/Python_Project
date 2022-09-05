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

'''
#Defining Class for user to guess number 
def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    global iter_count
    iter_count = 0
    while guess != random_number:
        guess = int(input(f'\nGuess a number between 1 and {x}: '))
        if guess < random_number:
            print('\nOops, guess again. This number is too low.')
        elif guess > random_number:
            print('\nOops, guess again. This number is too high.')
        iter_count = iter_count + 1;
       

    print(f'\nYay, congrats. You have guessed the number {random_number} correctly!!\n')
    print(f'You guessed the number in {iter_count} trials\n') 

#Defining Class for Computer to guess a Number 
def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    global count
    count=0
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low  # could also be high b/c low = high
        feedback = input(f'\nIs {guess} too high (H), too low (L), or correct (C)?? ').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
        count = count + 1;

    print(f'\nYay! The computer guessed your number, {guess}, correctly!\n')
    print(f'Computer guessed the number in {count} trials\n') 


guess(100)
print("\nNow select a number between 1-100 in your mind and let computer do the guessing")
computer_guess(100)

#Deciding who Wins the game 
def who_win():
    if count == iter_count:
        print("Its a Draw")

    elif count < iter_count:
        print("Computer turned out smarter than you")

    else:
        print('You are Winner!') 

who_win()

'''#Create a LabelFrame
labelframe= LabelFrame(app, text= "Guess the Number", font= ('Century 20 bold'),labelanchor= "n",bd=5,bg= "pink",width= 600, height= 450, cursor= "target")
labelframe.grid(column=20,row=55,pady=60,padx=90)

#Label for Player
l1= Label(labelframe, text="Player Guess", font= ('Helvetica 18 bold'))
l1.place(relx= .12, rely= .1)

#Label for Player guess
l1= Label(labelframe, text="Guess a number between 1 and 100:")
l1.place(relx= .10, rely= .3)

'''#Entry for Number 
value = Variable()
e1 = Entry(app,textvariable=value, width = 14)
e1.grid(column=9,row= 1,pady=120,padx= 20)
e1.delete(0,'end')'''

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


