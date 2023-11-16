from flask import render_template, redirect, url_for, flash
from ..extensions import db
from .forms import TodoForm, CategoryForm
from .models import Todo, Category
from . import todo_bp


@todo_bp.route('/')
def todo_page():
    form=TodoForm()
    form.categories.choices = [(c.id, c.name) for c in Category.query.all()] 
    return render_template("todo/todo.html", todo_list=Todo.query.all(), form=form)
 
@todo_bp.route("/add", methods=["POST"])
def add():
    form=TodoForm()
    print(form.categories.data)
    new_todo = Todo(
        title=form.title.data, 
        due_date=form.due_date.data, 
        category_id=form.categories.data,
        complete=False
    )
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

@todo_bp.route('/categories')
def category_page():
    return render_template("todo/categories.html", categories=Category.query.all(), form=CategoryForm())

@todo_bp.route("/categories", methods=["POST"])
def add_category():
    form=CategoryForm()
    
    if form.validate_on_submit():
        try:
            new_category = Category(name=form.name.data)
            db.session.add(new_category)
            db.session.commit()
            flash('Category created!', category='success')
        except:
            flash('Error!', category='danger')
            db.session.rollback()
    else:
        flash('Invalid form!', category='danger')

    return redirect(url_for('todo.category_page'))

@todo_bp.route("/categories/delete/<int:id>", methods=["POST"])
def delete_category(id):
    category = Category.query.get_or_404(id)
    try:
        db.session.delete(category)
        db.session.commit()
        flash('Category deleted!', category='success')
    except:
        flash('Error!', category='danger')
        db.session.rollback()
    return redirect(url_for("todo.category_page"))