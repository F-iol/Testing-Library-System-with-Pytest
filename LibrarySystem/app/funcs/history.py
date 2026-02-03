from app.classes.loan import Loan
from app.classes.user import User


def get_user_history(db,user_id):
    user = db.get(User,user_id)
    if not user:
        return 'Error: User not found'

    history =db.query(Loan).filter(Loan.user_id == user_id).all()
    if not history:
        return f'History for {user.user_name} is empty'
    
    text= ['History of borrows \n']
    for loan in history:
        status = "RETURNED" if loan.date_of_return else "NOT RETURNED"
        text.append(f'Title : {loan.book.title:20} | Status : {status} \n')
    return ''.join(text)