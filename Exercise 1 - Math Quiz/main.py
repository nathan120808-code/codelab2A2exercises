#library imports
import random
import tkinter as tk
from tkinter import messagebox

#essentials
main = tk.Tk()
main.title("Math Game")
main.geometry('800x500')
main.resizable(0,0)
main.configure(
    bg='black'
)

# global variables for customization
title_font = ('Helvetica', 40, 'bold')
button_font = ('Monospace', 15)

#GLOBAL VARIABLES
#settings for the game
TOTAL_QUES = 10 #10 times 10 equaes to 100 - the maximum score in quiz
FIRST_TRY = 10 #will be multiplied against total/ 10 points for first try
SECOND_TRY = 5 #will be multiplied against total/ 5 points on second

#this sets the range of the questions - easy means single digit numbers to be solved, moderate means double - so on so forth
RANGES = {
    'easy':(1,9),
    'moderate':(10,99),
    'advanced':(1000,9999)
}

#FUNCTIONS

def randomint(difficulty):
    """returns rnadom number, min max depends on the difficult"""
    low, high = RANGES[difficulty]
    return random.randint(low,high)

def decideOp():
    """randomly chooses if teh operation is addition or subtraction"""
    return random.choice(['+','-'])

def display_menu():
    """displays main ui"""

    #clears everything on the main win when player chooses to play again
    for widget in main.winfo_children():
        widget.destroy()

    #title
    title1 = tk.Label(main, text="Test your Math!",
                font = title_font
                ).pack(pady= 30)

    #difficulty levels - naming variables and assigning attributes and positioning
    dif1 = tk.Button(main, text="Easy",
                bg = 'green',
                font= button_font,
                width= 20,
                height= 2,
                command=lambda: open_questions("easy")).pack(pady= 10)
    dif2 = tk.Button(main, text="Intermediate",
                bg = 'yellow',
                font= button_font,
                width= 20,
                height= 2,
                command=lambda: open_questions('intermediate')).pack(pady= 10)
    dif3 = tk.Button(main, text='Advanced',
                bg='red',
                font= button_font,
                width= 20,
                height= 2,
                command=lambda: open_questions('advanced')).pack(pady= 10)

def display_problem(q-label, answer_entry, attempt_label, state, difficulty):
    "creates random problems, is displayed and clears answer box. and returns the correct answer to the problem"

    a = randomint(difficulty)
    b = randomint(difficulty)
    operation = decideOp()

    if operation == '+':
        correct_answer = a + b
    else:
        correct_answer = a - b

def open_questions(difficulty):
    """opens seperate window for the difficulty player chooses"""
    #window configs
    win = tk.Toplevel(main) #toplevel is a widget which creates a seperate pop up window
    win.title(f"{difficulty.capitalize()} Questions") #sets window title
    win.geometry(('600x300')) #window dimensions
    win.configure()
    win.transient(main) #prioritises this window over the main menu screen
    win.grab_set() #blocks any interaction with the main window until the questions are either completed or closed

    questions = QUESTIONS[difficulty] 
    state = {"index": 0, "score": 0} #tracks player's progress in teh quiz - index holds the position of teh current question the player is in, score is how many answers the player got right


    q_label = tk.Label(win, text="", font=("Arial", 14), wraplength=300) #this label is in place to display the questions
    q_label.pack(pady=15)

    #input widgets
    answer_entry = tk.Entry(win) 
    answer_entry.pack()

    def show_question():
        """this function enables the questions from the global dictionary to be directly called"""
        q_label.config(text=questions[state["index"]]["Q"]) #this configures the label from the parent function to display the current question
        answer_entry.delete(0, tk.END) #this deletes the text inside the entry box automotically after every question answered, its for the player's convenience

    def submit():
        """this function runs everytime the submit button is interacted with"""
        correct = questions[state["index"]]["A"].lower() #assigns the dataframe onto a variable for this function - .lower() is just to keep it in lowercase
        if answer_entry.get().strip().lower() == correct: #this statement checks if the inputted answer is correct
            state['score'] +=1 #adds point if the condition is achieved
            messagebox.showinfo("Result", "Correct")

        else:
            messagebox.showinfo("Result", f"Wrong, the answer was: {correct}")

        #these conditions check when to end 
        state['index'] +=1 #this adds an extra 1 in the index so it doesnt start at 0
        print("index:", state['index'], "total:", len(questions))
        if state['index'] < len(questions): #this checks if there are more questions (IF index pos is less than the amount of questions, then show_question() is activated)
            show_question()
        else:
            messagebox.showinfo(
                "Done!", f"Score: {state['score']}/{len(questions)}" )
            win.destroy()

    tk.Button(win, text='Submit', command=submit).pack(pady="10")
    show_question()








main.mainloop()