#!/usr/bin/env python3
import pygame, time, random
##Initialize Pygame, set colors, game display.
pygame.init()
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 155, 0)
blue = (17, 124, 190)
Dred = (200, 100, 90)
display_width = 1280
display_height = 720
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Virus Buster')
##Create clock, set size of Viruses, set framerate, initialize font.
clock = pygame.time.Clock()
block_size = 20
FPS = 75
font = pygame.font.SysFont('helvetica', 25)
##Define how to draw the "Buster" snake to screen.
def snake(block_size, snakelist):
    for XnY in snakelist:
        pygame.draw.rect(gameDisplay, green, [XnY[0], XnY[1], block_size, block_size])

##Define how to write text to screen in different locations.
    ##message_to_screen 1 is top middle of screen.
def message_to_screen(msg, color):
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, [display_width / 3, 0])

    ##message_to_screen2 is dead center of the screen.
def message_to_screen2(msg, color):
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, [display_width / 3, display_height / 2])

    ##message_to_screen3 through 6 are used to display the colors.
def message_to_screen3(msg, color):
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, [250, 200])


def message_to_screen4(msg, color):
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, [250, 150])


def message_to_screen5(msg, color):
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, [250, 100])


def message_to_screen6(msg, color):
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, [250, 50])
    
    ##message_to_screen7 is used to show the score (variable SnakeLength) during gameplay.
def message_to_screen7(msg, color):
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, [0 , 0])

    ##message_to_screen8 is a placeholder with no current use.
def message_to_screen8(msg, color):
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, [display_width-100, display_height - 100])

##Start game.
def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    intro = False
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
                else:
                    continue
        ##Set game display for intro screen.
        gameDisplay.fill(white)
        message_to_screen('Welcome to Virus Buster', green)
        message_to_screen2('Press C to play, or Escape to quit.', black)
        message_to_screen3('Virus', red)
        message_to_screen4('Rootkit', blue)
        message_to_screen5('Trojan', black)
        message_to_screen6('Ransomware', Dred)
        pygame.display.update()
        clock.tick(15)

