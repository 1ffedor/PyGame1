import pygame
import os
import sys
import random as rnd
from game_settings import *
from pictures import *
import time
import datetime



COLOR_NOT_WANTED = ""
COLOR_WANTED = ""


class MainMenu:

    def __init__(self):
        self.pygame_init()
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
        self.best_score = best_score

        self.start_game = False
        self.exit = False
        self.running = True

        self.font = pygame.font.Font(None, 70)

        self.main_menu_play_text_color = MAIN_MENU_SCORE_PLAY_TEXT_COLOR
        self.main_menu_play_rect_color = MAIN_MENU_SCORE_PLAY_RECT_COLOR

        self.main_menu_score_play_rect_x = MAIN_MENU_SCORE_PLAY_RECT_X
        self.main_menu_score_play_rect_y = MAIN_MENU_SCORE_PLAY_RECT_Y

        self.main_menu_play_rect_width = MAIN_MENU_SCORE_PLAY_RECT_WIDTH
        self.main_menu_play_rect_height = MAIN_MENU_SCORE_PLAY_RECT_HEIGHT

        self.main_menu_play_rect_x = MAIN_MENU_SCORE_PLAY_RECT_X
        self.main_menu_play_rect_y = MAIN_MENU_SCORE_PLAY_RECT_Y
        # self.pictures_heroes_animation_small = pictures_heroes_animation_small
        # self.pictures_heroes_large = pictures_heroes_large
        #
        # self.directory_heroes_animation_small_name = DIRECTORY_HEROES_ANIMATION_SMALL_NAME
        # self.directory_heroes_large_name = directory_heroes_large_name

        self.x, self.y = 0, 0

        if self.running:
            self.run()
        # self.delta_time = 1  # секунд
        # self.level_time = 200  # секунд
        #
        # self.ismiss = True  # нужно ли уменьшать время

    def run(self):
        while self.running:
            self.screen.fill('white')
            # board.render(screen)
            self.draw()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    self.pygame_quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # print(board.get_click(event.pos))  # вывод координат клетки ad
                    self.check_coords(event.pos)

                if event.type == pygame.MOUSEMOTION:
                    aim_x, aim_y = event.pos  # проверка на нажатие

            if pygame.mouse.get_focused():
                pygame.mouse.set_visible(False)

                self.aim_sprite.rect.x = aim_x - self.aim_size_x_half  # 25 - половина размера прицела
                self.aim_sprite.rect.y = aim_y - self.aim_size_y_half  # 25 - половина размера прицела
                self.aim_sprites_group.draw(self.screen2)

            self.clock.tick(self.fps)
            pygame.display.flip()

        # self.pygame_quit()

    def pygame_quit(self):
        pygame.quit()

    def pygame_init(self):
        pygame.init()

    def check_coords(self, pos):
        click_x, click_y = pos
        self.check_play_button(click_x, click_y)

    def check_play_button(self, click_x, click_y):
        width = self.main_menu_play_rect_width
        height = self.main_menu_play_rect_height
        x = self.main_menu_play_rect_x
        y = self.main_menu_play_rect_y
        if self.check_click(click_x, click_y, x, y, width, height):
            self.game_start()

    def check_click(self, click_x, click_y, x, y, width, height):
         if x <= click_x <= x + width and y <= click_y <= y + height:
            return True
         else:
            return False

    def game_start(self):
        self.running = False
        Game(PICTURES_HEROES_ANIMATION_SMALL, PICTURES_HEROES_LARGE, DIRECTORY_HEROES_ANIMATION_SMALL_NAME,
             DIRECTORY_HEROES_LARGE_NAME, level_start, best_score).run()
        print("start_game")

    def draw(self):
        self.draw_rect(MAIN_MENU_SCORE_PLAY_RECT_X, MAIN_MENU_SCORE_PLAY_RECT_Y,
                       MAIN_MENU_SCORE_PLAY_RECT_WIDTH, MAIN_MENU_SCORE_PLAY_RECT_HEIGHT, self.main_menu_play_rect_color)
        self.draw_text(f"Играть", MAIN_MENU_SCORE_PLAY_TEXT_X, MAIN_MENU_SCORE_PLAY_TEXT_Y, self.main_menu_play_text_color)
        # self.draw_text(f"Лучший результат: {self.best_score}", MAIN_MENU_SCORE_TEXT_X, MAIN_MENU_SCORE_TEXT_Y)  # счет

    def draw_text(self, to_write, x, y, color):
        text = self.font.render(f"{to_write}", True, color)
        text_x = x - text.get_width() // 2
        text_y = y - text.get_height() // 2
        self.screen.blit(text, (text_x, text_y))

    def draw_line(self):
        pygame.draw.line(self.screen, "black", [INFO_BOARD_X, 0],
                         [INFO_BOARD_X, INFO_BOARD_Y], 6)

    def draw_rect(self, x, y, width, height, color, *radius):
        pygame.draw.rect(self.screen, color, (x, y, width, height), 6)

    def load_image(self, name, directory_name, colorkey=None):
        fullname = os.path.join(directory_name, name)
        # если файл не существует, то выходим
        if not os.path.isfile(fullname):
            print(f"Файл с изображением '{fullname}' не найден")
            sys.exit()
        image = pygame.image.load(fullname)
        return image


