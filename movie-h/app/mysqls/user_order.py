from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from flask import current_app
from app.data_handle.user_order import order_handel
import time
from app.modules.seat_order import SeatOrder,db as sdb
import datetime

class OderData:

    o_id = ''
    s_id = ''
    s_oid = ''


    def __order_id(self,datas):
        for item in datas:
            self.o_id = int(item.id)
            break

    def __seat_id(self,datas):
        anchor = ''
        for x, item in enumerate(datas):
            if x >= 1:
                anchor += ',' + str(item.sid)
            else:
                anchor += str(item.sid)
        self.s_id = '(' + anchor + ')'
        self.s_oid = datas[0].sid

    @property
    def order_id_(self):
        return self.s_oid

    def __time_flow(self, datas):
        time_tup = time.localtime(time.time())
        time_tup = time.strftime('%Y-%m-%d %H:%M:%S', time_tup)
        date2 = datetime.datetime.strptime(datas[0].buy_date, "%Y-%m-%d %H:%M:%S")
        date1 = datetime.datetime.strptime(time_tup, "%Y-%m-%d %H:%M:%S")
        d = date1 - date2
        if d.seconds >= 960:
            self.drop(datas['batch'])
            return False
        else:
            return True

    @staticmethod
    def drop(batch=''):
        orders = SeatOrder.query.filter(
            SeatOrder.batch == batch
        ).all()
        if orders:
            for item in orders:
                item.tf = '1'
                sdb.session.commit()
        sdb.session.close()


    def __query_seat_data(self):
        engine = create_engine(current_app.config['SQLALCHEMY_DATABASE_URI'])
        Session = sessionmaker(bind=engine)
        session = Session()
        data_sql = """
            SELECT
            b.name as cinemas_name,seat.id,a.movie_img,a.name as movie_name,a.money,a.room,seat.row,seat.clumn,seat_order.buy_date,seat_order.tf,seat_order.batch
            from
            cinemas_movie as a,cinemas as b,seat,seat_order
            WHERE
            a.city_id = ( SELECT city_id from seat WHERE id = (SELECT sid from seat_order WHERE id = %s)) and
            a.cinemas_id = ( SELECT cinemas_id from seat WHERE id = (SELECT sid from seat_order WHERE id = %s)) and
            a.movie_id = ( SELECT movie_id from seat WHERE id = (SELECT sid from seat_order WHERE id = %s)) and
            a.city_id = b.city_id and
            a.cinemas_id = b.cinemas_id and
            seat.id in %s and
            seat_order.sid = %s
        """ % (self.o_id,self.o_id,self.o_id,self.s_id,self.order_id_)
        data = session.execute(data_sql)
        session.close()
        return data.fetchall()

    def run(self, datas,date):
        self.__order_id(datas)
        self.__seat_id(datas)
        if self.__time_flow(datas):
            seat_data = self.__query_seat_data()
            if seat_data:
                data = order_handel(seat_data,date)
                return data
            else:
                return False
        else:
            return False