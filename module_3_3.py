def print_params(a = 1, b = 'string', c = True):
    print(a, b, c)


print_params(9)
print_params(8, 3)
print_params()
print_params(b = 25)
print_params([1, 2, 3])

values_list = [None, 8, 'string8']
values_dict = {'a': True, 'b': 29.90, 'c': 234}

print()
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [18.82, 'str']

print()
print_params(*values_list_2, 409)