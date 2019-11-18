from app.modules.classic_top import ClassicTop,db as cdb
from app.modules.score_top import ScoreTop,db as sdb
from app.modules.soon_top import SoonTop,db as odb

class MovieRank:

    def __init__(self, type, page, pageSize):
        self.__type_verify(type, page, pageSize)

    def __type_verify(self, type, page, pageSize):
        if type == 'classic':
            self.__query_data(ClassicTop, cdb, page, pageSize, type)
        elif type == 'release':
            self.__query_data(ScoreTop, sdb, page, pageSize, type)
        elif type == 'soon':
            self.__query_data(SoonTop, odb, page, pageSize, type)

    def __query_data(self, table, cursor, page, pageSize,type):
        movie = table.query.order_by(table.rank.asc()).paginate(
                page=int(page), per_page=int(pageSize), max_per_page=30, error_out=True
            )
        cursor.session.close()
        self.__filter_data(movie, type)

    def __filter_data(self, data, type):
        anchor = {'data': [], 'total': '', 'pageSum': ''}
        if type == 'classic':
            self.__classic_data(anchor, data)
        elif type == 'release':
            self.__release_data(anchor, data)

    def __release_data(self, parent, children):
        for item in children.items:
            parent['data'].append(
                {'id': item.id, 'rank': item.rank, 'name': item.name,
                 'star': item.star, 'score': item.score,
                 'releaseTime': item.releaseTime, 'img': item.img}
            )
        parent['total'] = children.total
        parent['currenPage'] = children.page
        parent['pageSum'] = children.pages
        self.anchor = parent

    def __classic_data(self, parent, children):
        for item in children.items:
            parent['data'].append(
                {'id': item.id, 'rank': item.rank, 'name': item.name,
                 'star': item.star, 'score': item.score,
                 'releaseTime': item.releaseTime, 'img': item.img}
            )
        parent['total'] = children.total
        parent['currenPage'] = children.page
        parent['pageSum'] = children.pages
        self.anchor = parent