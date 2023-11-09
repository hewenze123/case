import json


class Point:
    with open('/Users/wen/Downloads/case/point/point.json', 'r') as file:
        f = json.load(file)

    a = f['A']['a']
    b = f['B']['b']
