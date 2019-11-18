from app.modules.user import User,db as udb
from app.data_handle.admin_user import data_handel
from app.modules.talk import db as tdb
from app.data_handle.admin_talk import data_handel_talk

class DataQuery:

    def __type_verify(self,types):
        if types == 'user':
            return self.__query_user()
        elif types == 'talk':
            return self.__query_talk()

    @staticmethod
    def __query_user():
        user = User.query.all()
        data = data_handel(user)
        udb.session.close()
        return data

    @staticmethod
    def __query_talk():
        sql = '''
            select
            a.id,a.username,a.main,c.`name`,b.`name`
            from
            movie_talk as a,classic_movie as c,user as b
            WHERE
            a.mid = c.id and
            (a.cat = 'classic' or a.cat = 'soon' or a.cat = 'release') and
            b.username = a.username
        '''
        data = tdb.session.execute(sql)
        tdb.session.close()
        data = data_handel_talk(data.fetchall())
        return data

    def run(self,types):
        return self.__type_verify(types)