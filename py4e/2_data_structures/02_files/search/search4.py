fhand = open('musica.txt')
for line in fhand:
    line = line.rstrip()
    if not 'Mendoza' in line :
        continue
    print(line)
