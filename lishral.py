def main_4():
    autoamor = automorpf()
    rezz = []
    for i in autoamor:
        for j in autoamor:
            if i != j and check_num_4(i*j):
                rezz.append(i*j)

    min_rez = min(rezz)
    nums = all_nums_4(min_rez)
    return  min_rez, nums


def automorpf():
    res_list = []
    for i in range(100000, 1000000):
        quad = i * i
        if str(quad).endswith(str(i)):
            res_list.append(i)

    return res_list


def check_num_4(num):
    reversed = 0
    for i in str(num)[::-1]:
        reversed += int(i)
        reversed *= 10
    reversed /= 10

    value = num + reversed

    if len(str(value)) % 2 == 0:
        for i in range(len(str(value)) / 2):
            if str(value)[i] != str(value)[len(str(value)) - i]:
                return False

    return True

def all_nums_4(num):
    list_rez = []
    for i in range(1, int(num ** 0.5)):
        val = num // i
        if val * i == num:
            list_rez.append([i, val])
            list_rez.append([-1 * i, -1 * val])

    return list_rez



print(main_4())