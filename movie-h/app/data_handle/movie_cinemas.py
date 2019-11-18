def data_handel(data):
    anchor = []
    for item in data:
        anchor.append(
            {'id':item[0],'city_id':item[1],'cinemas_id':item[2],'name':item[3],
             'address':item[4],'money':item[5]}
        )
    return anchor