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
    """reads txt file and loads lines into student dictionary"""
    students =[]
    if not os.path.exists(FILE):
        return students
    with open(FILE) as f:
        lines = f.read().splitlines()[1:] #skip line 1
    for line in lines:
        if line.strip():
            p = line.split(",") #p = [id,name,mark1,mark2,mark3,mark4]
            #splits the data seperately into their corresponding class
            students.append({"number": int(p[0]), #appends index 0 which is student id
                            "name": p[1], #appends name
                            "marks": [int(m) for m in p[2:5]], #appends index 2-5 which are course marks
                            "exam": int(p[5])}) #appends exam marks

    return students

def save():
    """writes whole list back to the txt file"""
    with open(FILE, "w") as f:
        f.write(f"{len(students)}\n")
        for s in students:
            #flat str list joined with commas
            parts = [str(s["number"]), s["name"]] + [str(m) for m in s["marks"]] + [str(s["exam"])]
            f.write(",".join(parts) + "\n")


#functions for calculating
def course_total(s):
    """returns total coursework marks"""
    return sum(s["marks"])

def score_total(s):
    """returns coursework + exam marks"""
    return course_total(s) + s['exam'] 

def percentage(s):
    """overall score based on 160 total marks"""
    return score_total(s) / TOTAL_MARK * 100

def grade_total(s):
    """provides ranking based total"""
    p = percentage(s)
    #basic conditionals covering the margin for each rank
    if p >= 70:
        return "A"
    if p >= 60:
        return "B"
    if p >= 50:
        return "C"
    if p >= 40:
        return "D"
    return "F"

#backend functionality
def show_student(records, summary=''):
    """every menu item prints through here with the same format - displaying all relevant student details"""
    output.delete("1.0", tk.END) #clear whatever shows in the output text label
    for s in records: #records are the list of students to be displayed
        output.insert(tk.END, f"{s['name']} ({s['number']}) Coursework: {sum(s['marks'])}/60"
                      f"Exam: {s['exam']}/100 Overall: {score_total(s):.1f}% Grade: {grade_total(s)}\n") #inserts this text into the output text label

    if summary: #optional text shwon under the list like class size or average
        output.insert(tk.END, "\n" + summary)

def has_students():
    """returns true if records (the txt file) is loaded by the load() function."""
    if not students: #if statement fires when students is empty - specifically the return false
        messagebox.showinfo("No data", "Please check if student records is in the local folder")
        return False
    return True #returns true after if statement happens(if the student marks file is available)

def find(prompt):
    """a search prompt which asks fro student number or name optionally"""
    if not has_students(): #if has_students returns false - nothing will be available to search
        return None
    query = simpledialog.askstring("Search student", prompt) #simple dialog using askstring
    if query: 
        for s in students: #for every student in students - the if statement below fires
            if query.strip().lower() in (str(s["number"]), s["name"].lower()): #if query is in dictionary it returns student details
                return s
        messagebox.showinfo("Not found", f"No student matches {query}") #if student is not recognized, messagebox loads this text

    return None

def ask_details(old=None):
    """asks for each class in turn - askinteger checks the ranges for us. If old is given (updating), each
    box starts filled with the current value"""
    old = old or {"number": None, "name": "", "marks": [None] * 3, "exam": None}
    number = simpledialog.askinteger("Student", "Student number (1000 - 9999):",
                                     initialvalue=old["number"], minvalue=1000, maxvalue=9999)
    name = simpledialog.askstring("Student", "Student Name:", initialvalue=old["name"]) if number else None
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

def number_take(number, ignore=None):
    #first compares value of dict with inputted number, and then ensures te exact item is not a duplicate, then iterates through the dict students
    return any(s['number'] == number and s is not ignore for s in students)

#functionality options
def view_all():
    if students:
        average = sum(percentage(s) for s in students) / len (students)
        show_student(students, f"Students in class: {len(students)}\n"
                     f"Average: {average:.1f}%")
    else:
        show_student([], "No available records")

def view_single():
    """locates student thorugh id or name with show_students() function"""
    s = find("Enter Student ID or Name")
    if s: 
        show_student([s])

def show_high():
    """shows student with the highest score through min max values"""
    if has_students():
        show_student([max(students, key=score_total)]) #checks for teh highest value with max in the students dict based on the key

def show_high():
    """same with show_high but provides lowest ranking student"""
    if has_students():
            show_student([min(students, key=score_total)])  #checks for teh lowest value with max in the students dict based on the key

def sort_records():
    """sorts by overall score - this will use sorted() which makes a new ordered list to be displayed without changing the data frame"""
    if has_students():
        ascending = messagebox.askyesno("Sort by overall grade",
                                        "Yes = Ascending\n No = Descending")
        show_student(sorted(students, key=percentage, reverse=not ascending))

def add_student():
    """asks for new student details"""
    new = ask_details()
    #
    if new and number_take(new['number']):
        messagebox.showerror("Error", "Student number already exists")
    #else appends new students and activates the necessary functions for it be saved onto the data frame - also fully displays all the details after
    else:
        students.append(new)
        save()
        view_all()

def update_student():
    """finds a student, confirms teh details, then replaces the old student's data and is saved on the main file"""
    s = find("Enter the number or name of student")

    if s:
        new = ask_details(s)
        #handles duplicate values
        if new and number_take(new["number"], ignore=s):
            messagebox.showerror("Error", "Student number already exists")
        
        elif new:
            s.update(new) #overwrites the dictionary value in place
            save()
            view_all()

#FRONTEND

main = tk.Tk()
main.title("Student Manager")
main.geometry("800x500")
main.resizable(0,0)
main.config(
    bg = "#323B4E"
)

title_label = tk.Label(main, text="Student Manager")


students = load()
main.mainloop()

