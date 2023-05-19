song = 'пара-ра-рам рам-пам-папам па-ра-па-да'
vowel = 'уеаоэяию'

temp = [list(filter(lambda x: x in vowel, i))
          for i in song.split()]

result = set(map(lambda x: len(x), temp))

print('Парам пам-пам' if len(result) == 1 else 'Пам парам')