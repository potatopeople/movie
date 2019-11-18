from app.modules.city import City,db as cdb
from app.data_handle.address import filter_address


def city_data():
    try:
        address = City.query.all()
        cdb.session.close()
        data = filter_address(address)
        return data
    except Exception as e:
        print('地址查询错误：',e)
        return []