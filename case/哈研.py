from time import sleep
from ele.哈研 import EleDenglu, EleYemian, EleTongzhigonggao, EleZuoyepindao, EleMobanleixing, EleMoBanzhongxin, \
    EleMoBanpeizhi, EleShujuguanli, EleJueseguanli, EleChengyuanbumen
from point.point import Point
from page.test_do import BasePage
from selenium.common import NoSuchElementException


class TestJiaxiaohudong(BasePage):  # 建议使用驼峰命名法，类名应该以大写字母开头
    def test_jiaxiaohudong(self):
        self.open_browser(EleDenglu.ceshi_url)
        self.move_and_type(Point.dla, '17310311997')
        self.move_and_type(Point.dlb, 'Aa123456_')
        self.handle_captcha()
        for i in range(100):
            try:
                self.locator_element(*EleDenglu.dukaqi)
                sleep(1)
                # 通知公告case---搜索导出---重置导出---查看明细导出---
                self.click(*EleYemian.jiaxiaohudong)
                self.click(*EleYemian.tongzhigonggao, sleep_time=6)
                self.switch(*EleYemian.iframe_tongzhigonggao)
                self.send_keys(*EleTongzhigonggao.faburen, value=1)  # 搜索导出
                self.send_keys(*EleTongzhigonggao.biaoti, value=1)
                self.send_keys(*EleTongzhigonggao.kaishishijian, value='2023-12-01')
                self.send_keys(*EleTongzhigonggao.jieshushijian, value='2023-12-01')
                self.click(*EleTongzhigonggao.sousuo, sleep_time=3)
                self.click(*EleTongzhigonggao.daochu)
                self.click(*EleTongzhigonggao.querendaochu)
                self.click(*EleTongzhigonggao.chongzhi, sleep_time=3)  # 重置导出
                self.click(*EleTongzhigonggao.daochu)
                self.click(*EleTongzhigonggao.querendaochu)
                self.click(*EleTongzhigonggao.chakan)  # 查看明细导出
                self.click(*EleTongzhigonggao.chakanmingxi, sleep_time=3)
                self.click(*EleTongzhigonggao.guanbimingxi)
                self.click(*EleTongzhigonggao.xiazaimingxi)
                self.click(*EleTongzhigonggao.querendaochu)
                self.click(*EleTongzhigonggao.fanhui)
                self.switch_quit()

                # 作业频道case---搜索导出---重置导出---查看明细导出---
                self.click(*EleYemian.jiaxiaohudong)
                self.click(*EleYemian.zuoyepindao, sleep_time=6)
                self.switch(*EleYemian.iframe_zuoyepindao, sleep_time=2)
                self.send_keys(*EleTongzhigonggao.faburen, value=1)  # 搜索导出
                self.send_keys(*EleTongzhigonggao.biaoti, value=1)
                self.send_keys(*EleTongzhigonggao.kaishishijian, value='2023-12-01')
                self.send_keys(*EleTongzhigonggao.jieshushijian, value='2023-12-01')
                self.down_enter(*EleZuoyepindao.xueke, num=2)
                self.click(*EleTongzhigonggao.sousuo, sleep_time=3)
                self.click(*EleTongzhigonggao.daochu)
                self.click(*EleTongzhigonggao.querendaochu)
                self.click(*EleTongzhigonggao.chongzhi, sleep_time=3)  # 重置导出
                self.click(*EleTongzhigonggao.daochu)
                self.click(*EleTongzhigonggao.querendaochu)
                self.click(*EleTongzhigonggao.chakan)  # 查看明细导出
                self.click(*EleTongzhigonggao.chakanmingxi, sleep_time=3)
                self.click(*EleTongzhigonggao.guanbimingxi)
                self.click(*EleTongzhigonggao.xiazaimingxi)
                self.click(*EleTongzhigonggao.querendaochu)
                self.click(*EleTongzhigonggao.fanhui)
                self.switch_quit()

                # 模版类型case---查询---重置---禁用/启用---新增---修改---删除---
                self.click(*EleYemian.jiaxiaohudong)
                self.click(*EleYemian.mobanleixing, sleep_time=6)
                self.switch(*EleYemian.iframe_mobanleixing, sleep_time=2)
                self.send_keys(*EleMobanleixing.leixingmingcheng, value=1)  # 查询
                self.down_enter(*EleZuoyepindao.xueke, num=1)
                self.click(*EleMobanleixing.chaxun, sleep_time=3)
                self.down_enter(*EleZuoyepindao.xueke, num=1)
                self.click(*EleMobanleixing.chaxun, sleep_time=3)
                self.down_enter(*EleZuoyepindao.xueke, num=1)
                self.click(*EleMobanleixing.chaxun, sleep_time=3)
                self.click(*EleTongzhigonggao.chongzhi, sleep_time=3)  # 重置
                self.click(*EleMobanleixing.jinyong)  # 禁用/启用
                self.click(*EleMobanleixing.jinyong)
                self.click(*EleMobanleixing.xinzeng)  # 新增
                self.send_keys(*EleMobanleixing.leixingmingcheng2, value="Py")
                self.click(*EleMobanleixing.queding, sleep_time=3)
                self.click(*tuple(EleMobanleixing.xiugai))  # 修改
                self.clear(*EleMobanleixing.leixingmingcheng2)
                self.send_keys(*EleMobanleixing.leixingmingcheng2, value="Py1")
                self.click(*EleMobanleixing.queding, sleep_time=3)
                self.click(*tuple(EleMobanleixing.xiugai))
                self.click(*EleMobanleixing.queding, sleep_time=3)
                self.click(*EleMobanleixing.shanchu)  # 删除
                self.click(*EleTongzhigonggao.querendaochu, sleep_time=3)
                self.switch_quit()

                # 模版中心---查询---重置---禁用/启用查看详情---新增---修改---删除---
                self.click(*EleYemian.jiaxiaohudong)
                self.click(*EleYemian.mobanzhongxin, sleep_time=6)
                self.switch(*EleYemian.iframe_mobanzhongxin, sleep_time=2)
                self.send_keys(*EleMobanleixing.leixingmingcheng, value=1)  # 查询
                self.down_enter(*EleMoBanzhongxin.mobanleixing, num=1)
                self.click(*EleMobanleixing.chaxun, sleep_time=3)
                self.down_enter(*EleMoBanzhongxin.mobanleixing, num=1)
                self.click(*EleMobanleixing.chaxun, sleep_time=3)
                self.down_enter(*EleMoBanzhongxin.mobanleixing, num=1)
                self.click(*EleMobanleixing.chaxun, sleep_time=3)
                self.down_enter(*EleZuoyepindao.xueke, num=1)
                self.click(*EleMobanleixing.chaxun, sleep_time=3)
                self.down_enter(*EleZuoyepindao.xueke, num=1)
                self.click(*EleMobanleixing.chaxun, sleep_time=3)
                self.down_enter(*EleZuoyepindao.xueke, num=1)
                self.click(*EleMobanleixing.chaxun, sleep_time=3)
                self.click(*EleTongzhigonggao.chongzhi, sleep_time=3)  # 重置
                self.click(*EleMobanleixing.jinyong)  # 禁用/启用查看详情
                self.click(*EleMoBanzhongxin.xiangqing, sleep_time=3)
                self.click(*EleMoBanzhongxin.fanhui)
                self.click(*EleMobanleixing.jinyong)
                self.click(*EleMoBanzhongxin.xiangqing, sleep_time=3)
                self.click(*EleMoBanzhongxin.fanhui)
                self.click(*EleMobanleixing.xinzeng)
                self.send_keys(*EleMoBanzhongxin.mobanmingcheng, value="Py")
                self.down_enter(*EleMoBanzhongxin.mobanleixing, num=1)
                self.send_keys(*EleMoBanzhongxin.neirong, value="Py")
                self.click(*EleMoBanzhongxin.tijiao, sleep_time=3)
                self.click(*EleMobanleixing.xinzeng)  # 新增
                self.send_keys(*EleMoBanzhongxin.mobanmingcheng, value="Py2")
                self.down_enter(*EleMoBanzhongxin.mobanleixing, num=1)
                self.click(*EleMoBanzhongxin.tingyong)
                self.send_keys(*EleMoBanzhongxin.neirong, value="Py2")
                self.click(*EleMoBanzhongxin.tijiao, sleep_time=3)
                self.click(*tuple(EleMoBanzhongxin.xiugai))  # 修改
                self.clear(*EleMoBanzhongxin.mobanmingcheng)
                self.send_keys(*EleMoBanzhongxin.mobanmingcheng, value="Py3")
                self.down_enter(*EleMoBanzhongxin.mobanleixing, num=2)
                self.click(*EleMoBanzhongxin.tingyong)
                self.clear(*EleMoBanzhongxin.neirong)
                self.send_keys(*EleMoBanzhongxin.neirong, value="Py3")
                self.click(*EleMoBanzhongxin.tijiao, sleep_time=3)
                self.click(*tuple(EleMoBanzhongxin.xiugai))
                self.click(*EleMoBanzhongxin.tijiao, sleep_time=3)
                self.click(*EleMoBanzhongxin.shanchu)  # 删除
                self.click(*EleTongzhigonggao.querendaochu, sleep_time=3)
                self.switch_quit()

                # 模版配置---查询---重置---添加模版类型---添加模版---删除模版---删除模版类型---模版排序---
                self.click(*EleYemian.jiaxiaohudong)
                self.click(*EleYemian.mobanpeizhi ,sleep_time=6)
                self.switch(*EleYemian.iframe_mobanpeizhi, sleep_time=2)
                self.send_keys(*EleMoBanpeizhi.yingyongmingcheng, value=1)  # 查询
                self.click(*EleMobanleixing.chaxun, sleep_time=3)
                self.click(*EleTongzhigonggao.chongzhi, sleep_time=3)  # 重置
                self.click(*EleMoBanpeizhi.peizhi)  # 添加模版类型
                self.click(*EleMoBanpeizhi.tianjiamobanleixing)
                self.click(*EleMoBanpeizhi.quanxuanleixing)
                self.click(*EleMoBanpeizhi.leixingbaocun, sleep_time=3)
                self.click(*EleMoBanpeizhi.tianjiamoban)  # 添加模版
                self.click(*EleMoBanpeizhi.danxuanmoban)
                self.click(*EleMoBanpeizhi.mobanbaocun, sleep_time=3)
                self.click(*EleMoBanpeizhi.tianjiamoban)  # 删除模版
                self.click(*EleMoBanpeizhi.shanchumoban)
                self.click(*EleMoBanpeizhi.mobanbaocun, sleep_time=3)
                self.click(*EleMoBanpeizhi.yichuleixing)  # 删除模版类型
                self.click(*EleTongzhigonggao.querendaochu, sleep_time=3)
                self.drag_left(*EleMoBanpeizhi.moban2)  # 模版排序
                self.click(*EleMoBanpeizhi.tijiao, sleep_time=3)
                self.drag_left(*EleMoBanpeizhi.moban2, offset_x=200, offset_y=0)
                self.click(*EleMoBanpeizhi.tijiao, sleep_time=3)
                self.drag_left(*EleMoBanpeizhi.moban2, offset_x=0, offset_y=-200)
                self.click(*EleMoBanpeizhi.tijiao, sleep_time=3)
                self.drag_left(*EleMoBanpeizhi.moban2, offset_x=0, offset_y=200)
                self.click(*EleMoBanpeizhi.tijiao, sleep_time=3)
                self.click(*EleMoBanpeizhi.guanbi, sleep_time=3)
                self.switch_quit()

                break
            except NoSuchElementException:  # 验证码错误-重新登录
                self.handle_captcha()

    def test_shenpixitong(self):
        self.open_browser(EleDenglu.ceshi_url)
        self.move_and_type(Point.dla, '17310311997')
        self.move_and_type(Point.dlb, 'Aa123456_')
        self.handle_captcha()
        for i in range(100):
            try:
                self.locator_element(*EleDenglu.dukaqi)
                sleep(1)
                # 数据管理case---查询导出---重置导出---查看详情---删除
                self.click(*EleYemian.shenpixitong)
                self.click(*EleYemian.shujuguanli, sleep_time=6)
                self.switch(*EleYemian.iframe_shujuguanli)
                self.down_enter(*EleZuoyepindao.xueke, num=1)  # 查询导出
                self.click(*EleShujuguanli.zhuangtai)
                self.click(*EleShujuguanli.shenhezhong)
                self.send_keys(*EleShujuguanli.tijiaoren, value='何')
                self.send_keys(*EleTongzhigonggao.kaishishijian, value='2023-12-01')
                self.send_keys(*EleTongzhigonggao.jieshushijian, value='2023-12-01')
                self.send_keys(*EleShujuguanli.kaishishijian, value='2023-12-01')
                self.send_keys(*EleShujuguanli.jieshushijian, value='2023-12-01')
                self.send_keys(*EleShujuguanli.shenqingbianhao, value='0')
                self.click(*EleTongzhigonggao.sousuo, sleep_time=3)
                self.click(*EleTongzhigonggao.daochu)
                self.click(*EleTongzhigonggao.querendaochu)
                self.click(*EleShujuguanli.zhuangtai)
                self.click(*EleShujuguanli.yitongguo)
                self.click(*EleTongzhigonggao.sousuo, sleep_time=3)
                self.click(*EleTongzhigonggao.daochu)
                self.click(*EleTongzhigonggao.querendaochu)
                self.click(*EleShujuguanli.zhuangtai)
                self.click(*EleShujuguanli.yibohui)
                self.click(*EleTongzhigonggao.sousuo, sleep_time=3)
                self.click(*EleTongzhigonggao.daochu)
                self.click(*EleTongzhigonggao.querendaochu)
                self.click(*EleShujuguanli.zhuangtai)
                self.click(*EleShujuguanli.yichexiao)
                self.click(*EleTongzhigonggao.sousuo, sleep_time=3)
                self.click(*EleTongzhigonggao.daochu)
                self.click(*EleTongzhigonggao.querendaochu)
                self.click(*EleTongzhigonggao.chongzhi, sleep_time=3)  # 重置导出
                self.click(*EleTongzhigonggao.daochu)
                self.click(*EleTongzhigonggao.querendaochu)
                self.click(*EleShujuguanli.xiangqing, sleep_time=3)  # 查看详情
                self.click(*EleShujuguanli.fanhui, sleep_time=3)
                self.click(*EleShujuguanli.xiangqing, sleep_time=3)
                self.click(*EleShujuguanli.shanchu)  # 删除
                self.click(*EleTongzhigonggao.querendaochu, sleep_time=3)
                self.switch_quit()

                # 角色管理case---搜索角色/成员---新增角色---修改角色---删除角色---添加成员---设置管理部门---移除成员
                self.click(*EleYemian.shenpixitong)
                self.click(*EleYemian.jueseguanli, sleep_time=6)
                self.switch(*EleYemian.iframe_jueseguanli)
                self.send_keys(*EleJueseguanli.juese, value='生')    # 搜索角色/成员
                self.clear(*EleJueseguanli.juese, sleep_time=3)
                self.send_keys(*EleJueseguanli.chengyuan, value='0')
                self.clear(*EleJueseguanli.chengyuan)
                self.click(*EleJueseguanli.xinzengjuese)   # 新增角色
                self.send_keys(*EleJueseguanli.juesemingcheng, value='Py')
                self.click(*EleMobanleixing.queding, sleep_time=3)
                self.shift_slide(*EleJueseguanli.huadong)   # 修改角色
                self.click(*EleJueseguanli.xiugaitubiao)
                self.click(*EleJueseguanli.bianjimingcheng)
                self.clear(*EleJueseguanli.juesemingcheng)
                self.send_keys(*EleJueseguanli.juesemingcheng, value='Py1')
                self.click(*EleMobanleixing.queding, sleep_time=3)
                self.click(*EleJueseguanli.xiugaitubiao)   # 删除角色
                self.click(*EleJueseguanli.shanchu)
                self.click(*EleTongzhigonggao.querendaochu, sleep_time=6)
                self.click(*EleJueseguanli.tianjiachengyuan, sleep_time=6)    # 添加成员
                self.send_keys(*EleJueseguanli.sousuo, value=1, sleep_time=3)
                self.click(*EleJueseguanli.youeryuan, sleep_time=3)
                self.click(*EleJueseguanli.shanchutubiao, sleep_time=3)
                self.click(*EleJueseguanli.qingkong, sleep_time=3)
                self.click(*EleJueseguanli.youeryuan, sleep_time=3)
                self.click(*EleMobanleixing.queding, sleep_time=3)
                self.click(*EleJueseguanli.shezhi, sleep_time=3)    # 设置管理部门
                self.click(*EleMobanleixing.queding, sleep_time=3)
                self.click(*EleJueseguanli.shezhi, sleep_time=3)
                self.send_keys(*EleJueseguanli.sousuo, value=1, sleep_time=3)
                self.click(*EleJueseguanli.youeryuan, sleep_time=3)
                self.click(*EleMobanleixing.queding, sleep_time=3)
                self.click(*EleJueseguanli.danxuanyichu)    # 移除成员
                self.click(*EleJueseguanli.yichuchengyuan)
                self.click(*EleTongzhigonggao.querendaochu, sleep_time=3)
                self.click(*EleJueseguanli.duoxuanyichu)
                self.click(*EleJueseguanli.yichuchengyuan)
                self.click(*EleTongzhigonggao.querendaochu, sleep_time=3)
                self.switch_quit()

                # 应用管理case---(暂无)
                #
                # 成员部门case---展开部门---搜索成员---同步成员
                self.click(*EleYemian.shenpixitong)
                self.click(*EleYemian.chengyuanbumen, sleep_time=10)
                self.switch(*EleYemian.iframe_chengyuanbumen)
                self.click(*EleChengyuanbumen.quanbuzhankai, sleep_time=3)
                self.click(*EleChengyuanbumen.zhankai, sleep_time=3)
                self.click(*EleChengyuanbumen.zhankai, sleep_time=3)
                self.send_keys(*EleJueseguanli.chengyuan, value='1')
                self.enter(sleep_time=3)
                self.clear(*EleJueseguanli.chengyuan)
                self.enter(sleep_time=3)
                self.click(*EleChengyuanbumen.tongbu)
                self.click(*EleTongzhigonggao.querendaochu, sleep_time=60)

            except NoSuchElementException:  # 验证码错误-重新登录
                self.handle_captcha()
