numbers = []
for index in range(1, 101):
    if ((index % 2 != 0) and (index % 3 == 0)):
        continue
    numbers.append(index)
print(numbers)
print(len(numbers))
