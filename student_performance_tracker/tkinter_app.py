# tkinter_app.py
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk
from db_handler import fetch_students, insert_student, update_student, delete_student
import plotter
import os

# --------------------- Functions --------------------- #
def refresh_table():
    """Fetch students and display in Treeview table."""
    for row in table.get_children():
        table.delete(row)
    students = fetch_students()
    for s in students:
        table.insert("", "end", values=(
            s['usn'],  # changed from 'id' to 'usn'
            s['name'],
            s['attendance'],
            s['study_hours'],
            s['marks']
        ))
    update_charts(students)

def submit():
    usn = usn_var.get().strip()
    name = name_var.get().strip()
    attendance = float(attendance_var.get().strip() or 0)
    study_hours = float(study_hours_var.get().strip() or 0)
    marks = int(marks_var.get().strip() or 0)

    if not usn:
        messagebox.showerror("Error", "Please enter a valid Student USN.")
        return

    insert_student(usn, name, attendance, study_hours, marks)
    messagebox.showinfo("Success", "Student added successfully!")
    clear_fields()
    refresh_table()

def update():
    usn = usn_var.get().strip()
    attendance = float(attendance_var.get().strip() or 0)
    study_hours = float(study_hours_var.get().strip() or 0)
    marks = int(marks_var.get().strip() or 0)

    if not usn:
        messagebox.showerror("Error", "Please enter a valid Student USN.")
        return

    update_student(usn, attendance, study_hours, marks)
    messagebox.showinfo("Success", "Student updated successfully!")
    clear_fields()
    refresh_table()

def delete():
    usn = usn_var.get().strip()
    if not usn:
        messagebox.showerror("Error", "Please enter a valid Student USN.")
        return

    delete_student(usn)
    messagebox.showinfo("Success", "Student deleted successfully!")
    clear_fields()
    refresh_table()

def clear_fields():
    usn_var.set("")
    name_var.set("")
    attendance_var.set("")
    study_hours_var.set("")
    marks_var.set("")

def update_charts(students):
    """Generate charts and display in Tkinter."""
    chart_paths = plotter.plot_student_data(students)
    for key, label in chart_labels.items():
        path = chart_paths.get(key)
        if path and os.path.exists(path):
            img = Image.open(path)
            img = img.resize((400, 250))
            photo = ImageTk.PhotoImage(img)
            label.config(image=photo)
            label.image = photo  # keep reference

# --------------------- Tkinter GUI --------------------- #
root = tk.Tk()
root.title("Student Performance Tracker")
root.geometry("1200x700")

# --- Left Frame: Form ---
form_frame = tk.Frame(root)
form_frame.pack(side="left", fill="y", padx=10, pady=10)

# Variables
usn_var = tk.StringVar()
name_var = tk.StringVar()
attendance_var = tk.StringVar()
study_hours_var = tk.StringVar()
marks_var = tk.StringVar()

# Form Fields
tk.Label(form_frame, text="Student USN").pack()
tk.Entry(form_frame, textvariable=usn_var).pack()

tk.Label(form_frame, text="Name").pack()
tk.Entry(form_frame, textvariable=name_var).pack()

tk.Label(form_frame, text="Attendance").pack()
tk.Entry(form_frame, textvariable=attendance_var).pack()

tk.Label(form_frame, text="Study Hours").pack()
tk.Entry(form_frame, textvariable=study_hours_var).pack()

tk.Label(form_frame, text="Marks").pack()
tk.Entry(form_frame, textvariable=marks_var).pack()

tk.Button(form_frame, text="Add Student", command=submit).pack(pady=5)
tk.Button(form_frame, text="Update Student", command=update).pack(pady=5)
tk.Button(form_frame, text="Delete Student", command=delete).pack(pady=5)
tk.Button(form_frame, text="Clear Fields", command=clear_fields).pack(pady=5)

# --- Right Frame: Table + Charts ---
right_frame = tk.Frame(root)
right_frame.pack(side="right", fill="both", expand=True, padx=10, pady=10)

# Table
columns = ("USN", "Name", "Attendance", "Study Hours", "Marks")
table = ttk.Treeview(right_frame, columns=columns, show="headings", height=10)
for col in columns:
    table.heading(col, text=col)
    table.column(col, width=100)
table.pack(pady=10)

# Charts
chart_labels = {}
chart_frame = tk.Frame(right_frame)
chart_frame.pack()

for chart_name in ["attendance", "study_hours", "marks"]:
    lbl = tk.Label(chart_frame)
    lbl.pack(side="left", padx=5)
    chart_labels[chart_name] = lbl

# Load initial data
refresh_table()

root.mainloop()
