# Paso 1: Definir el Tablero
def create_board():
    return [[' ' for _ in range(7)] for _ in range(6)]

# Paso 2: Mostrar el Tablero
def print_board(board):
    for row in board:
        print('|' + '|'.join(row) + '|')
    print('-' * 15)

# Paso 3: Hacer una Jugada
def make_move(board, column, player):
    for row in reversed(board):
        if row[column] == ' ':
            row[column] = player
            return True
    return False

# Paso 4: Verificar la Victoria
def check_winner(board, player):
    # Verificar horizontal
    for row in board:
        for col in range(4):
           
            if row[col] == player and row[col + 1] == player and row[col + 2] == player and row[col + 3] == player:
                return True
    
    # Verificar vertical
    for col in range(7):
        for row in range(3):
            if board[row][col] == player and board[row + 1][col] == player and board[row + 2][col] == player and board[row + 3][col] == player:
                return True
    
    # Verificar diagonal hacia abajo
    for row in range(3):
        for col in range(4):
            if board[row][col] == player and board[row + 1][col + 1] == player and board[row + 2][col + 2] == player and board[row + 3][col + 3] == player:
                return True
    
    # Verificar diagonal hacia arriba
    for row in range(3, 6):
        for col in range(4):
            if board[row][col] == player and board[row - 1][col + 1] == player and board[row - 2][col + 2] == player and board[row - 3][col + 3] == player:
                return True
    
    return False

# Paso 5: Jugar el Juego
def play_game():
    board = create_board()
    current_player = 'X'
    
    while True:
        print_board(board)
        col = int(input(f"Player {current_player}, choose a column (0-6): "))
        
        if col < 0 or col > 6:
            print("Invalid column. Try again.")
            continue
        
        if not make_move(board, col, current_player):
            print("Column is full. Try again.")
            continue
        
        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
           
                    

            
 
        
        
        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    play_game()
