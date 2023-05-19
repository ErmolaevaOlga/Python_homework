data = 'house=дом car=машина men=человек tree=дерево'
tp = tuple(map(lambda x: tuple(x.split('=')) ,[i for i in data.split()]))
print(tp)