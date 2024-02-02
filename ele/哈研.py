class EleDenglu:  # 登录
    ceshi_url = 'https://k12wx.xzxyun.com/campus-mng/loginsaas'  # 测试地址
    yufabu_url = 'https://yfb.xzxyun.com/campus-mng/loginSaas?'  # 预发布地址
    s_url = 'https://www.12306.cn/index/index.html'  # 生产地址
    yanzhengma = ("xpath", '//*[@id="app"]/div/div[2]/div/div/div[3]/form/div[3]/img')  # 验证码
    shuru = ("xpath", '//*[@id="app"]/div/div[2]/div/div/div[3]/form/div[3]/div/div/div[1]/input')  # 输入验证码
    dukaqi = ("xpath", '//*[@id="app"]/div/div[2]/header/div[2]/a[1]/span')  # 读卡器


class EleXuexiaoguanliyuan:  # 学校管理员
    zhanghao = ('xpath', '//*[@id="pane-2"]/div/div/div[1]/div/div[1]/div[1]/input')  # 输入账号
    chaxun = ('xpath', '//*[@id="pane-2"]/div/div/div[1]/div/div[1]/button[1]')  # 查询


class EleYemian:  # iframe/页面
    iframe_tongzhigonggao = ('xpath',  # 通知公告
                             "//iframe[contains(@src, '/api/basic/account/login-by-xzxyun?1=homeSchool/notice')]")
    iframe_zuoyepindao = ('xpath',  # 作业频道
                          "//iframe[contains(@src, '/api/basic/account/login-by-xzxyun?1=homeSchool/homework')]")
    iframe_mobanleixing = ('xpath',  # 模版类型
                           "//iframe[contains(@src, '/api/basic/account/login-by-xzxyun?1=templateManagement"
                           "/templateType')]")
    iframe_mobanzhongxin = ('xpath',  # 模版中心
                            "//iframe[contains(@src, '/api/basic/account/login-by-xzxyun?1=templateManagement"
                            "/templateCenter')]")
    iframe_mobanpeizhi = ('xpath',  # 模版配置
                          "//iframe[contains(@src, '/api/basic/account/login-by-xzxyun?1=templateManagement"
                          "/templateSettingList')]")

    iframe_shujuguanli = ('xpath',  # 数据管理
                          "//iframe[contains(@src, '/api/basic/account/login-by-xzxyun?1=dataManagement/index')]")
    iframe_jueseguanli = ('xpath',  # 角色管理
                          "//iframe[contains(@src, '/api/basic/account/login-by-xzxyun?1=organization"
                          "/roleManagement')]")
    iframe_yingyongguanli = ('xpath',  # 应用管理
                             "//iframe[contains(@src, '/api/basic/account/login-by-xzxyun?1=applicationManagement"
                             "/index')]")
    iframe_chengyuanbumen = ('xpath',  # 成员部门
                             "//iframe[contains(@src, '/api/basic/account/login-by-xzxyun?1=organization"
                             "/departmentMember')]")

    jiaxiaohudong = ('xpath', "//span[contains(text(),'家校互动管理')]")  # 家校互动
    tongzhigonggao = ('xpath', "//span[contains(text(),'通知公告')]")  # 通知公告
    zuoyepindao = ('xpath', "//span[text()='作业频道']")  # 作业频道
    mobanleixing = ('xpath', "//span[text()='模版类型']")  # 模版类型
    mobanzhongxin = ('xpath', "//span[text()='模版中心']")  # 模版中心
    mobanpeizhi = ('xpath', "//span[text()='模版配置']")  # 模版配置

    shenpixitong = ('xpath', "//span[contains(text(),'审批系统')]")  # 审批系统
    shujuguanli = ('xpath', "//span[contains(text(),'数据管理')]")  # 数据管理
    jueseguanli = ('xpath', "//span[contains(text(),'角色管理')]")  # 角色管理
    yingyongguanli = ('xpath', "//span[contains(text(),'应用管理')]")  # 应用管理
    chengyuanbumen = ('xpath', "//span[contains(text(),'成员部门')]")  # 成员部门


class EleTongzhigonggao:  # 通知公告
    faburen = ('xpath', "//input[contains(@class, 'el-input__inner') and @placeholder='请输入发布人']")  # 发布人
    biaoti = (  # 标题
        'xpath',
        "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[2]/div[1]/div[1]/div[1]/input[1]")
    kaishishijian = ('xpath', '//input[@placeholder="开始时间"]')  # 开始时间
    jieshushijian = ('xpath', '//input[@placeholder="结束时间"]')  # 结束时间
    sousuo = ('xpath', "//span[@class='' and text()=' 搜索 ']")  # 搜索
    chongzhi = ('xpath', "//span[@class='' and text()=' 重置 ']")  # 重置
    daochu = ('xpath', "//button[@class='el-button el-button--warning is-plain']")  # 导出
    querendaochu = ('xpath', '//span[text()="确认"]')  # 确认导出
    chakan = ('xpath', '(//span[text()=" 查看 "])[1]')  # 查询
    chakanmingxi = ('xpath', "/html/body/div[1]/div/div[1]/div/div/div/div[6]/div[2]/div[2]/button[2]/span")  # 查看明细
    guanbimingxi = ('xpath', '/html/body/div[3]/div/div/header/button')  # 关闭图标
    xiazaimingxi = ('xpath', '/html/body/div[1]/div/div[1]/div/div/div/div[6]/div[2]/div[2]/button[1]/span')  # 下载明细
    fanhui = ('xpath', '/html/body/div[1]/div/div[1]/div/div/div/div[1]/button')  # 返回


