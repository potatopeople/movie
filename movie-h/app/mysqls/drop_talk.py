from app.modules.talk import MovieTalk,db as tdb
from app.modules.admin import Admin,db as adb
import re

def talk_drop(tid,token):
    try:
        check_token(token)
        talk = MovieTalk.query.filter(
            MovieTalk.id == tid
        ).first()
        tdb.session.delete(talk)
        tdb.session.commit()
        tdb.session.close()
        return True
    except Exception as e:
        return False

def check_token(token):
    token = re.findall('Basic\s(.*)', token, re.S)[0]
    if token:
        user = Admin.query.filter(
            Admin.token == token
        ).first()
        adb.session.close()
        if user:
            return True
        else:
            return False
    else:
        return False