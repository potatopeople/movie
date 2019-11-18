from alipay import AliPay
from app.modules.seat_order import SeatOrder,db as sdb
import time,datetime
from app.mysqls.user_order import OderData

def time_check(batch,id_card):
    orders = SeatOrder.query.filter(
        SeatOrder.batch == batch
    ).first()
    if orders:
        time_tup = time.localtime(time.time())
        time_tup = time.strftime('%Y-%m-%d %H:%M:%S', time_tup)
        date2 = datetime.datetime.strptime(orders.buy_date, "%Y-%m-%d %H:%M:%S")
        date1 = datetime.datetime.strptime(time_tup, "%Y-%m-%d %H:%M:%S")
        d = date1 - date2
        if d.seconds >= 960:
            sdb.session.close()
            drop_os = OderData()
            drop_os.drop(batch)
            return False
        else:
            id_ca = SeatOrder.query.filter(
                SeatOrder.batch == batch
            ).all()
            for item in id_ca:
                item.id_card = id_card
                sdb.session.commit()
            sdb.session.close()
            return True
    else:
        sdb.session.close()
        return False

app_private_key_string = open("app/alipay/ying_yong_si_yao.txt").read()
alipay_public_key_string = open("app/alipay/zhi_fu_bao_gong_yao.txt").read()
app_private_key_string = '-----BEGIN RSA PRIVATE KEY-----\n'+ app_private_key_string +'\n-----END RSA PRIVATE KEY-----'
alipay_public_key_string = '-----BEGIN RSA PRIVATE KEY-----\n'+ alipay_public_key_string +'\n-----END RSA PRIVATE KEY-----'

APP_ID = '2016101700708456'
NOTIFY_URL = "http://localhost:8080/"
alipays = AliPay(
        appid=APP_ID,
        app_notify_url=None,
        app_private_key_string=app_private_key_string,
        alipay_public_key_string=alipay_public_key_string,  # 支付宝的公钥，验证支付宝回传消息使用，不是你自己的公钥,
        sign_type="RSA2",  # RSA 或者 RSA2
        debug=True  # 默认False ,若开启则使用沙盒环境的支付宝公钥
    )

def run(money,batch,id_card):
    if time_check(batch,id_card):
        ali = alipays
        order_string = ali.api_alipay_trade_page_pay(
            subject="土豆电影网", #订单主题
            out_trade_no= batch,#订单号
            total_amount=money, #金额
            return_url='http://localhost:8080/', #支付完成跳转的页面
            notify_url= 'http://118.113.10.124:5050/api/pay/success' #支付完成请求的url
        )
        return 'https://openapi.alipaydev.com/gateway.do?' + order_string
    else:
        return False