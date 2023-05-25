# This is a version update of the 1_-_while_loops. Now I'm going to use for loops and improve the game's mechanics. 
# The callenge consists in printing the table with the head and body of the snake. When the player chooses a direction,
# the head moves and the body must grow in the direction of the head. The snake can collide with the walls, the apple and itself.
# This version doesn't have a win condition, it only registers the total points that the player made by 'eating' the apples. 
# I'm not using this in an academic level or for commercial purposes. This code is only to demonstrate programming technics.
# This code was all written by me (@diguitarrista) and was inspired by a project from my class about introduction to computer science. 

import random

def apple_coord(ncol, nrow):
    x = random.randrange(1, ncol + 1)
    y = random.randrange(1, nrow + 1)
    return [x, y]

def play():
    print("Welcome to the Snake Game! The challenge is to complete the game without hitting itself or the walls.")
    print("The head is represented by the letter 'H', the apple for the letter 'a' and the body with '*'.")
    print()

    # Game loop.
    game()
    play_again = True
    while play_again:
        play_again_input = str(input("Do you want to play again? Type Y for yes or N for No: "))
        print()
        play_again_input = play_again_input.capitalize() # Make sure that the user's input is a capital letter. 
        if play_again_input == 'Y':
            game()
            play_again = True
        elif play_again_input == 'N':
            print("Thanks for playing! Bye!")
            play_again = False
        else:
            print("You must type the letters Y or N. Try again!")

def game():
    print("The numbers that you will choose below must be integers.")
    # Check the user's input.  
    check_positive = True
    while check_positive:
        inputs = check_inputs()
        n_col = inputs[0]
        n_row = inputs[1]
        xo = inputs[2]
        yo = inputs[3]
        if xo < 0 or yo < 0:
            print()
            print("The xo and yo must be higher than -1.")
            print()
        elif n_row <= 0 or n_col <= 0:
            print()
            print("The rows and the collumns must be higher than 0.")
            print()
        elif xo >= n_col or yo >= n_row:
            print()
            print("The xo and yo must be lower than the number of columns and rows")
            print()
        else:
            check_positive = False
            
    # Game loop.
    play = True
    # The snake starts in the position xo + 1, yo + 1.
    yo += 1
    direction = 7
    head_snake_initial = [xo + 1, yo]
    body_snake = []
    # Creates the apple.
    apple = apple_coord(n_col, n_row)
    ax = apple[0]
    ay = apple[1]

    while play:
        print()
        # Moves the snake and check for collisions
        head_snake = move_head(direction, head_snake_initial)
        hit = colision(ax, ay, head_snake, body_snake, n_col, n_row)
        # Check for collisions.
        if hit == True:
            play = False
            print("Finished!")
            print("You made points:", len(body_snake), "points.")
            print()
        # Game loop. Receive the input from the player. 
        else:
            # Check for colision with an apple.
            apple_colision = colision_apple(head_snake, ax, ay)
            if apple_colision:
                # Add the apple's coordinates to the body matrix. 
                body_snake.append([ax, ay])
                # Check if the apple will appear in the body coordinate.
                apple = check_apple(body_snake, head_snake, n_col, n_row)
                ax = apple[0]
                ay = apple[1]
            # Draw the board
            draw_board(ax, ay, head_snake, body_snake, n_col, n_row)
            print()
            print("Points:", len(body_snake), ".")
            print()
            # Check the user's input for the direction. 
            direction = check_direction(body_snake)
            if direction == 5:
                print("Finished")
                print("You made:", len(body_snake), "points.")
                print()
                play = False
            # This is the most important part of the code, the queue.
            # It moves the first part of the body to the head position,
            # then the other parts follow.
            # It takes off the first element of the matrix body and put
            # the head position. The head position can be the last element
            # since it doesn't matter because when it prints the table what
            # matters are the coordinates x and y
            if len(body_snake) > 0:
                body_snake.pop(0)
                body_snake.append([head_snake[0], head_snake[1]])

def check_inputs():
    check_inputs = True
    while check_inputs:
        try:
            n_col = int(input("Type the number of columns: "))
            n_row = int(input("Type the number of rows: "))
            xo = int(input("Type the x position where the snake starts: "))
            yo = int(input("Type the y position where the snake starts: "))
            check_inputs = False
        except ValueError:
            print()
            print("Invalid input. Try again for the beginning.")
            print()
    return [n_col, n_row, xo, yo]
                    
def check_direction(body):
    # Check the user's input for the direction. 
    check_direction = True
    while check_direction:
        try:
            direction = int(input("Type a number to move the snake: 1- right, 2- up, 3- left, 4- down, 5- finish: "))
            if direction < 0 or direction > 5:
                print("Invalid input. Please enter a number between 1 and 5.")
            check_direction = False
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")
            
    return direction

def draw_board(ax, ay, head, body, n_col, n_row):
    hx = head[0]
    hy = head[1]
    board = []
    # Create the board.
    for y in range(n_row + 2):
        board_row = []
        for x in range(n_col + 2):
            if x == 0 or y == 0 or x == n_col + 1 or y == n_row + 1:
                board_row.append("#")
            else:
                board_row.append(".")
        board.append(board_row)
    # Put the head, body and apple in the board.
    for j in range(n_row + 2):
        for i in range(n_col + 2):
            if ax == i and ay == j:
                board[j][i] = "a"
            elif hx == i and hy == j:
                board[j][i] = "H"
            else:
                for b in body:
                    if b[0] == i and b[1] == j:
                        board[j][i] = "*"         
    # Prints the board.
    for row in board:
        for k in range(len(row)):
            if k < len(row) - 1:
                print(row[k], end="")
            else:
                print(row[k])
                
def move_head(d, head):
    # Return the matrix with the head coordinates.
    if d == 1:
        head[0] += 1
    elif d == 3:
        head[0] -= 1
    elif d == 2:
        head[1] -= 1
    elif d == 4:
        head[1] += 1
    return head      
                   
def colision_apple(snake, ax, ay):
    # Check if the head colides with the apple.
    if snake[0] == ax and snake[1] == ay:
        return True
    else:
        return False

def check_apple(snake, head, ncol, nrow):
    # Check if the apple appears in any part of the snake.
    # If appears, it'll sort a new apple position. 
    apple = apple_coord(ncol, nrow)
    while ([apple[0], apple[1]] in snake) or ([apple[0], apple[1]] == head):
        apple = apple_coord(ncol, nrow)
    return apple
        
def colision(ax, ay, head, body, ncol, nrow):
    # Check if the head collides with the borders.
    if head[0] == ncol + 1 or head[1] == nrow + 1 or head[0] == 0 or head[1] == 0:
        print("Collision with wall.")
        return True
    # Check if the head collides with the body.
    elif head in body:
        print("Collision with itself")
        return True
    else:
        return False

play()
