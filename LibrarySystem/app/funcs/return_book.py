from sqlalchemy.orm import Session
from app.classes.book import Book
from app.classes.user import User
from app.classes.loan import Loan
from datetime import datetime,timezone

def return_book(db,book_id):
    loan = db.query(Loan).filter(
        Loan.book_id ==book_id,
        Loan.date_of_return ==None
    ).first()

    if not loan:
        return f"This book is not borrowed"
    
    try:
        loan.date_of_return = datetime.now(timezone.utc).date()
        book = db.query(Book).get(book_id)
        book.is_available =True
        
        db.add(book)
        db.add(loan)
        db.commit()
        return f'Book {book.title} returned '
    except Exception as e:
        db.rollback()
        return f'Error {e}'