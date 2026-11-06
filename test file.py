import tkinter as tk

#main window
root = tk.Tk()

#set window title
root.title("Sample window")

#set window size
root.geometry("1080x980")

custom_font = ("Arial",
            30,
            "bold")

label1 = tk.Label(root,text = "Hey, its me its verity", font = custom_font)
label1.pack(side="top",
           pady=20,
           )

button1 = tk.Button(root, text = "Ask me anything", font = custom_font, command = lambda: label1.config(text="I know about a lot of things"))
button1.pack(side="left",
           pady=20,)




#pack() attributes
#- side (top,left,right,bottom)
#- fill 
#- expand
#- anchor
#internal padding & external padding (ipad, pady)

#start event - opens the application
root.mainloop()



