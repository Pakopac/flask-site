from flask import Flask, render_template
from flask_flatpages import FlatPages
from flask_frozen import Freezer
from jinja2 import Template 
import json

app = Flask(__name__)
app.config.from_pyfile('settings.py')
pages = FlatPages(app)
freezer = Freezer(app)

# json importation
books_file = "./project/static/assets/books.json"
with open(books_file) as json_file:
    books_load = json.load(json_file)
books_dump = json.dumps(books_load)
books_json = json.loads(books_dump)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/project')
def project():
    return render_template('project.html', books=books_json)

@app.route('/book/<id>')
def book_by_id(id):
    return render_template('book_id.html', books=books_json, id=id)

@app.route('/contact')
def contact():
    return render_template('contact.html')
    
if __name__ == '__main__':
    app.run(debug=True)