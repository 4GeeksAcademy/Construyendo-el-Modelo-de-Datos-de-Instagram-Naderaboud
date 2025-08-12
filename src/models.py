from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Column, Table, ForeignKey, Enum
from sqlalchemy.orm import Mapped, mapped_column
import enum

db = SQLAlchemy()

class MediaType(enum.Enum):
    image = "image"
    video = "video"

followers_table = Table(
    "Followers",
    db.metadata,
    Column("followers_id", ForeignKey("user.id"), primary_key=True),
    Column("following_id", ForeignKey("user.id"), primary_key=True),

)


class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(
        String(120), unique=True, nullable=False)
    username: Mapped[str] = mapped_column(
        String(30), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)

    __tablename__ = "user"

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }


class Post (db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[str] = mapped_column(String(255), nullable=False)


    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id
        }

class Media (db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    type: Mapped[MediaType] = mapped_column(Enum(MediaType), nullable=False)  
    url: Mapped[str] = mapped_column(String(255), nullable=False)
    post_id: Mapped[int] = mapped_column(nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "type": self.type,
            "url": self.url,
            "post_id": self.post_id
        }


class Comment (db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(String(255), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id
        }
