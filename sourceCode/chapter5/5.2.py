def getdata(filename):
    try:
        with open(filename) as f:
            data = f.readline()
            data = data.strip().split(",")
    except IOError as err:
        print("IOError XD"+ str(err))
        return(None)
    return data


def sanitize(time_string):
    if "-" in time_string:
        splitter = "-"
    elif ":" in time_string:
        splitter = ":"
    else:
        return (time_string)
    (min, secs) = time_string.split(splitter)
    return(min + "." + secs)


def unique(list):
    unique_list= []
    for t in list:
        if t not in unique_list:
            unique_list.append(t)
    return unique_list


jdata = [sanitize(t) for t in getdata("james.txt")]
print(sorted(unique(jdata))[0:3])


