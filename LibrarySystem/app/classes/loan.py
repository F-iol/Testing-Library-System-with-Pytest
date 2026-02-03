from sqlalchemy import Column,Boolean,String,ForeignKey,Date,Integer
from sqlalchemy.orm import relationship
from app.database import Base
from datetime import datetime,timezone

class Loan(Base):
    __tablename__='loans'

    id = Column(Integer,primary_key=True,index=True)

    user_id =Column(Integer,ForeignKey('users.id'))
    book_id =Column(Integer,ForeignKey('books.id'))
    date_of_loan = Column(Date,default=lambda :datetime.now(timezone.utc))
    date_of_return =Column(Date,nullable=True)

    book = relationship('Book',back_populates='loans')
    user = relationship('User',back_populates='loans')


