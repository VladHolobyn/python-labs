from flask import render_template, redirect, url_for
from ..extensions import db
from .forms import TodoForm
from .models import Todo
from . import todo_bp


@todo_bp.route('/')
def todo_page():
    return render_template("todo/todo.html", todo_list=Todo.query.all(), form=TodoForm())
 
@todo_bp.route("/add", methods=["POST"])
def add():
    form=TodoForm()
    new_todo = Todo(title=form.title.data, due_date=form.due_date.data, complete=False)
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for("todo.todo_page"))
 
@todo_bp.route("/update/<int:id>")
def update(id):
    todo = Todo.query.get_or_404(id)
    todo.complete = not todo.complete   
    db.session.commit()
    return redirect(url_for("todo.todo_page"))
 
@todo_bp.route("/delete/<int:id>")
def delete(id):
    todo = Todo.query.get_or_404(id)
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("todo.todo_page"))
