import pygame
import os
import sys
import random as rnd
from game_settings import *


def load_image(name, name_directory, colorkey=None):
    fullname = os.path.join(name_directory, name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


def update_level(heroes_count):
    wanted = True
    for i in range(heroes_count):
        Hero(heroes_sprites_group, wanted)
        wanted = False


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


class Hero(pygame.sprite.Sprite):
    image = load_image("yellow.png", "data\smiles_1")
    image_wanted = load_image("blue.png", "data\smiles_1")

    def __init__(self, group, wanted):
        # НЕОБХОДИМО вызвать конструктор родительского класса Sprite.
        # Это очень важно !!!
        super().__init__(group)
        if wanted:
            self.image = Hero.image_wanted
        else:
            self.image = Hero.image
        self.wanted = wanted
        self.rect = self.image.get_rect()
        self.v = v = V // FPS
        self.update_position()
        self.create_v()

    def update_position(self):
        self.rect.x = rnd.randrange(70, GAME_FIELD_WIDTH)
        self.rect.y = rnd.randrange(70, GAME_FILED_HEIGHT)

    def update(self, *args):
        if self.wanted:
            if args and args[0].type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(args[0].pos):
                for hero in heroes_sprites_group:
                    hero.update_position()

    def move(self):
        # движение по полю
        # 1 - случайное направление
        # 2 - отражение при подходе к стене
        # 3 - случайная смена направления в движении
        self.motion_reflection()
        x, y = self.rect.x, self.rect.y
        self.rect.x += self.vx
        self.rect.y += self.vy
        self.move_random_direction()

    def motion_reflection(self):
        if self.rect.x > GAME_FIELD_WIDTH:  # правее
            self.vx = -abs(self.vx)
        elif self.rect.x < 50:  # левее
            self.vx = abs(self.vx)
        if self.rect.y > GAME_FILED_HEIGHT:  # выше
            self.vy = -abs(self.vy)
        elif self.rect.y < 50:  # ниже
            self.vy = abs(self.vy)

    def create_v(self):
        # print(v)
        self.vx = int(rnd.randrange(-self.v, self.v) + rnd.uniform(-rnd.random(), rnd.random()))
        self.vy = (self.v ** 2 - self.vx ** 2) ** 0.5
        if rnd.random() > 0.5:
            self.vy *= -1
        if rnd.random() > 0.5:
            self.vx *= -1
        # self.vx = V // (rnd.random() * FPS)
        # self.vy = V // (rnd.random() * FPS)
        # print(self.vx, self.vy)

    def move_random_direction(self):
        if rnd.random() > 0.99:
            self.create_v()


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('игра')
    board = Board(30, 20)

    size = SCREEN_SIZE
    fps = FPS
    aim_size = AIM_SIZE
    aim_size_x = AIM_SIZE[0]
    aim_size_y = AIM_SIZE[1]
    aim_size_x_half = AIM_SIZE_HALF[0]
    aim_size_y_half = AIM_SIZE_HALF[1]

    screen = pygame.display.set_mode(size)
    screen2 = pygame.display.set_mode(size)
    screen3 = pygame.display.set_mode(size)

    clock = pygame.time.Clock()

    # группа прицел
    aim_sprites_group = pygame.sprite.Group()
    # создадим спрайт
    aim_sprite = pygame.sprite.Sprite()
    # определим его вид
    aim_sprite.image = load_image("aim1.png", "data")
    # и размеры
    aim_sprite.rect = aim_sprite.image.get_rect()
    # добавим спрайт в группу
    aim_sprites_group.add(aim_sprite)

    heroes_sprites_group = pygame.sprite.Group()

    update_level(200)

    running = True
    while running:
        screen.fill('white')
        #board.render(screen)
        heroes_sprites_group.draw(screen3)  # отрисовка персонажей
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(board.get_click(event.pos))  # вывод координат клеткиad
                pass
            if event.type == pygame.MOUSEMOTION:
                x, y = event.pos

            heroes_sprites_group.update(event)  # обновление позиции персонажей

        if pygame.mouse.get_focused():
            pygame.mouse.set_visible(False)

            aim_sprite.rect.x = x - AIM_SIZE_HALF[0]  # 25 - половина размера прицела
            aim_sprite.rect.y = y - AIM_SIZE_HALF[1]  # 25 - половина размера прицела
            aim_sprites_group.draw(screen2)

        for hero in heroes_sprites_group:
            hero.move()


        clock.tick(FPS)
        pygame.display.flip()
    pygame.quit()
