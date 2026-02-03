import pytest
from app.funcs.borrow import borrow_book

@pytest.mark.parametrize('u_id,b_id,expected',[(999,1,'user does not exist'),(1,999,'book is unavailable')])
def test_borrow_not_found(db_session,added_book,added_user,u_id,b_id,expected):
    user_id = added_user.id if u_id==1 else u_id
    book_id = added_book.id if b_id ==1 else b_id

    result = borrow_book(db_session,user_id,book_id)
    assert expected in result.lower()