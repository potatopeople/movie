

DEBUG = True

#配置数据库:mysqls、驱动、用户名、密码、ip地址、端口号、数据库名

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@localhost:3306/movie'

#redis配置
CACHE_TYPE = 'redis'
# 主机
CACHE_REDIS_HOST = '127.0.0.1'
# 端口
CACHE_REDIS_PORT = 6379
# 数据库
CACHE_REDIS_DB = 1
