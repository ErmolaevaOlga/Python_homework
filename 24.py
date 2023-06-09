# В фермерском хозяйстве в Карелии выращивают чернику. Она растёт на круглой грядке,
# причём кусты высажены только по окружности. Таким образом, у каждого куста есть
# ровно два соседних. Всего на грядке растёт N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на
# них выросло различное число ягод — на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом,
# собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать
# за один заход собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.

# Input: 1 3 2 1 1 6
# Output: 10

m = [int(i) for i in input().split()]
result = []
for i in range(len(m) - 1):
    result.append(m[i - 1] + m[i] + m[i + 1])
result.append(m[len(m)-2] + m[len(m)-1] + m[0])
print(max(result))
    # if i == 0:
    #     result.append(m[-1] + m[i] + m[2])
