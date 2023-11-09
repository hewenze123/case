from point.point import Point
from do.do import BasePage


class A:
    def __init__(self):
        self.basepage = BasePage()

    def a(self):
        self.basepage.move_and_click(Point.a)

        self.basepage.move_and_type(Point.a, "ddd")

if __name__ == '__main__':
    aa = A()
    aa.a()