class EleZuoyepindao:  # 作业频道
    xueke = ('xpath', "//input[@placeholder='请选择']")  # 学科/请选择


class EleMobanleixing:  # 模版类型
    leixingmingcheng = ('xpath', "//input[@type='text' and @placeholder='请输入类型名称' and not(@maxlength)]")  # 类型名称
    leixingmingcheng2 = ('xpath', "//input[@type='text' and @placeholder='请输入类型名称' and @maxlength='10']")  # 类型名称2
    chaxun = ('xpath', "//button[contains(@class, 'el-button--primary') and contains(span, '查询')]")  # 查询
    jinyong = ('xpath', "//span[@class='el-switch__core']")  # 禁用
    xinzeng = ('xpath', "//button[@class='el-button el-button--primary is-plain' and contains(span, '新增')]")  # 新增
    queding = ('xpath', "//span[text()='确 定']")  # 确定
    xiugai = ("xpath",  # 修改
              "/html/body/div[1]/div/div[1]/div/div/div[2]/div[2]/div[1]/div[3]/div/div[1]/div/table/tbody/tr[1]/td["
              "3]/div/button[1]/span")
    shanchu = ("xpath",  # 删除
               "/html/body/div[1]/div/div[1]/div/div/div[2]/div[2]/div[1]/div[3]/div/div[1]/div/table/tbody/tr[1]/td["
               "3]/div/button[2]/span")


class EleMoBanzhongxin:  # 模版中心
    mobanleixing = ('xpath', '//input[contains(@placeholder, "模板类型") and @type="text"]')  # 模版类型
    xiangqing = ('xpath',  # 详情
                 "/html/body/div[1]/div/div[1]/div/div/div[2]/div[2]/div[1]/div[3]/div/div[1]/div/table/tbody/tr["
                 "1]/td[5]/div/button[1]/span")
    fanhui = ('xpath', "/html/body/div[1]/div/div[1]/div/div/div[1]/div[2]/button/span")  # 返回
    shanchu = ('xpath',  # 删除
               "/html/body/div[1]/div/div[1]/div/div/div[2]/div[2]/div[1]/div[3]/div/div[1]/div/table/tbody/tr[1]/td["
               "5]/div/button[3]/span")
    xiugai = ('xpath',  # 修改
              "/html/body/div[1]/div/div[1]/div/div/div[2]/div[2]/div[1]/div[3]/div/div[1]/div/table/tbody/tr[1]/td["
              "5]/div/button[2]/span")
    mobanmingcheng = ('xpath', '//input[contains(@placeholder, "模板名称（必填）") and @type="text"]')  # 模版名称
    neirong = ('xpath', "//textarea[@class='el-textarea__inner' and @placeholder='内容（必填）']")  # 内容
    tingyong = ('xpath', "/html/body/div[1]/div/div[1]/div/div/div[2]/form/div[2]/div/div/label[2]/span[1]/span")  # 停用
    tijiao = ('xpath', "/html/body/div[1]/div/div[1]/div/div/div[4]/button[2]/span")  # 提交


class EleMoBanpeizhi:  # 模版配置
    yingyongmingcheng = ('xpath', '//input[contains(@placeholder, "请输入应用名称") and @type="text"]')  # 应用名称
    peizhi = ('xpath',  # 配置
              '/html/body/div/div/div[1]/div/div/div[2]/div/div[1]/div[3]/div/div[1]/div/table/tbody/tr/td['
              '4]/div/button/span')

    tianjiamobanleixing = ('xpath', "//span[text()=' +添加模板类型 ']")  # 添加模版类型
    quanxuanleixing = ('xpath', "/html/body/div[2]/div/div/div/div/div[1]/div[2]/table/thead/tr/th["  # 全选类型
                                "1]/div/label/span/span")
    leixingbaocun = ('xpath', "/html/body/div[2]/div/div/footer/div/button[2]/span")  # 保存类型
    tianjiamoban = ('xpath', "//span[text()=' 添加模板 ']")  # 添加模版
    danxuanmoban = ('xpath', "/html/body/div[3]/div/div/div/div[2]/div[2]/div[1]/div/div[2]/button/span")  # 单选模版
    mobanbaocun = ('xpath', "/html/body/div[3]/div/div/footer/div/button[2]")  # 保存模版
    shanchumoban = ('xpath', "/html/body/div[3]/div/div/div/div[1]/div[3]/div/div[2]/button/span")  # 删除模版
    yichuleixing = ('xpath', "//span[text()=' 移除类型 ']")  # 移除类型
    moban2 = ('xpath', "/html/body/div[1]/div/div[1]/div/div/div[4]/div[2]/div/div[1]/div")  # 模版2
    tijiao = ('xpath', "/html/body/div[1]/div/div[1]/div/div/div[5]/button[2]/span")  # 提交
    guanbi = ('xpath', "//span[text()=' 关闭 ']")  # 关闭


