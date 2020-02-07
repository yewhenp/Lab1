import math


def main_3():
    threemorph = threemorpf()
    rezz = []
    for i in threemorph:
        for j in threemorph:
            if i != j and check_num_1(i*j):
                rezz.append(i*j)

    rez_val = max(rezz)

    return rez_val, all_nums(rez_val)


def threemorpf():
    res_list = []
    for i in range(10000, 100000):
        cub = i * i * i
        if str(cub).endswith(str(i)):
            res_list.append(i)

    return res_list


def check_num_3(num):
    for i in range(len(str(num))):
        try:
            if int(str(num)[i]) > int(str(num)[i + 1]):
                return False
        except:
            continue

    return True


def all_nums_3(num):
    rez_list = []
    xyMax = int(num ** 0.5)
    for x in range(xyMax + 1):
        y = int((num - x ** 2) ** 0.5)
        if (x ** 2 + y ** 2 == num):
            rez_list.append([x, y])

    return rez_list


print(main_3())