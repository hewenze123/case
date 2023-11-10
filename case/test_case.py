import pytest
from PIL import Image

from point.point import Point
from page.test_do import BasePage


class Test_A:
    def __init__(self):
        self.basepage = BasePage()

    def test_a(self):
        self.basepage.move_and_click(Point.a)
        self.basepage.move_and_type(Point.a, "ddd")

        # 获取屏幕截图
        screenshot = self.basepage.take_screenshot()

        # 期望的图片
        expected_image_path = "path/to/expected_image.png"
        expected_image = Image.open(expected_image_path)

        # 检查屏幕截图是否包含期望的图片
        assert self.image_contains(screenshot, expected_image), "屏幕截图中不包含期望的图片"

    def image_contains(self, screenshot, expected_image):
        # 这里使用适当的图像处理逻辑来检查 screenshot 是否包含 expected_image
        # 这可能涉及到模式匹配、特征匹配等图像处理技术
        # 这里简化为比较两个图片是否相等
        return screenshot == expected_image
