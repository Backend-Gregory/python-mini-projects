current_player = 'X'

def get_move(board, player):
    while True:
        try:
            row = int(input(f'Ход {player}. Введите строку (0-2)'))
            col = int(input(f'Ход {player}. Введите столбец (0-2)'))
            if 0 <= row <= 2 and 0 <= col <= 2:
                if board[row][col] == '.':
                    return row, col
                else:
                    print('Клетка занята')
            else:
                 print("Координаты должны быть от 0 до 2")
        except ValueError:
            print("Введите числа!")

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

while True:
    row, col = get_move(pole, current_player)
    pole[row][col] = current_player
    print_pole(pole)
    current_player = 'O' if current_player == 'X' else 'X'
        
    