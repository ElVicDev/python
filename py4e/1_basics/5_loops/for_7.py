print('El siguiente programa encuentra el promedio entre count y sum')
count = 0
add = 0
print('Before', count, add)
for value in [9, 41, 12, 3, 74, 15] :
    count = count + 1
    add = add + value
    print(count, add, value)
print('after', count, add, add / count)