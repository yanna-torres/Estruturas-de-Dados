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

BG = pygame.image.load("images/codigo.png")

# FPS do 'jogo'
FPS = 60

# CIRCLE RADIUS
RADIUS = 13

FONT = pygame.font.SysFont('cambriamath', 20, True)
HEADING = pygame.font.SysFont('cambriamath', 35, True)

x, Y = 15, 60


# Estrutura -> Codigo de Barras
class EmptyStructure(Exception):
    pass


class BinaryNode:

    def __init__(self, data=None, parent=None, left=None, right=None):
        self._data = data
        self._parent = parent
        self._left = left
        self._right = right

    def __repr__(self):
        return str(self._data)

    def __eq__(self, comp):
        if self.data() == comp:
            return True
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __le__(self, other):
        if isinstance(other, BinaryNode):
            return self.data() <= other.data()
        else:
            return False

    def data(self):
        """Returns the value of the main element in the node"""
        return self._data

    def left(self):
        """Returns the value of the left child"""
        return self._left

    def right(self):
        """Returns the value of the right child"""
        return self._right

    def parent(self):
        """Returns the value of the parent of the Node"""
        return self._parent

    def set_data(self, value):
        """Set the value of the main element in the node"""
        self._data = value

    def set_left(self, value):
        """Set the value of the left child"""
        self._left = value

    def set_right(self, value):
        """Set the value of the right child"""
        self._right = value

    def set_parent(self, value):
        """Set the value of the parent"""
        self._parent = value


class BarCodeNumberTree:

    def __init__(self):
        self._root = BinaryNode(0)
        self._root.set_left(BinaryNode(0, self._root))
        self._root.set_right(BinaryNode(1, self._root))
        self._left_tree()
        self._right_tree()

    def _left_tree(self):
        """Metodo privado para montar o lado esquerdo da arvore"""
        left = self._root.left()
        left.set_left(BinaryNode(0, left))
        left.set_right(BinaryNode(1, left))

        left = left.left()
        left.set_right(BinaryNode(1, left))

        right = left.right()
        right.set_left(BinaryNode(0, right))
        right.set_right(BinaryNode(1, right))

        left = right.left()
        left.set_right(BinaryNode(1, left))
        left.right().set_left(BinaryNode(9, left.right()))

        right = right.right()
        right.set_left(BinaryNode(0, right))
        right.left().set_left(BinaryNode(0, right.left()))

        right = self._root.left().right()
        right.set_right(BinaryNode(1, right))
        right.set_left(BinaryNode(0, right))

        left = right.left()
        left.set_left(BinaryNode(0, left))
        left = left.left()
        left.set_right(BinaryNode(1, left))
        left.right().set_left(BinaryNode(2, left.right()))

        right = right.right()
        right.set_left(BinaryNode(0))
        left = right.left()
        left.set_left(BinaryNode(0))
        left.left().set_left(BinaryNode(1, left.left()))

    def _right_tree(self):
        """Metodo privado para montar o lado direito da arvore"""
        right_main = self._root.right()
        right_main.set_left(BinaryNode(0, right_main))
        right_main.set_right(BinaryNode(1, right_main))

        left = right_main.left()
        left.set_left(BinaryNode(0, left))
        left.set_right(BinaryNode(1, left))

        right = left.right()
        right.set_right(BinaryNode(1, right))
        right = right.right()
        right.set_right(BinaryNode(1, right))
        right.right().set_left(BinaryNode(6, right.right()))

        left = left.left()
        left.set_left(BinaryNode(0, left))
        left.left().set_right(BinaryNode(1, left.left()))
        left.left().right().set_left(BinaryNode(4, left.left().right()))

        right = right_main.right()
        right.set_left(BinaryNode(0, right))
        right.set_right(BinaryNode(1, right))

        left = right.left()
        left.set_left(BinaryNode(0, left))
        left.left().set_left(BinaryNode(0, left.left()))
        left.left().left().set_left(BinaryNode(5, left.left().left()))
        left.set_right(BinaryNode(1, left))
        left.right().set_right(BinaryNode(1, left.right()))
        left.right().right().set_left(BinaryNode(8, left.right().right()))

        right = right.right()
        right.set_left(BinaryNode(0, right))
        right.left().set_right(BinaryNode(1, right.left()))
        right.left().right().set_left(BinaryNode(7, right.left().right()))
        right.set_right(BinaryNode(1))
        right.right().set_left(BinaryNode(0))
        right.right().left().set_left(BinaryNode(3, right.right().left()))

    def _inoder_tree(self, root=None):
        """Retorna todos os valores da arvore, seguindo esta ordem: left, root, right."""
        if self.empty():
            raise EmptyStructure("The tree is empty")

        result = []
        if root is None:
            root = self._root

        if root.left() is not None:
            result = self._inoder_tree(root.left())
        result.append(root)
        if root.right() is not None:
            result = result + self._inoder_tree(root.right())

        return result

    def root(self):
        """Retorna o valor que esta na raiz da arvore"""
        return self._root

    def empty(self):
        """Retorna se a arvore esta vazia ou nao"""
        return self.root() is None

    def search_num(self, numero):
        """Busca um numero binario e retorna seu valor em decimal"""
        num = str(numero)
        return self._search(num, self._root)

    def _search(self, num, root):
        if len(num) <= 2:
            return str(root.left())
        elif root.left() == int(num[1]):
            return self._search(num[1:], root.left())
        else:
            return self._search(num[1:], root.right())

    def find_binary(self, num):
        """Busca um numero decimal e retorna seu valor em binario"""
        list_tree = self._inoder_tree()
        i = list_tree.index(num)
        elem = list_tree[i]
        return self._binary(elem.parent()) + "1"

    def _binary(self, elem):
        if elem.parent() is None:
            return str(elem.data())
        else:
            return self._binary(elem.parent()) + str(elem.data())


