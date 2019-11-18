def order_handel(data,date):
    anchor = {'seat':[]}
    for i,item in enumerate(data):
        if i == 0:
            anchor['cinemas_name'] = item[0]
            anchor['img'] = item[2]
            anchor['movie_name'] = item[3]
            anchor['money'] = len(data) * item[4]
            anchor['room'] = item[5]
            anchor['buy_date'] = item[8]
            anchor['batch'] = item[10] #用户订单号
            anchor['tf'] = item[9]
            anchor['movie_date'] = date
        anchor['seat'].append(
            {'id':item[1],'row':item[6],'clumn':item[7]}
        )
    return anchor