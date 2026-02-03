from sqlalchemy import Column,Integer,String,Boolean
from app.database import Base
from sqlalchemy.orm import relationship
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer,primary_key =True,index=True)
    first_name = Column(String)
    last_name = Column(String)
    user_name = Column(String,unique=True,nullable=False)
    is_librarian =Column(Boolean,default=False)

    loans = relationship('Loan',back_populates='user')
    def __repr__(self):
        return f' {"User" if not self.is_librarian else "Librarian"} {self.user_name}'