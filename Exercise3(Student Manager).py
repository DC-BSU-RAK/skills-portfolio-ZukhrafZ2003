import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
import os

# ------------------ FILE SETUP ------------------
FILE_NAME = "studentMarks.txt"

if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, "w") as f:
        f.write("10\n")
        f.write("1345,John Curry,8,15,7,45\n")
        f.write("2345,Sam Sturtivant,14,15,14,77\n")
        f.write("9876,Lee Scott,17,11,16,99\n")
        f.write("3724,Matt Thompson,19,11,15,81\n")
        f.write("1212,Ron Herrema,14,17,18,66\n")
        f.write("8439,Jake Hobbs,10,11,10,43\n")
        f.write("2344,Jo Hyde,6,15,10,55\n")
        f.write("9384,Gareth Southgate,5,6,8,33\n")
        f.write("8327,Alan Shearer,20,20,20,100\n")
        f.write("2983,Les Ferdinand,15,17,18,92\n")

# ------------------ DATA FUNCTIONS ------------------
def load_students():
    with open(FILE_NAME, "r") as f:
        lines = f.readlines()[1:]
    students = []
    for line in lines:
        parts = line.strip().split(",")
        code = int(parts[0])
        name = parts[1]
        marks = list(map(int, parts[2:]))
        coursework_total = sum(marks[:3])
        exam_mark = marks[3]
        overall = coursework_total + exam_mark
        percentage = (overall / 160) * 100
        grade = get_grade(percentage)
        students.append({
            "code": code,
            "name": name,
            "coursework": coursework_total,
            "exam": exam_mark,
            "percentage": percentage,
            "grade": grade
        })
    return students

def get_grade(percentage):
    if percentage >= 70:
        return "A"
    elif percentage >= 60:
        return "B"
    elif percentage >= 50:
        return "C"
    elif percentage >= 40:
        return "D"
    else:
        return "F"

def save_students(students):
    with open(FILE_NAME, "w") as f:
        f.write(str(len(students)) + "\n")
        for s in students:
            # reconstruct marks assuming coursework and exam are stored
            f.write(f"{s['code']},{s['name']},{s['coursework']//3},{s['coursework']//3},{s['coursework']//3},{s['exam']}\n")

# ------------------ DISPLAY FUNCTIONS ------------------
def display_all():
    students = load_students()
    output_text.delete(1.0, tk.END)
    total = 0
    for s in students:
        output_text.insert(tk.END, f"\nName: {s['name']}\nID: {s['code']}\n"
                            f"Coursework: {s['coursework']}/60\nExam: {s['exam']}/100\n"
                            f"Overall: {s['percentage']:.2f}% | Grade: {s['grade']}\n" + "-"*40 + "\n")
        total += s['percentage']
    avg = total / len(students)
    output_text.insert(tk.END, f"\nTotal Students: {len(students)}\nAverage Percentage: {avg:.2f}%")

def display_individual():
    students = load_students()
    code = simpledialog.askinteger("Student Lookup", "Enter Student ID:")
    found = False
    output_text.delete(1.0, tk.END)
    for s in students:
        if s['code'] == code:
            output_text.insert(tk.END, f"\nName: {s['name']}\nID: {s['code']}\n"
                                f"Coursework: {s['coursework']}/60\nExam: {s['exam']}/100\n"
                                f"Overall: {s['percentage']:.2f}% | Grade: {s['grade']}\n")
            found = True
    if not found:
        messagebox.showerror("Error", "Student not found!")

def show_highest():
    students = load_students()
    best = max(students, key=lambda s: s['percentage'])
    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, f" Highest Scorer \n\n"
                        f"Name: {best['name']}\nID: {best['code']}\n"
                        f"Coursework: {best['coursework']}/60\nExam: {best['exam']}/100\n"
                        f"Overall: {best['percentage']:.2f}% | Grade: {best['grade']}")

def show_lowest():
    students = load_students()
    low = min(students, key=lambda s: s['percentage'])
    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, f" Lowest Scorer \n\n"
                        f"Name: {low['name']}\nID: {low['code']}\n"
                        f"Coursework: {low['coursework']}/60\nExam: {low['exam']}/100\n"
                        f"Overall: {low['percentage']:.2f}% | Grade: {low['grade']}")

def sort_students():
    students = load_students()
    choice = messagebox.askquestion("Sort Order", "Sort in ascending order?")
    students.sort(key=lambda s: s['percentage'], reverse=(choice == "no"))
    output_text.delete(1.0, tk.END)
    for s in students:
        output_text.insert(tk.END, f"{s['name']} - {s['percentage']:.2f}% | Grade {s['grade']}\n")

def add_student():
    students = load_students()
    code = simpledialog.askinteger("Add Student", "Enter Student ID:")
    name = simpledialog.askstring("Add Student", "Enter Student Name:")
    c1 = simpledialog.askinteger("Coursework 1", "Mark out of 20:")
    c2 = simpledialog.askinteger("Coursework 2", "Mark out of 20:")
    c3 = simpledialog.askinteger("Coursework 3", "Mark out of 20:")
    exam = simpledialog.askinteger("Exam", "Mark out of 100:")
    coursework = c1 + c2 + c3
    percentage = (coursework + exam) / 160 * 100
    grade = get_grade(percentage)
    students.append({"code": code, "name": name, "coursework": coursework, "exam": exam, "percentage": percentage, "grade": grade})
    save_students(students)
    messagebox.showinfo("Success", f"Student {name} added!")

def delete_student():
    students = load_students()
    code = simpledialog.askinteger("Delete Student", "Enter Student ID:")
    new_list = [s for s in students if s['code'] != code]
    if len(new_list) == len(students):
        messagebox.showerror("Error", "Student not found!")
    else:
        save_students(new_list)
        messagebox.showinfo("Deleted", "Student deleted successfully!")

def update_student():
    students = load_students()
    code = simpledialog.askinteger("Update Student", "Enter Student ID:")
    for s in students:
        if s['code'] == code:
            s['exam'] = simpledialog.askinteger("Update Exam", "Enter new Exam mark:")
            s['percentage'] = (s['coursework'] + s['exam']) / 160 * 100
            s['grade'] = get_grade(s['percentage'])
            save_students(students)
            messagebox.showinfo("Updated", "Record updated successfully!")
            return
    messagebox.showerror("Error", "Student not found!")

# ------------------ GUI SETUP ------------------
root = tk.Tk()
root.title("Student Manager")
root.geometry("900x600")
root.configure(bg="#030303")

title_label = tk.Label(root, text=" Student Manager System", font=("Helvetica", 22, "bold"), bg="#F3B2ED", fg="white", pady=10)
title_label.pack(fill="x")

# Buttons Frame
frame = tk.Frame(root, bg="#BBDEFB")
frame.pack(fill="x", pady=10)

buttons = [
    ("View All Records", display_all),
    ("View Individual", display_individual),
    ("Highest Scorer", show_highest),
    ("Lowest Scorer", show_lowest),
    ("Sort Records", sort_students),
    ("Add Student", add_student),
    ("Delete Student", delete_student),
    ("Update Record", update_student)
]

for text, cmd in buttons:
    tk.Button(frame, text=text, command=cmd, bg="#64B5F6", fg="black",
              font=("Arial", 11, "bold"), relief="flat", width=17, height=2,
              activebackground="#0D47A1", activeforeground="white").pack(side="left", padx=5, pady=5)

# Output area
output_text = tk.Text(root, wrap="word", bg="white", fg="#212121", font=("Consolas", 11))
output_text.pack(padx=10, pady=10, fill="both", expand=True)

root.mainloop()

