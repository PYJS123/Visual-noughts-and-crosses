board = [[' ', ' ', ' '],
         [' ', ' ', ' '],
         [' ', ' ', ' ']]
player1 = True
frameCount = 0
systemCheck = 0
wwonn = ''

BLACKTRSP = 0, 0, 0

HEIGHT = 700
WIDTH = HEIGHT

def draw():
    screen.draw.filled_rect(Rect((0, 0), (WIDTH, HEIGHT)), BLACKTRSP)
    drawLines()
    drawBoard()

    screen.draw.text('Please put in an\nempty square', center=(WIDTH / 2, HEIGHT / 2), fontsize=p5map(100, 0, 700, 0, HEIGHT), color=(0, 255, 255), alpha=systemCheck / 255)
    if wwonn != '':
        screen.clear()
        screen.draw.text(wwonn + " has won!\n'Y' to replay,\n'N' not to", center=(WIDTH / 2, HEIGHT / 2), fontsize=p5map(100, 0, 700, 0, HEIGHT), color=(255, 0, 255))

def on_key_down(key):
    global wwonn
    if wwonn != '':
        if key == keys.Y:
            global board
            board = [[' ', ' ', ' '],
                     [' ', ' ', ' '],
                     [' ', ' ', ' ']]
            wwonn = ''
            systemCheck = 0
        elif key == keys.N:
            exit()

def on_mouse_down(pos):
    x = pos[0]
    y = pos[1]
    # board[(p5rund(x - (WIDTH / 6)) - 1) + 1][(p5rund(y - (HEIGHT / 6)) - 1) + 1] = 1
    x = (p5rund(x - (WIDTH / 6), WIDTH) - 1) + 1
    y = (p5rund(y - (HEIGHT / 6), HEIGHT) - 1) + 1
    global player1
    if board[y][x] == ' ':
        if player1 == True:
            board[y][x] = 'X'
            player1 = False
        else:
            board[y][x] = 'O'
            player1 = True
    else:
        global systemCheck
        systemCheck = 300

    if checkWon() != 'n':
        clock.schedule_unique(cch, 0.1)

def cch():
    global wwonn
    wwonn = checkWon()

def update():
    global frameCount
    frameCount += 1

    global systemCheck
    systemCheck -= 3

def checkWon():
    for y in range(0, len(board), 1):  # Check rows
        if board[y][0] == board[y][1] and board[y][1] == board[y][2] and board[y][0] != ' ':
            return board[y][0]  # Who won
    for x in range(0, len(board), 1):  # Check columns
        if board[0][x] == board[1][x] and board[1][x] == board[2][x] and board[0][x] != ' ':
            return board[0][x]
    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] != ' ':  # Check diagonals
        return board[0][0]
    if board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[0][2] != ' ':  # Check diagonals
        return board[0][0]
    return 'n'

def drawBoard():
    for y in range(0, len(board), 1):
        for x in range(0, len(board[0]), 1):
            screen.draw.text(board[y][x], center=((x * (WIDTH / 3)) + (WIDTH/6), y * (HEIGHT / 3) + (HEIGHT / 6)), fontsize=HEIGHT / 3)

def drawLines():
    strk = p5map(10, 0, 600, 0, HEIGHT)
    screen.draw.filled_rect(Rect((((WIDTH / 3) - (strk / 2)), 0), (strk, HEIGHT)), (255, 255, 0))
    screen.draw.filled_rect(Rect(((((WIDTH / 3) * 2) - (strk / 2)), 0), (strk, HEIGHT)), (255, 255, 0))
    screen.draw.filled_rect(Rect((0, ((HEIGHT / 3) - (strk / 2))), (WIDTH, strk)), (255, 255, 0))
    screen.draw.filled_rect(Rect((0, (((HEIGHT / 3) * 2) - (strk / 2))), (WIDTH, strk)), (255, 255, 0))

def p5rund(n, rw):
    return round((n * len(board)) / rw)

def p5map(n, start1, stop1, start2, stop2):
    return ((n-start1) / (stop1-start1)) * (stop2 - start2) + start2