role = []
line_spoken = []
try:
    with open("sketch.txt", "r") as data:
        for each_line in data:
            try:
                (role, line_spoken) = each_line.split(":", 1)  #多重赋值
                print(role, end="")
                print(" said :", end="")
                print(line_spoken, end="")
            except:
                pass
except IOError as err:
    print("reason" + err)
help(each_line.split)

