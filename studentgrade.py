project = int(input("Project marks: "))
internal = int(input("Internal marks: "))
external = int(input("external marks: "))
if project >= 50 and internal >= 50 and external >= 50:
    pro = (70/100) * project
    inter = (10/100) * internal
    ext = (20/100) * external
    res = pro+inter+ext
    print(res)
    if res > 90:
        print("Grade is A")
    elif res > 80:
        print("Grade is B")
    else:
        print("Grade is C")
elif internal < 50:
    print("Failed in internal")
elif external < 50:
    print("Failed in external")
else:
    print("Failed in project")
