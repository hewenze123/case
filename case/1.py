from time import sleep
import ddddocr
from selenium.common import NoSuchElementException
from page.test_do import BasePage
from point import point
from point.point import Point


class Step_campus(BasePage):
    def step_campus(self):
        self.open_browser()
        self.get_url("https://k12school.xzxyun.com/campus-mng/login?")
        self.driver.maximize_window()
        self.move_and_type(point.Point.dla, 17310311997)
        self.move_and_type(point.Point.dlb, 'Aa123456')
        imgCode = self.driver.find_element("xpath", '//*[@id="pane-0"]/form/div[3]/img')
        shurukuang = self.driver.find_element("xpath", '//*[@id="pane-0"]/form/div[3]/div/div/div[1]/input')
        imgCode.screenshot('codee.png')
        orc = ddddocr.DdddOcr()
        with open('../case/codee.png', 'rb') as fp:
            image = fp.read()
        result = orc.classification(image)
        shurukuang.send_keys(result)
        for i in range(100):
            try:
                self.driver.find_element("xpath", '//*[@id="app"]/div/div[2]/header/div[1]/i[1]')
                self.move_and_type(Point.kca, 'ddd')

                break
            except NoSuchElementException:
                shurukuang.clear()
                imgCode.screenshot('codee.png')
                orc = ddddocr.DdddOcr()
                with open('../case/codee.png', 'rb') as fp:
                    image = fp.read()
                result = orc.classification(image)
                shurukuang.send_keys(result)
                sleep(3)
                self.move_and_click(point.dla)
                print("测试完成")




if __name__ == '__main__':
    # 创建 Step_campus 类的实例
    step_campus_instance = Step_campus()
    # 调用实例方法
    step_campus_instance.step_campus()
