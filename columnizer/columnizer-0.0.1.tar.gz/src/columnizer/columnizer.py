#!/usr/bin/python
from enum import Enum

class ColumnTextAlignment(Enum):
    LEFT = 0,
    RIGHT = 1,
    CENTER = 2


class ColumnTableStyle(object):
    def __init__\
    (
        self,
        left_edge = "| ",
        right_edge = " |",
        column_seperator = " | ",
        row_seperator = "-",
        left_row_edge = "+",
        right_row_edge = "+",
        header_row_seperator = "="
    ):
        super().__init__()
        self.left_edge = left_edge
        self.right_edge = right_edge
        self.column_seperator = column_seperator
        self.row_seperator = row_seperator
        self.left_row_edge = left_row_edge
        self.right_row_edge = right_row_edge
        self.header_row_seperator = header_row_seperator

class ColumnTableStyleHeavy(ColumnTableStyle):
    def __init__(self):
        super().__init__(left_edge="|| ", right_edge=" ||", row_seperator="=")

class ColumnTableStyleDotMatrix(ColumnTableStyle):
    def __init__(self):
        super().__init__(left_edge="| O | ", right_edge=" | O |", row_seperator=".")

class ColumnTableStyleNone(ColumnTableStyle):
    def __init__(self):
        super().__init__(left_edge="",
                         right_edge="",
                         row_seperator="",
                         column_seperator=" ")


class ColumnBase(object):
    def __init__(self, width = 10):
        self.width = width
        super().__init__()

    def apply(self, text):
        pass


class ColumnClipped(ColumnBase):
    def __init__(self, width=10):
        super().__init__(width)

    def apply(self, text):
        result = []
        if len(text) >= self.width:
            result.append(text[:self.width])
        else:
            remainder = self.width - len(text)
            result.append( f"{text}{' '*remainder}")

        return result


class ColumnLineWrap(ColumnBase):
    def __init__(self, width=10):
        super().__init__(width)

    def apply(self, text):
        import copy
        input_text = copy.copy(text)
        result = []

        while len(input_text) >= self.width:
            line = input_text[:self.width]
            input_text = input_text[self.width:]
            result.append(line)

        remainder = self.width - len(input_text)
        result.append( f"{input_text}{' '*remainder}")

        return result


class ColumnWordWrap(ColumnBase):
    def __init__(self, width=10, alignment:ColumnTextAlignment=ColumnTextAlignment.LEFT):
        super().__init__(width)
        self.alignment = alignment

    def apply(self, text):
        result = []
        words = text.split(" ")
        line = ""
        for word in words:
            if line == "":
                if len(word) > self.width:
                    result.append(word[:self.width-1]+"-")
                    line = word[self.width-1:]
                else:
                    line = word
                continue

            if len(line) + len(word) + 1 > self.width:
                result.append(line)
                line = word
            else:
                line += " "+word

        if len(line):
            result.append(line)

        aligned_result = []

        for line in result:
            remainder = self.width - len(line)
            if remainder == 0:
                continue
            if self.alignment == ColumnTextAlignment.LEFT:
                aligned_result.append(line+" "*remainder)
            if self.alignment == ColumnTextAlignment.RIGHT:
                aligned_result.append(" "*remainder+line)
            if self.alignment == ColumnTextAlignment.CENTER:
                leftsize = int(remainder/2)
                rightsize = remainder - leftsize
                aligned_result.append(" "*leftsize + line + " "*rightsize)

        return aligned_result


class Columnizer(object):
    def __init__(
                     self,
                     columns = [],
                     style = ColumnTableStyle(),
                     first_row_headers = False
                 ):
        self.columns = columns
        self.style = style
        self.first_row_headers = first_row_headers

    def apply(self, rows):
        style = self.style
        formatted_rows = []
        for row in rows:
            result_row = []
            for i, c_text in enumerate(row):
                column = self.columns[i]
                columnized_text = column.apply(c_text)
                result_row.append(columnized_text)
            formatted_rows.append(result_row)

        # Form the output
        width =0
        for c in self.columns:
            width += c.width
        full_width = width + ((len(self.columns)-1) * len(style.column_seperator))
        full_width += len(style.left_edge) + len(style.right_edge)
        if self.first_row_headers:
            top_edge = style.header_row_seperator * full_width
        else:
            top_edge = style.row_seperator * full_width
        formatted_output = top_edge + "\n"
        for row_count, row in enumerate(formatted_rows):
            max_len = 0
            for c in row:
                if len(c) > max_len:
                    max_len=len(c)

            for line in range(0, max_len):
                formatted_output += style.left_edge
                for i, c in enumerate(row):
                    if len(c) > line:
                        formatted_output += c[line]
                    else:
                        formatted_output += " " * self.columns[i].width
                    if i + 1 < len(row):
                        formatted_output += style.column_seperator
                    else:
                        formatted_output+= style.right_edge
                        formatted_output += "\n"
            if self.first_row_headers and row_count == 0:
                formatted_output += style.header_row_seperator * full_width
            else:
                formatted_output += style.row_seperator * full_width
            formatted_output += "\n"
        return formatted_output


if __name__ == "__main__":
    def test_columns(columnizer):
        test_text = "the quick brown fox jumped over the lazy dogs!"
        column_count = len(columnizer.columns)
        test_rows = []
        if columnizer.first_row_headers:
            header_titles=["A","B","C","D","E","F","G","H"]
            test_rows.append(header_titles[:column_count])
        test_rows.append([test_text for _ in range(0,column_count)])
        result = columnizer.apply(test_rows)
        print (result)

    c = Columnizer(
        columns=[ColumnClipped(width=25), ColumnLineWrap(width=17), ColumnWordWrap(width=17),
                 ColumnWordWrap(alignment=ColumnTextAlignment.RIGHT, width=17),
                 ColumnWordWrap(alignment=ColumnTextAlignment.CENTER, width=17)],
        style = ColumnTableStyleHeavy())

    print ("Heavy:")
    test_columns(c)

    c = Columnizer(
        columns=[ColumnClipped(width=25), ColumnLineWrap(width=17), ColumnWordWrap(width=17),
                 ColumnWordWrap(alignment=ColumnTextAlignment.RIGHT, width=17),
                 ColumnWordWrap(alignment=ColumnTextAlignment.CENTER, width=17)])

    print ("Default:")
    test_columns(c)

    print ("Default + Headers:")
    c.first_row_headers = True
    test_columns(c)