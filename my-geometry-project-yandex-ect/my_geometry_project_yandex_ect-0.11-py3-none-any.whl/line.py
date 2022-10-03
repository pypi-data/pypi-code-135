from my_geometry_project_yandex_ect.point import *

class Line:
    def __init__(self, point1: Point, point2: Point):
        self.points = (point1, point2)

    def __repr__(self):
        return "Line(%s, %s)" % self.points

    def length(self):
        point1, point2 = self.points
        x1, y1 = point1.coord
        x2, y2 = point2.coord
        len = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
        return round(len, 4)