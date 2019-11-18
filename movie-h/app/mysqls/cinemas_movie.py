from app.modules.cinemas_movie import db as cdb, CinemasMovie
from app.data_handle.cinemas_movie import DataHandel

def movie_data(cid,nid,money):
    try:
        data = CinemasMovie.query.filter(
            CinemasMovie.city_id==cid,
            CinemasMovie.cinemas_id == nid
        ).all()
        cdb.session.close()
        run = DataHandel()
        data = run.data_handel(data,money)
        return data
    except Exception as e:
        print('请求错误:',e)
        return []