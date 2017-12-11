import nester


class AthleteList(list):
    def __init__(self, a_name, a_dob=None, a_times=[]):
        list.__init__([])
        self.name = a_name
        self.dob = a_dob
        self.extend(a_times)

    def top3(self):
        return sorted(set([sanitize(t) for t in self]))[0:3]


def sanitize(time_string):
    if "-" in time_string:
        splitter = "-"
    elif ":" in time_string:
        splitter = ":"
    else:
        return time_string
    (mi, secs) = time_string.split(splitter)
    return mi + "." + secs


def getdata(filename):
    try:
        with open(filename) as f:
            data = f.readline()
            data = data.strip().split(",")
            return AthleteList(data.pop(0), data.pop(0), data)
    except IOError as err:
        print("IOError XD" + str(err))
        return None


james = getdata("james2.txt")
print(james.name + "'s fastest times is:" + str(james.top3()))