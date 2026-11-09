#library imports
from tkinter import *
from tkinter import messagebox

#essentials
main = Tk()
main.title("Math Quiz")
main.geometry('800x500')
main.configure(
    bg='black'
)

# global variables for customization
title_font = ('Helvetica', 40, 'bold')
button_font = ('Monospace', 15)

# questions
# NOTE: all the questions were generated using Gemini
#DICTIONARY for the questions - acting as a global dictionary
QUESTIONS = {
    "easy": [
        {"Q":  "What is 2 + 4", "A": "6" },
        {"Q": "How many sides does a hexagon have?"},
        {"Q": "What is 7 × 8?"}
        
    ],
    "intermediate": [
        {}
    ],
    "advanced": [
        {}
    ]
}


def open_questions(difficulty):
    """opens seperate window for the difficulty player chooses"""
    #window configs
    win = Tk.Toplevel(main) #toplevel is a widget which creates a seperate pop up window
    win.title(f"{difficulty.capitalize()} Questions") #sets window title
    win.geometry(('600x300')) #window dimensions

    questions = QUESTIONS[difficulty] 
    state = {"index": 0, "score": 0} #tracks player's progress in teh quiz - index holds the position of teh current question the player is in, score is how many answers the player got right


    q_label = Tk.Label(win, text="", font=("Arial", 14), wraplength=300) #this label is in place to display the questions
    q_label.pack(pady=15)

    #input widgets
    answer_entry = Tk.Entry(win) 
    answer_entry.pack()

    def show_question():
        """this function enables the questions from the global dictionary to be directly called"""
        q_label.config(text=questions[state["index"]]["Q"])
        answer_entry.delete(0, Tk.END)

    def submit():
        """this function runs everytime the submit button is interacted with"""
        correct = questions[state["index"]["a"]].lower() #assigns the dataframe onto a variable for this function - .lower() is just to keep it in lowercase
        if answer_entry.get().strip().lower() == correct: #this statement checks if the inputted answer is correct
            state['score'] +=1 #adds point if the condition is achieved

        #these conditions check when to end 
        state['index'] +=1 #this adds an extra 1 in the index so it doesnt start at 0
        if state['index'] < len(questions): #once the index passes 10 which should be more than the length of the dataframe, it calls the show_question function
            show_question
        else:
            messagebox.showinfo(
                "Done!", f"Score: {state['score']}/{len(questions)}" 

            )
            win.destroy




#title
title1 = Label(main, text="Test your Math!",
               font = title_font
               ).pack(pady= 30)

#difficulty levels - naming variables and assigning attributes and positioning
dif1 = Button(main, text="Easy",
              bg = 'green',
              font= button_font,
              width= 20,
              height= 2,
              command=lambda: s).pack(pady= 10)
dif2 = Button(main, text="Intermediate",
            bg = 'yellow',
            font= button_font,
            width= 20,
            height= 2).pack(pady= 10)
dif3 = Button(main, text='Advanced',
              bg='red',
              font= button_font,
              width= 20,
              height= 2).pack(pady= 10)


main.mainloop()