from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Page"

@app.route('/get/note', methods=['GET'])
def note():
    return "Last Note"

if __name__ == '__main__':
    app.run(debug=True)