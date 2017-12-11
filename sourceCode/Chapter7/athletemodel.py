import sys
sys.path.append(r"C:\Users\han1\PycharmProjects\HeadFirstPython\AthleteList")
from AthleteList import AthleteList
import pickle
def getdata(filename):
    try:
        with open(filename) as f:
            data = f.readline()
            data = data.strip().split(",")
            return AthleteList(data.pop(0), data.pop(0), data)
    except IOError as err:
        print("IOError XD" + str(err))
        return None


def put_to_store(file_list):
    all_athletes = {}
    for t in file_list:
        ath = getdata(t)
        all_athletes[ath.name] = ath
    try:
        with open("athletes.pickle","wb") as athf:
            pickle.dump(all_athletes,athf)
    except IOError as err:
        print("IO error(get_from_store)" + str(err))
    return all_athletes


def get_from_store():
    all_athletes = {}
    try:
        with open("athletes.pickle", "rb") as athf:
            all_athletes = pickle.load(athf)
    except IOError as err:
        print("IO error(get_from_store)" + str(err))
    return all_athletes





