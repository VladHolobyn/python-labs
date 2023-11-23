from sqlalchemy import Integer, String, Boolean, TIMESTAMP
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime
from ..extensions import db
import enum

class EnumPriority(enum.Enum):
    low = 1 
    medium = 2 
    high = 3

class Post(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(100))
    text: Mapped[str] = mapped_column(String)
    image: Mapped[str] = mapped_column(String, nullable=True)
    created: Mapped[TIMESTAMP] = mapped_column(TIMESTAMP, default=datetime.now())
    type: Mapped[EnumPriority] = mapped_column(db.Enum(EnumPriority), default=EnumPriority.low.name) 
    enabled: Mapped[bool] = mapped_column(Boolean, default=False)
    user_id: Mapped[int] = mapped_column(Integer, db.ForeignKey('user.id', name='fk_user'))

    def __repr__(self) -> str:
        return f"ID:{self.id} Title:{self.title} Created:{self.created} UserID: {self.user_id}"

# class Category(db.Model):
#     id: Mapped[int] = mapped_column(Integer, primary_key=True)
#     name: Mapped[str] = mapped_column(String)
#     todos = db.relationship('Todo', backref='category')
