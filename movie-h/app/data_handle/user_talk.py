def data_handel(datas):
    anchor = []
    if len(datas):
        for item in datas:
            anchor.append(
                {
                    'id':item[0],
                    'name':item[1],
                    'img':item[2],
                    'main':item[3],
                    'time':item[4]
                }
            )
        return anchor
    else:
        return []