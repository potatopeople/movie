from app.modules.user import User,db as udb
from app.data_handle.user_talk import data_handel

def query_talks(datas):
    try:
        sql = '''
            select
            b.id,a.name,a.avatar,b.main,b.time
            from
            user as a,movie_talk as b
            where
            a.username = b.username and b.mid = %s and b.cat = %s
        '''% (int(datas['mid']),"'"+str(datas['cat'])+"'")
        data = udb.session.execute(sql)
        udb.session.close()
        datas = data_handel(data.fetchall())
        return datas
    except Exception as e:
        print(e)
        return False