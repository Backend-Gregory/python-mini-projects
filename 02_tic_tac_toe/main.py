def print_pole(pole):
    print("   0   1   2")
    for i in range(3):
        print(i, end=' ')
        for j in range(3):
            print(pole[i][j], end=' ')
            if j < 2:
                print('|', end=' ')
        print()
        if i < 2:
            print('  -----------')

n, m = 3, 3
pole = [['.' for _ in range(m)] for _ in range(n)]

print_pole(pole)