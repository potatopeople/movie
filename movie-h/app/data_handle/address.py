

def filter_address(address):
    anchor = {'all': []}
    for item in address:
        if item.spin in anchor.keys():
            anchor[item.spin].append({'id':item.city_id,'name':item.name})
        else:
            anchor[item.spin] = []
            anchor[item.spin].append({'id':item.city_id,'name':item.name})
        anchor['all'].append({'id':item.city_id,'name':item.name,'spin':item.spin})
    return anchor