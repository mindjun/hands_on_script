for i in range(1, 10):
    for j in range(1, i+1):
        print('{}*{}={:-2}'.format(j, i, i*j), end=' ')
    print()


for i in range(1, 10):
    for j in range(1, i+1):
        print('%s*%s=%-2s' % (j, i, i*j), end=' ')
    print()


for i in range(1, 8, 2):
    print(' ' * (4 - (i + 1) // 2) + '*' * i)
for i in range(5, 0, -2):
    print(' ' * (4 - (i + 1) // 2) + '*' * i)
