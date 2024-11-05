# Арифметика
print ('1st program')
print (9 ** 0.5 * 5)
print(' ')

#Логика
print ('2nd program')
print (9.99 > 9.98 and 1000 != 1000.1)
print(' ')

#Школьная загадка
print ('3rd program')
print (2 * 2 + 2)
print(2 * (2 + 2))
print (2 * 2 + 2 == 2 * (2 + 2))
print (' ')

#Первый после точки
print ('4th program')
s = '123.456'
s = float(s)
s = s * 10
s = int(s)
s = s % 10
print(s)
# or print (int (float ('123.456') * 10) % 10)