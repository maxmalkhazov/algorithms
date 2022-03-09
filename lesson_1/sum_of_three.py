from random import randint

number = randint(100,999)


# convert int to str
# number_str = str(number)

# result = []
final_result = 0

for digit in str(number):
    final_result += int(digit)

# put digits in a list
# for digit in number_str:
  #  result.append(digit)

# convert digits to int and sum
# for digit in result:
  #  final_result += int(digit)

print(number)
# print(result)
print(final_result)