from app.classes.loan import Loan
from app.funcs.history import get_user_history
from app.funcs.borrow import borrow_book
from app.funcs.return_book import return_book


def test_get_user_history(db_session,added_user,added_book,added_book_2):
    borrow_book(db_session,added_user.id,added_book.id)
    borrow_book(db_session,added_user.id,added_book_2.id)
    history = get_user_history(db_session,added_user.id)
    assert isinstance(history,str)
    assert "Harry Potter" in history
    assert "Narnia" in history
    assert history.count('Status : NOT RETURNED')==2
    
    return_book(db_session,added_book_2.id)
    history = get_user_history(db_session,added_user.id)

    assert history.count('Status : RETURNED') ==1
    assert history.count('Status : NOT RETURNED')==1

    
