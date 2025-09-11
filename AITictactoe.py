import pygame

pygame.init()
width, height = 400, 400
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Ti-ti-tictactoe!")
isOn = True

# Layout
GRID_COLOR = (239, 121, 138)
BACKGROUND_COLOR = (36, 22, 35)
ELEMENT_COLOR = (222, 184, 65)
LINE_WIDTH = 3

posX = []
posO = []
player = 'X'

game_over = False
winning_line = None

WINNING_COMBINATIONS = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),  
    (0, 3, 6), (1, 4, 7), (2, 5, 8),  
    (0, 4, 8), (2, 4, 6)            
]

def drawX(window, squareIndex):
    squareSize = width / 3
    column = squareIndex % 3
    line = squareIndex // 3
    squareX = column * squareSize
    squareY = line * squareSize
    padding = 20
    topLeft = (squareX + padding, squareY + padding)
    bottomRight = (squareX + squareSize - padding, squareY + squareSize - padding)
    topRight = (squareX + squareSize - padding, squareY + padding)
    bottomLeft = (squareX + padding, squareY + squareSize - padding)
    pygame.draw.line(window, ELEMENT_COLOR, topLeft, bottomRight, 12)
    pygame.draw.line(window, ELEMENT_COLOR, topRight, bottomLeft, 12)

def drawO(window, squareIndex):
    squareSize = width / 3
    column = squareIndex % 3
    line = squareIndex // 3
    squareX = column * squareSize
    squareY = line * squareSize
    centerX = squareX + squareSize / 2
    centerY = squareY + squareSize / 2
    radius = squareSize / 3
    pygame.draw.circle(window, ELEMENT_COLOR, (centerX, centerY), radius, 12)

# The game is HERE   |
#                   \/
while isOn == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isOn = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseX, mouseY = pygame.mouse.get_pos()
            column = int(mouseX // (width / 3))
            line = int(mouseY // (height / 3))
            squareIndex = line * 3 + column
            if squareIndex in posX or squareIndex in posO:
                print("Busy!")
            else:
                if player == 'X':
                    posX.append(squareIndex)
                    player = 'O'
                elif player == 'O':
                    posO.append(squareIndex)
                    player = 'X'
    window.fill(BACKGROUND_COLOR)
    #Vertical lines
    pygame.draw.line(window, GRID_COLOR, (width / 3, 0), (width / 3, height), LINE_WIDTH)
    pygame.draw.line(window, GRID_COLOR, (2 * width / 3, 0), (2 * width / 3, height), LINE_WIDTH)
    # Horizontal lines
    pygame.draw.line(window, GRID_COLOR, (0, height / 3), (width, height / 3), LINE_WIDTH)
    pygame.draw.line(window, GRID_COLOR, (0, 2 * height / 3), (width, 2 * height / 3), LINE_WIDTH)


    for pos in posX:
        drawX(window, pos)

    for pos in posO:
        drawO(window, pos)
    
    pygame.display.update()

pygame.quit()