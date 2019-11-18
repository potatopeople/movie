from app.modules.seat import Seat,db as sdb
from app.modules.seat_order import SeatOrder,db as odb
from app.modules.user import User,db as udb
import time


class MovieOrder:

    @staticmethod
    def __query_seat(seat_id):
        try:
            seat = Seat.query.filter(
                Seat.id.in_(seat_id)
            ).all()
            sdb.session.close()
            return seat
        except Exception as e:
            print('座位查询错误:',e)

    @staticmethod
    def __buy_seat(seat_id): #选择座位
        try:
            seat = Seat.query.filter(
                Seat.id.in_(seat_id)
            ).all()
            for item in seat:
                item.chose = 2
            sdb.session.commit()
            sdb.session.close()
        except Exception as e:
            print('购买错误',e)

    @staticmethod
    def __create_order(seat_id, phone): #生成订单信息
        try:
            for item in seat_id:
                time_tup = time.localtime(time.time())
                cur_time = time.strftime('%Y-%m-%d %H:%M:%S', time_tup)
                orders = SeatOrder(sid=int(item),phone=phone,buy_date=str(cur_time),tf='0',batch=time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))+phone)
                odb.session.add(orders)
                odb.session.commit()
            odb.session.close()
            return True
        except Exception as e:
            print('订单生成失败:', e)
            return False

    @staticmethod
    def __check_order(phone):
        orders = SeatOrder.query.filter(
            SeatOrder.phone == phone,
            SeatOrder.tf == '0'
        ).all()
        if len(orders):
            return False
        else:
            return True

    @staticmethod
    def __seat_handel(seat_data): #检查是否有已被购买的座位
        anchor = []
        for item in seat_data:
            if item.chose == '2' or item.chose == 2:
                anchor.append(
                    {'id':item.id,'row':item.row,'clumn':item.clumn}
                )
        return anchor

    @staticmethod
    def __seat_data_filter(data):
        anchor = []
        for item in data:
            anchor.append(item['sid'])
        return anchor

    @staticmethod
    def __get_phone(token):
        phone = User.query.filter(User.token == token).first()
        udb.session.close()
        phone = phone.username
        return phone


    def run(self,data, token):
        phone = self.__get_phone(token)
        if phone:
            seat_id = self.__seat_data_filter(data)
            if self.__check_order(phone):
                seat_data = self.__query_seat(seat_id)
                seat_data = self. __seat_handel(seat_data)
                if len(seat_data): #有被购买的座位
                    return [2,seat_data]
                else:
                    self.__buy_seat(seat_id)
                    if self.__create_order(seat_id,phone):
                        return [0,[]]
                    else:
                        return [1,[]]
            else:
                return [3, []]
        else:
            return [4,[]]