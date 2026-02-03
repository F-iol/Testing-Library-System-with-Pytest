from app.classes.loan import Loan
from app.funcs.borrow import borrow_book


def test_borrow_book(db_session,added_user,added_book):
    result = borrow_book(db_session,added_user.id,added_book.id)
    loan =db_session.query(Loan).filter(Loan.book_id == added_book.id).first()
    assert 'succesfully' in result.lower()
    assert added_book.is_available is False
    assert loan is not None
    assert  loan.user_id == added_user.id
    