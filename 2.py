# Задача 2: Найдите сумму цифр трехзначного числа.
# *Пример:*

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

number = int(input("Введите трехзначное число: "))

fist_number = number // 100
second_number = (number // 10) % 10
fird_number = number % 10

print(f"{fist_number} + {second_number} + {fird_number} = {fist_number+second_number+fird_number}")