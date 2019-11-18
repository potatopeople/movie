from app.modules.user import User,db as udb
from sqlalchemy import or_
from app.data_handle.user_intro import user_intro

def query_user(phone='',token=''):
    user = User.query.filter(
        or_(
            User.username == phone,
            User.token == token
        )
    ).first()
    udb.session.close()
    return user_intro(user)