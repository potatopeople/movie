from datetime import datetime,timedelta
import random


class DataHandel:

    def data_handel(self, data,money):
        anchor = {'cinemas_img':'','data':[]}
        for item in data:
            anchor['cinemas_img'] = item.cinemas_img
            curren_date = self.__get_date(item.play_time)
            anchor['data'].append(
                {'id': item.id, 'city_id': item.city_id, 'cinemas_id': item.cinemas_id,
                 'name': item.name, 'score': item.score, 'play_time': item.play_time,
                 'catgory':item.catgory,'star':item.star,'lang':item.lang,'movie_id':item.movie_id,
                 'movie_img':item.movie_img,'cinemas_img':item.cinemas_img,'movie_time':curren_date[0],
                 'movie_leave':curren_date[1],'movie_money': item.money,'seat':item.seat,
                 'movie_room':item.room}
            )
        return anchor

    def __get_date(self,play_time):
        curen_data = datetime.now()
        random_num = random.randint(1, 10)
        detal = timedelta(hours=random_num)
        play_times = play_time.replace('分钟','')
        leave_detal = timedelta(minutes=int(play_times))
        date = curen_data + detal
        if int(int(date.strftime('%H'))) >= 23 or int(date.strftime('%H')) <= 9:
            curren_date = '22:30'
            leave_time = self.__leave_time(int(play_times))
        else:
            curren_date = date.strftime('%H:%M')
            leave_time = (date + leave_detal).strftime('%H:%M')
        return [curren_date,leave_time]

    @staticmethod
    def __leave_time(time):
        hourse = 22
        minutes = 30 + time
        for item in range(minutes // 60):
            if hourse == 24:
                hourse = 0
            hourse += 1
        minutes = minutes % 60
        if hourse == 24:
            hourse = '00'
        elif hourse <= 10:
            hourse = '0' + str(hourse)
        if minutes < 10:
            minutes = '0' + str(minutes)
        return  str(hourse) + '：' + str(minutes)