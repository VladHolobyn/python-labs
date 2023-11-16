from flask import render_template, redirect, url_for, flash, current_app
from .extensions  import db
from app.forms import TodoForm, FeedbackForm
from app.models import Todo, Feedback
from datetime import datetime


@current_app.route('/todos')
def todos():
    todo_list = Todo.query.all()
    return render_template("todo.html", todo_list=todo_list, form=TodoForm())
 
@current_app.route("/todos/add", methods=["POST"])
def add_todo():
    form=TodoForm()
    new_todo = Todo(title=form.title.data, due_date=form.due_date.data, complete=False)
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for("todos"))
 
@current_app.route("/todos/update/<int:id>")
def update_todo(id):
    todo = Todo.query.get_or_404(id)
    todo.complete = not todo.complete   
    db.session.commit()
    return redirect(url_for("todos"))
 
@current_app.route("/todos/delete/<int:id>")
def delete_todo(id):
    todo = Todo.query.get_or_404(id)
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("todos"))


@current_app.route('/feedbacks', methods=["GET", "POST"])
def feedbacks():
    form=FeedbackForm()

    if form.validate_on_submit():
        new_feedback = Feedback(
            topic= form.topic.data,
            text=form.text.data,
            mark=form.mark.data,
            user_email=form.email.data,  
            date=datetime.now())
        
        try:
            db.session.add(new_feedback)
            db.session.commit()
            flash("Feedback added!", category="success")
        except:
            db.session.rollback()
            flash("Something went wrong!", category="danger")
        return redirect(url_for("feedbacks"))

    feedbacks = Feedback.query.all()
    return render_template("feedbacks.html", feedbacks=feedbacks, form=form)
 
@current_app.route("/feedbacks/delete/<int:id>")
def delete_feedback(id):
    feedback = Feedback.query.get_or_404(id)
    try:
        db.session.delete(feedback)
        db.session.commit()
        flash("Feedback deleted!", category="success")
    except:
        db.session.rollback()
        flash("Something went wrong!", category="danger")
    
    return redirect(url_for("feedbacks"))
