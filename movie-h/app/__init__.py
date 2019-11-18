from flask import Flask
from app.modules.imaegs import db
from app.modules.performer import db
from app.modules.movie_catgory import db
from app.modules.release import db
from app.modules.soon import db
from app.modules.classic import db
from app.modules.classic_top import db
from app.modules.score_top import db
from app.modules.soon_top import db
from app.modules.city import db
from app.modules.cinemas import db
from app.modules.cinemas_movie import db
from app.modules.seat import db
from app.modules.user import db
from app.modules.seat_order import db
from app.modules.admin import db
from app.modules.talk import db
from flask_cache import Cache
from flask_cors import *

cache = Cache()

def create_app():
    global cache
    app = Flask(__name__)  # 实例化Flask
    app.config.from_object('app.secure')  # 配置文件模块路径
    app.config.from_object('app.setting')
    cache.init_app(app)
    CORS(app, supports_credentials = True)
    register_blueprint(app)
    db.init_app(app) # 注册到app中
    db.create_all(app=app) # 调用映射数据库
    return app

def register_blueprint(apps):
    from app.api.login import login
    from app.api.email import email
    from app.api.register_user import register_user
    from app.api.verify_token import verify_token
    from app.api.movie_list import movie_list
    from app.api.movie_catgory import movie_catgory
    from app.api.movie_top import movie_top
    from app.api.movie_search import movie_search
    from app.api.address import address
    from app.api.cinemas import cinemas
    from app.api.cinemas_movie import cinemas_movie
    from app.api.movie_cinemas import movie_cinemas
    from app.api.seat import movie_seat
    from app.api.order import movie_order
    from app.api.send_code import send_code
    from app.api.get_order import get_order
    from app.api.pay_api import pay_api
    from app.api.admin_login import admin_login
    from app.api.pay_end import pay_end
    from app.api.save_user import save_user
    from app.api.send_talk import send_talk
    from app.api.query_talk import query_talk
    from app.api.admin_query import admin_query
    from app.api.drop_talk import drop_talk
    apps.register_blueprint(login)
    apps.register_blueprint(email)
    apps.register_blueprint(register_user)
    apps.register_blueprint(verify_token)
    apps.register_blueprint(movie_list)
    apps.register_blueprint(movie_catgory)
    apps.register_blueprint(movie_top)
    apps.register_blueprint(movie_search)
    apps.register_blueprint(address)
    apps.register_blueprint(cinemas)
    apps.register_blueprint(cinemas_movie)
    apps.register_blueprint(movie_cinemas)
    apps.register_blueprint(movie_seat)
    apps.register_blueprint(movie_order)
    apps.register_blueprint(send_code)
    apps.register_blueprint(get_order)
    apps.register_blueprint(pay_api)
    apps.register_blueprint(admin_login)
    apps.register_blueprint(pay_end)
    apps.register_blueprint(save_user)
    apps.register_blueprint(send_talk)
    apps.register_blueprint(query_talk)
    apps.register_blueprint(admin_query)
    apps.register_blueprint(drop_talk)