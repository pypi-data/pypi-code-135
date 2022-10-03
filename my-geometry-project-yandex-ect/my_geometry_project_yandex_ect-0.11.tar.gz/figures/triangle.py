from my_geometry_project_yandex_ect.point import *
from my_geometry_project_yandex_ect.figures.line import *

class Triangle:
    def __init__(self, point1: Point, point2: Point, point3: Point):
        self.points = (point1, point2, point3)

    def __repr__(self):
        return "Triangle(%s, %s, %s)" % self.points

    def aSide(self):
        return Line(self.points[0], self.points[1])

    def bSide(self):
        return Line(self.points[1], self.points[2])

    def cSide(self):
        return Line(self.points[0], self.points[2])

    def perimeter(self):
        per = self.aSide().length() + self.bSide().length() + self.cSide().length()
        return round(per, 4)

    def square(self):
        p = self.perimeter() / 2
        a = self.aSide().length()
        b = self.bSide().length()
        c = self.cSide().length()
        s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
        return round(s, 4)