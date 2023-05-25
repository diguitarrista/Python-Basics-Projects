# This is a challenge to build a simple version of the snake game using only while loops, strings and fuctions.
# The challenge consists in printing the table with the head and body of the snake. When the player chooses a direction,
# the head moves and the body must grow in the direction of the head. The snake can collide with the walls and itself,
# that's the other part of the callenge, keep the coordinates of the body without using matrix, vectors, dictionaries, etc.
# I put a win condition just for the sake of the game. The codition for the original snake game is different from this.
# I'm not using this in an academic level or for commercial purposes. This code is only to demonstrate programming technics.
# This code was all written by me (@diguitarrista) and was inspired by a project from my class about introduction to computer science. 

def play():
    print("Welcome to the Snake Game! The challenge is to complete the game without hitting itself or the walls.")
    print("The head is represented by the letter H and the body with *.")
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
    # Check the user's input
    check_positive = True
    while check_positive:
        inputs = check_inputs()
        n_col = inputs[0]
        n_row = inputs[1]
        xo = inputs[2]
        yo = inputs[3]
        if xo <= 0 or yo <= 0 or n_row <= 0 or n_col <= 0:
            print()
            print("You must choose the numbers > 0.")
            print()
        elif xo >= n_col or yo >= n_row:
            print()
            print("The xo and yo must be lower than the number of columns and rows")
            print()
        else:
            check_positive = False
            
    # The snake starts in the position xo - 1, yo - 1.
    yo -= 1
    body_snake = "" # It's the string that will keep the snake body positions
    direction = 3

    # Game loop.
    play = True

    while play:
        print()
        # Add the direction to the string body_snake (directions) to calculate the body path from xo, yo.
        body_snake += str(direction)
        hx, hy = head_snake(body_snake, xo, yo)
        hit = collision(body_snake, xo, yo, hx, hy, n_col, n_row)
        # Check for collisions.
        if hit:
            play = False
            print("Finished!")
            print("You made points:", len(body_snake) - 1, "points.")
            print()
        # Check if the player completed the game.
        elif (len(body_snake) - 1) == ((n_row*n_col) - 1):
            play = False
            print("Finished!")
            print("You won!")
            print("You made points:", len(body_snake) - 1, "points.")
            print()
        # Game loop. Receive the input from the player. 
        else:
            draw_board(body_snake, xo, yo, hx, hy, n_col, n_row)
            print()
            print("Points:", str(len(body_snake) - 1) + ".")
            print()
            
            direction = check_direction()
            if direction == "5":
                play = False
                print("Finished")
                print("You made points:", len(body_snake) - 1, "points.")
                print()

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
            print("Invalid input. Try again from the beginning.")
            print()
    return [n_col, n_row, xo, yo]

def check_direction():
    check_direction = True
    # Check the user's input 
    while check_direction:
        direction = input("Type a number to move the snake: 1- right, 2- up, 3- left, 4- down, 5- finish: ")
        try:
            test = int(direction)
            if test > 0 and test < 6:
                check_direction = False
            else:
                print("Invalid input. Please enter a number between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")
    return direction

def draw_board(body_snake, xo, yo, x, y, n_col, n_row):
    col = 0
    row = 0
    # top
    top = n_col + 2
    while top > 0:
        print("#", end="")
        top -= 1
    print()
    # middle
    while row < n_row:
        print("#", end="")
        while col < n_col:
            # body
            body = body_snake_coordinates(body_snake, xo, yo, col, row)
            if body:
                col += 1
            # head
            elif x == col and y == row:
                print("H", end="")
                col += 1
            # rest of the table
            else:
                print(".", end="")
                col += 1
        print("#")
        row += 1
        col = 0
    # bottom
    bot = n_col + 2
    while bot > 0:
        print("#", end="")
        bot -= 1
    print()

def reverse(number):
    count_digits = 1
    reversed = ""
    if len(number) > 1:
        # Count the number of digits of direction.
        x = int(number)
        y = x // 10 # The last digit is the snake's head
        while y > 0:
            count_digits += 1
            y = y // 10
        # Divide by the number of digits.
        while count_digits > 0:
            r = x%10
            # Invert the position of the digits.
            reversed += str(r)
            x = x // 10
            count_digits -= 1
        return int(reversed)
    else:
        return int(number)

def body_snake_coordinates(body_snake, xo, yo, col, row):
    n = reverse(body_snake)
    # Return True if any part of the snake is in (col, row) and print the body.
    while n > 0:
        r = n%10
        if r == 1:
            xo += 1
        elif r == 3:
            xo -= 1
        elif r == 2:
            yo -= 1
        elif r == 4:
            yo += 1
        if n > 10 and xo == col and yo == row:
            print("*", end="")
            return True
        n = n // 10

def head_snake(body_snake, xo, yo):
    n = reverse(body_snake)
    # Return the head's position.
    while n > 0:
        r = n%10
        if r == 1:
            xo += 1
        elif r == 3:
            xo -= 1
        elif r == 2:
            yo -= 1
        elif r == 4:
            yo += 1
        if n < 10:
            head_snake_coordinates = xo, yo
        n = n//10
    return head_snake_coordinates

def collision(body_snake, xo, yo, x, y, n_col, n_row):
    n = reverse(body_snake)
    # Check if the head collides with the body.
    while n > 0:
        r = n%10
        if r == 1:
            xo += 1
        elif r == 3:
            xo -= 1
        elif r == 2:
            yo -= 1
        elif r == 4:
            yo += 1
        if n > 10 and xo == x and yo == y and r < 5:
            print("Collision with itself.")
            return True
        n = n // 10

    # Check if the head collides with the borders.
    if x == n_col or y == n_row or x == -1 or y == -1:
        print("Collision with wall.")
        return True
    else:
        return False
 
play()