# Apresentacao visual do funcionamento
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
    case = 0
    while run:
        pygame.display.update()
        clock.tick(FPS)
        if case != 7:
            animation(new_s_x, reader_x, reader_y)
        else:
            WIN.blit(BG, (0, 0))
            # WIN.fill(GREY_150)
            message = HEADING.render('O número presente no código de barras é:', True, BLACK)
            number = HEADING.render('7', True, BLACK)
            pygame.draw.rect(WIN, WHITE, pygame.Rect(150, HEIGHT/2 - 100, 750, 40))
            pygame.draw.rect(WIN, WHITE, pygame.Rect(WIDTH / 2-10, HEIGHT / 2, 22, 40))
            WIN.blit(message, (150, HEIGHT/2 - 100))
            WIN.blit(number, (WIDTH / 2-10, HEIGHT / 2))

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
    # WIN.fill(BACKGROUND_COLOR)
    WIN.blit(BG, (0, 0))
    draw_barcode()
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
    # number = FONT.render('7', True, BLACK)
    # WIN.blit(number, (60, 90))


def scanner(pos_x, pos_y):
    pygame.draw.circle(WIN, RED, (pos_x, pos_y), 5, 5)


def reader(pos_x, pos_y):
    pygame.draw.circle(WIN, RED, (pos_x, pos_y), 8, 8)


def animation(s_x, r_x, r_y):
    draw_tree()
    scanner(s_x, Y)
    reader(r_x, r_y)


if __name__ == "__main__":
    bc = BarCodeNumberTree()
    codigo = bc.search_num("0111011")
    codigo = codigo + bc.search_num("0110111")
    codigo = codigo + bc.search_num("0110001")
    codigo = codigo + bc.search_num("0100011")
    codigo = codigo + " "
    codigo = codigo + bc.search_num("0011001")
    codigo = codigo + bc.search_num("0001101")
    codigo = codigo + bc.search_num("0010011")
    codigo = codigo + bc.search_num("0001011")
    print("buscador de número binário -> decimal")
    print(codigo)  # resultado esperado: 7854 1029
    print("")
    print("buscador de número decimal -> binário")
    print(f"7854 1029 = {bc.find_binary(7)} {bc.find_binary(8)} {bc.find_binary(5)} {bc.find_binary(4)}  {bc.find_binary(1)} {bc.find_binary(0)} {bc.find_binary(2)} {bc.find_binary(9)}")
    setup()
    main()
