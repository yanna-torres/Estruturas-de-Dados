import pygame
import os

pygame.font.init()

# CONSTANTES DA TELA
WIDTH, HEIGHT = 1000, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

# COLORS
BACKGROUND_COLOR = 53, 143, 101
WHITE = 255, 255, 255
BLACK = 0, 0, 0
GREY_150 = 150, 150, 150

# FPS do 'jogo'
FPS = 60

# CIRCLE RADIUS
RADIUS = 13

FONT = pygame.font.SysFont('cambriamath', 20, True)

def setup():
    pygame.display.set_caption("Trabalho Final - Yanna")
    WIN.fill(BACKGROUND_COLOR)
    pygame.display.update()
    draw_tree()
    draw_barcode()
    pygame.display.update()


def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

    pygame.quit()


def draw_tree():
    draw_lines_tree()
    draw_circles_tree()
    draw_numbers_tree()


def draw_circles_tree():
    # ROOT
    pygame.draw.circle(WIN, WHITE, (WIDTH/2, 250), RADIUS, RADIUS)

    # LEFT TREE of root
    pygame.draw.circle(WIN, WHITE, (WIDTH/3 - 100, 330), RADIUS, RADIUS)

    pygame.draw.circle(WIN, WHITE, (WIDTH/5 - 70, 410), RADIUS, RADIUS)
    pygame.draw.circle(WIN, BLACK, (WIDTH/5 - 70, 530), RADIUS, RADIUS)
    pygame.draw.circle(WIN, WHITE, (WIDTH/11-20, 610), RADIUS, RADIUS)

    pygame.draw.circle(WIN, BLACK, (2*WIDTH/11, 610), RADIUS, RADIUS)
    pygame.draw.circle(WIN, BLACK, (WIDTH/11-20, 690), RADIUS, RADIUS)
    pygame.draw.circle(WIN, WHITE, (2*WIDTH/11, 690), RADIUS, RADIUS)

    pygame.draw.circle(WIN, BLACK, (2*WIDTH/5 - 70, 410), RADIUS, RADIUS)
    pygame.draw.circle(WIN, WHITE, (3*WIDTH/11, 530), RADIUS, RADIUS)
    pygame.draw.circle(WIN, WHITE, (3*WIDTH/11, 610), RADIUS, RADIUS)
    pygame.draw.circle(WIN, BLACK, (3*WIDTH/11, 690), RADIUS, RADIUS)

    pygame.draw.circle(WIN, BLACK, (4*WIDTH/11+20, 530), RADIUS, RADIUS)
    pygame.draw.circle(WIN, WHITE, (4*WIDTH/11+20, 610), RADIUS, RADIUS)
    pygame.draw.circle(WIN, WHITE, (4*WIDTH/11+20, 690), RADIUS, RADIUS)

    # RIGHT TREE of root
    pygame.draw.circle(WIN, BLACK, (2*WIDTH/3 + 100, 330), RADIUS, RADIUS)

    pygame.draw.circle(WIN, WHITE, (3*WIDTH/5 + 70, 410), RADIUS, RADIUS)

    pygame.draw.circle(WIN, WHITE, (7*WIDTH/11, 530), RADIUS, RADIUS)
    pygame.draw.circle(WIN, WHITE, (7*WIDTH/11, 610), RADIUS, RADIUS)
    pygame.draw.circle(WIN, BLACK, (7*WIDTH/11, 690), RADIUS, RADIUS)

    pygame.draw.circle(WIN, BLACK, (8*WIDTH/11, 530), RADIUS, RADIUS)
    pygame.draw.circle(WIN, BLACK, (8*WIDTH/11, 610), RADIUS, RADIUS)
    pygame.draw.circle(WIN, BLACK, (8*WIDTH/11, 690), RADIUS, RADIUS)

    pygame.draw.circle(WIN, BLACK, (4*WIDTH/5 + 70, 410), RADIUS, RADIUS)

    pygame.draw.circle(WIN, WHITE, (8.2*WIDTH/11 + 70, 530), RADIUS, RADIUS)
    pygame.draw.circle(WIN, WHITE, (8*WIDTH/11 + 70, 610), RADIUS, RADIUS)
    pygame.draw.circle(WIN, BLACK, (8.5*WIDTH/11 + 70, 610), RADIUS, RADIUS)
    pygame.draw.circle(WIN, WHITE, (8*WIDTH/11 + 70, 690), RADIUS, RADIUS)
    pygame.draw.circle(WIN, BLACK, (8.5*WIDTH/11 + 70, 690), RADIUS, RADIUS)

    pygame.draw.circle(WIN, BLACK, (9.5*WIDTH/11 + 70, 530), RADIUS, RADIUS)
    pygame.draw.circle(WIN, WHITE, (9.3*WIDTH/11 + 70, 610), RADIUS, RADIUS)
    pygame.draw.circle(WIN, BLACK, (9.3*WIDTH/11 + 70, 690), RADIUS, RADIUS)

    pygame.draw.circle(WIN, BLACK, (9.8*WIDTH/11 + 70, 610), RADIUS, RADIUS)
    pygame.draw.circle(WIN, WHITE, (9.8*WIDTH/11 + 70, 690), RADIUS, RADIUS)


