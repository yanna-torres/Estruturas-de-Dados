import pygame

pygame.font.init()

# CONSTANTES DA TELA
WIDTH, HEIGHT = 1000, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

# COLORS
BACKGROUND_COLOR = 53, 143, 101
WHITE = 255, 255, 255
BLACK = 0, 0, 0
GREY_150 = 150, 150, 150
RED = 255, 0, 0

# FPS do 'jogo'
FPS = 60

# CIRCLE RADIUS
RADIUS = 13

FONT = pygame.font.SysFont('cambriamath', 20, True)
HEADING = pygame.font.SysFont('cambriamath', 35, True)

x, Y = 15, 60


def setup():
    pygame.display.set_caption("Trabalho Final - Yanna")
    draw_tree()
    scanner(x, Y)
    pygame.display.update()


def main():
    clock = pygame.time.Clock()
    run = True
    new_s_x = 15
    reader_x = WIDTH/2
    reader_y = 150
    move_scanner = True
    case = 7
    while run:
        clock.tick(FPS)
        if case != 7:
            animation(new_s_x, reader_x, reader_y)
        else:
            WIN.fill(BACKGROUND_COLOR)
            message = HEADING.render('O número presente no código de barras é:', True, BLACK)
            number = HEADING.render('7', True, BLACK)
            WIN.blit(message, (150, HEIGHT/2 - 100))
            WIN.blit(number, (WIDTH / 2-10, HEIGHT / 2))
            pygame.display.update()

        if move_scanner:
            new_s_x += 0.5

        if (new_s_x - 5) % 10 == 0 and new_s_x > 30:
            move_scanner = False

            if case == 0:
                reader_y += 0.5

                if reader_y == 250:
                    case = 1
                    move_scanner = True

            elif case == 1:
                reader_x += 0.5
                reader_y = ((40*reader_x) / 133) + (13250 / 133)

                if reader_x == 766:
                    case = 2
                    move_scanner = True

            elif case == 2:
                reader_x += 0.5
                reader_y = ((10*reader_x) / 13) - (3370 / 13)

                if reader_x == 870:
                    case = 3
                    move_scanner = True

            elif case == 3:
                reader_x += 0.5
                reader_y = ((40*reader_x) / 21) - (8730 / 7)

                if reader_x == 933:
                    case = 4
                    move_scanner = True

            elif case == 4:
                reader_x -= 0.5
                reader_y = -(40/9)*(reader_x - 933) + 530

                if reader_x == 915:
                    case = 5
                    move_scanner = True

            elif case == 5:
                reader_y += 0.5

                if reader_y == 690:
                    case = 6

            elif case == 6:
                reader_y += 0.5

                if reader_y == 715:
                    move_scanner = True
                    case = 7

        # Para o programa parar quando
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

    pygame.quit()


def draw_tree():
    WIN.fill(BACKGROUND_COLOR)
    pygame.display.update()
    draw_barcode()
    draw_lines_tree()
    draw_circles_tree()
    draw_numbers_tree()
    pygame.display.update()


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


def scanner(pos_x, pos_y):
    pygame.draw.circle(WIN, RED, (pos_x, pos_y), 5, 5)


def reader(pos_x, pos_y):
    pygame.draw.circle(WIN, RED, (pos_x, pos_y), 8, 8)


def animation(s_x, r_x, r_y):
    draw_tree()
    scanner(s_x, Y)
    reader(r_x, r_y)
    pygame.display.update()


if __name__ == "__main__":
    setup()
    main()
