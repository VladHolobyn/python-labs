from flask import Blueprint, render_template, redirect, url_for
from app.extensions  import db
from app.todo.forms import TodoForm
from app.todo.models import Todo

todo = Blueprint('todo', __name__, template_folder='templates')


@todo.route('/')
def todo_page():
    return render_template("todo/todo.html", todo_list=Todo.query.all(), form=TodoForm())
 
@todo.route("/add", methods=["POST"])
def add():
    form=TodoForm()
    new_todo = Todo(title=form.title.data, due_date=form.due_date.data, complete=False)
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for("todo.todo_page"))
 
@todo.route("/update/<int:id>")
def update(id):
    todo = Todo.query.get_or_404(id)
    todo.complete = not todo.complete   
    db.session.commit()
    return redirect(url_for("todo.todo_page"))
 
@todo.route("/delete/<int:id>")
def delete(id):
    todo = Todo.query.get_or_404(id)
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("todo.todo_page"))
