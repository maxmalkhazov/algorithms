first_list = [1, 6, 7, 37, 4]
second_list = [523, 44]

print(first_list)
print(second_list)

print(first_list + second_list)

print(first_list[2])
print(first_list[-2])

first_list.append(199)

# first_list.clear()

print(first_list.count(6))

print(first_list.index(37))


first_list.insert(1, 99)
print(first_list)

first_list.pop(3)
print(first_list)

first_list.remove(37)
print(first_list)

first_list.reverse()
print(first_list)

first_list.sort()
print(first_list)