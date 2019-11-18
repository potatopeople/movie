from app.modules.talk import MovieTalk,db as mdb
import time

def add_talk(name,datas):
    try:
        talk = MovieTalk(main=datas['main'],username=name,cat=datas['cat'],mid=datas['mid'],time=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
        mdb.session.add(talk)
        mdb.session.commit()
        mdb.session.close()
        return True
    except Exception as e:
        return False