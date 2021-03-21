from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from flask_sqlalchemy import SQLAlchemy
from wtforms import StringField, TextField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///tasks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    state = db.Column(db.String(10))

#get user input (using FlaskForm)
class TodoForm(FlaskForm):
    title = StringField(label=('Your task:'), validators=[DataRequired()])
    state = SelectField(u'Current Status:', choices=[('To Do'), ('Doing'), ('Done')])
    submit = SubmitField('Add task to Kanban')

# create database for tasks
db.create_all()
# commit entries for the database
db.session.commit()

#to render all tasks
@app.route("/", methods=["GET", "POST"])
def index():
    form = TodoForm()
    todo_list = Todo.query.all()
    return render_template("base.html", form=form, todo_list=todo_list)

#to add a new task
@app.route('/add', methods=['POST', 'GET'])
def new_task():
    title = request.form.get("title")
    state = request.form.get("state")
    new_todo = Todo(title=title, state=state)
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for("index"))

#to delete a task
@app.route("/delete/<int:todo_id>")
def delete(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("index"))

#to move a task to the right (to update status)
@app.route("/update_right/<int:todo_id>")
def update_right(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    if todo.state == "To Do":
        todo.state = "Doing"
    elif todo.state == "Doing":
        todo.state = "Done"
    db.session.commit()
    return redirect(url_for("index"))

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)