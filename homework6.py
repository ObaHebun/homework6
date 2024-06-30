my_dict = {'Roman' : 2000,  'Marat' : 2000, 'Isya' : 2001, 'Shpek' : 2002}
print('Dictionary: ', my_dict)
print('Existing value: ', my_dict.get('Roman'))
print('Not existing value: ', my_dict.get('Slav'))
my_dict.update({'Anna' : 1988,
                'Julia' : 1995})
a = my_dict.pop('Shpek')
print('Deleted value: ', a)
print('Modified dictionary: ', my_dict)

my_set = {1, 4, 4, 4, 1, 1, True, (1, 2, 3), 1.5, 1.5}
print(my_set)
my_set.add(5)
my_set.add('Stroka')
my_set.discard(4)
print(my_set)