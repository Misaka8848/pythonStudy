import nester

# 字符串规整，返回格式化字符串
def sanitize(time_string):
    if "-" in time_string:
        splitter = "-"
    elif ":" in time_string:
        splitter = ":"
    else:
        return time_string
    (min, secs) = time_string.split(splitter)
    return min + "." + secs


class AthleteList(list):
    def __init__(self, a_name, a_dob=None, a_time=[]):
        list.__init__([])
        self.name = a_name
        self.dob = a_dob
        self.extend(a_time)

    def top3(self):
        return sorted(set([sanitize(t) for t in self]))[0:3]


# 返回选手数据字典
def get_coatch_data(filename):
    try:
        with open(filename) as f:
            data = f.readline()
        d_l = data.strip().split(",")
        return AthleteList(d_l.pop(0), d_l.pop(0), d_l)
    except IOError as ioerr:
        print("File error: " + str(ioerr))
        return None


sarah = get_coatch_data("sarah2.txt")
print(sarah.name + " 's birthday is " + sarah.dob, end="")
print(" and she's fast times are: ", end="")

