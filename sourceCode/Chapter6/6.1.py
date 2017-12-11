class Athlete:
    def __init__(self, a_name, a_dob=None, a_Times=[0]):
        self.name = a_name
        self.dob = a_dob
        self.Times = a_Times

    def top3(self):
        return sorted({sanitize(t) for t in self.Times})[0:3]

    def add_Time(self, add_data):
        self.Times.append(add_data)

    def add_Times(self, add_list):
        self.Times.extend(add_list)


def getdata(filename):
    try:
        with open(filename) as f:
            data = f.readline()
            data = data.strip().split(",")
            return Athlete(data.pop(0), data.pop(0), data)
    except IOError as err:
        print("IOError XD" + str(err))
        return None


def sanitize(time_string):
    if "-" in time_string:
        splitter = "-"
    elif ":" in time_string:
        splitter = ":"
    else:
        return time_string
    (mi, secs) = time_string.split(splitter)
    return mi + "." + secs


sarah = getdata("sarah2.txt")
mikey = getdata("mikey2.txt")
print(sarah.top3())
sarah.add_Time("1")
print(sarah.top3())
sarah.add_Times(["1", "2"])
print(sarah.top3())