from app.database import SessionLocal,engine,Base
from app.classes.user import User
from app.classes.book import Book
from app.classes.loan import Loan
from app.funcs.borrow import borrow_book
from app.funcs.return_book import return_book
from app.funcs.history import get_user_history

Base.metadata.create_all(bind=engine)
db = SessionLocal()

try:
    new_user = User(first_name = 'Jhon',
                    last_name='Doe',
                    user_name='JD',
    )
    new_book = Book(title='Harry Potter',author='J. K. Rowling')
    new_book_2 = Book(title='Narnia' , author ='C.S. Lewis')
    db.add(new_user)
    db.add(new_book)
    db.add(new_book_2)
    db.commit()

    print('TEST')
    print(f'User added {new_user.user_name}')
    result_borrow = borrow_book(db,new_user.id,new_book_2.id)
    print(result_borrow)

    result_return = return_book(db,new_book.id)
    print(result_return)
    result_borrow_2=borrow_book(db,new_user.id,new_book.id)
    print(result_borrow_2)
    result_return_2=return_book(db,new_book_2.id)
    print(result_return_2)

    
    history=get_user_history(db,user_id=new_user.id)
    print(history)


except Exception as e:
    print(e)
    db.rollback()
finally:
    db.close()