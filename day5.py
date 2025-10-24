x = float(input(""))

is_even = x % 2 == 0
is_divisible_by_3 = x % 3 == 0
is_not_divisible_by_3 = x % 3 != 0

if (is_even):
    if (is_not_divisible_by_3):
        print("B")
    else:
        print("C")
else:
    print("D")
