from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from flask import current_app
from app.data_handle.movie_cinemas import data_handel


def query_cinemas(mid,cid):
    engine = create_engine(current_app.config['SQLALCHEMY_DATABASE_URI'])
    Session = sessionmaker(bind=engine)
    session = Session()
    data_sql = """
        SELECT
        a.id,a.city_id,a.cinemas_id,a.`name`,a.address,a.money
        FROM cinemas AS a,cinemas_movie AS b
        WHERE
        b.movie_id = %s and b.cinemas_id = a.cinemas_id AND a.city_id = %s
    """%(mid,cid)
    data = session.execute(data_sql)
    data = data_handel(data.fetchall())
    session.close()
    return data