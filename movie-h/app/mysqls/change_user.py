from app.modules.user import User,db as udb
import re

def changes_data(token,data):
    try:
        basic = re.findall('Basic\s(.*)', token, re.S)[0]
        if basic:
            user = User.query.filter(
                User.token == basic
            ).first()
            user.name = data['name']
            user.sex = data['sex']
            udb.session.commit()
            udb.session.close()
            return True
        else:
            return False
    except Exception as e:
        print(e)
        return False