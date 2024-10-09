# Задание "Слишком древний шифр"
first_field = []
second_field = []
for i in range (21):
    first_field.append(i)
# for i in first_field:
    sum_ = ''
    for j in range(1, i):
        for k in range(j + 1, i):
            if i % (j + k) == 0:
                sum_ = sum_ + (str(j) + str(k))
    second_field.append(sum_)

for i in range(3, 21):
    print(first_field[i], '- ' + second_field[i])