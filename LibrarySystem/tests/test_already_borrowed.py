from app.classes.loan import Loan
from app.funcs.borrow import borrow_book


def test_already_borrowed(db_session,added_user,borrowed_book):
    initial_count = db_session.query(Loan).count()
    result = borrow_book(db_session,added_user.id,borrowed_book.id)

    assert 'already borrowed' in result.lower()

    final_count = db_session.query(Loan).count()
    assert initial_count == final_count