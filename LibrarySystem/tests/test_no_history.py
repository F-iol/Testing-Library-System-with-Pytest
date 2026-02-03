import pytest
from app.funcs.history import get_user_history
from app.funcs.borrow import borrow_book

@pytest.mark.parametrize('user_key,excepted_content',[('with_history','Harry Potter'),('empty_1','is empty'),('empty_2','is empty'),('NotExisting','not found')])
def test_no_history(db_session,get_test_history,added_book,user_key,excepted_content):
    if user_key == 'NotExisting':
        user_id = 999
    else:
        current_user = get_test_history[user_key]
        user_id =current_user.id

    if user_key =='with_history':
        borrow_book(db_session,user_id,added_book.id)

    result =get_user_history(db_session,user_id)

    assert excepted_content in result