#coding=utf-8
with open("james.txt", "r") as jamesfile, open("julie.txt","r") as juliefile, open("mikey.txt","r") as mikeyfile, open("sarah.txt","r") as sarahfile:
    jamesdata = jamesfile.readline().strip().split(",")
    juliedata = juliefile.readline().strip().split(",")
    mikeydata = mikeyfile.readline().strip().split(",")
    sarahdata = sarahfile.readline().strip().split(",")
"""print(sorted(jamesdata))
print(sorted(juliedata))
print(sorted(mikeydata))
print(sorted(sarahdata))"""


def sanitize(time_string):
    if "-" in time_string:
        splitter = "-"
    elif ":" in time_string:
        splitter = ":"
    else:
        return (time_string)
    (min, secs) = time_string.split(splitter)
    return(min + "." + secs)


"""clean_james = []
clean_julie = []
clean_mikey = []
clean_sarah = []

for t in jamesdata:
    clean_james.append(sanitize(t))
for t in juliedata:
    clean_julie.append(sanitize(t))
for t in mikeydata:
    clean_mikey.append(sanitize(t))
for t in sarahdata:
    clean_sarah.append(sanitize(t))"""

mdata = sorted([sanitize(t) for t in mikeydata])
jdata = sorted([sanitize(t) for t in jamesdata])
judata = sorted([sanitize(t) for t in juliedata])
sdata = sorted([sanitize(t) for t in sarahdata])


def unique(list):
    unique_list= []
    for t in list:
        if t not in unique_list:
            unique_list.append(t)
    return unique_list

umikey = unique(mdata)
ujames = unique(jdata)
ujulie = unique(judata)
usarah = unique(sdata)

print(umikey[0:3])
print(ujames[0:3])
print(ujulie[0:3])
print(usarah[0:3])

    