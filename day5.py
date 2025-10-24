x = int(input(""))

is_even = (x % 2 == 0)
is_divisible_by_3 = (x % 3 == 0)
is_not_divisible_by_3 = (x % 3 != 0)

if (is_even and is_not_divisible_by_3):
    print("B")
elif (is_even and is_divisible_by_3):
    print("C")
elif (is_even):
    print("A")
else:
    print("D")
