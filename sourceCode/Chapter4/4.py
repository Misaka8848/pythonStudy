import pickle
import nester
man = []
other = []
try:
    with open("sketch.txt") as data:
        for each_line in data:
            try:
                (role, line_spoken) = each_line.split(":", 1)
                line_spoken = line_spoken.strip()
                if role == "Man":
                    man.append(line_spoken)
                elif role == "Other Man":
                    other.append(line_spoken)
            except ValueError:
                pass
except IOError as err:
    print("GG" + str(err))
"""try:
    with open("man.pickle","wb") as man_file,open("other.pickle", "wb") as other_file:
        pickle.dump(man,file =man_file)
        pickle.dump(other,file = other_file)
except IOError as err :
    print("File error :"+str(err))"""
with open("man.txt","w") as man_file,open("othet.txt", "w") as other_file:
    nester.print_lol(man,fn=man_file)
    nester.print_lol( other,fn=other_file)
