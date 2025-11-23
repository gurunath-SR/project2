from flask import Flask, render_template
app = Flask(__name__)

with app.app_context():
    render_template('teacher/teacher_dashboard.html')
