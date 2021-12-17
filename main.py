import pygame
import os
import sys


FPS = 120
SCREEN_SIZE = (1200, 800)
X, Y = 0, 0

def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


class Board:
    # создание поля
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.board_coords = []
        # значения по умолчанию
        self.left = 0
        self.top = 0
        self.cell_size = 40
        self.check_append = True
    # настройка внешнего вида

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        for i in range(self.height):
            if self.check_append:
                self.board_coords.append([])
            for j in range(self.width):
                x, y = self.left + j * self.cell_size, self.top + i * self.cell_size
                x1, y1 = self.cell_size, self.cell_size
                if self.check_append:
                    self.board_coords[i].append((x, y, x + x1, y + y1))
                pygame.draw.rect(screen, ('black'), (x, y, x1, y1), 1)
        self.check_append = False

    def get_cell(self, mouse_pos):
        x, y = mouse_pos
        x1, y1 = None, None
        for row in range(len(self.board_coords)):
            for col in range(len(self.board_coords[row])):
                x_cell, y_cell, x_cell1, y_cell1 = self.board_coords[row][col]
                if x >= x_cell and x <= x_cell1 and y >= y_cell and y <= y_cell1:
                    x1, y1 = col, row
        if x1 != None and y1 != None:
            return (x1, y1)
        else:
            return None

    def on_click(self, cell_coords):
        return cell_coords

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        return self.on_click(cell)


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('игра')
    board = Board(30, 20)
    size = 1200, 800

    screen = pygame.display.set_mode(size)
    screen2 = pygame.display.set_mode(size)

    clock = pygame.time.Clock()

    all_sprites = pygame.sprite.Group()

    # создадим спрайт
    sprite = pygame.sprite.Sprite()
    # определим его вид
    sprite.image = load_image("aim2.png")
    # и размеры
    sprite.rect = sprite.image.get_rect()
    # добавим спрайт в группу
    all_sprites.add(sprite)

    running = True

    while running:
        screen.fill('white')
        board.render(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(board.get_click(event.pos))
                pass
            if event.type == pygame.MOUSEMOTION:
                x, y = event.pos
        if pygame.mouse.get_focused():
            pygame.mouse.set_visible(False)
            all_sprites.draw(screen2)
            sprite.rect.x = x - 25  # 25 - половина размера прицела
            sprite.rect.y = y - 25  # 25 - половина размера прицела
        clock.tick(FPS)
        pygame.display.flip()
    pygame.quit()
