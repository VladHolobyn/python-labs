from sqlalchemy import Integer, String, Boolean, Date, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from datetime import date, datetime
from app import db

class Todo(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(100))
    due_date: Mapped[date] = mapped_column(Date, nullable=True) 
    complete: Mapped[bool] = mapped_column(Boolean)

class Feedback(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_email: Mapped[str] = mapped_column(String)
    topic: Mapped[str] = mapped_column(String)
    text: Mapped[str] = mapped_column(String)
    mark: Mapped[int] = mapped_column(Integer)
    date: Mapped[datetime] = mapped_column(DateTime) 

class User(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str] = mapped_column(String(20), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    image_file: Mapped[str] = mapped_column(String(20), nullable=False, default='default.jpg')
    password: Mapped[str] = mapped_column(String(60), nullable=False)
    
    def __repr__(self) -> str:
        return f"User({self.username}, {self.email})"
