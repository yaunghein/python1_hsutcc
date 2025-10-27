# x = float(input(""))

# if (x % 2 == 0):
#     if (x % 3 != 0):
#         print("B")
#     else:
#         print("C")
# else:
#     print("D")

# number = 2
# while number <= 20:
#     print(number)
#     number += 2

# current_pm = int(input(""))
# if (current_pm >= 5 and current_pm <= 9):
#     print("OPEN")
# else:
#     print("CLOSED")

# number_of_left_socks = int(input(""))
# number_of_right_socks = int(input(""))
# print(min(number_of_left_socks, number_of_right_socks))

# score = int(input(""))
# if (score >= 0 and score <= 40):
#     print("Emerging")
# elif (score > 40 and score <= 80):
#     print("Developing")
# else:
#     print("Achieved")

# apple_cakes = int(input(""))
# orange_cakes = int(input(""))
# bag_one_size = int(input(""))
# bag_two_size = int(input(""))

# if ((apple_cakes <= bag_one_size and orange_cakes <= bag_two_size)
#         or (apple_cakes <= bag_two_size and orange_cakes <= bag_one_size)):
#     print("YES")
# else:
#     print("NO")

# number = int(input(""))
# while number > 0:
#     print(number)
#     number -= 1

# number = int(input(""))
# sum_of_squares = 0
# for i in range(1, number + 1):
#     sum_of_squares += i ** 2
# print(sum_of_squares)

# iterations = int(input(""))
# sum = 0
# for i in range(iterations):
#     number = int(input(""))
#     sum += number
# print(sum)

# start_number = int(input(""))
# end_number = int(input(""))
# for i in range(start_number, end_number + 1):
#     if i % 2 == 0:
#         print(i)

# number_of_integers = int(input(""))
# zero_count = 0
# for i in range(number_of_integers):
#     number = int(input(""))
#     if number == 0:
#         zero_count += 1
# print(zero_count)

# total_heroes = int(input(""))
# heroes = []
# for i in range(total_heroes - 1):
#     hero_number = int(input(""))
#     heroes.append(hero_number)
# for i in range(1, total_heroes + 1):
#     if i not in heroes:
#         print(i)

# integer_one = int(input(""))
# integer_two = int(input(""))
# print(str(integer_one) + str(integer_two), integer_one + integer_two)

# letters = input("")
# index = int(input("")) - 1
# print(letters[index])

# original_text = input("")
# text_to_insert = input("")
# index_to_insert = len(original_text) // 2
# new_text = (original_text[:index_to_insert] +
#             text_to_insert + original_text[index_to_insert:])
# print(new_text)

# original_text = input("")
# index_to_split = len(original_text) // 2
# print(original_text[index_to_split:] + original_text[:index_to_split])

# text = input("")
# middle_index = len(text) // 2
# print(text[middle_index - 1:middle_index + 2])

# text = input("")
# for index in range(len(text)):
#     print(text[index])

# string = input("")
# respectfulness = 0
# for character in string:
#     if (character == "f"):
#         respectfulness += 1
# print(respectfulness)

# result = input("")
# alice_wins = 0
# bob_wins = 0
# for character in result:
#     if character == "A":
#         alice_wins += 1
#     elif character == "B":
#         bob_wins += 1
#     else:
#         pass
# if alice_wins > bob_wins:
#     print("ALICE")
# elif bob_wins > alice_wins:
#     print("BOB")
# else:
#     print("DRAW")

# original_word = input("")
# reversed_word = ""
# index = len(original_word) - 1
# while index >= 0:
#     reversed_word += original_word[index]
#     index -= 1
# if original_word == reversed_word:
#     print("YES")
# else:
#     print("NO")

# text = input("")
# print("_".join(text))

# number_of_elements = int(input(""))
# numbers = list(map(int, input().split()))
# index = int(input(""))
# print(numbers[index])

# number_of_elements = int(input(""))
# numbers = list(map(int, input().split()))
# increase_by = int(input(""))
# for i in range(number_of_elements):
#     numbers[i] += increase_by
# print(" ".join(map(str, numbers)))

# number_of_elements = int(input(""))
# numbers = list(map(int, input().split()))
# even_indices_numbers = []
# for i in range(number_of_elements):
#     if i % 2 == 0:
#         even_indices_numbers.append(numbers[i])
# print(" ".join(map(str, even_indices_numbers)))

# number_of_elements = int(input(""))
# numbers = list(map(int, input().split()))
# even_numbers = []
# for index in range(number_of_elements):
#     if numbers[index] % 2 == 0:
#         even_numbers.append(numbers[index])
# print(" ".join(map(str, even_numbers)))

# number_of_elements = int(input(""))
# numbers = list(map(int, input().split()))
# distinct_integers = []
# for index in range(number_of_elements):
#     if numbers[index] not in distinct_integers:
#         distinct_integers.append(numbers[index])
# print(len(distinct_integers))

# number_of_elements = int(input(""))
# numbers = list(map(int, input().split()))
# sign = None
# has_same_sign_pair = 'NO'
# for number in numbers:
#     if (sign is None):
#         sign = 'plus' if number >= 0 else 'minus'
#         continue
#     if (number >= 0 and sign == 'plus') or (number < 0 and sign == 'minus'):
#         has_same_sign_pair = "YES"
#         break
#     else:
#         sign = 'plus' if number >= 0 else 'minus'
# print(has_same_sign_pair)
