import os

# Main project folder
project_name = "student_performance_tracker"

# Folder structure
folders = [
    f"{project_name}/forms",
    f"{project_name}/static/css",
    f"{project_name}/static/charts",
    f"{project_name}/templates",
]

# Starter files with initial content
files = {
    f"{project_name}/app.py": "# Flask backend\n",
    f"{project_name}/db_handler.py": "# MySQL connection & queries\n",
    f"{project_name}/forms/student_form.html": "<!-- Input form for student details -->\n",
    f"{project_name}/static/css/tailwind.css": "/* Tailwind CSS */\n",
    f"{project_name}/templates/dashboard.html": "<!-- Dashboard visualization page -->\n",
    f"{project_name}/tkinter_app.py": "# Tkinter admin interface\n",
    f"{project_name}/plotter.py": "# Graph plotting functions\n",
    f"{project_name}/requirements.txt": "flask\nmysql-connector-python\ntkinter\nmatplotlib\ntailwindcss\n",
}

# Create folders
for folder in folders:
    os.makedirs(folder, exist_ok=True)
    # Add __init__.py in each folder
    init_path = os.path.join(folder, "__init__.py")
    with open(init_path, "w", encoding="utf-8") as f:
        f.write("# Package initializer\n")

# Create files
for path, content in files.items():
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

print(f"✅ Project structure with __init__.py created under: {project_name}/")
