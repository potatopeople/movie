def data_handel_talk(datas):
    anchor = []
    for item in datas:
        anchor.append(
            {'id':item[0],'username':item[1],'movie':item[3],'name':item[4],'main':item[2]}
        )
    return anchor