import json


class Point:
    with open(r'C:\Users\Administrator\Desktop\case\point\point.json', 'r', encoding='utf-8') as file:
        f = json.load(file)

    kca = f['课程']['添加']
    kcb = f['课程']['输入']
    kcc = f['课程']['备注']
    kcd = f['课程']['新增']
    kce = f['课程']['修改']
    kcf = f['课程']['删除']
    kcg = f['课程']['确定']

    dla = f['登录']['账号']
    dlb = f['登录']['密码']
    dlc = f['登录']['登录']

    tz_faburen = f['通知']['发布人']
    tz_biaoti = f['通知']['标题']
    tz_sousuo = f['通知']['搜索']
    tz_chongzhi = f['通知']['重置']
    tz_daochu = f['通知']['导出']
    tz_querendaochu = f['通知']['确认导出']
    tz_querendaochu2 = f['通知']['确认导出2']
    tz_chakan = f['通知']['查看']
    tz_fanhui = f['通知']['返回']
    tz_xiazaimingxi1 = f['通知']['下载明细1']
    tz_chakanmingxi1 = f['通知']['查看明细1']
    tz_xiazaimingxi2 = f['通知']['下载明细2']
    tz_chakanmingxi2 = f['通知']['查看明细2']
    tz_querenxiazai = f['通知']['确认下载']
    tz_tupian = f['通知']['图片']
    tz_xiazaitupian = f['通知']['下载图片']
    tz_suoxiao = f['通知']['缩小']
    tz_fangda = f['通知']['放大']
    tz_quanping = f['通知']['全屏']
    tz_xiazai = f['通知']['下载']
    tz_zuoxuanzhuan = f['通知']['左旋转']
    tz_youxuanzhuan = f['通知']['右旋转']
    tz_guanbitupian = f['通知']['关闭图片']
    print(kcg)