from app.http.zhi_fu_bao import alipays
from app.modules.seat_order import SeatOrder,db as sdb


class NotifyVerify:

    @staticmethod
    def __rsa_check(data):
        signature = data.pop("sign")
        success = alipays.verify(data, signature)
        if success and data["trade_status"] in ("TRADE_SUCCESS", "TRADE_FINISHED"):
            return True
        else:
            return False

    @staticmethod
    def __query_sql(data):
        #trade_no = data['trade_no']  # 支付宝交易号
        out_trade_no = data['out_trade_no']  # 订单号
        print(out_trade_no)
        #trade_status = data['trade_status']  # 交易状态
        #total_amount = data['total_amount']  # 支付价格
        orders = SeatOrder.query.filter(
                SeatOrder.batch == out_trade_no
            ).all()
        if orders:
            for item in orders:
                item.tf = '2'
        sdb.session.commit()
        sdb.session.close()

    def run(self,data):
        if self.__rsa_check(data):
            self.__query_sql(data)
            return True
        else:
            return False