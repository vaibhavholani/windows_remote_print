# app.py
from flask import Flask, render_template, request, redirect, url_for, flash
import win32api
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'
app.secret_key = 'some_secret'

if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file:
            # Using os.path.abspath to get the absolute path of the file
            filepath = os.path.abspath(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
            file.save(filepath)
            print_file(filepath)
            flash('File printed successfully!')
    return render_template('index.html')

def print_file(filepath):
    if os.path.exists(filepath):
        win32api.ShellExecute(0, "print", filepath, None, ".", 0)
    else:
        print(f"File not found: {filepath}")
        
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
