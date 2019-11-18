from app.modules.seat_order import SeatOrder,db as odb
from app.modules.seat import Seat,db as sdb


class DropOrder:

    seat_id = []

    def __drop_order(self, phone):
        try:
            orders = SeatOrder.query.filter(
                SeatOrder.phone == phone,
                SeatOrder.tf == '0'
            ).all()
            for item in orders:
                item.tf = '1'
                self.seat_id.append(item.sid)
                odb.session.commit()
            odb.session.close()
            return True
        except Exception as e:
            print(e)
            return False

    def __seat_drop(self,):
       try:
           seat = Seat.query.filter(
               Seat.id.in_(self.seat_id)
           ).all()
           for item in seat:
               item.chose = '0'
               sdb.session.commit()
           sdb.session.close()
           return True
       except Exception as e:
            print(e)
            return False

    def run(self,phone):
        if self.__drop_order(phone):
            if self.__seat_drop():
                return True
            else:
                return False