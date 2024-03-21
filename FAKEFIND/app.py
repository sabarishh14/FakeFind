from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' in request.files:
        file = request.files['file']
        if file:
            file.save(file.filename)
            file_directory = file.filename
            return f'Saved file to {file_directory}'
    return 'No file provided.'

if __name__ == '__main__':
    app.run(debug=True)
