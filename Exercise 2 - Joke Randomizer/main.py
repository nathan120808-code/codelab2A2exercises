import tkinter as tk
import os
import random

main = tk.Tk()
main.title("Joke Generator")
main.geometry("800x500")
main.resizable(0,0)
main.config(
    bg="#1A2A3A"
)

#GLOBAL dataset (this was figured using gemini)
JOKE_DATA = os.path.join(os.path.dirname(os.path.abspath(__file__)), "randomJokes.txt")


def joke_gen(path):
    "Reads teh txt file - follows this setup for each line: Setup? punchline"

    jokes = [] #starts with an empty list
    with open(path, encoding="utf-8") as f: #opens the joke file and sets its encoding
        for line in f: #goes through it one line at a time - strip() then removes the trailing newline, if statement skips blank lines or ones without "?"
            line = line.strip()
            if not line or "?" not in line:
                continue
            #these were figured using gemini(the 2 lines below this point)
            cut = line.index("?") + 1 #this moves the cutting point passed the "?" point in each line
            jokes.append((line[:cut].strip(),line[cut:].strip())) #this directs where should the lines be cut, and it sets them into a pair eg: jokes.append(setup, punchline)
    return jokes

try:
    JOKES = joke_gen(JOKE_DATA) #this allows the main file to be called, only locally - its then assigned into a global variable as JOKES
except OSError: #otherwise if it isnt found locally, it will raise an oserror - turning JOKES into an empty list
    JOKES = []

current_joke = None #will be used in future function

def joke_new():
    "Picks the joke at random consistently, this is for teh generator button"
    global current_joke

    #this line is developed with claude
    choices = [j for j in JOKES if j != current_joke] or JOKES #this goes through every joke - ensuring the ones that arent teh active joke stay on display. It prevents repetition of the same joke
                                                               #JOKES is instead a fallback if the list is empty - which only happens if the list is one joke
    current_joke = random.choice(choices) #picks random pair from the collected list

    question_label1.config(text=current_joke[0])
    question_label2.config(text="")
    gen_button1.config(state='normal')
    gen_button2.config(state='normal')

def show_punchline():
    """show punchlien below question_label1"""
    if current_joke:
        question_label2.config(text=current_joke[1])
        gen_button1.config(state='disabled') #disabled button if punchline is shown

def quit_app():
    main.destroy()

#FRONTEND

#title
title1 = tk.Label(main, text="Joke Generator",font=('Robotica', 25), fg= "#ffffff", bg= "#1A2A3A")
title1.pack(pady=25)

#joke button
alexa_b = tk.Button(main, text="Alexa tell me a joke", font=('Robotica', 16), command=joke_new)
alexa_b.pack(pady=10)


#JOKE DISPLAY
#joke setup
question_label1 = tk.Label(main, text="",font=('Robotica', 18), fg= "#ffffff", bg= "#1A2A3A", wraplength=700,justify="center")
question_label1.pack(pady=(20,10))

#joke punchline
question_label2 = tk.Label(main, text="",font=('Robotica', 18,'italic'), fg= "#ffffff", bg= "#1A2A3A", wraplength=700, justify='center')
question_label2.pack(pady=10)

#ROW AND BUTTONS
button_row = tk.Frame(main, bg='#1A2A3A')
button_row.pack(pady=25)

#punchline
gen_button1= tk.Button(button_row, text="Show Punchline", font=('Robotica', 15), width = 14, state="disabled", command=show_punchline)
gen_button1.grid(row=0,column=0,padx=8)
#next button
gen_button2 = tk.Button(button_row, text="Next Joke", font=('Robotica', 15), width = 14, state="disabled", command=joke_new)
gen_button2.grid(row=0,column=1,padx=8)
#quit button
gen_button3 = tk.Button(button_row, text="Quit", font=('Robotica', 15), width = 14, command=quit_app)
gen_button3.grid(row=0,column=2,padx=8)

if not JOKES: #IF the jokes txt file is not available locally - this statement will activate, disabling teh joke button and displaying the unavail text
    alexa_b.config(state="disabled")
    question_label1.config(text="Couldn't find any jokes. Make sure randomJokes.txt is in the local folder")

main.mainloop()