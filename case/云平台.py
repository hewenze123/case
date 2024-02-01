from ele.哈研 import EleDenglu
from ele.云平台 import EleYemian
from point.point import Point
from page.test_do import BasePage
from selenium.common import NoSuchElementException


class TestYunpingtai(BasePage):  # 建议使用驼峰命名法，类名应该以大写字母开头
    def test_guanliyuanyujuese(self):
        self.open_browser(EleDenglu.ceshi_url)
        self.move_and_type(Point.dla, '17310311997')
        self.move_and_type(Point.dlb, 'Aa123456_')
        self.handle_captcha()

        for i in range(100):
            try:
                self.locator_element(*EleDenglu.dukaqi)  # 初始化读卡器-登录
                self.click(*EleYemian.qiehuanjuese)
                self.click(*EleYemian.yunpingtaijuese)
                self.click(*EleYemian.queding1, sleep_time=2)
                self.click(*EleYemian.guanliyuanyujuese)
                self.click(*EleYemian.xuexiaoguanliyuan)  # 学校管理员
                self.send_keys(*EleYemian.dengluzhanghao, value=1)  # 查询
                self.down_enter(*EleYemian.zhanghaozhuangtai, num=1)
                self.click(*EleYemian.chaxun, sleep_time=3)
                self.down_enter(*EleYemian.zhanghaozhuangtai, num=1)
                self.click(*EleYemian.chaxun, sleep_time=3)
                self.down_enter(*EleYemian.zhanghaozhuangtai, num=1)
                self.click(*EleYemian.chaxun, sleep_time=3)
                self.click(*EleYemian.qingchu, sleep_time=3)
                self.click(*EleYemian.tianjiaguanliyuan)  # 新增管理员
                self.send_keys(*EleYemian.shoujihao, value='18845674568')
                self.send_keys(*EleYemian.denglumima, value='Aa123456_')
                self.click(*EleYemian.danxuanjuese)
                self.click(*EleYemian.queding2, sleep_time=3)
                self.click(*EleYemian.qiyong)  # 启用/禁用
                self.click(*EleYemian.qiyong)
                self.click(*EleYemian.xiugaimima)  # 修改密码
                self.send_keys(*EleYemian.xinmima, value='Aa12345678_')
                self.send_keys(*EleYemian.querenmima, value='Aa12345678_')
                self.click(*EleYemian.xianshimima)
                self.click(*EleYemian.xianshimima)
                self.click(*EleYemian.xiugai, sleep_time=3)
                self.click(*EleYemian.bianji)  # 修改管理员
                self.send_keys(*EleYemian.xingming, value='Py')
                self.click(*EleYemian.queding2, sleep_time=3)
                self.click(*EleYemian.bianji)
                self.click(*EleYemian.queding2, sleep_time=3)
                self.click(*EleYemian.jiechusuoding)  # 解除锁定
                self.click(*EleYemian.queding3)
                self.click(*EleYemian.shanchu)  # 删除管理员
                self.click(*EleYemian.queding4)

                self.click(*EleYemian.guanliyuanyujuese)
                self.click(*EleYemian.yonghuzhuanguanliyuan)  # 用户转管理员
                self.send_keys(*EleYemian.dengluzhanghao, value='4')  # 查询
                self.click(*EleYemian.chaxun, sleep_time=3)
                self.click(*EleYemian.qingchu, sleep_time=3)
                self.click(*EleYemian.guanliyuan)
                self.send_keys(*EleYemian.dengluzhanghao, value='4')
                self.click(*EleYemian.chaxun, sleep_time=3)
                self.click(*EleYemian.qingchu, sleep_time=3)
                self.click(*EleYemian.yonghu)
                self.click(*EleYemian.sheweiguanliyuan)  # 设为管理员
                self.send_keys(*EleYemian.denglumima, value='Aa123456_')
                self.click(*EleYemian.danxuanjuese)
                self.click(*EleYemian.queding2, sleep_time=3)
                self.click(*EleYemian.guanliyuan)
                self.click(*EleYemian.qiyong2)  # 启用/禁用
                self.click(*EleYemian.qiyong2)
                self.click(*EleYemian.xiugaimima)  # 修改密码
                self.send_keys(*EleYemian.xinmima, value='Aa12345678_')
                self.send_keys(*EleYemian.querenmima, value='Aa12345678_')
                self.click(*EleYemian.xianshimima)
                self.click(*EleYemian.xianshimima)
                self.click(*EleYemian.xiugai, sleep_time=3)
                self.click(*EleYemian.bianji)  # 修改管理员
                self.click(*EleYemian.danxuanjuese2)
                self.click(*EleYemian.queding2, sleep_time=3)
                self.click(*EleYemian.bianji)
                self.click(*EleYemian.queding2, sleep_time=3)
                self.click(*EleYemian.jiechusuoding)  # 解除锁定
                self.click(*EleYemian.queding3)
                self.click(*EleYemian.chexiaoguanli)  # 撤销管理员
                self.click(*EleYemian.queding4, sleep_time=3)

                self.click(*EleYemian.guanliyuanyujuese)
                self.click(*EleYemian.jueseguanli)  # 角色管理
                self.click(*EleYemian.qiyong3)  # 启用/禁用
                self.click(*EleYemian.qiyong3)
                self.click(*EleYemian.tianjiajuese)  # 添加角色
                self.send_keys(*EleYemian.juesemingcheng, value='py')
                self.click(*EleYemian.caidanquanxuan)
                self.click(*EleYemian.queding2, sleep_time=3)
                self.click(*EleYemian.bianji)  # 修改管理员
                self.send_keys(*EleYemian.juesemingcheng, value='Py')
                self.click(*EleYemian.queding2, sleep_time=3)
                self.click(*EleYemian.bianji)
                self.click(*EleYemian.queding2, sleep_time=3)
                self.click(*EleYemian.shanchu)  # 删除管理员
                self.click(*EleYemian.queding5)

                self.click(*EleYemian.guanliyuanyujuese)
                self.click(*EleYemian.caozuorizhi)  # 操作日志
                self.send_keys(*EleYemian.guanliyuanzhanghao, value='1')  # 查询操作日志
                self.send_keys(*EleYemian.caozuomokuai, value='管理')
                self.send_keys(*EleYemian.kaishiriqi, value='2023-1-1')
                self.send_keys(*EleYemian.jieshuriqi, value='2024-1-1')
                self.down_enter(*EleYemian.mingandu, num=2)
                self.down_enter(*EleYemian.mokuaigongneng, num=2)
                self.click(*EleYemian.chaxun, sleep_time=3)
                self.down_enter(*EleYemian.mingandu, num=1)
                self.down_enter(*EleYemian.mokuaigongneng, num=1)
                self.click(*EleYemian.chaxun, sleep_time=3)
                self.down_enter(*EleYemian.mingandu, num=1)
                self.down_enter(*EleYemian.mokuaigongneng, num=1)
                self.click(*EleYemian.chaxun, sleep_time=3)
                self.down_enter(*EleYemian.mokuaigongneng, num=1)
                self.click(*EleYemian.chaxun, sleep_time=3)
                self.down_enter(*EleYemian.mokuaigongneng, num=1)
                self.click(*EleYemian.chaxun, sleep_time=3)
                self.down_enter(*EleYemian.mokuaigongneng, num=1)
                self.click(*EleYemian.chaxun, sleep_time=3)
                self.click(*EleYemian.qingchu, sleep_time=3)

                self.click(*EleYemian.guanliyuanyujuese)
                self.click(*EleYemian.denglurizhi)  # 登录日志
                self.send_keys(*EleYemian.guanliyuanzhanghao, value='1')  # 查询登录日志
                self.send_keys(*EleYemian.kaishiriqi, value='2023-1-1')
                self.send_keys(*EleYemian.jieshuriqi, value='2024-1-1')
                self.click(*EleYemian.chaxun, sleep_time=3)
                self.click(*EleYemian.qingchu, sleep_time=3)

                self.click(*EleYemian.guanliyuanyujuese)
                self.click(*EleYemian.shouyeguanli)  # 首页管理
                self.click(*EleYemian.shanchu)  # 删除首页样式
                self.click(*EleYemian.queding5, sleep_time=3)
                self.click(*EleYemian.tianjiayangshi)  # 新增首页样式
                self.send_keys(*EleYemian.yangshimingcheng, value='py')
                self.click(*EleYemian.tianjia)
                self.click(*EleYemian.gongneng1)
                self.click(*EleYemian.queding6)
                self.click(*EleYemian.qingkonggongneng)
                self.click(*EleYemian.tianjia)
                self.click(*EleYemian.gongneng11)
                self.click(*EleYemian.queding66)
                self.click(*EleYemian.queding2, sleep_time=3)
                self.click(*EleYemian.bianji)  # 编辑首页样式
                self.send_keys(*EleYemian.yangshimingcheng, value='py')
                self.click(*EleYemian.qingkonggongneng)
                self.click(*EleYemian.tianjia)
                self.click(*EleYemian.gongneng11)
                self.click(*EleYemian.queding66)
                self.click(*EleYemian.queding2, sleep_time=3)
                self.click(*EleYemian.bianji)
                self.click(*EleYemian.queding2, sleep_time=3)

                break
            except NoSuchElementException:  # 验证码错误-重新登录
                self.handle_captcha()

    def test_jichuxinxiguanli(self):
        self.open_browser(EleDenglu.ceshi_url)
        self.move_and_type(Point.dla, '17310311997')
        self.move_and_type(Point.dlb, 'Aa123456_')
        self.handle_captcha()

        for i in range(100):
            try:
                self.locator_element(*EleDenglu.dukaqi)  # 初始化读卡器-登录
                self.click(*EleYemian.qiehuanjuese)
                self.click(*EleYemian.yunpingtaijuese)
                self.click(*EleYemian.queding1, sleep_time=2)

                break
            except NoSuchElementException:  # 验证码错误-重新登录
                self.handle_captcha()