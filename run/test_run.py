import pytest
from case.云平台 import TestYunpingtai
from case.哈研 import TestJiaxiaohudong


class Test_SaaS:
    def test_guanliyuanyujuese(self):  # 管理员与角色
        lp = TestYunpingtai()
        lp.test_guanliyuanyujuese()

    def test_jichuxinxiguanli(self):  # 基础信息管理
        lp = TestYunpingtai()
        lp.test_jichuxinxiguanli()

    def test_jiaxiaohudong(self):  # 家校互动管理
        lp = TestJiaxiaohudong()
        lp.test_jiaxiaohudong()

    def test_shenpixitong(self):  # 审批系统
        lp = TestJiaxiaohudong()
        lp.test_shenpixitong()


if __name__ == '__main__':
    pytest.main(['-s', './'])
