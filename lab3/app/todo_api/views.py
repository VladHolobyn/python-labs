from flask import  request, jsonify
from app.todo.models import Todo, Category
from ..extensions import db
from . import todo_api_bp
from datetime import datetime


@todo_api_bp.route('/', methods=["GET"])
def get_all_todos():
    todos = Todo.query.all()
    todos_dict = [
        {
            "id": todo.id,
            "title": todo.title, 
            "due_date": todo.due_date.strftime("%Y-%m-%d") if  todo.due_date else None, 
            "complete": todo.complete,
            "category_id": todo.category_id
        } for todo in todos]
    
    return jsonify(todos_dict)
