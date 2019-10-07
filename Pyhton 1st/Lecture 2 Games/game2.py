import numpy as np

def get_user_input(board, board_size, pid):
    while True:
        x_loc = -1
        y_loc = -1
        input_str_x = input("Player {} > Please insert location x: ".format(pid))
        input_str_y = input("Player {} > Please insert location y: ".format(pid))
        # check range
        if input_str_x.isdigit() and int(input_str_x) >=0 and int(input_str_x) < board_size:
            x_loc = int(input_str_x)
        if input_str_y.isdigit() and int(input_str_y) >=0 and int(input_str_y) < board_size:
            y_loc = int(input_str_y)
        # check empty
        if x_loc != -1 and y_loc != -1 and board[x_loc,y_loc]==0:
            break
    return x_loc, y_loc

def check_result(board, board_size, x, y, pid):
    # check horizontal
    if sum(board[:,y] == pid) == board_size:
        return True
    # check vertical
    if sum(board[x,:] == pid) == board_size:
        return True
    # check diagonal
    if sum(board.diagonal() == pid) == board_size:
        return True
    # check diagonal
    if sum(np.fliplr(board).diagonal() == pid) == board_size:
        return True
    return False


if __name__ == "__main__":
    board_size = 3
    # inital game board
    board = np.zeros((board_size,board_size))
    pid = 1
    count = 0 
    while True:
        # display
        print(board)
        # get user input
        x,y = get_user_input(board, board_size, pid)
        # update board
        board[x,y] = pid
        # check result
        is_win = check_result(board,board_size, x, y, pid)
        if is_win:
            print("Player {} won".format(pid))
            break
        # check draw
        count +1
        if count == board_size**2:
            print("Draw game")
            break
        pid *= -1 
    print(board)
    print("game over")