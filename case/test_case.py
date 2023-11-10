from point.point import Point
from page.test_do import BasePage

target_image_path = "/Users/case/图片/img.png"

class Test_A(BasePage):
    def __init__(self):
        super().__init__()

    def test_a(self):
        # 使用 BasePage 类中的方法
#        self.move_and_click(Point.kca)
#        self.move_and_type(Point.kca, "ddd")

        # 使用自定义方法
        self.check_and_click(target_image_path, Point.kca)
        self.check_and_type(target_image_path, Point.kca, 'ddd')
