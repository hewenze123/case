from time import sleep
from PIL import ImageGrab
import pyautogui
import cv2
import numpy as np
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

from ele.哈研 import EleDenglu
from point.point import Point
import ddddocr
from selenium.webdriver.common.keys import Keys


class BasePage:
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.pyautogui = pyautogui

    def move_and_click(self, args):  # 点击
        self.pyautogui.moveTo(args)
        self.pyautogui.click()

    def move_and_type(self, args, text):  # 输入
        self.pyautogui.moveTo(args)
        self.pyautogui.click()
        self.pyautogui.typewrite(text)

    def enter(self, sleep_time=1):
        self.pyautogui.press('enter')
        sleep(sleep_time)

    def open_browser(self, url):
        self.driver.implicitly_wait(3)
        self.driver.get(url)
        self.driver.maximize_window()

    def close_browser(self):
        self.driver.close()

    def locator_element(self, *args):
        return self.driver.find_element(*args)

    def send_keys(self, *args, value, sleep_time=1):
        self.locator_element(*args).send_keys(value)
        sleep(sleep_time)

    def clear(self, *args, sleep_time=1):
        self.locator_element(*args).clear()
        sleep(sleep_time)

    def click(self, *args, sleep_time=1):
        self.locator_element(*args).click()
        sleep(sleep_time)

    def switch(self, *args, sleep_time=1):
        self.driver.switch_to.frame(self.locator_element(*args))
        sleep(sleep_time)

    def switch_quit(self, sleep_time=1):
        self.driver.switch_to.default_content()
        sleep(sleep_time)

    def down_enter(self, *args, num=1):
        self.click(*args)  # 点击下拉框，打开选项列表
        for _ in range(num):  # 模拟按下两次向下箭头键
            self.send_keys(*args, value=Keys.ARROW_DOWN)
            # sleep(1)  # 等待一秒，确保选项列表正确加载
        self.send_keys(*args, value=Keys.RETURN)  # 模拟按下回车键

    def drag_left(self, *args, offset_x=-200, offset_y=0, sleep_time=1):
        """
        根据传入的定位参数找到元素，然后进行鼠标点击并向左拖动。
        Args:
            *args: 定位参数，可以是元组 (By, value) 或者直接是 XPath 字符串。
            offset_x (int): X 轴的拖动偏移量，默认为 -100。
            offset_y (int): Y 轴的拖动偏移量，默认为 0。
        """
        element = self.locator_element(*args)
        actions = ActionChains(self.driver)
        actions.click_and_hold(element).move_by_offset(offset_x, offset_y).release().perform()
        sleep(sleep_time)

    def shift_slide(self, *args, offset_x=200, offset_y=0, sleep_time=1):
        actions = ActionChains(self.driver)
        actions.key_down(Keys.SHIFT).click_and_hold(self.locator_element(*args)).move_by_offset(offset_x, offset_y).release().key_up(Keys.SHIFT)
        actions.perform()

    def click_image(self, image_path):
        location = pyautogui.locateCenterOnScreen(image_path, confidence=0.25)
        if location is not None:
            pyautogui.click(location[0], location[1])
            print("点击图片成功")
        else:
            print("图片不存在")

    def handle_captcha(self):
        img_code = self.locator_element(*EleDenglu.yanzhengma)  # 使用下划线连接变量名，符合PEP8规范
        img_code.screenshot('codee.png')

        # 将文件路径声明为一个常量，以便在多个地方使用
        image_path = '/Users/case/run/codee.png'

        orc = ddddocr.DdddOcr()
        with open(image_path, 'rb') as fp:
            image = fp.read()
        result = orc.classification(image)

        # 使用多行分开不同的操作，以提高可读性
        self.clear(*EleDenglu.shuru)
        self.send_keys(*EleDenglu.shuru, value=result)
        self.move_and_click(Point.dlc)

    def check_and_click(self, target_image_path, args, threshold=0.4):
        def load_image(image_path):
            try:
                image = cv2.imread(image_path)
                if image is None:
                    raise FileNotFoundError(f"无法找到图像文件: {image_path}")
                return image
            except Exception as e:
                print(f"加载图像时出错: {e}")
                return None

        def capture_screenshot():
            screenshot = ImageGrab.grab()
            screenshot = np.array(screenshot)
            return cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR)

        # 加载目标图像
        target_image = load_image(target_image_path)

        # 截取屏幕截图
        screenshot = capture_screenshot()

        # 使用模板匹配
        result = cv2.matchTemplate(screenshot, target_image, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

        # 如果最大匹配值大于阈值，则认为图像匹配
        if max_val > threshold:
            print("屏幕中包含目标图像！")
            self.move_and_click(args)
            print(f"执行移动和点击操作，点击坐标: {args}")
        else:
            print("屏幕中未找到目标图像。")
            # 在关键的地方添加调试输出
            print(f"目标图像大小: {target_image.shape}")
            print(f"截图大小: {screenshot.shape}")

    def check_and_type(self, target_image_path, args, text, threshold=0.4):
        def load_image(image_path):
            try:
                image = cv2.imread(image_path)
                if image is None:
                    raise FileNotFoundError(f"无法找到图像文件: {image_path}")
                return image
            except Exception as e:
                print(f"加载图像时出错: {e}")
                return None

        def capture_screenshot():
            screenshot = ImageGrab.grab()
            screenshot = np.array(screenshot)
            return cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR)

        # 加载目标图像
        target_image = load_image(target_image_path)

        # 截取屏幕截图
        screenshot = capture_screenshot()

        # 使用模板匹配
        result = cv2.matchTemplate(screenshot, target_image, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

        # 如果最大匹配值大于阈值，则认为图像匹配
        if max_val > threshold:
            print("屏幕中包含目标图像！")
            self.move_and_type(args, text)
            print(f"执行移动和点击操作，点击坐标: {args}")
        else:
            print("屏幕中未找到目标图像。")
            # 在关键的地方添加调试输出
            print(f"目标图像大小: {target_image.shape}")
            print(f"截图大小: {screenshot.shape}")
