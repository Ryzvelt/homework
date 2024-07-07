def generate_password(n):
    result = ""

    for i in range(1, 21):
        for j in range(i+1, 21):  
            if (i + j) % n == 0:  
                result += str(i) + str(j)
    return result
number = int(input("Введите число для пароля от 3 до 20: "))
while number < 3 or number > 20:
    number = int(input("Некорректный ввод. Введите число от 3 до 20: "))
password = generate_password(number)
print(f"Пароль для числа {number}: {password}")
print("Поздравляю, вы сбежали!")
