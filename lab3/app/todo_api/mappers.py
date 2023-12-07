
class TodoMapper():
    
    def toDto(todo):
        return {
            "id": todo.id,
            "title": todo.title, 
            "due_date": todo.due_date.strftime("%Y-%m-%d") if  todo.due_date else None, 
            "complete": todo.complete,
            "category_id": todo.category_id
        }
