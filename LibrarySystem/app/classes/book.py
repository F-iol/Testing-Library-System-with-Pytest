from sqlalchemy import Column,Integer,String,Boolean
from app.database import Base
from sqlalchemy.orm import relationship

class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer,primary_key =True,index=True)
    title =Column(String)
    author = Column(String)
    is_available = Column(Boolean,default=True)
   
    loans = relationship('Loan',back_populates='book')

    def __repr__(self):
        return f"Book {self.title} of {self.author} is {'available' if self.is_available else 'unavailable'})"