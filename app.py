from flask import Flask, render_template, request, redirect, url_for
# from forms import RegistrationForm, LoginForm
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = ''
db = SQLAlchemy(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    complete = db.Column(db.Boolean)

# @app.route("/register")
# def register(task_id):
#     form = RegistrationForm()
#     return render_template('register.html', title='Register', form=form)

# @app.route("/login")
# def login(task_id):
#     form = LoginForm()
#     return render_template('login.html', title='Login', form=form)



@app.route('/')
def index():
    #show all tasks
    task_list = Task.query.all()
    # print(task_list)
    return render_template('base.html', task_list=task_list)

@app.route("/add", methods=["POST"])
def add():
    #add new item
    title=request.form.get("title")
    new_task = Task(title=title, complete=False)
    db.session.add(new_task)
    db.session.commit()
    return redirect(url_for("index"))

# @app.route("/update/<int:task_id>")
# def update(task_id):
#     task = Task.query.filter_by(id=task_id).first()
#     task.complete = not task.complete
#     db.session.commit()
#     return redirect(url_for("index"))

@app.route("/delete/<int:task_id>")
def delete(task_id):
    task = Task.query.filter_by(id=task_id).first()
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for("index"))


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)

