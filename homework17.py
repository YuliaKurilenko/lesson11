def my_numbers(x):
    return  x % 2 and x ** 2
my_number = [1, 2, 5, 7, 12, 11, 35, 4, 89, 10]
result = map(my_numbers, filter(my_numbers,my_number))
# print(result)
print(list(result))
def they_numbers(x):
    return  x % 2 and x ** 2
they_number = [1, 25, 49, 121, 1225, 7921]
result = map(they_numbers, filter(they_numbers,they_number))
# print(result)
print(list(result))
