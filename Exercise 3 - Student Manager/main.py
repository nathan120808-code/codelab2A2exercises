import os
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog

#globals
TOTAL_MARK = 160 #out of 160

#data line layout for notes
#2345,Sam Sturtivant,14,15,14,77
#student code, name, course marks(3), exam marks

#each student is a dict
# {"number": studentid, "name": "studentname", "marks": [1,2,3], "exam": 100}

#to link the txt file
FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "studentMarks.txt")

#file handler
def load():
    """reads txt file and loads liens into dictionaries"""
    students =[]
    if not os.path.exists(FILE):
        return students
    with open(FILE) as f:
        lines = f.read().splitlines()[1:] #skip line 1
    for line in lines:
        if line.strip():
            p = line.split(",")
            #splits the data seperately into their corresponding class
            students.append({"number": int(p[0]),
                            "name": p[1],
                            "marks": [int(m) for m in p[2:5]],
                            "exam": int(p[5])})

    return students

def save():
    """writes whole list back to the txt file"""
    with open(FILE, "w") as f:
        f.write(f"{len(students)}\n")
        for s in students:
            parts = [str(s["number"]),
                      s["name"] + [str(m) for m in s["marks"]] + [str(s["exam"])]]
            f.write(",".join(parts) + "\n")


#functions for calculating
def course_total(s):
    """returns total coursework marks"""
    return sum(s["marks"]) + s["exam"] #gathers student marks and exam marks and are added together

def score_total(s):
    """returns total of exam + course marks"""
    return course_total(s) / TOTAL_MARK * 100

def grade_total(s):
    """provides ranking based total"""
    st = score_total(s)
    #basic conditionals covering the margin for each rank
    if st >= 70:
        return "A"
    if st >= 60:
        return "B"
    if st >= 50:
        return "C"
    if st >= 40:
        return "D"
    return "F"

#backend functionality
def show_student(records, summar=''):
    """every menu item prints through here with the same format - displaying all relevant student details"""
    output.delete("1.0", tk.END)
    for s in records:
        output.insert(tk.END, f"{s['name']} ({s['number']}) Coursework: {sum(s['marks'])}/60"
                      f"Exam: {s['exam']}/100 Overall: {score_total(s):.1f}% Grade: {grade_total(s)}\n")

def has_students():
    """"""
    if not students:
        messagebox.showinfo("No data", "Please check if student records is in the local folder")

def find(prompt):
    """a search prompt which asks fro student number or name optionally"""
    if not has_students():
        return None
    query = simpledialog.askstring("Search student", prompt)
    if query:
        for s in students:
            if query.strip().lower() in (str(s["number"]), s["name"].lower()):
                return s
        messagebox.showinfo("Not found", f"No student matches {query}")

    return None

def ask_details(old=None):
    """asks for each class in turn - askinteger checks the ranges for us. If old is given (updating), each
    box starts filled with the current value"""
    old = old or {"number": None, "name": "", "marks": [None] * 3, "exam": None}
    number = simpledialog.askinteger("Student", "Student number (1000 - 9999):",
                                     initialvalue=old["number"], minvalue=1000, maxvalue=9999)
    name = simpledialog.askstring("Student", "Student Name:" initialvalue=old["name"]) if number else None
    if not name:
        return None
    marks = []
    for i in range(3):
        m = simpledialog.askinteger("Student",f'Course mark {i + 1} {0-20}:',
                                    initialvalue=old["marks"][i], minvalue=0, maxvalue=20)
        if m is None:
            return None
        marks.append(m)

    exam = simpledialog.askinteger("Student", "Exam mark (0-100)",
                                   initialvalue=old['exam'], minvalue=0, maxvalue=100)

    if exam is None:
        return None
    return {"number": number, "name": name.replace(',', ""), "marks": marks, "exam": exam}

#FRONTEND

main = tk.Tk()
main.title("Student Manager")
main.geometry("800x500")
main.resizable(0,0)
main.config(
    bg = "#323B4E"
)

title_label = tk.Label(main, text="Student Manager")

