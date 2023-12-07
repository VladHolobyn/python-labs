from flask import  request, jsonify
from app.todo.models import Todo, Category
from ..extensions import db
from . import todo_api_bp
from .mappers import TodoMapper
from .validators import TodoValidator


@todo_api_bp.route('/', methods=["GET"])
def get_all_todos():
    todos = Todo.query.all()
    todos_dict = [TodoMapper.toDto(todo) for todo in todos]
    
    return jsonify(todos_dict)


@todo_api_bp.route('/<int:id>', methods=["GET"])
def get_todo(id):
    todo = Todo.query.filter_by(id=id).first()

    if not todo:
        return jsonify({"message": f"Todo with id:{id} not found"}), 404
    
    return jsonify(TodoMapper.toDto(todo))
 

@todo_api_bp.route("/", methods=["POST"])
def create_todo():

    data = request.get_json()
    if not data:
        return jsonify({"message": "No data provided"}), 400
    
    isValid, response = TodoValidator.validateForCreate(data)
    if not isValid:
        return jsonify({'message': response['message']}),  response['status_code']

    todo = TodoMapper.toEntity(data)

    try: 
        db.session.add(todo)
        db.session.commit()

        new_todo = Todo.query.filter_by(id=todo.id).first()
        return jsonify(TodoMapper.toDto(new_todo)), 201
    except:
        db.session.rollback()
        return jsonify({"message": "Error"}), 500


@todo_api_bp.route('/<int:id>', methods=["PUT"])
def update_todo(id):  

    data = request.get_json()
    if not data:
        return jsonify({"message": "No data provided"}), 400
    
    todo = Todo.query.filter_by(id=id).first()
    if not todo:
        return jsonify({"message": f"Todo with id:{id} not found"}), 404
    
    isValid, response = TodoValidator.validateForUpdate(data)
    if not isValid:
        return jsonify({'message': response['message']}),  response['status_code']

    TodoMapper.updateFromDto(todo, data)

    try: 
        db.session.commit()
        new_todo = Todo.query.filter_by(id=id).first()
        return jsonify(TodoMapper.toDto(new_todo)), 200
    except:
        db.session.rollback()
        return jsonify({"message": "Error"}), 500
 
