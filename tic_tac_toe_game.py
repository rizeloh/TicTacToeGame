import pygame
import sys

# Инициализация Pygame
pygame.init()

# Размеры экрана
SCREEN_SIZE = 300
LINE_WIDTH = 15
WIN_LINE_WIDTH = 15
SQUARE_SIZE = SCREEN_SIZE // 3
CIRCLE_RADIUS = SQUARE_SIZE // 3
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25
SPACE = SQUARE_SIZE // 4

# Цвета
BG_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)
CIRCLE_COLOR = (239, 231, 200)
CROSS_COLOR = (84, 84, 84)

# Настройка экрана
screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
pygame.display.set_caption('Tic Tac Toe')
screen.fill(BG_COLOR)

# Настройка игрового поля
board = [[None]*3 for _ in range(3)]
player = 'X'

def draw_lines():
    # Горизонтальные линии
    pygame.draw.line(screen, LINE_COLOR, (0, SQUARE_SIZE), (SCREEN_SIZE, SQUARE_SIZE), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (0, 2 * SQUARE_SIZE), (SCREEN_SIZE, 2 * SQUARE_SIZE), LINE_WIDTH)
    # Вертикальные линии
    pygame.draw.line(screen, LINE_COLOR, (SQUARE_SIZE, 0), (SQUARE_SIZE, SCREEN_SIZE), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (2 * SQUARE_SIZE, 0), (2 * SQUARE_SIZE, SCREEN_SIZE), LINE_WIDTH)

def draw_figures():
    for row in range(3):
        for col in range(3):
            if board[row][col] == 'O':
                pygame.draw.circle(screen, CIRCLE_COLOR, (int(col * SQUARE_SIZE + SQUARE_SIZE//2), int(row * SQUARE_SIZE + SQUARE_SIZE//2)), CIRCLE_RADIUS, CIRCLE_WIDTH)
            elif board[row][col] == 'X':
                pygame.draw.line(screen, CROSS_COLOR, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SPACE), CROSS_WIDTH)
                pygame.draw.line(screen, CROSS_COLOR, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE), (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), CROSS_WIDTH)

def check_win(player):
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == player:
            draw_vertical_winning_line(col, player)
            return True
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] == player:
            draw_horizontal_winning_line(row, player)
            return True
    if board[0][0] == board[1][1] == board[2][2] == player:
        draw_desc_diagonal(player)
        return True
    if board[2][0] == board[1][1] == board[0][2] == player:
        draw_asc_diagonal(player)
        return True
    return False

def draw_vertical_winning_line(col, player):
    posX = col * SQUARE_SIZE + SQUARE_SIZE//2
    if player == 'O':
        color = CIRCLE_COLOR
    else:
        color = CROSS_COLOR
    pygame.draw.line(screen, color, (posX, 15), (posX, SCREEN_SIZE - 15), WIN_LINE_WIDTH)

def draw_horizontal_winning_line(row, player):
    posY = row * SQUARE_SIZE + SQUARE_SIZE//2
    if player == 'O':
        color = CIRCLE_COLOR
    else:
        color = CROSS_COLOR
    pygame.draw.line(screen, color, (15, posY), (SCREEN_SIZE - 15, posY), WIN_LINE_WIDTH)

def draw_asc_diagonal(player):
    if player == 'O':
        color = CIRCLE_COLOR
    else:
        color = CROSS_COLOR
    pygame.draw.line(screen, color, (15, SCREEN_SIZE - 15), (SCREEN_SIZE - 15, 15), WIN_LINE_WIDTH)

def draw_desc_diagonal(player):
    if player == 'O':
        color = CIRCLE_COLOR
    else:
        color = CROSS_COLOR
    pygame.draw.line(screen, color, (15, 15), (SCREEN_SIZE - 15, SCREEN_SIZE - 15), WIN_LINE_WIDTH)

def restart():
    screen.fill(BG_COLOR)
    draw_lines()
    global board, player
    board = [[None]*3 for _ in range(3)]
    player = 'X'

draw_lines()

# Основной цикл игры
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseX = event.pos[0]
            mouseY = event.pos[1]
            clicked_row = mouseY // SQUARE_SIZE
            clicked_col = mouseX // SQUARE_SIZE
            if board[clicked_row][clicked_col] is None:
                board[clicked_row][clicked_col] = player
                if check_win(player):
                    pygame.time.wait(500)
                    restart()
                player = 'O' if player == 'X' else 'X'
                draw_figures()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart()
    pygame.display.update()
