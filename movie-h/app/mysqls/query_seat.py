from app.modules.seat import Seat,db as sdb
from app.data_handle.seat import DataHandel

def seat_data(cid,nid,mid):
    try:
        # data = Seat.query.filter(
        #     Seat.city_id.between(cid,cid),
        #     Seat.cinemas_id.between(nid,nid),
        #     Seat.movie_id.between(mid,mid)
        # ).all()
        sql = '''
        SELECT * FROM `seat` WHERE
        city_id BETWEEN %s and %s and
        cinemas_id between %s and %s and
        movie_id between %s and %s
        ''' % (cid,cid,nid,nid,mid,mid)
        seat = sdb.session.execute(sql)
        sdb.session.close()
        handel = DataHandel()
        data = handel.run(seat.fetchall())
        return data
    except Exception as e:
        print(e,'查询错误')
        return ['查询错误']