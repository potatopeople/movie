from .blueprint import pay_end
from flask import request,jsonify
from app.libs.notify_verify import NotifyVerify

@pay_end.route('/api/pay/success',methods=['POST'])
def pay_success():
    try:
        print('支付完成')
        data = request.form.to_dict()
        run = NotifyVerify()
        tf = run.run(data)
        if tf:
            return jsonify('success')
        else:
            return jsonify('fail')
    except Exception as e:
        return jsonify('fail')