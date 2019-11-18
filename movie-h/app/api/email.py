from .blueprint import email
from flask import request, jsonify
from app.public.returnResponse import formats
from app.libs.email import EmailVerify
from .. import cache

@email.route('/api/emailVerify', methods=['POST'])
@cache.cached(timeout=10)
def email_post():
    emails = EmailVerify(request.json)
    print("接收",request.json)
    if emails.type_prompt():
        print("返回：",emails.prompt)
        return jsonify(formats(emails.prompt, 200, {}))
    else:
        print("返回：", emails.prompt)
        return jsonify(formats(emails.prompt, 500, {}))


