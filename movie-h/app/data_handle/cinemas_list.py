def data_handel(data):
    anchor = []
    for item in data:
        anchor.append(
            {'id':item.id,'city_id':item.city_id,'cinemas_id':item.cinemas_id,
             'name':item.name,'address':item.address,'money':item.money}
        )
    return anchor
