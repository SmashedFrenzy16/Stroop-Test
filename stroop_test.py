from tkinter import *
import random


colors = ['Red', 'Blue', 'Green', 'Pink', 'Black',
           'Yellow', 'Orange', 'White', 'Purple', 'Brown']

score = 0

timeLeft = 30

def startGame(event):

    if timeLeft == 30:

        countdown()

    nextColor()

def nextColor():

    global score
    global timeLeft

    if timeLeft > 0:

        e.focus_set()

        if e.get().lower() == colors[1].lower():

            score += 1

        
        e.delete(0, END)

        random.shuffle(colors)

        label.config(fg = str(colors[1]), text = str(colors[0]))

        scoreLabel.config(text = "Score: " + str(score))


def countdown():

    global timeLeft

    if timeLeft > 0:

        timeLeft -= 1

        timeLabel.config(text = "Time left: "
                               + str(timeLeft))
                                 
        timeLabel.after(1000, countdown)

root = Tk()



root.title("Stroop Test")





root.geometry("375x200")


instructions = Label(root, text = "Type in the color "
                        "of the words, and not the word text!",
                                      font = ('Helvetica', 12))

instructions.pack()

scoreLabel = Label(root, text = "Press enter to start",
                                      font = ('Helvetica', 12))

scoreLabel.pack()

timeLabel = Label(root, text = "Time left: " +
              str(timeLeft), font = ('Helvetica', 12))

timeLabel.pack()

label = Label(root, font = ('Helvetica', 60))

label.pack()



e = Entry(root)


root.bind('<Return>', startGame)


e.focus_set()

e.pack()

root.mainloop()
