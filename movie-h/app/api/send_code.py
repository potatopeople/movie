from .blueprint import send_code
from app.public.returnResponse import formats
from flask import jsonify,request
from app.http.send_phone import SendPhone


@send_code.route('/api/send_code/<phone>',methods=['GET'])
def sendCode(phone):
    try:
        run = SendPhone()
        code = run.run(phone,request.args['type'],request.args['code'])
        if code:
            if not request.args['code']:
                print(code)
                return jsonify(formats('OK!', 200, {'token': run.token}))
            else:
                return jsonify(formats('OK!', 200, code))
        else:
            return jsonify(formats(run.prompt, 300, []))
    except Exception as e:
        print('错误：',e)
        return jsonify(formats('服务器错误！', 500, []))