class Game:

    def __init__(self, pictures_heroes_animation_small, pictures_heroes_large, directory_heroes_animation_small_name,
                 directory_heroes_large_name, level_start, best_score):
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
        self.best_score = best_score

        self.isupdate_level = False
        self.running = True
        self.score = 0

        self.pictures_heroes_animation_small = pictures_heroes_animation_small
        self.pictures_heroes_large = pictures_heroes_large

        self.directory_heroes_animation_small_name = DIRECTORY_HEROES_ANIMATION_SMALL_NAME
        self.directory_heroes_large_name = directory_heroes_large_name

        self.x, self.y = 0, 0

        self.delta_time = 1  # секунд
        self.level_time = 200  # секунд

        self.ismiss = True  # нужно ли уменьшать время

    def run(self):
        self.update_level(self.level)

        i = 0
        x, y = self.x, self.y
        # t = time.time()

        start_ticks = pygame.time.get_ticks()  # starter tick
        while self.running:
            self.screen.fill('white')
            # board.render(screen)
            self.heroes_sprites_group.draw(self.screen3)

            self.level_time = max(0, self.level_time)

            seconds = round(self.level_time + (start_ticks - pygame.time.get_ticks()) / 1000)  # calculate how many seconds
            # print(seconds)
            seconds_res = time.gmtime(seconds)
            current_level_time = time.strftime("%S", seconds_res)

            InfoBoard(self.screen4, self.score, self.best_score, current_level_time)

            if seconds <= 0:
                self.running = False

            self.ismiss = True  # нужно ли уменьшать время

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # print(board.get_click(event.pos))  # вывод координат клеткиad
                    self.heroes_sprites_group.update(event)

                if event.type == pygame.MOUSEMOTION:
                    x, y = event.pos  # проверка на нажатие

            if pygame.mouse.get_focused():
                pygame.mouse.set_visible(False)

                self.aim_sprite.rect.x = x - self.aim_size_x_half  # 25 - половина размера прицела
                self.aim_sprite.rect.y = y - self.aim_size_y_half  # 25 - половина размера прицела
                self.aim_sprites_group.draw(self.screen2)
            # self.heroes_sprites_group.update()
            i += 1
            i %= 8
            for hero in self.heroes_sprites_group:
                if i == 7:
                    hero.update_image()
                if hero.ismiss() and self.ismiss:
                    self.level_time -= 5
                    self.level_time = max(1, self.level_time)
                    self.ismiss = False  # уменьшили время, уже не нужно

                if not hero.isupdate_level():
                    hero.unmiss()  # убрать флаг об уменьшении времени у всех героев
                    hero.move()
                else:
                    self.isupdate_level = True
                    self.level = hero.current_level()
                    self.score += 1
                    self.level_time = 20
                    start_ticks = pygame.time.get_ticks()
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
        image_wanted, image_wanted_large, images_not_wanted = self.choose_picture()
        Hero(self.heroes_sprites_group, wanted, self.level, image_wanted, image_wanted_large, images_not_wanted, table_info)
        for i in range(heroes_count):
            Hero(self.heroes_sprites_group, wanted, self.level, image_wanted, image_wanted_large, images_not_wanted)
            wanted = False
            table_info = False

    def choose_picture(self, *pictures_used):
        pictures = self.pictures_heroes_animation_small[:]
        directory_heroes_animation_small_name = self.directory_heroes_animation_small_name  # директория с фреймами для анимации
        directory_heroes_large_name = self.directory_heroes_large_name

        # if pictures_used:
        #     for picture in pictures_used:
        #         if picture in pictures:
        #             pictures.remove(picture)

        pictures_not_wanted = self.choose_pictures_not_wanted(pictures, self.level)
        for picture_not_wanted in pictures_not_wanted:
            pictures.remove(picture_not_wanted)
        picture_wanted = pictures[rnd.randrange(len(pictures))]
        picture_wanted_large = picture_wanted.split('_')[1] + '_large.png'

        images_not_wanted = [self.load_image(picture, directory_heroes_animation_small_name) for picture in pictures_not_wanted]
        image_wanted = self.load_image(picture_wanted, directory_heroes_animation_small_name)
        image_wanted_large = self.load_image(picture_wanted_large, directory_heroes_large_name)

        return image_wanted, image_wanted_large, images_not_wanted

    def choose_pictures_not_wanted(self, pictures, level):
        pictures = pictures[:]
        pictures_not_wanted = []
        pictures_count = min(level, len(pictures) - 1)
        # print(pictures_count)
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

    def __init__(self, heroes_sprites_group, wanted, level, image_wanted, image_wanted_large, images_not_wanted, table_info=False):
        # НЕОБХОДИМО вызвать конструктор родительского класса Sprite.
        # Это очень важно !!!
        super().__init__(heroes_sprites_group)

        # image_wanted, image_not_wanted, color_hero_wanted, color_hero_not_wanted = self.change_color()
        # self.color_hero_wanted, self.color_hero_not_wanted = color_hero_wanted, color_hero_not_wanted

        self.heroes_sprites_group = heroes_sprites_group

        self.score = 0
        self.update_level = False
        self.miss = False

        self.level = level
        self.table_info = table_info
        self.wanted = wanted
        self.v = V // FPS

        if table_info:
            self.image = image_wanted_large
        else:
            if wanted:
                sheet = image_wanted
            else:
                sheet = images_not_wanted[rnd.randrange(2)]
            self.cur_frame = 0
            self.frames = []
            self.cut_sheet(sheet, 8, 1)

            self.image = self.frames[self.cur_frame]
            # self.rect = self.rect.move(0, 0)
        self.rect = self.image.get_rect()
        self.update_position()

        # self.pictures = PICTURES
        self.create_v()

    def cut_sheet(self, sheet, columns, rows):
        self.rect = pygame.Rect(0, 0, 35, 35)
        self.rect = pygame.Rect(0, 0, 35, 35)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)))

    def update_image(self):
        if not self.table_info:
            self.cur_frame = (self.cur_frame + 1) % len(self.frames)
            self.image = self.frames[self.cur_frame]

    def change_color(self, *pictures_used):
        picture_hero_not_wanted, picture_hero_wanted = self.choose_color("data\smiles_1")
        image_not_wanted = self.load_image(picture_hero_not_wanted, "data\smiles_1")
        image_wanted = self.load_image(picture_hero_wanted, "data\smiles_1")
        return image_wanted, image_not_wanted, picture_hero_wanted, picture_hero_not_wanted

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

    def update_position(self):
        if self.table_info:
            self.rect.x, self.rect.y = INFO_BOARD_X + (WIDTH - INFO_BOARD_Y) // 5, HEIGHT // 16
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

        if args and args[0].type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(args[0].pos):
            if self.wanted and not self.table_info:
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
        else:
            self.miss = True

    def ismiss(self):
        return self.miss

    def unmiss(self):
        self.miss = False

    def current_score(self):
        return self.score

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
        self.vx = int([rnd.randrange(-self.v, -self.v // 3), rnd.randrange(self.v // 3, self.v)][rnd.randrange(1)] + rnd.uniform(-rnd.random(), rnd.random()))
        # self.vx = int(rnd.randrange(-self.v, self.v) + rnd.uniform(-rnd.random(), rnd.random()))
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
        if rnd.random() > 0.995:
            self.create_v()

    def jump(self):
        self.rect = self.rect.move(rnd.randrange(3) - 1, rnd.randrange(3) - 1)


class InfoBoard:

    def __init__(self, screen, score, best_score, current_level_time):
        self.screen = screen
        self.score = score
        self.best_score = best_score

        self.rect_color = INFO_BOARD_RECT_COLOR
        self.time_text_color = INFO_BOARD_TIME_TEXT_COLOR
        self.score_text_color = INFO_BOARD_SCORE_TEXT_COLOR

        self.current_level_time = current_level_time
        self.font = pygame.font.Font(None, 70)
        self.draw()
        # print(score)

    def draw(self):
        self.draw_line()
        self.draw_rect(INFO_BOARD_RECT_X, INFO_BOARD_RECT_Y, INFO_BOARD_RECT_WIDTH, INFO_BOARD_RECT_HEIGHT, self.rect_color)
        self.draw_text(f"Время: {self.current_level_time}", INFO_BOARD_TIME_TEXT_X, INFO_BOARD_TIME_TEXT_Y, self.time_text_color)  # таймер
        self.draw_text(f"Счёт: {self.score}", INFO_BOARD_SCORE_TEXT_X, INFO_BOARD_SCORE_TEXT_Y, self.score_text_color)  # счет

    def draw_line(self):
        pygame.draw.line(self.screen, "black", [INFO_BOARD_X, 0],
                         [INFO_BOARD_X, INFO_BOARD_Y], 6)

    def draw_rect(self, x, y, width, height, color, *radius):
        pygame.draw.rect(self.screen, color, (x, y, width, height), 6)

    def draw_text(self, to_write, x, y, color):
        text = self.font.render(f"{to_write}", True, "black")
        text_x = x - text.get_width() // 2
        text_y = y - text.get_height() // 2
        self.screen.blit(text, (text_x, text_y))

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
    level_start, best_score = 100, 1
    MainMenu()
    # Game(PICTURES_HEROES_ANIMATION_SMALL, PICTURES_HEROES_LARGE, DIRECTORY_HEROES_ANIMATION_SMALL_NAME,
    #      DIRECTORY_HEROES_LARGE_NAME, level_start, best_score).run()
