fname = input('Enter the file name: ')
fhand = open(fname)
count = 0
for line in fhand:
    if line.startswith('a') :
        count = count + 1
print('There were', count, '"a" lines in', fname)
