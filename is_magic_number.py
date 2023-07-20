def get_sum(number: int) -> int:
    if number < 10:
        return number
    tot_sum = 0
    while number > 0:
        rem = number % 10
        tot_sum += rem
        number //= 10

    return get_sum(tot_sum)


def is_magic_number(num: int) -> int:
    return get_sum(num) == 1


try:
    number = int(input("Please enter a number : "))
    print(is_magic_number(number))
except ValueError:
    print("Invalid Input. Enter only a number")
