def data_handel(datas):
    anchor = []
    for item in datas:
        anchor.append(
            {
                'id':item.id,
                'username':item.username,
                'name':item.name,
                'sex':item.sex,
                'avatar':item.avatar}
        )
    return anchor