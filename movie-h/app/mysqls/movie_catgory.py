from app.modules.movie_catgory import MovieCatgory,db as cdb


def getData():
    try:
        data = MovieCatgory.query.all()
        cdb.session.close()
        anchor = {
            'catgorys': [],
            'years': [],
            'region': []
        }
        for item in data:
            if item.catgory:
                anchor['catgorys'].append(item.catgory)
            if item.years:
                anchor['years'].append(item.years)
            if item.region:
                anchor['region'].append(item.region)
        return [200, anchor]
    except Exception as e:
        print(e)
        return [300, '查询失败']