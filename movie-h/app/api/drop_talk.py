from .blueprint import drop_talk
from flask import jsonify,request
from app.public.returnResponse import formats
from app.mysqls.drop_talk import talk_drop


@drop_talk.route('/api/admin/talk/drop/<tid>',methods=['DELETE'])
def admin_talk(tid):
    try:
        tf = talk_drop(tid,request.headers.get('Authorization'))
        if tf:
            return jsonify(formats('ok!',200,[]))
        else:
            return jsonify(formats('删除失败！',500,[]))
    except Exception as e:
        return jsonify(formats(e,500,[]))
