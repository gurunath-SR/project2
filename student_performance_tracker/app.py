# '''
# # app.py
# from flask import Flask, render_template, request, redirect, url_for
# from db_handler import fetch_students, insert_student, update_student, delete_student
# import plotter

# # --------------------- Flask App Initialization --------------------- #
# app = Flask(__name__)

# # --------------------- Dashboard --------------------- #
# @app.route('/')
# @app.route('/dashboard')
# def dashboard():
#     students = fetch_students()  # fetch all students
#     chart_paths = plotter.plot_student_data(students)  # generate charts
#     return render_template('dashboard.html', students=students, charts=chart_paths)

# # --------------------- Add Student --------------------- #
# @app.route('/add_student', methods=['GET', 'POST'])
# def add_student_route():
#     if request.method == 'POST':
#         student = {
#             'usn': request.form['usn'].strip(),
#             'name': request.form['name'].strip(),
#             'attendance': float(request.form.get('attendance', 0)),
#             'study_hours': float(request.form.get('study_hours', 0)),
#             'ADA': float(request.form.get('ADA', 0)),
#             'DBMS': float(request.form.get('DBMS', 0)),
#             'SEPM': float(request.form.get('SEPM', 0)),
#             'RMK': float(request.form.get('RMK', 0)),
#             'CC': float(request.form.get('CC', 0)),
#             'ESK': float(request.form.get('ESK', 0)),
#             'SDK': float(request.form.get('SDK', 0))
#         }
#         try:
#             insert_student(student)
#         except ValueError as e:
#             return str(e)  # Or render a template with an error message
#         return redirect(url_for('dashboard'))

#     return render_template('student_form.html', student=None, form_action=url_for('add_student_route'))

# # --------------------- Edit Student --------------------- #
# @app.route('/edit_student/<usn>')
# def edit_student_route(usn):
#     students = fetch_students()
#     student = next((s for s in students if s['usn'] == usn), None)
#     if not student:
#         return "Student not found", 404
#     return render_template('student_form.html', student=student, form_action=url_for('update_student_route'))

# # --------------------- Update Student --------------------- #
# @app.route('/update_student', methods=['POST'])
# def update_student_route():
#     student = {
#         'usn': request.form['usn'].strip(),
#         'attendance': float(request.form.get('attendance', 0)),
#         'study_hours': float(request.form.get('study_hours', 0)),
#         'ADA': float(request.form.get('ADA', 0)),
#         'DBMS': float(request.form.get('DBMS', 0)),
#         'SEPM': float(request.form.get('SEPM', 0)),
#         'RMK': float(request.form.get('RMK', 0)),
#         'CC': float(request.form.get('CC', 0)),
#         'ESK': float(request.form.get('ESK', 0)),
#         'SDK': float(request.form.get('SDK', 0))
#     }
#     update_student(student)
#     return redirect(url_for('dashboard'))

# # --------------------- Delete Student --------------------- #
# @app.route('/delete_student/<student_id>', methods=['POST'])
# def delete_student_route(student_id):
#     delete_student(student_id)
#     return redirect(url_for('dashboard'))

# # --------------------- Run Flask --------------------- #
# if __name__ == '__main__':
#     app.run(debug=True)
# '''

#------------------------------------------------------------------------


# app.py
from flask import Flask, render_template, request, redirect, url_for
from db_handler import fetch_students, fetch_student_by_usn, insert_student, update_student, delete_student
import plotter

app = Flask(__name__)

# --------------------- Dashboard --------------------- #
@app.route('/')
@app.route('/dashboard')
def dashboard():
    students = fetch_students()  # fetch all students
    chart_paths = plotter.plot_student_data(students)  # generate charts
    return render_template('dashboard.html', students=students, charts=chart_paths)

## --------------------- View Student Details --------------------- #
@app.route('/student/<usn>')
def view_student(usn):
    student = fetch_student_by_usn(usn)
    if not student:
        return "Student not found", 404
    return render_template('student_details.html', student=student)

# --------------------- Add Student --------------------- #
@app.route('/add_student', methods=['GET', 'POST'])
def add_student_route():
    if request.method == 'POST':
        # Read data from form
        student = {
            'usn': request.form['usn'].strip(),
            'name': request.form['name'].strip(),
            'attendance': float(request.form.get('attendance', 0)),
            'study_hours': float(request.form.get('study_hours', 0)),
        }

        # Read subject marks
        subjects = ['ADA','DBMS','SEPM','RMK','CC','ESK','SDK']
        total_marks = 0
        for sub in subjects:
            student[sub] = float(request.form.get(sub, 0))
            total_marks += student[sub]

        student['marks'] = total_marks

        insert_student(student)
        return redirect(url_for('dashboard'))

    # GET request — show empty form
    return render_template('student_form.html', student=None, form_action=url_for('add_student_route'))

# --------------------- Edit Student --------------------- #
@app.route('/edit_student/<usn>')
def edit_student_route(usn):
    student = fetch_student_by_usn(usn)
    if not student:
        return "Student not found", 404

    return render_template('student_form.html', student=student, form_action=url_for('update_student_route'))

# --------------------- Update Student --------------------- #
@app.route('/update_student', methods=['POST'])
def update_student_route():
    student = {
        'usn': request.form['usn'].strip(),
        'name': request.form['name'].strip(),
        'attendance': float(request.form.get('attendance', 0)),
        'study_hours': float(request.form.get('study_hours', 0)),
    }

    # Update subject marks
    subjects = ['ADA','DBMS','SEPM','RMK','CC','ESK','SDK']
    total_marks = 0
    for sub in subjects:
        student[sub] = float(request.form.get(sub, 0))
        total_marks += student[sub]

    student['marks'] = total_marks

    update_student(student)
    return redirect(url_for('dashboard'))

# --------------------- Delete Student --------------------- #
@app.route('/delete_student/<student_id>', methods=['POST'])
def delete_student_route(student_id):
    delete_student(student_id)
    return redirect(url_for('dashboard'))

# --------------------- Run App --------------------- #
if __name__ == '__main__':
    app.run(debug=True)
