from app.modules.soon import SoonMovie,db as sdb
from app.modules.release import ReleaseMovie,db as rdb
from app.modules.classic import ClassicMovie,db as cdb
from app.data_handle.movie_list import DataHandle
import time


class MovieListy:

    page = ''
    pageSize = ''
    orderBy = ''
    showType = ''
    prompt = ''
    anchor = ''
    val1 = '99999999'
    val2 = '0'

    def __init__(self, data):
        self.showType = data['showType']
        self.page = data['page']
        self.pageSize = data['pageSize']
        self.orderBy = data['orderBy']
        self.catgory = data['catgory']
        self.years = data['region']
        self.region = data['years']

    def _filter(self):
        if self.catgory == 'all':
            self.cat = '%'
        else:
            self.cat = '%'+self.catgory+'%'
        if self.years == 'all':
            self.year = '%'
        else:
            self.year = self._year_filter(self.years)
        if self.region == 'all':
            self.reg = '%'
        else:
            self.reg = '%'+self.region+'%'

    def _year_filter(self, years):
        if '以后' in years:
            self.val2 = str(int(years[0:4]) + 1)
            return '%'
        elif '年代' in years:
            return '19' + years[0:1] + '%'
        elif '-' in years or '_' in years:
            self.val1 = str(int(years[0:4]) + 1)
            self.val2 = years[5:9]
            return '%'
        elif '更早' in years:
            self.val1 = '1970'
            pass
        else:
            return years + '%'

    def check_catgory(self):
        self._filter()
        if self.showType == 'soon':
            return self.__soon_movie()
        elif self.showType == 'release':
            return self.__release_movie()
        elif self.showType == 'classic':
            return self.__classic_movie()
        else:
            self.prompt = '查询类型错误'
            return False

    def _order_by(self, table):
        if self.orderBy == '0':
            if (table == ReleaseMovie) or (table == ClassicMovie):
                return table.score.desc()
            elif table == SoonMovie:
                return table.people.desc()
        elif self.orderBy == '2':
            if (table == ReleaseMovie) or (table == ClassicMovie):
                return table.releaseTime.desc()
            elif table == SoonMovie:
                return table.releaseTime.desc()
        elif (self.orderBy == '1') and (table == SoonMovie):
            return table.releaseTime.asc()

    def __classic_movie(self):
        try:
            order = self._order_by(ClassicMovie)
            #date = time.strftime('%Y', time.localtime(time.time()))
            movie = ClassicMovie.query.filter(
                #ClassicMovie.releaseTime < date,
                ClassicMovie.catgory.like(self.cat),
                ClassicMovie.address.like(self.reg),
                ClassicMovie.releaseTime.like(self.year),
                ClassicMovie.releaseTime < self.val1,
                ClassicMovie.releaseTime >= self.val2
            ).order_by(order).paginate(
                page=int(self.page), per_page=int(self.pageSize), max_per_page=30, error_out=True
            )
            cdb.session.close()
            data = DataHandle('classic', movie, self.orderBy)
            self.anchor = data.anchor
            return True
        except Exception as e:
            print(e)
            self.prompt = '查询失败'
            return False

    def __release_movie(self):
        try:
            order = self._order_by(ReleaseMovie)
            movie = ReleaseMovie.query.filter(
                ReleaseMovie.catgory.like(self.cat),
                ReleaseMovie.address.like(self.reg),
                ReleaseMovie.releaseTime.like(self.year),
                ReleaseMovie.releaseTime < self.val1,
                ReleaseMovie.releaseTime >= self.val2
            ).order_by(order).paginate(
                page=int(self.page), per_page=int(self.pageSize), max_per_page=30, error_out=True
            )
            rdb.session.close()
            data = DataHandle('release', movie, self.orderBy)
            self.anchor = data.anchor
            return True
        except Exception as e:
            print(e)
            self.prompt = '查询失败'
            return False

    def __soon_movie(self):
        try:
            order = self._order_by(SoonMovie)
            dateFormat = '%'
            date = time.strftime('%Y', time.localtime(time.time()))
            if self.orderBy == '1':
                date = time.strftime('%Y-%m-%d', time.localtime(time.time()))
                dateFormat = '%-%-%'
            movie = SoonMovie.query.filter(
                SoonMovie.releaseTime.like(dateFormat),
                SoonMovie.releaseTime > date,
                SoonMovie.catgory.like(self.cat),
                SoonMovie.address.like(self.reg),
                SoonMovie.releaseTime.like(self.year),
                SoonMovie.releaseTime < self.val1,
                SoonMovie.releaseTime >= self.val2
            ).order_by(order,SoonMovie.people.desc()).paginate(
                page=int(self.page),per_page=int(self.pageSize),max_per_page=30,error_out=True
            )
            sdb.session.close()
            data = DataHandle('soon', movie, self.orderBy)
            self.anchor = data.anchor
            return True
        except Exception as e:
            print(e)
            self.prompt = '查询失败'
            return False
