from app.modules.cinemas import db as cdb, Cinemas
from app.data_handle.cinemas_list import data_handel

def cinemas_list(cid):
    try:
        data = Cinemas.query.filter(Cinemas.city_id==cid).all()
        cdb.session.close()
        data = data_handel(data)
        return data
    except Exception as e:
        print('请求错误:',e)
        return []