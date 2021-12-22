import pygame
import os
import sys
import random as rnd
from game_settings import *
from pictures import *
import time


COLOR_NOT_WANTED = ""
COLOR_WANTED = ""


class Game:

    def __init__(self, PICTURES, DIRECTORY_NAME, level_start, best_result):
        pygame.init()
        pygame.display.set_caption('игра')

        self.size = SCREEN_SIZE
        self.fps = FPS
        self.aim_size = AIM_SIZE
        self.aim_size_x = AIM_SIZE[0]
        self.aim_size_y = AIM_SIZE[1]
        self.aim_size_x_half = AIM_SIZE_HALF[0]
        self.aim_size_y_half = AIM_SIZE_HALF[1]

        self.screen = pygame.display.set_mode(self.size)
        self.screen2 = pygame.display.set_mode(self.size)
        self.screen3 = pygame.display.set_mode(self.size)
        self.screen4 = pygame.display.set_mode(self.size)

        self.clock = pygame.time.Clock()

        self.aim_sprites_group = pygame.sprite.Group()
        self.aim_sprite = pygame.sprite.Sprite()  # создадим спрайт
        self.aim_sprite.image = self.load_image("aim1.png", "data")  # определим его вид
        self.aim_sprite.rect = self.aim_sprite.image.get_rect()  # и размеры
        self.aim_sprites_group.add(self.aim_sprite)  # добавим спрайт в группу

        self.heroes_sprites_group = pygame.sprite.Group()

        self.level = level_start
        self.best_result = best_result

        self.isupdate_level = False
        self.running = True

        self.pictures = PICTURES[:]

        self.directory_name = DIRECTORY_NAME
        self.x, self.y = 0, 0

    def run(self):
        self.update_level(self.level)
        x, y = self.x, self.y
        while self.running:
            self.screen.fill('white')
            # board.render(screen)
            self.heroes_sprites_group.draw(self.screen3)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # print(board.get_click(event.pos))  # вывод координат клеткиad
                    pass
                if event.type == pygame.MOUSEMOTION:
                    x, y = event.pos

                self.heroes_sprites_group.update(event)  # проверка на нажатие

            if pygame.mouse.get_focused():
                pygame.mouse.set_visible(False)

                self.aim_sprite.rect.x = x - self.aim_size_x_half  # 25 - половина размера прицела
                self.aim_sprite.rect.y = y - self.aim_size_y_half  # 25 - половина размера прицела
                self.aim_sprites_group.draw(self.screen2)

            for hero in self.heroes_sprites_group:
                if not hero.isupdate_level():
                    hero.move()
                else:
                    self.isupdate_level = True
                    self.level = hero.current_level()
                    break
            if self.isupdate_level:
                for hero in self.heroes_sprites_group:
                    hero.remove(self.heroes_sprites_group)
                self.update_level(self.level)
                self.isupdate_level = False

            self.clock.tick(self.fps)
            pygame.display.flip()

        pygame.quit()

    def load_image(self, name, directory_name, colorkey=None):
        fullname = os.path.join(directory_name, name)
        # если файл не существует, то выходим
        if not os.path.isfile(fullname):
            print(f"Файл с изображением '{fullname}' не найден")
            sys.exit()
        image = pygame.image.load(fullname)
        return image

    def update_level(self, heroes_count):
        wanted = True
        table_info = True
        image_wanted, images_not_wanted = self.choose_picture(self.directory_name)
        Hero(self.heroes_sprites_group, wanted, self.level, image_wanted, images_not_wanted, table_info)
        for i in range(heroes_count):
            Hero(self.heroes_sprites_group, wanted, self.level, image_wanted, images_not_wanted)
            wanted = False
            table_info = False

    def choose_picture(self, directory_name, *pictures_used):
        pictures = self.pictures[:]
        directory_name = self.directory_name
        # if pictures_used:
        #     for picture in pictures_used:
        #         if picture in pictures:
        #             pictures.remove(picture)
        pictures_not_wanted = self.choose_pictures_not_wanted(self.pictures, self.level)
        for picture_not_wanted in pictures_not_wanted:
            pictures.remove(picture_not_wanted)
        picture_wanted = pictures[rnd.randrange(len(pictures))]
        images_not_wanted = [self.load_image(picture, directory_name) for picture in pictures_not_wanted]
        image_wanted = self.load_image(picture_wanted, directory_name)
        return (image_wanted, images_not_wanted)

    def choose_pictures_not_wanted(self, pictures, level):
        pictures = pictures[:]
        pictures_not_wanted = []
        pictures_count = min(level, len(pictures) - 1)
        print(pictures_count)
        try:
            for n in range(pictures_count):
                picture_not_wanted = pictures[rnd.randrange(len(pictures))]
                pictures_not_wanted.append(picture_not_wanted)
                pictures.remove(picture_not_wanted)
            return pictures_not_wanted
        except Exception as e:
            print(e)



