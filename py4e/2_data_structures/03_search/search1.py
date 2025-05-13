fhand = open('musica.txt')
for line in fhand:
    line = line.rstrip()
    if line.startswith('L') :
        print(line)
