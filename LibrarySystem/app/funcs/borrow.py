from sqlalchemy.orm import Session
from app.classes.book import Book
from app.classes.user import User
from app.classes.loan import Loan


def borrow_book(db,user_id,book_id):
    book = db.query(Book).get(book_id)
    user = db.query(User).get(user_id)
    if not book:
        return 'Book is unavailable'
    if not user:
        return 'User does not exist'
    if not book.is_available:
        return f'Book: {book.title} is already borrowed'

    try:
        book.is_available =False
        new_loan = Loan(user_id=user_id,book_id=book_id)

        db.add(new_loan)
        db.commit()
        return f'Book: {book.title} has been succesfully borrowed'
    except Exception as e:
        db.rollback()
        return e

    