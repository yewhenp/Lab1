import math

def read_values():
    """
    None -> (float, float, float, float)
    This func just read data from user
    """
    try:
        a = float(input("Enter a: "))
        b = float(input("Enter b: "))
        c = float(input("Enter c: "))
        acc = float(input("Enter accuracy (lesser than 1)(lesser = better): "))
        return a, b, c, acc
    except:
        print("Something is incorrect!")
        return 0, 0, 0, 1


def count_side(work_side, stable_tg, acc, check_tg):
    point = 2 * acc

    current_size = acc

    while point < work_side:
        current_size = stable_tg * point
        if check_size(current_size, work_side, check_tg, point):
            break

        point += acc

    return current_size


def check_size(size_of_squae, work_side, stable_tg, point):
    normal_heigh = stable_tg * (work_side - point - size_of_squae)
    if round(normal_heigh, 3) == round(size_of_squae):
        return  True
    else:
        return False


def find_edge(a, b, c):
    alpha_cos = (c ** 2 + b ** 2 - a ** 2) / (2 * c * b)
    beta_cos = (a ** 2 + c ** 2 - b ** 2) / (2 * a * c)
    gamma_cos = (a ** 2 + b ** 2 - c ** 2) / (2 * a * b)

    alpha_tg = math.tan(math.acos(alpha_cos))
    beta_tg = math.tan(math.acos(beta_cos))
    gamma_tg = math.tan(math.acos(gamma_cos))

    return alpha_tg, beta_tg, gamma_tg


def find_height(a, b, c):
    p = (a + b + c) / 2

    square = math.sqrt(p * (p - a) * (p - b) * (p - c))

    heigh_a = 2 * square / a
    heigh_b = 2 * square / b
    heigh_c = 2 * square / c

    return heigh_a, heigh_b, heigh_c


def main():
    a, b, c, acc = read_values()
    alpha_tg, beta_tg, gamma_tg = find_edge(a, b, c)

    heigh_a, heigh_b, heigh_c = find_height(a, b, c)
    side_a = a * heigh_a / (a + heigh_a)
    side_b = b * heigh_b / (b + heigh_b)
    side_c = c * heigh_c / (c + heigh_c)

    side = max(side_a, side_b, side_c)

    size1 = count_side(a, beta_tg, acc/10000, gamma_tg)
    size2 = count_side(c, alpha_tg, acc/10000, beta_tg)
    size3 = count_side(b, gamma_tg, acc/10000, alpha_tg)

    size = max(size1, size2, size3)

    print("Value, received by my method: ", size)
    print("Value, received by formula: ", side)
    print("Accurancy: ", abs(size - side))


main()