def draw_lines_tree():
    pygame.draw.line(WIN, GREY_150, (WIDTH / 2, 250), (WIDTH / 3 - 100, 330), 5)
    pygame.draw.line(WIN, GREY_150, (WIDTH / 2, 250), (2 * WIDTH / 3 + 100, 330), 5)

    pygame.draw.line(WIN, GREY_150, (WIDTH / 3 - 100, 330), (WIDTH/5 - 70, 410), 5)
    pygame.draw.line(WIN, GREY_150, (WIDTH / 3 - 100, 330), (2*WIDTH/5 - 70, 410), 5)
    pygame.draw.line(WIN, GREY_150, (2 * WIDTH / 3 + 100, 330), (3*WIDTH/5 + 70, 410), 5)
    pygame.draw.line(WIN, GREY_150, (2 * WIDTH / 3 + 100, 330), (4*WIDTH/5 + 70, 410), 5)

    pygame.draw.line(WIN, GREY_150, (WIDTH/5 - 70, 410), (WIDTH/5 - 70, 530), 5)
    pygame.draw.line(WIN, GREY_150, (2*WIDTH/5 - 70, 410), (3*WIDTH/11, 530), 5)
    pygame.draw.line(WIN, GREY_150, (2*WIDTH/5 - 70, 410), (4*WIDTH/11+20, 530), 5)
    pygame.draw.line(WIN, GREY_150,  (3*WIDTH/5 + 70, 410), (7*WIDTH/11, 530), 5)
    pygame.draw.line(WIN, GREY_150,  (3*WIDTH/5 + 70, 410), (8*WIDTH/11, 530), 5)
    pygame.draw.line(WIN, GREY_150, (4*WIDTH/5 + 70, 410), (8.2*WIDTH/11 + 70, 530), 5)
    pygame.draw.line(WIN, GREY_150, (4*WIDTH/5 + 70, 410), (9.5*WIDTH/11 + 70, 530), 5)

    pygame.draw.line(WIN, GREY_150, (WIDTH/5 - 70, 530), (WIDTH/11-20, 610), 5)
    pygame.draw.line(WIN, GREY_150, (WIDTH/5 - 70, 530), (2*WIDTH/11, 610), 5)
    pygame.draw.line(WIN, GREY_150, (3*WIDTH/11, 530), (3*WIDTH/11, 610), 5)
    pygame.draw.line(WIN, GREY_150, (4*WIDTH/11+20, 530), (4*WIDTH/11+20, 610), 5)
    pygame.draw.line(WIN, GREY_150, (7*WIDTH/11, 530), (7*WIDTH/11, 610), 5)
    pygame.draw.line(WIN, GREY_150, (8*WIDTH/11, 530), (8*WIDTH/11, 610), 5)
    pygame.draw.line(WIN, GREY_150, (8.2*WIDTH/11 + 70, 530), (8*WIDTH/11 + 70, 610), 5)
    pygame.draw.line(WIN, GREY_150, (8.2*WIDTH/11 + 70, 530), (8.5*WIDTH/11 + 70, 610), 5)
    pygame.draw.line(WIN, GREY_150, (9.5*WIDTH/11 + 70, 530), (9.3*WIDTH/11 + 70, 610), 5)
    pygame.draw.line(WIN, GREY_150, (9.5*WIDTH/11 + 70, 530), (9.8*WIDTH/11 + 70, 610), 5)

    pygame.draw.line(WIN, GREY_150, (WIDTH/11-20, 610), (WIDTH/11-20, 690), 5)
    pygame.draw.line(WIN, GREY_150, (2*WIDTH/11, 610), (2*WIDTH/11, 690), 5)
    pygame.draw.line(WIN, GREY_150, (3*WIDTH/11, 610), (3*WIDTH/11, 690), 5)
    pygame.draw.line(WIN, GREY_150, (4*WIDTH/11+20, 610), (4*WIDTH/11+20, 690), 5)
    pygame.draw.line(WIN, GREY_150, (7*WIDTH/11, 610), (7*WIDTH/11, 690), 5)
    pygame.draw.line(WIN, GREY_150, (8*WIDTH/11, 610), (8*WIDTH/11, 690), 5)
    pygame.draw.line(WIN, GREY_150, (8*WIDTH/11 + 70, 610), (8*WIDTH/11 + 70, 690), 5)
    pygame.draw.line(WIN, GREY_150, (8.5*WIDTH/11 + 70, 610), (8.5*WIDTH/11 + 70, 690), 5)
    pygame.draw.line(WIN, GREY_150, (9.3*WIDTH/11 + 70, 610), (9.3*WIDTH/11 + 70, 690), 5)
    pygame.draw.line(WIN, GREY_150, (9.8*WIDTH/11 + 70, 610), (9.8*WIDTH/11 + 70, 690), 5)


