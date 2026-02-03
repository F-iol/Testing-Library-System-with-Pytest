import pytest
from app.classes.book import Book
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.database import Base
from app.classes.user import User
import uuid
from app.classes.loan import Loan
from datetime import datetime ,timezone

@pytest.fixture(scope='session')
def engine():
    return create_engine('sqlite:///:memory:')

@pytest.fixture(scope='session')
def setup_database(engine):
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)

@pytest.fixture
def db_session(engine,setup_database):
    Session = sessionmaker(bind=engine)
    session = Session()
    yield session
    session.close()

@pytest.fixture
def test_book():
    return Book(title='Harry Potter',author='J. K. Rowling')

@pytest.fixture
def test_book_2():
    return Book(title='Narnia',author='C.S. Lewis')

@pytest.fixture
def test_username():
    unique = str(uuid.uuid4())[:8]
    return User(first_name='John',last_name='Doe',user_name=f'JD_user_{unique}')

@pytest.fixture
def added_book(db_session,test_book):
    db_session.add(test_book)
    db_session.commit()
    return test_book

@pytest.fixture
def added_book_2(db_session,test_book_2):
    db_session.add(test_book_2)
    db_session.commit()
    return test_book_2

@pytest.fixture
def added_user(db_session,test_username):
    db_session.add(test_username)
    db_session.commit()
    return test_username

@pytest.fixture
def borrowed_book(db_session,added_book,added_user):
    new_loan =Loan(book_id=added_book.id,user_id=added_user.id,date_of_loan=datetime.now(timezone.utc).date()
    )
    
    added_book.is_available =False
    db_session.add(new_loan)
    db_session.commit()
    return added_book

@pytest.fixture
def get_test_history(db_session,added_user):
    suffix = str(uuid.uuid4())[:6]
    user_empty = User(first_name='Anna',last_name="_",user_name=f'Anna_{suffix}')
    user_no_loans = User(first_name='Emily',last_name='Empty',user_name=f'EE_{suffix}')
    db_session.add_all([user_no_loans,user_empty])
    db_session.commit()
    return {
        'with_history':added_user,
        'empty_1':user_empty,
        'empty_2':user_no_loans
    }