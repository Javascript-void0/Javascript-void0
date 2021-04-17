from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///java.db'
db = SQLAlchemy(app)

class Timer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    dt = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return str(self.id)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    return "Hello"

@app.route('/timer', methods=['GET', 'START'])
def timer():
    return render_template('timer.html')

if __name__ == "__main__":
    app.run(debug=True)