class Hero(pygame.sprite.Sprite):
    # color_hero_not_wanted, color_hero_wanted = Game.choose_color("data\smiles_1")
    # image_not_wanted = Game.load_image(color_hero_not_wanted, "data\smiles_1")
    # image_wanted = Game.load_image(color_hero_wanted, "data\smiles_1")

    def __init__(self, heroes_sprites_group, wanted, level, image_wanted, images_not_wanted, table_info=False):
        # НЕОБХОДИМО вызвать конструктор родительского класса Sprite.
        # Это очень важно !!!
        super().__init__(heroes_sprites_group)

        # image_wanted, image_not_wanted, color_hero_wanted, color_hero_not_wanted = self.change_color()
        # self.color_hero_wanted, self.color_hero_not_wanted = color_hero_wanted, color_hero_not_wanted

        self.heroes_sprites_group = heroes_sprites_group

        self.score = 0

        self.table_info = table_info

        if wanted:
            self.image = image_wanted
            self.update_info_board(self.score)
        else:
            self.image = images_not_wanted[rnd.randrange(2)]

        self.wanted = wanted

        self.rect = self.image.get_rect()

        self.v = V // FPS

        self.update_position()

        self.update_level = False

        self.level = level

        self.pictures = PICTURES
        self.create_v()

    # def choose_color(self, name_directory, *pictures_used):
    #     pictures = self.pictures[:]
    #     if pictures_used:
    #         for picture in pictures_used:
    #             if picture in pictures:
    #                 pictures.remove(picture)
    #     picture_not_wanted = pictures[rnd.randrange(len(pictures))]
    #     pictures.remove(picture_not_wanted)
    #     picture_wanted = pictures[rnd.randrange(len(pictures))]
    #     return (picture_not_wanted, picture_wanted)

    def change_color(self, *pictures_used):
        picture_hero_not_wanted, picture_hero_wanted = self.choose_color("data\smiles_1")
        image_not_wanted = self.load_image(picture_hero_not_wanted, "data\smiles_1")
        image_wanted = self.load_image(picture_hero_wanted, "data\smiles_1")
        return (image_wanted, image_not_wanted, picture_hero_wanted, picture_hero_not_wanted)

    def create_colors(self):
        pass

    def choose_color(self, name_directory, *pictures_used):
        pictures = PICTURES[:]
        if pictures_used:
            for picture in pictures_used:
                if picture in pictures:
                    pictures.remove(picture)
        picture_not_wanted = pictures[rnd.randrange(len(pictures))]
        pictures.remove(picture_not_wanted)
        picture_wanted = pictures[rnd.randrange(len(pictures))]
        return (picture_not_wanted, picture_wanted)

    def update_info_board(self, score):
        pass
        # InfoBoard(screen4, image_wanted, score)

    def update_position(self):
        if self.table_info:
            self.rect.x, self.rect.y = INFO_BOARD_WIDTH + (WIDTH - INFO_BOARD_WIDTH) // 5, HEIGHT // 16
        else:
            self.rect.x = rnd.randrange(70, GAME_FIELD_WIDTH)
            self.rect.y = rnd.randrange(70, GAME_FILED_HEIGHT)

    def load_image(self, name, name_directory, colorkey=None):
        fullname = os.path.join(name_directory, name)
        # если файл не существует, то выходим
        if not os.path.isfile(fullname):
            print(f"Файл с изображением '{fullname}' не найден")
            sys.exit()
        image = pygame.image.load(fullname)
        return image

    def update(self, *args):
        if self.wanted and not self.table_info:
            if args and args[0].type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(args[0].pos):
                self.update_level = True
                #self.create_colors()
                # for hero in heroes_sprites_group:
                #     # hero.change_v(2)
                #     #hero.change_color()
                #     hero.jump()
                # for hero in self.heroes_sprites_group:
                #     # hero.change_v(2)
                #     #hero.change_color()
                #     hero.update_position()
                self.score += 1
                self.level += 10
                self.update_info_board(self.score)

    def isupdate_level(self):
        return self.update_level

    def current_level(self):
        return self.level

    def move(self):
        if not self.table_info:
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
        #self.vx = int([rnd.randrange(-self.v, -self.v // 2), rnd.randrange(self.v // 2, self.v)][rnd.randrange(1)] + rnd.uniform(-rnd.random(), rnd.random()))
        self.vx = int(rnd.randrange(-self.v, self.v) + rnd.uniform(-rnd.random(), rnd.random()))
        self.vy = (self.v ** 2 - self.vx ** 2) ** 0.5
        if rnd.random() > 0.5:
            self.vy *= -1
        if rnd.random() > 0.5:
            self.vx *= -1
        # self.vx = V // (rnd.random() * FPS)
        # self.vy = V // (rnd.random() * FPS)
        # print(self.vx, self.vy)

    def change_v(self, k):
        self.v += k
        self.create_v()

    def move_random_direction(self):
        if rnd.random() > 0.99:
            self.create_v()

    def jump(self):
        self.rect = self.rect.move(rnd.randrange(3) - 1, rnd.randrange(3) - 1)


