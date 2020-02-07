"""
nymberstasks.py
All tasks from exam
"""


def main_1():
    """
    None -> (int, list(list))
    Main func for variant 1
    """
    kaprikar_list = kaprikar()
    rezz = []
    for i in kaprikar_list:
        for j in kaprikar_list:
            if i != j and palindrom(i*j):
                rezz.append(i*j)

    min_rez = min(rezz)

    return min_rez, all_nums_1(min_rez)


def kaprikar():
    """
    None -> list
    This func generates kapricar numbers between 1000 and 10000
    >>> kaprikar()
    [1000, 2223, 2728, 4879, 4950, 5050, 5292, 7272, 7777, 9999]
    """
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
            except ValueError:
                continue

    return rez_list


def palindrom(num):
    """
    int -> bool
    This func checks if the num is NOT a palindrom
    >>> palindrom(121)
    False
    >>> palindrom(1221)
    False
    >>> palindrom(1212)
    True
    >>> palindrom(1111110)
    True
    """
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
    """
    int -> list(list)
    Generates all possible x and y that x**2 + y**2 = num
    >>> all_nums_1(10)
    [[1, 3], [-1, -3], [1, -3], [-1, 3], [3, 1], [-3, -1], [3, -1], [-3, 1]]
    >>> all_nums_1(11)
    []
    """
    rez_list = []
    numbermaximum = int(num ** 0.5)
    for number1 in range(numbermaximum + 1):
        number2 = int((num - number1 ** 2) ** 0.5)
        if number1 ** 2 + number2 ** 2 == num:
            rez_list.append([number1, number2])
            rez_list.append([-1 * number1, -1 * number2])
            rez_list.append([number1, -1 * number2])
            rez_list.append([-1 * number1, number2])

    return rez_list


def main_2():
    """
    None -> (int, list(list))
    Main func for variant 2
    """
    leyland_list = sorted(list(leyland()))
    rezz = []
    for i in leyland_list:
        for j in leyland_list:
            if i != j and palindrom(i*j):
                rezz.append(i*j)

    rez_val = max(rezz)
    nums = all_nums_2(rez_val)
    return rez_val, nums


def leyland():
    """
    None -> list
    This func generates leyland numbers with 5 digits in it
    >>> leyland()
    [16580, 18785, 20412, 23401, 32993, 60049, 65792, 69632, 93312, 94932]
    """
    res_set = set()
    for number1 in range(2, 100):
        for number2 in range(2, 100):
            num = number1**number2 + number2**number1
            if len(str(num)) == 5:
                res_set.add(num)

    res_list = sorted(list(res_set))
    return res_list


def all_nums_2(num):
    """
    int -> list(list)
    Generates all possible x and y that x*y = num
    >>> all_nums_2(6)
    [[1, 6], [-1, -6], [2, 3], [-2, -3]]
    """
    list_rez = []
    for i in range(1, int(num ** 0.5) + 1):
        val = num // i
        if val * i == num:
            list_rez.append([i, val])
            list_rez.append([-1 * i, -1 * val])

    return list_rez


def main_3():
    """
    None -> (int, list(list))
    Main func for variant 3
    """
    threemorph = threemorpf()
    rezz = []
    for i in threemorph:
        for j in threemorph:
            if i != j and in_order(i*j):
                rezz.append(i*j)

    rez_val = max(rezz)

    return rez_val, all_nums_1(rez_val)


def threemorpf():
    """
    None -> list
    This func generates threemorpf numbers between 10000 and 100000
    >>> threemorpf()
    [18751, 31249, 40625, 49999, 50001, 59375, \
68751, 81249, 90624, 90625, 99999]
    """
    res_list = []
    for i in range(10000, 100000):
        cub = i * i * i
        if str(cub).endswith(str(i)):
            res_list.append(i)

    return res_list


def in_order(num):
    """
    int -> bool
    This func checks if digits in number goes in right order
    >>> in_order(12345)
    True
    >>> in_order(123345)
    True
    >>> in_order(12545)
    False
    """
    for i in range(len(str(num))):
        try:
            if int(str(num)[i]) > int(str(num)[i + 1]):
                return False
        except IndexError:
            continue

    return True


def main_4():
    """
    None -> (int, list(list))
    Main func for variant 4
    """
    autoamor = automorpf()
    rezz = []
    for i in autoamor:
        for j in autoamor:
            if i != j and check_num_4(i*j):
                rezz.append(i*j)

    min_rez = min(rezz)
    nums = all_nums_2(min_rez)
    return min_rez, nums


def automorpf():
    """
    None -> list
    This func generates automorpf numbers between 100000 and 1000000
    >>> automorpf()
    [109376, 890625]
    """
    res_list = []
    for i in range(100000, 1000000):
        quad = i * i
        if str(quad).endswith(str(i)):
            res_list.append(i)

    return res_list


def check_num_4(num):
    """
    int -> bool
    Htis func sums num and reversed num and start palindrom func for this value
    """
    reverse = 0
    for i in str(num)[::-1]:
        reverse += int(i)
        reverse *= 10
    reverse /= 10

    value = num + reverse

    return palindrom(value)


def choose_prog(val):
    """
    char -> None
    This func starts chosen program from exam
    """
    if val == "1":
        print(main_1())
    elif val == "2":
        print(main_2())
    elif val == "3":
        print(main_3())
    elif val == "4":
        print(main_4())
    elif val == "0":
        print("Goodbye!")
    else:
        print("Incorrect input!")


def main():
    """
    None -> None
    Main func of program
    """
    val = ""
    while val != "0":
        val = input("Please, enter a number of variant (1-4) or 0 to exit: ")
        choose_prog(val)


if __name__ == "__main__":
    main()
