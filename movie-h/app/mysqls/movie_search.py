from app.modules.classic import ClassicMovie,db as cdb
from app.data_handle.movie_search import MovieSearchHandel


class MovieSearch:

    def __init__(self, data):
        self.keywords = '%' + data['keywords'] + '%'
        self.page = data['page']
        self.pageSize = data['pageSize']

    def __query_data(self):
        try:
            movie = ClassicMovie.query.filter(
                ClassicMovie.name.like(self.keywords)
            ).paginate(
                page=int(self.page), per_page=int(self.pageSize), max_per_page=30, error_out=True
            )
            cdb.session.close()
            return self.__handel_data(movie)
        except Exception as e:
            print(e)
            self.prompt = '查询失败'
            return False

    def __handel_data(self, movie):
        data = MovieSearchHandel(movie)
        data = data.run()
        self.data = data
        return True

    def run(self):
        return self.__query_data()