from app.todo.models import Category

class TodoValidator:
    def validate(dto):
        if not dto:
            return False, {
                'message': "No data provided",
                'status_code': 400
            }
        
        if not dto.get('title'):
            return False, {
                'message': "Title must be provided",
                'status_code': 422
            }
        
        category_id = dto.get('category_id')
        if  category_id and Category.query.filter_by(id=category_id).first() is None :
            return False, {
                'message': "Category does not exist",
                'status_code': 422
            }
        
        return True, None
    