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

def check_winner(board):
    win_combinations = [
        [(0,0), (0,1), (0,2)],
        [(1,0), (1,1), (1,2)],
        [(2,0), (2,1), (2,2)],
        [(0,0), (1,0), (2,0)],
        [(0,1), (1,1), (2,1)],
        [(0,2), (1,2), (2,2)],
        [(0,0), (1,1), (2,2)],
        [(0,2), (1,1), (2,0)]
    ]

    for combo in win_combinations:
        a, b, c = combo
        if board[a[0]][a[1]] == board[b[0]][b[1]] == board[c[0]][c[1]] != '.':
            return board[a[0]][a[1]]
        
    return None

def is_draw(board):
    for row in board:
        if '.' in row:
            return False
    return True


pole = [['.' for _ in range(3)] for _ in range(3)]

print_pole(pole)

while True:
    row, col = get_move(pole, current_player)
    pole[row][col] = current_player
    print_pole(pole)
    
    winner = check_winner(pole)
    if winner != None:
        print(f'Победитель {winner}')
        break
    elif is_draw(pole):
        print("Ничья!")
        break

    current_player = 'O' if current_player == 'X' else 'X'
    