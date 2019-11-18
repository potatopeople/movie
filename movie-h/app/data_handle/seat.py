
class DataHandel:

    def __get_row(self, data):
        row = [item[4] for item in data]
        row = self.__clear_repeat(row)
        return row

    @staticmethod
    def __clear_repeat(data):
        row = []
        for item in data:
            if item not in row:
                row.append(item)
        return row

    @staticmethod
    def __data_handel_row(row):
        anchor = {}
        for item in row:
            anchor[item] = []
        return anchor

    @staticmethod
    def __data_handel_clumn(row, data):
        for item in data:
            row[item.row].append(
                {'id': item[1],'clumn':item[5],'chose':item[6]}
            )
        return row

    def run(self,data):
        row = self.__get_row(data)
        row = self.__data_handel_row(row)
        data = self.__data_handel_clumn(row, data)
        return data