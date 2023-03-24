from flask import Flask, flash, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URI")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = os.getenv("SECRET_KEY")
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Posts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text, nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.now())

@app.route('/')
def index():
    posts = Posts.query.order_by(Posts.created_at.desc()).all()
    return render_template('index.html', posts=posts)

@app.route('/add')
def add():
    return render_template('add.html')

@app.route('/create_post', methods=['POST'])
def create_post():
    title = request.form['title']
    content = request.form['content']
    if title == '' or content == '':
        error_message = 'Por favor complete todos los campos'
        flash(error_message)
        return redirect(url_for('add'))
    post = Posts(title=title, content=content)
    db.session.add(post)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/post/<int:post_id>', methods=['GET'])
def post(post_id):
    post = db.session.query(Posts).filter(Posts.id==post_id).first()
    print('anda eso?') 
    return render_template('view.html', post=post)

if __name__ == '__main__':
    app.run(debug=True)