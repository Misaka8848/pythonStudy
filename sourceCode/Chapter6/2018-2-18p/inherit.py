def sanitize(ts):
    if ',' in ts:
        splitter = ','
    elif '-' in ts:
        splitter = '-'
    else:
        return ts
    (mi,sec) = ts.split(splitter)
    return mi + '.' + sec


# 继承Python内置的list类
class namedList(list): # 提供一个要继承的类
    def __init__(self, a_name, a_dob, a_speed):
        list.__init__([])
        self.name = a_name
        self.a_dob = a_dob
        self.speed = a_speed

    def to3(self):
        return [sanitize(self.speed) for t in self.speed ]
    def
