from app.mysqls.movie_top import MovieRank


class MovieTop:

    data = ''
    prompt = ''

    def __init__(self, data):
        self.data = data

    def verify(self):
        if 'type' and 'page' and 'pageSize' in self.data.keys():
            data = MovieRank(self.data['type'], self.data['page'], self.data['pageSize'])
            self.data = data.anchor
            return True
        else:
            self.prompt = '字段错误'
            return False