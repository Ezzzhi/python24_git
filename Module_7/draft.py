import io
from pprint import pprint

name = 'products.txt'
file = open(name, 'r', encoding='utf-8')
print(file.tell())
pprint(file.read())
print(file.tell())
print(file.closed)
file.close()
print(file.closed)