##Initialize gameplay screen.
def gameLoop():
    gameExit = False
    gameOver = False
    lead_x = display_width / 2
    lead_y = display_height / 2
    lead_x_change = 0
    lead_y_change = 0
    snakeList = []
    snakeLength = 1
    randAppleX = round(random.randrange(0, display_width - block_size))
    randAppleY = round(random.randrange(0, display_height - block_size))
    randAppleW = round(random.randrange(0, display_width - block_size))
    randAppleZ = round(random.randrange(0, display_height - block_size))
    randAppleA = round(random.randrange(0, display_width - block_size))
    randAppleB = round(random.randrange(0, display_height - block_size))
    randAppleC = round(random.randrange(0, display_width - block_size))
    randAppleD = round(random.randrange(0, display_height - block_size))
    while not gameExit: ##While the game is open
        while gameOver == True: ##While the player is dead, check for win condition.
            if snakeLength > 100:
                gameDisplay.fill(black)
                message_to_screen2('You Win, final score ' + str(snakeLength) + ' press C to play again or Escape to quit', red)
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        gameOver = False
                        gameExit = True
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            gameExit = True
                            gameOver = False
                        if event.key == pygame.K_c:
                            gameLoop()
                        else:
                            continue
            else:
                if snakeLength < 100:
                    gameDisplay.fill(black)
                    message_to_screen2('Game over, final score ' + str(snakeLength) + ' press C to play again or Escape to quit', red)
                    pygame.display.update()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        gameOver = False
                        gameExit = True
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            gameExit = True
                            gameOver = False
                        if event.key == pygame.K_c:
                            gameLoop()
                        else:
                            continue
        ##Define movement controls.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    lead_y_change = -block_size
                    lead_x_change = 0
                elif event.key == pygame.K_a:
                    lead_x_change = -block_size
                    lead_y_change = 0
                elif event.key == pygame.K_s:
                    lead_y_change = block_size
                    lead_x_change = 0
                elif event.key == pygame.K_d:
                    lead_x_change = block_size
                    lead_y_change = 0
                else:
                    continue
        
        ##Define kill condition. Define snakeHead array.
        if lead_x >= display_width or lead_x < 0 or lead_y >= display_height or lead_y < 0:
            gameOver = True
        lead_x += lead_x_change
        lead_y += lead_y_change
        gameDisplay.fill(black)
        AppleThickness = 30
        BossSize = 10
        pygame.draw.rect(gameDisplay, red, [randAppleX, randAppleY, AppleThickness, AppleThickness])
        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)
        if len(snakeList) > snakeLength:
            del snakeList[0]
        for eachSegment in snakeList[:-1]:
            if eachSegment == snakeHead:
                gameOver = True
                continue
    ##Activate other Viruses when Snake is long enough.
        if snakeLength >= 10:
            pygame.draw.rect(gameDisplay, blue, [randAppleW, randAppleZ, AppleThickness, AppleThickness])
        if snakeLength >= 20:
            pygame.draw.rect(gameDisplay, black, [randAppleA, randAppleB, AppleThickness, AppleThickness])
        if snakeLength >= 50:
            pygame.draw.rect(gameDisplay, Dred, [randAppleC, randAppleD, AppleThickness, AppleThickness])
        message_to_screen7(str(snakeLength), red)
        snake(block_size, snakeList)
        pygame.display.update()
        if lead_x > randAppleX and lead_x < randAppleX + AppleThickness or lead_x + block_size > randAppleX and lead_x + block_size < randAppleX + AppleThickness:
            if lead_y > randAppleY and lead_y < randAppleY + AppleThickness:
                randAppleX = round(random.randrange(0, display_width - block_size))
                randAppleY = round(random.randrange(0, display_height - block_size))
                snakeLength += 1
            elif lead_y + block_size > randAppleY and lead_y + block_size < randAppleY + AppleThickness:
                randAppleX = round(random.randrange(0, display_width - block_size))
                randAppleY = round(random.randrange(0, display_height - block_size))
                snakeLength += 1
        if lead_x > randAppleW and lead_x < randAppleW + AppleThickness or lead_x + block_size > randAppleW and lead_x + block_size < randAppleW + AppleThickness:
            if lead_y > randAppleZ and lead_y < randAppleZ + AppleThickness:
                randAppleW = round(random.randrange(0, display_width - block_size))
                randAppleZ = round(random.randrange(0, display_height - block_size))
                snakeLength += 2
            elif lead_y + block_size > randAppleZ and lead_y + block_size < randAppleZ + AppleThickness:
                randAppleW = round(random.randrange(0, display_width - block_size))
                randAppleZ = round(random.randrange(0, display_height - block_size))
                snakeLength += 2
        if lead_x > randAppleA and lead_x < randAppleA + AppleThickness or lead_x + block_size > randAppleA and lead_x + block_size < randAppleA + AppleThickness:
            if lead_y > randAppleB and lead_y < randAppleB + AppleThickness:
                randAppleA = round(random.randrange(0, display_width - block_size))
                randAppleB = round(random.randrange(0, display_height - block_size))
                snakeLength += 3
            elif lead_y + block_size > randAppleB and lead_y + block_size < randAppleB + AppleThickness:
                randAppleA = round(random.randrange(0, display_width - block_size))
                randAppleB = round(random.randrange(0, display_height - block_size))
                snakeLength += 3
        if lead_x > randAppleC and lead_x < randAppleC + AppleThickness or lead_x + block_size > randAppleC and lead_x + block_size < randAppleC + AppleThickness:
            if lead_y > randAppleD and lead_y < randAppleD + AppleThickness:
                randAppleC = round(random.randrange(0, display_width - block_size))
                randAppleD = round(random.randrange(0, display_height - block_size))
                snakeLength += 5
            elif lead_y + block_size > randAppleD and lead_y + block_size < randAppleD + AppleThickness:
                randAppleC = round(random.randrange(0, display_width - block_size))
                randAppleD = round(random.randrange(0, display_height - block_size))
                snakeLength += 5
        clock.tick(15)

    pygame.quit()
    quit()


game_intro()
gameLoop()
