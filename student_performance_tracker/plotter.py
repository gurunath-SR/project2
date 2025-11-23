import matplotlib.pyplot as plt
import os

# --------------------- Plot Student Data --------------------- #
def plot_student_data(students):
    """
    Generates bar charts for student performance:
    - Attendance
    - Study Hours
    - Marks
    
    Returns a dictionary of chart file paths relative to 'static/' folder.
    """
    chart_paths = {}

    if not students:
        return chart_paths  # No students, return empty dict

    # Extract data from student dictionaries
    names = [s['name'] for s in students]
    attendances = [s['attendance'] for s in students]
    study_hours = [s['study_hours'] for s in students]
    marks = [s['marks'] for s in students]

    # Ensure static charts folder exists
    charts_dir = os.path.join(os.getcwd(), 'static', 'charts')
    os.makedirs(charts_dir, exist_ok=True)

    # --------------------- Attendance Chart --------------------- #
    plt.figure(figsize=(10, 5))
    plt.bar(names, attendances, color='skyblue')
    plt.title("Student Attendance")
    plt.ylabel("Attendance (%)")
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    attendance_path = os.path.join(charts_dir, 'attendance.png')
    plt.savefig(attendance_path)
    plt.close()
    chart_paths['attendance'] = 'charts/attendance.png'  # relative path for Flask

    # --------------------- Study Hours Chart --------------------- #
    plt.figure(figsize=(10, 5))
    plt.bar(names, study_hours, color='lightgreen')
    plt.title("Student Study Hours")
    plt.ylabel("Hours")
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    study_hours_path = os.path.join(charts_dir, 'study_hours.png')
    plt.savefig(study_hours_path)
    plt.close()
    chart_paths['study_hours'] = 'charts/study_hours.png'

    # --------------------- Marks Chart --------------------- #
    plt.figure(figsize=(10, 5))
    plt.bar(names, marks, color='salmon')
    plt.title("Student Marks")
    plt.ylabel("Marks")
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    marks_path = os.path.join(charts_dir, 'marks.png')
    plt.savefig(marks_path)
    plt.close()
    chart_paths['marks'] = 'charts/marks.png'

    return chart_paths
