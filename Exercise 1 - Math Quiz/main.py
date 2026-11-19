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

def decideOperation():
    """randomly chooses if teh operation is addition or subtraction"""
    return random.choice(['+','-'])

def displayMenu():
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
                command=lambda: open_questions('moderate')).pack(pady= 10)
    dif3 = tk.Button(main, text='Advanced',
                bg='red',
                font= button_font,
                width= 20,
                height= 2,
                command=lambda: open_questions('advanced')).pack(pady= 10)


def displayProblem(q_label, answer_entry, attempt_label, state, difficulty):
    """creates random problems, is displayed and clears answer box. and returns the correct answer to the problem"""

    #a and b are assigned random numbers based on teh global dictionary's numebr range per difficulty
    a = randomint(difficulty) 
    b = randomint(difficulty)
    operation = decideOperation()

    if operation == '+': #simple conditional to determine addition or subtraction
        correct_answer = a + b
    else:
        correct_answer = a - b

    #sets the text in q_label to display the problem in this format
    q_label.config(text=f"Question {state['index'] + 1} of {TOTAL_QUES}\n\n{a} {operation} {b} =")

    attempt_label.config(text='First attempt = 10 points')
    answer_entry.delete(0,tk.END) #clears entry box for player convenience

    return correct_answer


def isCorrect(user_answer, correct_answer, attempt, parent):
    """checks player answer, then shows a message indicating if they were right or wrong"""
    #this conditional checks if the user's answer is correct, checks if it was submitted first or second try,
    #then prompts the appropriate amount of points
    if user_answer == correct_answer:
        points = FIRST_TRY if attempt == 1 else SECOND_TRY
        messagebox.showinfo("Result", f"Correct! + {points} points", parent=parent)
        return True #exits function immediately if answer is correct

    #only reached if answer is wrong
    #conditional checks if attempt is equal to 1, otherwise if the user misses their second chance, it prompts the appropriate message
    if attempt == 1:
        messagebox.showinfo("Result", "Wrong, one more try!", parent = parent)
    else:
        messagebox.showinfo("Result", f"Wrong! The answer was: {correct_answer}", parent=parent)

    return False



def get_rank(score):
    """converts the points into a letter rating"""
    #basic conditional statements covering the entry point of each rank
    if score >= 70:
        return "A"
    elif score >= 60:
        return "B"
    elif score >= 50:
        return "C"
    elif score >= 40:
        return "D"
    else:
        return "F"

def displayResults(score, win):
    """displays user total score and rank, it also prompts the user if they want to play again"""
    #gathers the highest possible score
    peak_score = TOTAL_QUES * FIRST_TRY
    #displays user's score out of highest, their letter rank (which is gathered from get_rank function)
    messagebox.showinfo("Finished", f"Final score: {score}/{peak_score}\nRank: {get_rank(score)}", parent = win)

    win.destroy()

    #conditional that prompts if the user wants to play again
    if messagebox.askyesno("Play again?", "play the quiz again?"):
        displayMenu()
    else:
        win.destroy()

#quiz window (seperate)

def open_questions(difficulty):
    """opens seperate window for the difficulty player chooses"""
    #window configs
    win = tk.Toplevel(main) #toplevel is a widget which creates a seperate pop up window
    win.title(f"{difficulty.capitalize()} Questions") #sets window title
    win.geometry(('600x300')) #window dimensions
    win.configure()
    win.transient(main) #prioritises this window over the main menu screen
    win.grab_set() #blocks any interaction with the main window until the questions are either completed or closed

    state = {"index": 0, "score": 0, "attempt": 1, "answer": None} #tracks player's progress in teh quiz - index holds the position of teh current question the player is in, score is how many answers the player got right


    q_label = tk.Label(win, text="", font=("Robotica", 14), wraplength=300) #this label is in place to display the questions
    q_label.pack(pady=15)

    #attempts
    a_label = tk.Label(win, text="", font=("Robotica", 14))
    a_label.pack(pady=3)

    #input widgets
    answer_entry = tk.Entry(win) 
    answer_entry.pack(pady=5)

    def submit():
        try:
            user_answer = int(answer_entry.get().strip())
        except ValueError:
            messagebox.showwarning("Invalid input", "Enter a whole number", parent=win)

        #conditional determining the answer's state(whether 1st or 2nd try) and assigns appropriate points
        if isCorrect(user_answer, state["answer"], state["attempt"], win):
            #10 points on first attempt, 5 points on second onto the state of 'score'
            state['score'] += FIRST_TRY if state['attempt'] == 1 else SECOND_TRY 
            next_question()
        elif state['attempt'] == 1:
            #wrong on first try - changes state of attempts from 1 to 2 and displays appropriate message
            state["attempt"] = 2
            a_label.config(text="2nd Attempt - 5 pts")
            answer_entry.delete(0,tk.END)
        #moves on to next question if second try is wrong
        else:
            next_question()

    def next_question():
        """moves to next problem, or ends quiz if the final question is reached"""
        state['index'] += 1 #adds 1 so index doesnt start at 0
        state["attempt"] = 1 #constantly sets every question attempt state to 1
        #if teh question number is below 10(max), displayProblem is called which continues to generate a new problem
        if state['index'] < TOTAL_QUES:
            state['answer'] = displayProblem(q_label, answer_entry, a_label, state, difficulty)
        #if index is more than max question, displayResults is called, displaying score state and seperate window
        else:
            displayResults(state['score'], win)

    tk.Button(win, text='Submit', command=submit).pack(pady="10")

    #first problem
    state['answer'] = displayProblem(q_label, answer_entry, a_label, state, difficulty)



#startup
displayMenu()
main.mainloop()