
'''
import mysql.connector

# --------------------- Database Connection --------------------- #
def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="gurunath@2004",
        database="student_tracker_v2"
    )

# --------------------- Insert Student --------------------- #
def insert_student(usn, name, attendance, study_hours, marks):
    conn = get_connection()
    cursor = conn.cursor()

    # Check if USN already exists
    cursor.execute("SELECT usn FROM students WHERE usn = %s", (usn,))
    result = cursor.fetchone()
    if result:
        # If exists, update the record
        sql_update = """
            UPDATE students
            SET name=%s, attendance=%s, study_hours=%s, marks=%s
            WHERE usn=%s
        """
        cursor.execute(sql_update, (name, attendance, study_hours, marks, usn))
    else:
        # Insert new student
        sql_insert = """
            INSERT INTO students (usn, name, attendance, study_hours, marks)
            VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(sql_insert, (usn, name, attendance, study_hours, marks))

    conn.commit()
    cursor.close()
    conn.close()

# --------------------- Update Student --------------------- #
def update_student(usn, attendance, study_hours, marks):
    conn = get_connection()
    cursor = conn.cursor()
    sql = "UPDATE students SET attendance=%s, study_hours=%s, marks=%s WHERE usn=%s"
    cursor.execute(sql, (attendance, study_hours, marks, usn))
    conn.commit()
    cursor.close()
    conn.close()

# --------------------- Delete Student --------------------- #
def delete_student(usn):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE usn=%s", (usn,))
    conn.commit()
    cursor.close()
    conn.close()

# --------------------- Fetch Students --------------------- #
def fetch_students():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)  # dictionary=True to get column names as keys
    cursor.execute("SELECT * FROM students")  # fetch all students
    students = cursor.fetchall()
    cursor.close()
    conn.close()
    return students
'''


'''
# db_handler.py
import mysql.connector

# --------------------- Database Connection --------------------- #
def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="gurunath@2004",
        database="student_tracker_v2"
    )

# --------------------- Fetch Students --------------------- #
def fetch_students():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    cursor.close()
    conn.close()
    return students

#-------------------------------------------------------------#
def fetch_student_by_usn(usn):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    query = "SELECT * FROM students WHERE usn=%s"
    cursor.execute(query, (usn,))
    student = cursor.fetchone()
    cursor.close()
    conn.close()
    return student

# --------------------- Insert Student --------------------- #
def insert_student(student):
    # Calculate total marks automatically
    total_marks = (
        student.get('ADA', 0) + student.get('DBMS', 0) +
        student.get('SEPM', 0) + student.get('RMK', 0) +
        student.get('CC', 0) + student.get('ESK', 0) +
        student.get('SDK', 0)
    )
    
    conn = get_connection()
    cursor = conn.cursor()
    query = """
        INSERT INTO students 
        (usn, name, attendance, study_hours, marks, ADA, DBMS, SEPM, RMK, CC, ESK, SDK)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    values = (
        student['usn'],
        student['name'],
        student.get('attendance', 0),
        student.get('study_hours', 0),
        total_marks,
        student.get('ADA', 0),
        student.get('DBMS', 0),
        student.get('SEPM', 0),
        student.get('RMK', 0),
        student.get('CC', 0),
        student.get('ESK', 0),
        student.get('SDK', 0)
    )
    cursor.execute(query, values)
    conn.commit()
    cursor.close()
    conn.close()

# --------------------- Update Student --------------------- #
def update_student(student):
    total_marks = (
        student.get('ADA', 0) + student.get('DBMS', 0) +
        student.get('SEPM', 0) + student.get('RMK', 0) +
        student.get('CC', 0) + student.get('ESK', 0) +
        student.get('SDK', 0)
    )

    conn = get_connection()
    cursor = conn.cursor()
    query = """
        UPDATE students
        SET attendance=%s, study_hours=%s, marks=%s,
            ADA=%s, DBMS=%s, SEPM=%s, RMK=%s, CC=%s, ESK=%s, SDK=%s
        WHERE usn=%s
    """
    values = (
        student.get('attendance', 0),
        student.get('study_hours', 0),
        total_marks,
        student.get('ADA', 0),
        student.get('DBMS', 0),
        student.get('SEPM', 0),
        student.get('RMK', 0),
        student.get('CC', 0),
        student.get('ESK', 0),
        student.get('SDK', 0),
        student['usn']
    )
    cursor.execute(query, values)
    conn.commit()
    cursor.close()
    conn.close()

# --------------------- Delete Student --------------------- #
def delete_student(usn):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE usn=%s", (usn,))
    conn.commit()
    cursor.close()
    conn.close()
'''


import mysql.connector
from datetime import datetime

# --------------------- Database Connection --------------------- #
def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="gurunath@2004",
        database="student_tracker_v2"
    )

# --------------------- Fetch All Students --------------------- #
def fetch_students():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    cursor.close()
    conn.close()
    return students

# --------------------- Fetch One Student by USN --------------------- #
def fetch_student_by_usn(usn):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM students WHERE usn=%s", (usn,))
    student = cursor.fetchone()
    cursor.close()
    conn.close()
    return student

# --------------------- Insert Student --------------------- #
def insert_student(student):
    total_marks = sum([
        student.get('ADA', 0), student.get('DBMS', 0), student.get('SEPM', 0),
        student.get('RMK', 0), student.get('CC', 0), student.get('ESK', 0), student.get('SDK', 0)
    ])
    
    conn = get_connection()
    cursor = conn.cursor()
    query = """
        INSERT INTO students 
        (usn, name, attendance, study_hours, marks, ADA, DBMS, SEPM, RMK, CC, ESK, SDK, dob)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    values = (
        student['usn'],
        student['name'],
        student.get('attendance', 0),
        student.get('study_hours', 0),
        total_marks,
        student.get('ADA', 0),
        student.get('DBMS', 0),
        student.get('SEPM', 0),
        student.get('RMK', 0),
        student.get('CC', 0),
        student.get('ESK', 0),
        student.get('SDK', 0),
        student.get('dob')  # datetime.date object
    )
    cursor.execute(query, values)
    conn.commit()
    cursor.close()
    conn.close()

# --------------------- Update Student --------------------- #
def update_student(student):
    total_marks = sum([
        student.get('ADA', 0), student.get('DBMS', 0), student.get('SEPM', 0),
        student.get('RMK', 0), student.get('CC', 0), student.get('ESK', 0), student.get('SDK', 0)
    ])
    
    conn = get_connection()
    cursor = conn.cursor()
    query = """
        UPDATE students
        SET attendance=%s, study_hours=%s, marks=%s,
            ADA=%s, DBMS=%s, SEPM=%s, RMK=%s, CC=%s, ESK=%s, SDK=%s,
            dob=%s
        WHERE usn=%s
    """
    values = (
        student.get('attendance', 0),
        student.get('study_hours', 0),
        total_marks,
        student.get('ADA', 0),
        student.get('DBMS', 0),
        student.get('SEPM', 0),
        student.get('RMK', 0),
        student.get('CC', 0),
        student.get('ESK', 0),
        student.get('SDK', 0),
        student.get('dob'),
        student['usn']
    )
    cursor.execute(query, values)
    conn.commit()
    cursor.close()
    conn.close()

# --------------------- Delete Student --------------------- #
def delete_student(usn):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE usn=%s", (usn,))
    conn.commit()
    cursor.close()
    conn.close()
