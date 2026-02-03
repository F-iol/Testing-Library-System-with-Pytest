from app.funcs.return_book import return_book
from app.classes.loan import Loan


def test_nothing_to_return(db_session,added_book):
    result = return_book(db_session,added_book.id)
    loan = db_session.query(Loan).filter(Loan.book_id==added_book.id).first()
    assert 'is not borrowed' in result.lower()
    assert not loan
