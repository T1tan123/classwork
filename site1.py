from flask import Flask, render_template
from modals import db, Users

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

db.init_app(app)

@app.route('/')
def index():
    return render_template('base.html')

with app.app_context():
    db.create_all()
    print('[+] Таблица созданна')


app.run(debug=True)