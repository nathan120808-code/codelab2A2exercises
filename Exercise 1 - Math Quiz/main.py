#library imports
from tkinter import *

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
        {"Q: What is 2 + 4"},
        {"Q: How many sides does a hexagon have?"},
        {"Q: What is 7 × 8?"}
        
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
    win = Tk.Toplevel(main)
    win.title(f"{difficulty.capitalize()} Questions")
    win.geometry(('600x300'))

    questions = QUESTIONS[difficulty]
    state = {"index": 0, "score": 0} #tracks player's progress in teh quiz - index holds the position of teh current question the player is in, score is how many answers the player got right


    q_label = Tk.Label(win, text="", font=("Arial", 14), wraplength=300)
    q_label.pack(pady=15)

    answer_entry = Tk.Entry(win)
    answer_entry.pack()

    def show_question():
        """this function enables the questions from the global dictionary to be directly called"""
        q_label.config(text=questions[state["index"]]["q"])
        answer_entry.delete(0, Tk.END)




#title
title1 = Label(main, text="Test your Math!",
               font = title_font
               )

#difficulty levels - naming variables and assigning attributes
dif1 = Button(main, text="Easy",
              bg = 'green',
              font= button_font,
              width= 20,
              height= 2,
              command=lambda: s)
dif2 = Button(main, text="Intermediate",
            bg = 'yellow',
            font= button_font,
            width= 20,
            height= 2)
dif3 = Button(main, text='Advanced',
              bg='red',
              font= button_font,
              width= 20,
              height= 2)

#positioning
title1.pack(
    pady= 30
)
dif1.pack(
    pady= 10
)
dif2.pack(
    pady= 10
)
dif3.pack(
    pady= 10
)


main.mainloop()