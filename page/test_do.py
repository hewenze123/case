from PIL import Image, ImageGrab
import pyautogui
import cv2
import numpy as np
from selenium import webdriver


class BasePage:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.pyautogui = pyautogui

    def move_and_click(self, args):  # 点击
        self.pyautogui.moveTo(args)
        self.pyautogui.click()

    def move_and_type(self, args, text):    # 输入
        self.pyautogui.moveTo(args)
        self.pyautogui.click()
        self.pyautogui.typewrite(text)

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

    def open_browser(self):
        self.driver.implicitly_wait(1)

    def close_browser(self):
        self.driver.close()

    def get_url(self, url):
        self.driver.get(url)

    def locator_element(self, args):
        return self.driver.find_element(*args)

    def send_keys(self, args, value):
        self.locator_element(args).send_keys(value)

    def clear(self, args):
        self.locator_element(args).clear()

    def click(self, args):
        self.locator_element(args).click()
