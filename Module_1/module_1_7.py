# Задание "Средний балл"
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3],
          [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
avr_grades = {}
students_list = list(students)
students_list.sort()

avr_grades[students_list[0]] = round(sum(grades[0])/len(grades[0]))
avr_grades[students_list[1]] = round(sum(grades[1])/len(grades[1]))
avr_grades[students_list[2]] = round(sum(grades[2])/len(grades[2]))
avr_grades[students_list[3]] = round(sum(grades[3])/len(grades[3]))
avr_grades[students_list[4]] = round(sum(grades[4])/len(grades[4]))
print(avr_grades)
# здесь, конечно, надо использовать цикл, но в задании было сказано
# "на основе полученных ранее знаний (синтаксиса и инструментов)",
# поэтому решение такое. Если есть более интресное решение на основе
# полученных знаний, хотелось бы знать

# Решение с помощью цикла
print('')
print('Average grades:')
for i in range(0, 4):
    avr_grades[students_list[i]] = round(sum(grades[i]) / len(grades[i]))
for i,j in avr_grades.items():
    print(i + ':', j)

