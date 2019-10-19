for i in range(2, 10):
    for j in range(1, 10):
        print('%d * %d = %3d' % (i, j, i * j), end='  ')
        k = 10 - j
        print('%d * %d = %3d' % (i, k, i * k))
