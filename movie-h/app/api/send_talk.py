from .blueprint import send_talk
from flask import jsonify,request
from app.public.returnResponse import formats
from app.libs.send_talk import SendTalk

@send_talk.route('/api/movie/send_talk',methods=['PUT'])
def user_talk():
    try:
        pater = request.json
        token = request.headers.get('Authorization')
        run = SendTalk()
        data = run.run(token,pater)
        if data:
            return jsonify(formats('ok!',200,[]))
        else:
            return jsonify(formats(run.prompt,300,[]))
    except Exception as e:
        return jsonify(formats(e,500,[]))