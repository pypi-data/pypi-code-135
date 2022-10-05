try:
    from Shop import Shop
except ModuleNotFoundError:
    from shop.Shop import Shop


class Filter:
    def __init__(self, column_name, args, empty=False):
        self.incl = []
        self.excl = []
        self.column_name = column_name
        self.empty = empty
        if not empty:
            for arg in args:
                if isinstance(arg, str):
                    if arg[:2] == 'n:':
                        self.excl.append(arg[2:])
                    else:
                        self.incl.append(arg)

    def __repr__(self):
        return f'column: {self.column_name}, incl: {self.incl}, excl: {self.excl}'

    def is_good(self, d: dict):
        if self.empty:
            return True

        string = d[self.column_name]
        if isinstance(string, str):
            for i in self.incl:
                if i not in string:
                    return False
            for i in self.excl:
                if i in string:
                    return False
            return True
        return False

    @staticmethod
    def apply(fil, shop):
        if not fil.empty:
            list_of_items = [item for item in shop if fil.is_good(item)]
            result = Shop()
            for i in list_of_items:
                result.append(i)
            result.all_keys = shop.all_keys
            return result
        else:
            return shop

    @staticmethod
    def from_user_input():
        column_name = input('Podaj nazwe kolumny, jeżeli pusta, to pokaże się cały plik')
        if column_name == '':
            return Filter('', [], empty=True)
        args = []
        while True:
            temp = input('Podaj argument filtrowania, lub wciśnij enter, żeby zakończyć podawanie argumentów')
            if temp == '':
                break
            args += temp
        return Filter(column_name, args)


def test():
    print(Filter('title', ['n:do']))


if __name__ == '__main__':
    test()