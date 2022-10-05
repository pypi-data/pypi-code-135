import re

try:
    import xlrd
except ImportError:
    raise 'pip install ninjatools[excel] or ninjatools[all] to use excel functions!'


class Excel:
    def __init__(self, workbook_path):
        self.wb = xlrd.open_workbook(workbook_path)
        self.sheet_name = None

    @staticmethod
    def get_cell(cell) -> tuple:
        """
        Returns a tuple of the cell
        :param cell:
        :return:
        """
        r = re.compile("([a-zA-Z]+)([0-9]+)")
        m = r.match(cell)
        col = m.group(1).upper()
        number_row = int(m.group(2)) - 1

        abc = ["A", "B", "C", "D", "E", "F", "G", "H", "I",
               "J", "K", "L", "M", "N", "O", "P", "Q", "R",
               "S", "T", "U", "V", "W", "X", "Y", "Z"]

        number_col = 0

        for char in col:
            number_col += abc.index(char)

        return number_row, number_col

    def get_sheets(self) -> list:
        """
        Returns a list of sheets
        :return:
        """
        return [_ for _ in self.wb.sheet_names()]

    def cell(self, cell, sheet_name=None) -> str:
        """
        Reads a cell
        :param cell:
        :param sheet_name:
        :return:
        """
        sheet_name = sheet_name if sheet_name else self.sheet_name
        ws = self.wb.sheet_by_name(sheet_name)
        return str(ws.cell(*self.get_cell(cell)).value)

    def read_range(self, cell_1, cell_2, sheet_name=None) -> list:
        """
        Reads a range of cells
        :param cell_1:
        :param cell_2:
        :param sheet_name:
        :return:
        """
        sheet_name = sheet_name if sheet_name else self.sheet_name

        var = self.get_cell(cell_1)
        var2 = self.get_cell(cell_2)

        ws = self.wb.sheet_by_name(sheet_name)

        data = []
        for _ in range(var[0], var2[0] + 1):
            temp = []
            for __ in range(var[1], var2[1] + 1):
                temp.append(ws.cell(_, __).value)

            data.append(temp)

        return data

    def read_indefinitely(self, start_cell: str, num_of_columns: int, num_of_rows=None, steps: int = 1) -> list:
        """
        Reads a range of cells indefinitely
        :param start_cell:
        :param num_of_columns:
        :param num_of_rows:
        :param steps:
        :return:
        """

        data = []

        char = start_cell[0]
        i = int(start_cell[1:])

        while True:
            try:
                data.append([self.cell(f'{char}{i}') for _ in range(num_of_columns)])
                if num_of_rows:
                    if len(data) >= num_of_rows:
                        break
            except (Exception,):
                break
            i += steps

        return data

    @staticmethod
    def convert_to_dict(data: list, key_idx: int, header_idx: int = 0) -> dict:
        """
        Converts a list to a dictionary
        :param data:
        :param key_idx:
        :param header_idx:
        :return:
        """
        dict_data = {}
        for row in data:
            dict_data[data[key_idx]] = dict(zip(data[header_idx], row))

        return dict_data

    # TODO: Cell write values/formulas
