import json


class Point:
    with open('/Users/case/point/point.json', 'r') as file:
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
    print(kcg)