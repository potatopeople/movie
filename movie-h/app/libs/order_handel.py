from app.modules.user import User,db as udb
from app.modules.seat_order import SeatOrder,db as sdb
import re
from app.mysqls.user_order import OderData
from app.mysqls.drop_order import DropOrder

class OrderHandel:

    prompt = ''

    @staticmethod
    def __check_token(token):
        try:
            basic = re.findall('Basic\s(.*)',token,re.S)[0]
            user = User.query.filter(User.token == basic).first()
            udb.session.close()
            if user:
                return user.username
            else:
                return False
        except Exception as error:
            print(error)
            return False

    @staticmethod
    def __query_order(phone,types): #查询用户订单
        orders = SeatOrder.query.filter(
            SeatOrder.phone == phone,
            SeatOrder.tf == types
        ).all()
        sdb.session.close()
        if orders:
            return orders
        else:
            return False

    def run(self,token,types,date):
        phone = self.__check_token(token)
        if phone:
            if types != '1':
                data = self.__query_order(phone,types)
                if data:
                    orders = OderData()
                    data = orders.run(data,date)
                    if data:
                        return data
                    else:
                        self.prompt = '订单已过期'
                        return False
                else:
                    self.prompt = '没有您的订单信息'
                    return False
            else:
                run = DropOrder()
                if run.run(phone):
                    return True
                else:
                    self.prompt = '数据库发生异常'
                    return False
        else:
            self.prompt = '请重新登录账户！'
            return False