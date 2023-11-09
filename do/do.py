import pyautogui


class BasePage:
    def __init__(self):
        self.pyautogui = pyautogui
    def move_and_click(self, args):
        self.pyautogui.moveTo(args)
        self.pyautogui.click()

    def move_and_type(self, args, text):
        self.pyautogui.moveTo(args)
        self.pyautogui.click()
        self.pyautogui.typewrite(text)
