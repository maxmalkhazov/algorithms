num = int(input('Enter number: '))

def odd_and_even(num):
    num_str = str(num)
    odd_list = []
    even_list = []

    for digit in num_str:
        if int(digit) % 2 == 0:
            even_list.append(int(digit))
        else:
            odd_list.append(int(digit))

    return f' odd numbers: {odd_list}, even numbers: {even_list}. Total of odd numbers is {len(odd_list)} and total of even numbers is {len(even_list)}.'

print(odd_and_even(num))