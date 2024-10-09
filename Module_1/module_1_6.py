# 2. Работа со словарями:
my_dict = {'Bart': 'dog', 'Shmulya': 'kitty', 'Martha': 'dog'}
print('Dict:', my_dict)
print('Existing value:', my_dict['Shmulya'])
print('Not existing value:', my_dict.get('Furfur'))
my_dict.update({'Furfur': 'cat', 'Motya': 'cat'})
print('Deleted value:', my_dict.pop('Martha'))
print('Modified dictionary:', my_dict)
print('')

# 3. Работа с множествами
my_set = {234, ('cat', 'dog', 'rabbit'), True}
print('Set:', my_set)
my_set.add(12.5)
my_set.add('John')
my_set.remove(True)
print('Modified set:', my_set)
