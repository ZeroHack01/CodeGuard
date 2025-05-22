from flask import Flask, render_template, request
import os
from scanner import scan_file

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'php', 'js', 'html', 'py'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def index():
    issues = []
    filename = None
    if request.method == 'POST':
        file = request.files['codefile']
        if file and allowed_file(file.filename):
            filename = file.filename
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            issues = scan_file(file_path)
    return render_template('index.html', issues=issues, filename=filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
