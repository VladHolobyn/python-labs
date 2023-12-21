from marshmallow.fields import Enum, Nested
from ...extensions import ma
from app.posts.models import Post, EnumPriority, PostCategory


class CategorySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model=PostCategory

class PostSchema(ma.SQLAlchemyAutoSchema):
    type = Enum(EnumPriority)
    category = Nested(CategorySchema)
    class Meta:
        model=Post

