import pytest
from unittest.mock import MagicMock
from app.funcs.borrow import borrow_book
from app.funcs.return_book import return_book

def test_borrow_exception(db_session,added_user,added_book):
    db_session.commit = MagicMock(side_effect =Exception('DB connection failed'))
    
    result =borrow_book(db_session,added_user.id,added_book.id)
    assert 'DB connection failed' in str(result)

def test_return_exception(db_session,borrowed_book):
    db_session.commit = MagicMock(side_effect =Exception('DB connection failed'))

    result = return_book(db_session,borrowed_book.id)
    assert 'DB connection failed' in str(result)