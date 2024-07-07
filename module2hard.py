def generate_password(n):
    result = ''
    for i in range(1, 21):
        for j in range(i, 21):
            if (i + j) <= 20 and n % (i + j) == 0:
                result += str(i) + str(j)
    return result

for n in range(3, 21):
    print(f"{n} - {generate_password(n)}")