class InfoBoard:

    def __init__(self, screen, image_wanted, score):
        self.screen = screen
        self.draw()

    def draw(self):
        self.draw_line()
        self.draw_rect()

    def draw_line(self):
        pygame.draw.line(self.screen, "black", [INFO_BOARD_WIDTH, 0],
                         [INFO_BOARD_WIDTH, INFO_BOARD_HEIGHT], 4)

    def draw_rect(self):
        x1, y1 = INFO_BOARD_WIDTH + (WIDTH - INFO_BOARD_WIDTH) // 5, HEIGHT // 16
        a = 200
        pygame.draw.rect(self.screen, "black", (x1, y1, a, a), 4)

# class Board:
#     # создание поля
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#         self.board = [[0] * width for _ in range(height)]
#         self.board_coords = []
#         # значения по умолчанию
#         self.left = 0
#         self.top = 0
#         self.cell_size = 40
#         self.check_append = True
#     # настройка внешнего вида
#
#     def set_view(self, left, top, cell_size):
#         self.left = left
#         self.top = top
#         self.cell_size = cell_size
#
#     def render(self, screen):
#         for i in range(self.height):
#             if self.check_append:
#                 self.board_coords.append([])
#             for j in range(self.width):
#                 x, y = self.left + j * self.cell_size, self.top + i * self.cell_size
#                 x1, y1 = self.cell_size, self.cell_size
#                 if self.check_append:
#                     self.board_coords[i].append((x, y, x + x1, y + y1))
#                 pygame.draw.rect(screen, ('black'), (x, y, x1, y1), 1)
#         self.check_append = False
#
#     def get_cell(self, mouse_pos):
#         x, y = mouse_pos
#         x1, y1 = None, None
#         for row in range(len(self.board_coords)):
#             for col in range(len(self.board_coords[row])):
#                 x_cell, y_cell, x_cell1, y_cell1 = self.board_coords[row][col]
#                 if x >= x_cell and x <= x_cell1 and y >= y_cell and y <= y_cell1:
#                     x1, y1 = col, row
#         if x1 != None and y1 != None:
#             return (x1, y1)
#         else:
#             return None
#
#     def on_click(self, cell_coords):
#         return cell_coords
#
#     def get_click(self, mouse_pos):
#         cell = self.get_cell(mouse_pos)
#         return self.on_click(cell)



if __name__ == '__main__':
    # pygame.init()
    # pygame.display.set_caption('игра')
    # board = Board(30, 20)
    #
    # size = SCREEN_SIZE
    # fps = FPS
    # aim_size = AIM_SIZE
    # aim_size_x = AIM_SIZE[0]
    # aim_size_y = AIM_SIZE[1]
    # aim_size_x_half = AIM_SIZE_HALF[0]
    # aim_size_y_half = AIM_SIZE_HALF[1]
    #
    # screen = pygame.display.set_mode(size)
    # screen2 = pygame.display.set_mode(size)
    # screen3 = pygame.display.set_mode(size)
    # screen4 = pygame.display.set_mode(size)
    #
    # clock = pygame.time.Clock()
    #
    # # группа прицел
    # aim_sprites_group = pygame.sprite.Group()
    # # создадим спрайт
    # aim_sprite = pygame.sprite.Sprite()
    # # определим его вид
    # aim_sprite.image = load_image("aim1.png", "data")
    # # и размеры
    # aim_sprite.rect = aim_sprite.image.get_rect()
    # # добавим спрайт в группу
    # aim_sprites_group.add(aim_sprite)
    #
    # heroes_sprites_group = pygame.sprite.Group()
    #
    # update_level(200)
    # running = True
    # while running:
    #     screen.fill('white')
    #     # board.render(screen)
    #     heroes_sprites_group.draw(screen3)
    #
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             running = False
    #         if event.type == pygame.MOUSEBUTTONDOWN:
    #             print(board.get_click(event.pos))  # вывод координат клеткиad
    #             pass
    #         if event.type == pygame.MOUSEMOTION:
    #             x, y = event.pos
    #
    #         heroes_sprites_group.update(event)  # обновление позиции персонажей
    #
    #     if pygame.mouse.get_focused():
    #         pygame.mouse.set_visible(False)
    #
    #         aim_sprite.rect.x = x - AIM_SIZE_HALF[0]  # 25 - половина размера прицела
    #         aim_sprite.rect.y = y - AIM_SIZE_HALF[1]  # 25 - половина размера прицела
    #         aim_sprites_group.draw(screen2)
    #
    #     for hero in heroes_sprites_group:
    #         hero.move()
    #
    #     clock.tick(FPS)
    #     pygame.display.flip()
    # pygame.quit()
    level_start, best_result = 1, 1
    Game(PICTURES, DIRECTORY_NAME, level_start, best_result).run()