class EleShujuguanli:  # 数据管理
    tijiaoren = ('xpath', '//input[@class = "el-input__inner" and @placeholder="请输入姓名"]')  #
    shenqingbianhao = ('xpath', '//input[@class = "el-input__inner" and @placeholder="请输入编号"]')  #
    zhuangtai = ('xpath', "/html/body/div[1]/div/div[1]/div/div/div[1]/form/div[2]/div/div/div/div")

    shenhezhong = ('xpath', "//li[contains(span, '审核中')]")
    yitongguo = ('xpath', "//li[contains(span, '已通过')]")
    yibohui = ('xpath', "//li[contains(span, '已驳回')]")
    yichexiao = ('xpath', "//li[contains(span, '已撤销')]")
    kaishishijian = ('xpath', '/html/body/div[1]/div/div[1]/div/div/div[1]/form/div[5]/div[2]/div/input[1]')  # 开始时间
    jieshushijian = ('xpath', '/html/body/div[1]/div/div[1]/div/div/div[1]/form/div[5]/div[2]/div/input[2]')  # 结束时间
    xiangqing = ('xpath', '//span[text()=" 详情 "]')  #
    fanhui = ('xpath', '//span[text()=" 返回 "]')  #
    shanchu = ('xpath', '//span[text()=" 删除 "]')  #


class EleJueseguanli:  # 数据管理
    juese = ('xpath', "//input[@placeholder='搜索角色']")
    chengyuan = ('xpath', "//input[@placeholder='搜索成员姓名、学工号']")
    xinzengjuese = ('xpath', '//span[text()=" 新增角色 "]')
    juesemingcheng = ('xpath', "//input[@placeholder='请输入角色名称']")
    huadong = ('xpath', '/html/body/div[1]/div/div[1]/div/div/div[1]/div[1]/div[2]/div/div[1]/div/div/div[1]/div['
                        '2]/div/div[1]/div/table/tbody/tr[1]/td[1]/div')
    xiugaitubiao = ('xpath', '//html/body/div[1]/div/div[1]/div/div/div[1]/div[1]/div[2]/div/div[1]/div/div/div['
                             '1]/div[2]/div/div[1]/div/table/tbody/tr[1]/td[2]/div/i')
    bianjimingcheng = ('xpath', '/html/body/div[3]/div[2]/div/div[1]')
    shanchu = ('xpath', '/html/body/div[3]/div[2]/div/div[2]')
    tianjiachengyuan = ('xpath', '//span[text()=" 添加成员 "]')
    sousuo = ('xpath', '//input[@placeholder="搜索"]')
    youeryuan = ('xpath', '/html/body/div[4]/div/div/div/div[2]/div[1]/div[2]/div[2]/div/div[1]/div/div[2]/div/label['
                          '1]/span/span')
    shanchutubiao = ('xpath', '//html/body/div[4]/div/div/div/div[2]/div[2]/div[2]/div/div/div[1]/div/div['
                              '1]/div/div/i[2]')
    qingkong = ('xpath', '//span[text()=" 清空 "]')
    shezhi = ('xpath', '//span[text()=" 设置 "]')
    yichuchengyuan = ('xpath', '//span[text()=" 移除成员 "]')
    danxuanyichu = ('xpath', '/html/body/div[1]/div/div[1]/div/div/div[1]/div[2]/div[3]/div[1]/div[3]/div/div['
                             '1]/div/table/tbody/tr[1]/td[1]/div/label/span/span')
    duoxuanyichu = ('xpath', '/html/body/div[1]/div/div[1]/div/div/div[1]/div[2]/div[3]/div[1]/div['
                             '2]/table/thead/tr/th[1]/div/label/span/span')


class EleChengyuanbumen:  # 成员部门
    quanbuzhankai = ('xpath', "//span[contains(@class, 'span-color') and text()='全部展开']")
    zhankai = ('xpath', "/html/body/div[1]/div/div[1]/div/div/div/div/div[1]/div[2]/div/div[1]/div/div/div[1]/div[1]")
    tongbu = ('xpath', '//span[text()=" 同步 "]')