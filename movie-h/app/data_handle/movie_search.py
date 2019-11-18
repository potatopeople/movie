
class MovieSearchHandel:

    def __init__(self, movie):
        self.movie = movie

    @staticmethod
    def __movie_handelO(movie):
        anchor = {'data': [], 'total': '', 'pageSum': ''}
        if len(movie.items):
            for item in movie.items:
                anchor['data'].append({
                    'id':item.id,'name':item.name,'elname':item.elname,
                    'img':item.img,'cat':item.cat,'score':item.score,
                    'catgory':item.catgory,'address':item.address,
                    'releaseTime':item.releaseTime,'play_cat':item.play_cat
                })
            anchor['total'] = movie.total
            anchor['currenPage'] = movie.page
            anchor['pageSum'] = movie.pages
            return anchor
        else:
            return []

    def run(self):
        return self.__movie_handelO(self.movie)