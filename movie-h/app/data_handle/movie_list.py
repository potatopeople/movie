import re


class DataHandle:

    def __init__(self, type, data, orderBy):
        if type == 'release':
            self.__release_data(data, orderBy)
        elif type == 'soon':
            self.__soon_data(data, orderBy)
        elif type == 'classic':
            self.__classic_data(data, orderBy)

    def __release_data(self, data, orderBy):
        anchor = {'data': [], 'total': '', 'pageSum': ''}
        for item in data.items:
            anchor['data'].append(
                {'id': item.id, 'rid': item.rid, 'name': item.name, 'elname': item.elname,
                 'img': item.img, 'cat': item.cat, 'score': item.score, 'catgory': item.catgory,
                 'address': item.address, 'playTime': item.playTime, 'releaseTime': item.releaseTime,
                 'ticketRank': item.ticketRank, 'introduction': item.introduction,'play_cat':item.play_cat}
            )
        anchor['total'] = data.total
        anchor['currenPage'] = data.page
        anchor['pageSum'] = data.pages
        if orderBy == '1':
            anchor['data'] = sorted(anchor['data'],key=self.__ticket_orderBy,reverse=True)
        self.anchor = anchor

    @staticmethod
    def __ticket_orderBy(data):  #按照票房排序
        if '暂无' in data['ticketRank']:
            num = 0.0
            number = float(num)
        else:
            num = re.findall('\d*\.*\d*', data['ticketRank'])
            number = float(num[0])
        if '亿' in data['ticketRank']:
            number *= 100000000
        elif '万' in data['ticketRank']:
            number *= 10000
        elif not number:
            number = 0
        return number

    def __soon_data(self, data, orderBy):
        anchor = {'data': [], 'total': '', 'pageSum': ''}
        for item in data.items:
            anchor['data'].append(
                {'id': item.id, 'sid': item.sid, 'name': item.name, 'elname': item.elname,
                 'img': item.img, 'cat': item.cat, 'people': item.people, 'catgory': item.catgory,
                 'address': item.address, 'playTime': item.playTime, 'releaseTime': item.releaseTime,
                 'ticketRank': item.ticketRank, 'introduction': item.introduction,'play_cat':item.play_cat}
            )
        anchor['total'] = data.total
        anchor['currenPage'] = data.page
        anchor['pageSum'] = data.pages
        self.anchor = anchor

    def __classic_data(self, data, orderBy):
        anchor = {'data': [], 'total': '', 'pageSum': ''}
        for item in data.items:
            anchor['data'].append(
                {'id': item.id,'cid': item.cid, 'name': item.name,'elname': item.elname,
                 'img': item.img,'cat': item.cat,'score': item.score,'catgory': item.catgory,
                 'address': item.address,'playTime': item.playTime,'releaseTime': item.releaseTime,
                 'ticketRank': item.ticketRank,'introduction': item.introduction,'play_cat':item.play_cat}
            )
        anchor['total'] = data.total
        anchor['currenPage'] = data.page
        anchor['pageSum'] = data.pages
        self.anchor = anchor