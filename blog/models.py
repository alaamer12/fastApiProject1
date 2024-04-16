from sqlalchemy import Column, Integer, String
from .database import Base


class Blog(Base):
    __tablename__ = "blogs"

    id = Column(Integer, primary_key=True, index=True)
    title = Column("title", String(55))
    body = Column("body", String(255))
