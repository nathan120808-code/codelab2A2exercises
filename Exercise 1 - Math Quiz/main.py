#library imports
from tkinter import *

#essentials
main = Tk()
main.title("Math Quiz")
main.geometry('800x500')
main.configure(
    bg='black'
)

# global variables
title_font = ('Helvetica', 40, 'bold')
button_font = ('Monospace', 15)

# questions
# NOTE: all the questions were generated using Gemini
QUESTIONS = {
    "easy": [
        {"Q: What is 2 + 4"}
        {"Q: How many sides does a hexagon have?"}
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
    win = tk.Toplevel(main)
    win.title(f"{difficulty.capitalize()} Questions")
    win.geometry(('600x300'))

    questions = QUESTIONS[difficulty]




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