def draw_numbers_tree():
    # f = pygame.font.get_fonts()
    # print(f)
    number = FONT.render('0', True, BLACK)
    WIN.blit(number, (175, 720))

    number = FONT.render('1', True, BLACK)
    WIN.blit(number, (375, 720))

    number = FONT.render('2', True, BLACK)
    WIN.blit(number, (265, 720))

    number = FONT.render('3', True, BLACK)
    WIN.blit(number, (955, 720))

    number = FONT.render('4', True, BLACK)
    WIN.blit(number, (630, 720))

    number = FONT.render('5', True, BLACK)
    WIN.blit(number, (790, 720))

    number = FONT.render('6', True, BLACK)
    WIN.blit(number, (720, 720))

    number = FONT.render('7', True, BLACK)
    WIN.blit(number, (910, 720))

    number = FONT.render('8', True, BLACK)
    WIN.blit(number, (835, 720))

    number = FONT.render('9', True, BLACK)
    WIN.blit(number, (65, 720))


def draw_barcode():
    pygame.draw.rect(WIN, WHITE, pygame.Rect(30, 30, 10, 60))
    pygame.draw.rect(WIN, BLACK, pygame.Rect(40, 30, 10, 60))
    pygame.draw.rect(WIN, BLACK, pygame.Rect(50, 30, 10, 60))
    pygame.draw.rect(WIN, BLACK, pygame.Rect(60, 30, 10, 60))
    pygame.draw.rect(WIN, WHITE, pygame.Rect(70, 30, 10, 60))
    pygame.draw.rect(WIN, BLACK, pygame.Rect(80, 30, 10, 60))
    pygame.draw.rect(WIN, BLACK, pygame.Rect(90, 30, 10, 60))
    number = FONT.render('7', True, BLACK)
    WIN.blit(number, (60, 90))


if __name__ == "__main__":
    setup()
    main()
