# from .blueprint import cache_order
# from .. import cache
# from app.public.returnResponse import formats
# from flask import jsonify
#
#
# @cache_order.route('/api/movie/cache_order/<phone>',methods=['GET'])
# @cache.cached(timeout=60) #缓存的数据
# def get_order(phone):
#     data = cache.get('movie_order')
#     return jsonify(formats('OK!', 200, data))
#
# @cache_order.before_request #缓存前的处理
# def handel_before():
#     try:
#         data = cache.get('movie_order')
#         print(cache.get('order'))
#         if not data:
#             return jsonify(formats('订单为空!', 200, []))
#     except TypeError as e:
#         print('过期：', e)
#         return jsonify(formats('订单已过期，请重新选择', 300, []))
