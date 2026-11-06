#library imports
from tkinter import *

#essentials
main = Tk()
main.title("Math Quiz")
main.geometry('800x500')
main.configure(
    bg='black'
)

# questions
questions = {
    "Easy": [
        {"What is 2 = 2"}
    ],
    "Intermediate": [
        {}
    ],
    "Advanced": [
        {}
    ]

}


#extras
title_font = ('Helvetica', 40, 'bold')
button_font = ('Monospace', 15)

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