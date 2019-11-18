from app.mysqls.movie_list import MovieListy

class MovieList:
    json = ''
    prompt = ''
    data = ''

    def __init__(self, json):
        self.json = json

    def verify_filed(self):
        if 'orderBy' and 'showType' and 'page' and 'pageSize' in self.json.keys():
            movie = MovieListy(self.json)
            if movie.check_catgory():
                self.data = movie.anchor
                self.prompt = movie.prompt
                return True
            else:
                self.prompt = movie.prompt
                return False
        else:
            self.prompt = '字段错误'
            return False