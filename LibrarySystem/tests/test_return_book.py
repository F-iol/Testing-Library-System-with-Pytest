from app.funcs.return_book import return_book
from app.classes.loan import Loan


def test_return_book(db_session,borrowed_book):
    
    result = return_book(db_session,borrowed_book.id)
    return_date = db_session.query(Loan).filter(Loan.book_id == borrowed_book.id).first()

    assert 'returned' in result.lower()
    assert borrowed_book.is_available is True
    assert return_date.date_of_return is not None
    