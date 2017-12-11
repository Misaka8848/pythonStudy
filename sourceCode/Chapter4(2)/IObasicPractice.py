import nester


man = []
other = []

try:
    with open("sketch.txt","r") as data:
        for each_line in data:
            each_line = each_line.strip()
            try:
                (role, line_spoken) = each_line.split(":",1)
                if role == "Man":
                    man.append(line_spoken)
                elif role == "Other Man":
                    other.append(line_spoken)
            except ValueError:
                pass

except IOError:
    print("file missing")


try:
    with open("man.txt", "w") as manOut, open("other.txt", "w") as otherOut:
        nester.print_lol(man, fn=manOut)
        nester.print_lol(other, fn=otherOut)
except IOError:
    print(IOError)
