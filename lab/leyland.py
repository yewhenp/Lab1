import math


def main_2():
    leyland_list = sorted(list(leyland()))
    rezz = []
    for i in leyland_list:
        for j in leyland_list:
            if i != j and check_num_2(i*j):
                rezz.append(i*j)

    rez_val = max(rezz)
    nums = all_nums_2(rez_val)
    return rez_val, nums


def leyland():
    res_set = set()
    for x in range(2, 100):
        for y in range(2, 100):
            num = x**y + y**x
            if len(str(num)) == 5:
                res_set.add(num)

    return res_set


def check_num_2(num):
    if len(str(num)) % 2 == 0:
        for i in range(len(str(num)) // 2):
            if str(num)[i] != str(num)[len(str(num)) - i - 1]:
                return True
    else:
        for i in range((len(str(num)) - 1) // 2):
            if str(num)[i] != str(num)[len(str(num)) - i - 1]:
                return True
    return False


def all_nums_2(num):
    list_rez = []
    for i in range(1, int(num ** 0.5)):
        val = num // i
        if val * i == num:
            list_rez.append([i, val])
            list_rez.append([-1 * i, -1 * val])

    return list_rez

    return rez_list


#print(all_nums_2(500))
print(main_2())