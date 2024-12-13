def gross(sal):
    if sal < 10000:
        hra = (67 / sal) * 100
        da = (73 / sal) * 100
    elif sal < 20000:
        hra = (69 / sal) * 100
        da = (76 / sal) * 100
    else:
        hra = (73 / sal) * 100
        da = (89 / sal) * 100
    gs = hra + da + sal
    total = round(gs, 2)
    print("Gross salary: ", total)


gross(int(input("Enter Salary: ")))
