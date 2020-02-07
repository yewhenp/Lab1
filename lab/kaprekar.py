def main_1():
    kaprikar_list = kaprikar()
    rezz = []
    for i in kaprikar_list:
        for j in kaprikar_list:
            if i != j and check_num_1(i*j):
                rezz.append(i*j)

    min_rez = min(rezz)

    return  min_rez, all_nums_1(min_rez)


def kaprikar():
    rez_list = []
    for i in range(1000, 10000):
        value = i ** 2
        first_val = ""
        second_val = str(value)
        counter = 1

        for elem in str(value):
            first_val += elem
            second_val = second_val[counter::]

            try:
                if int(first_val) + int(second_val) == i:
                    rez_list.append(i)
            except:
                continue

    return rez_list


def check_num_1(num):
    if len(str(num)) % 2 == 0:
        for i in range(len(str(num)) // 2):
            if str(num)[i] != str(num)[len(str(num)) - i - 1]:
                return True
    else:
        for i in range((len(str(num)) - 1) // 2):
            if str(num)[i] != str(num)[len(str(num)) - i - 1]:
                return True
    return False


def all_nums_1(num):
    rez_list = []
    xyMax = int(num ** 0.5)
    for x in range(xyMax + 1):
        y = int((num - x ** 2) ** 0.5)
        if (x ** 2 + y ** 2 == num):
            rez_list.append([x, y])

    return rez_list



print(main_1())