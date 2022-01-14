import pygame
import os
import sys
import random as rnd
from game_settings import *
# from pictures import *
import glob
import time
import sqlite3
import datetime
# from math import sqrt


COLOR_NOT_WANTED = ""
COLOR_WANTED = ""


class MainMenu:

    def __init__(self, ):
        self.pygame_init()
        pygame.display.set_caption('Catch a Smile (v.0.1)')

        # константы
        self.size = SCREEN_SIZE
        self.fps = FPS

        self.set_of_heroes = 0  # номер набора смайлов
        self.set_of_heroes_isbought = False
        self.set_of_heroes_coins_need = 0
        self.get_from_db()

        self.aim_size = AIM_SIZE
        self.aim_size_x = AIM_SIZE[0]
        self.aim_size_y = AIM_SIZE[1]
        self.aim_size_x_half = AIM_SIZE_HALF[0]
        self.aim_size_y_half = AIM_SIZE_HALF[1]

        self.title_sprite_directory = MAIN_MENU_TITLE_SPRITE_DIRECTORY
        self.title_sprite_name = MAIN_MENU_TITLE_SPRITE_NAME
        self.title_sprite_x = MAIN_MENU_TITLE_SPRITE_X
        self.title_sprite_y = MAIN_MENU_TITLE_SPRITE_Y

        self.best_score_and_coins_sprite_directory = MAIN_MENU_BEST_SCORE_AND_COINS_SPRITE_DIRECTORY
        self.best_score_and_coins_sprite_name = MAIN_MENU_BEST_SCORE_AND_COINS_SPRITE_NAME

        self.best_score_and_coins_sprite_x = MAIN_MENU_BEST_SCORE_AND_COINS_SPRITE_X
        self.best_score_and_coins_sprite_y = MAIN_MENU_BEST_SCORE_AND_COINS_SPRITE_Y

        self.best_score_text_center_x = MAIN_MENU_BEST_SCORE_TEXT_CENTER_X
        self.best_score_text_center_y = MAIN_MENU_BEST_SCORE_TEXT_CENTER_Y
        self.coins_count_text_center_x = MAIN_MENU_COINS_COUNT_TEXT_CENTER_X
        self.coins_count_text_center_y = MAIN_MENU_COINS_COUNT_TEXT_CENTER_Y
        self.best_score_and_coins_count_text_color = MAIN_MENU_BEST_SCORE_AND_COINS_COUNT_TEXT_COLOR
        self.best_score_and_coins_count_text_size = MAIN_MENU_BEST_SCORE_AND_COINS_COUNT_TEXT_SIZE

        self.play_sprite_directory = MAIN_MENU_PLAY_SPRITE_DIRECTORY
        self.play_sprite_name = MAIN_MENU_PLAY_SPRITE_NAME
        self.play_sprite_x = MAIN_MENU_PLAY_SPRITE_X
        self.play_sprite_y = MAIN_MENU_PLAY_SPRITE_Y
        self.play_sprite_wight = MAIN_MENU_PLAY_SPRITE_WIGHT
        self.play_sprite_height = MAIN_MENU_PLAY_SPRITE_HEIGHT

        self.play_text_center_x = MAIN_MENU_PLAY_TEXT_CENTER_X
        self.play_text_center_y = MAIN_MENU_PLAY_TEXT_CENTER_Y
        self.play_text_color = MAIN_MENU_PLAY_TEXT_COLOR
        self.play_text_size = MAIN_MENU_PLAY_TEXT_SIZE

        self.set_of_heroes_sprite_directory = MAIN_MENU_SET_OF_HEROES_SPRITE_DIRECTORY
        self.set_of_heroes_sprite_name = MAIN_MENU_SET_OF_HEROES_SPRITE_NAME
        self.set_of_heroes_sprite_x = MAIN_MENU_SET_OF_HEROES_SPRITE_X
        self.set_of_heroes_sprite_y = MAIN_MENU_SET_OF_HEROES_SPRITE_Y

        self.set_of_heroes_lock_directory = MAIN_MENU_SET_OF_HEROES_LOCK_DIRECTORY
        self.set_of_heroes_lock_sprite_name = MAIN_MENU_SET_OF_HEROES_LOCK_SPRITE_NAME
        self.set_of_heroes_lock_sprite_x = MAIN_MENU_SET_OF_HEROES_LOCK_SPRITE_X
        self.set_of_heroes_lock_sprite_y = MAIN_MENU_SET_OF_HEROES_LOCK_SPRITE_Y

        self.set_of_heroes_text_center_x = MAIN_MENU_SET_OF_HEROES_TEXT_CENTER_X
        self.set_of_heroes_text_center_y = MAIN_MENU_SET_OF_HEROES_TEXT_CENTER_Y
        self.set_of_heroes_text_color = MAIN_MENU_SET_OF_HEROES_TEXT_COLOR
        self.set_of_heroes_text_size = MAIN_MENU_SET_OF_HEROES_TEXT_SIZE

        self.arrow_left_sprite_directory = MAIN_MENU_ARROW_LEFT_SPRITE_DIRECTORY
        self.arrow_left_sprite_name = MAIN_MENU_ARROW_LEFT_SPRITE_NAME
        self.arrow_left_sprite_x = MAIN_MENU_ARROW_LEFT_SPRITE_X
        self.arrow_left_sprite_y = MAIN_MENU_ARROW_LEFT_SPRITE_Y

        self.arrow_right_sprite_directory = MAIN_MENU_ARROW_RIGHT_SPRITE_DIRECTORY
        self.arrow_right_sprite_name = MAIN_MENU_ARROW_RIGHT_SPRITE_NAME
        self.arrow_right_sprite_x = MAIN_MENU_ARROW_RIGHT_SPRITE_X
        self.arrow_right_sprite_y = MAIN_MENU_ARROW_RIGHT_SPRITE_Y

        self.font_directory = FONT_DIRECTORY

        # экраны
        self.background_screen = pygame.display.set_mode(self.size)
        self.static_elements_screen = pygame.display.set_mode(self.size)
        self.hero_screen = pygame.display.set_mode(self.size)
        self.heroes_lock_screen = pygame.display.set_mode(self.size)
        self.aim_screen = pygame.display.set_mode(self.size)

        self.clock = pygame.time.Clock()

        # группы спрайтов
        self.aim_sprites_group = pygame.sprite.Group()
        self.aim_sprite = pygame.sprite.Sprite()  # создадим спрайт
        self.aim_sprite.image = self.load_image("aim2.png", "data")  # определим его вид
        self.aim_sprite.rect = self.aim_sprite.image.get_rect()  # и размеры
        self.aim_sprites_group.add(self.aim_sprite)  # добавим спрайт в группу

        self.hero_sprite_x = MAIN_MENU_HERO_SPITE_X
        self.hero_sprite_y = MAIN_MENU_HERO_SPITE_Y

        self.static_elements_sprites_group = pygame.sprite.Group()
        self.heroes_lock_sprites_group = pygame.sprite.Group()
        self.hero_sprites_group = pygame.sprite.Group()

        # создаем спрайты
        self.title_sprite = pygame.sprite.Sprite()
        self.title_sprite.image = self.load_image(f"{self.title_sprite_name}", f"{self.title_sprite_directory}")  # определим его вид
        self.title_sprite.rect = self.title_sprite.image.get_rect()  # и размеры
        self.title_sprite.rect.x = self.title_sprite_x
        self.title_sprite.rect.y = self.title_sprite_y
        self.static_elements_sprites_group.add(self.title_sprite)  # добавим спрайт в группу

        self.best_score_and_coins_sprite = pygame.sprite.Sprite()
        self.best_score_and_coins_sprite.image = \
            self.load_image(f"{self.best_score_and_coins_sprite_name}",
                            f"{self.best_score_and_coins_sprite_directory}")  # определим его вид
        self.best_score_and_coins_sprite.rect = self.best_score_and_coins_sprite.image.get_rect()  # и размеры
        self.best_score_and_coins_sprite.rect.x = self.best_score_and_coins_sprite_x
        self.best_score_and_coins_sprite.rect.y = self.best_score_and_coins_sprite_y
        self.static_elements_sprites_group.add(self.best_score_and_coins_sprite)  # добавим спрайт в группу

        self.set_of_heroes_lock_sprite = pygame.sprite.Sprite()  # создадим спрайт
        self.set_of_heroes_lock_sprite.image = \
            self.load_image(f"{self.set_of_heroes_lock_sprite_name}",
                            f"{self.set_of_heroes_lock_directory}")  # определим его вид
        self.set_of_heroes_lock_sprite.rect = self.set_of_heroes_lock_sprite.image.get_rect()  # и размеры
        self.set_of_heroes_lock_sprite.rect.x = self.set_of_heroes_lock_sprite_x
        self.set_of_heroes_lock_sprite.rect.y = self.set_of_heroes_lock_sprite_y
        self.heroes_lock_sprites_group.add(self.set_of_heroes_lock_sprite)  # добавим спрайт в группу

        self.isdraw_heroes_lock = False  # рисовать ли замок

        self.set_of_heroes_sprite = pygame.sprite.Sprite()  # создадим спрайт
        self.set_of_heroes_sprite.image = \
            self.load_image(f"{self.set_of_heroes_sprite_name}",
                            f"{self.set_of_heroes_sprite_directory}")  # определим его вид
        self.set_of_heroes_sprite.rect = self.set_of_heroes_sprite.image.get_rect()  # и размеры
        self.set_of_heroes_sprite.rect.x = self.set_of_heroes_sprite_x
        self.set_of_heroes_sprite.rect.y = self.set_of_heroes_sprite_y
        self.static_elements_sprites_group.add(self.set_of_heroes_sprite)  # добавим спрайт в группу

        # кнопка играть
        self.play_sprite = pygame.sprite.Sprite()  # создадим спрайт
        self.play_sprite.image = \
            self.load_image(f"{self.play_sprite_name}",
                            f"{self.play_sprite_directory}")  # определим его вид
        self.play_sprite.rect = self.play_sprite.image.get_rect()  # и размеры
        self.play_sprite.rect.x = self.play_sprite_x
        self.play_sprite.rect.y = self.play_sprite_y
        self.static_elements_sprites_group.add(self.play_sprite)  # добавим спрайт в группу

        # стрелки
        self.arrow_left_sprite = pygame.sprite.Sprite()  # создадим спрайт
        self.arrow_left_sprite.image = \
            self.load_image(f"{self.arrow_left_sprite_name}",
                            f"{self.arrow_left_sprite_directory}")  # определим его вид
        self.arrow_left_sprite.rect = self.arrow_left_sprite.image.get_rect()  # и размеры
        self.arrow_left_sprite.rect.x = self.arrow_left_sprite_x
        self.arrow_left_sprite.rect.y = self.arrow_left_sprite_y
        self.static_elements_sprites_group.add(self.arrow_left_sprite)  # добавим спрайт в группу

        self.arrow_right_sprite = pygame.sprite.Sprite()  # создадим спрайт
        self.arrow_right_sprite.image = \
            self.load_image(f"{self.arrow_right_sprite_name}", f"{self.arrow_right_sprite_directory}")  # определим его вид
        self.arrow_right_sprite.rect = self.arrow_right_sprite.image.get_rect()  # и размеры
        self.arrow_right_sprite.rect.x = self.arrow_right_sprite_x
        self.arrow_right_sprite.rect.y = self.arrow_right_sprite_y
        self.static_elements_sprites_group.add(self.arrow_right_sprite)  # добавим спрайт в группу

        self.hero_sprite = pygame.sprite.Sprite()  # создадим спрайт
        self.hero_sprite.image = self.get_picture()
        self.hero_sprite.rect = self.hero_sprite.image.get_rect()  # и размеры
        self.hero_sprite.rect.x = self.hero_sprite_x
        self.hero_sprite.rect.y = self.hero_sprite_y
        self.hero_sprites_group.add(self.hero_sprite)  # добавим спрайт в

        self.level_start = 1

        self.start_game = False
        self.exit = False
        self.running = True

        # self.pictures_heroes_animation_small = pictures_heroes_animation_small
        # self.pictures_heroes_large = pictures_heroes_large
        #
        # self.directory_heroes_animation_small_name = DIRECTORY_HEROES_ANIMATION_SMALL_NAME
        # self.directory_heroes_large_name = directory_heroes_large_name

        self.ischange_smiles_picture = False  # менять ли картинку
        self.change_smiles_picture_side = 0  # в какую сторону менять лево -1, право +1
        self.isdraw_heroes_lock_text = False  # рисовать ли текст сколько монет осталось


        self.isgame_start = False
        if self.running:
            self.run()
        # self.delta_time = 1  # секунд
        # self.level_time = 200  # секунд
        #
        # self.ismiss = True  # нужно ли уменьшать время

    def get_from_db(self):
        directory = DB_DIRECTORY
        name = DB_NAME
        fullname = os.path.join(directory, name)
        con = sqlite3.connect(fullname)
        cur = con.cursor()
        result = cur.execute(f"""SELECT * FROM statistics""").fetchall()
        self.set_of_heroes = result[0][2]
        self.coins_count = result[0][1]
        self.best_score = result[0][0]

        result = cur.execute(f"""SELECT * FROM collections WHERE num = {self.set_of_heroes}""").fetchall()

        self.set_of_heroes_isbought = result[0][1]
        self.set_of_heroes_coins_need = result[0][2]
        con.commit()

    def update_db(self):
        directory = DB_DIRECTORY
        name = DB_NAME
        fullname = os.path.join(directory, name)
        con = sqlite3.connect(fullname)
        cur = con.cursor()
        # sql = """UPDATE statistics SET best_score = """ + str(max(int(self.score), int(result[0])))
        sql = """UPDATE statistics SET best_score = """ + str(self.best_score)
        cur.execute(sql)
        sql = """UPDATE statistics SET coins = """ + str(self.coins_count)
        cur.execute(sql)
        sql = """UPDATE statistics SET collection_of_heroes = """ + str(self.set_of_heroes)
        cur.execute(sql)
        sql = """UPDATE collections SET num = """ + str(self.set_of_heroes)
        cur.execute(sql)
        sql = """UPDATE collections SET isbought = """ + str(self.set_of_heroes_isbought)
        cur.execute(sql)

        con.commit()

    def get_picture(self):
        pictures_heroes_large = [], []
        self.directory_heroes_large_name = f"data\heroes_{self.set_of_heroes}\heroes_large"
        picture = glob.glob(f'{self.directory_heroes_large_name}\*.png')[0].split("\\")[-1]
        # for file in glob.glob(f'{self.directory_heroes_large_name}\*.png'):
        #     pictures_heroes_large.append(file.split("\\")[-1])
        # return pictures_heroes_large[0]
        hero_image = self.load_image(picture, self.directory_heroes_large_name)
        return hero_image

    def run(self):
        while self.running:
            self.background_screen.fill('white')
            self.play_text_color = MAIN_MENU_PLAY_TEXT_COLOR

            mouse_x, mouse_y = pygame.mouse.get_pos()
            aim_x, aim_y = mouse_x, mouse_y
            self.check_coords((mouse_x, mouse_y))

            self.check_hero()  # проверить наборы

            if self.ischange_smiles_picture:
                self.set_of_heroes = (self.set_of_heroes + self.change_smiles_picture_side) % 2
                # self.update_db()
                self.hero_sprite.image = self.get_picture()
                self.ischange_smiles_picture = False

            self.hero_sprites_group.draw(self.hero_screen)
            if self.isdraw_heroes_lock:
                self.heroes_lock_sprites_group.draw(self.heroes_lock_screen)
            self.static_elements_sprites_group.draw(self.static_elements_screen)
            self.draw_texts()

            if pygame.mouse.get_focused():
                pygame.mouse.set_visible(False)

                self.aim_sprite.rect.x = aim_x - self.aim_size_x_half  # 25 - половина размера прицела
                self.aim_sprite.rect.y = aim_y - self.aim_size_y_half  # 25 - половина размера прицела
                self.aim_sprites_group.draw(self.aim_screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    self.update_db()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    # print(board.get_click(event.pos))  # вывод координат клетки ad
                    self.check_coords(event.pos, True)

            self.clock.tick(self.fps)
            pygame.display.flip()
        self.update_db()
        if self.isgame_start:

            self.game_start()
            # self.running = False
        else:
            self.pygame_quit()

    def pygame_quit(self):
        pygame.quit()

    def pygame_init(self):
        pygame.init()

    def check_coords(self, pos, button_down=False):
        click_x, click_y = pos
        self.check_play_button(click_x, click_y, button_down)
        self.check_arrows(click_x, click_y, button_down)

    def check_arrows(self, click_x, click_y, button_down):
        self.check_left_arrow(click_x, click_y, button_down)
        self.check_right_arrow(click_x, click_y, button_down)

    def check_left_arrow(self, click_x, click_y, button_down):
        width, height = self.arrow_left_sprite.image.get_size()
        x, y = self.arrow_left_sprite_x, self.arrow_left_sprite_y
        if self.check_click(click_x, click_y, x, y, width, height):
            if button_down:
                self.ischange_smiles_picture = True
                self.change_smiles_picture_side = -1

    def check_right_arrow(self, click_x, click_y, button_down):
        width, height = self.arrow_right_sprite.image.get_size()
        x, y = self.arrow_right_sprite_x, self.arrow_right_sprite_y
        if self.check_click(click_x, click_y, x, y, width, height):
            if button_down:
                self.ischange_smiles_picture = True
                self.change_smiles_picture_side = 1

    def check_hero(self):
        if self.set_of_heroes_isbought:  # если не куплен
            self.isdraw_heroes_lock = True
            if self.coins_count >= self.set_of_heroes_coins_need:  # если монет хватает
                self.isdraw_heroes_lock_text = True
                # рисовать кнопку купить
            else:
                # рисовать текст
                self.isdraw_heroes_lock_text = True


    def check_play_button(self, click_x, click_y, button_down):
        width, height = self.play_sprite.image.get_size()
        x, y = self.play_sprite_x, self.play_sprite_y
        if self.check_click(click_x, click_y, x, y, width, height):
            if button_down:  # buttondown
                self.isgame_start = True
                self.running = False
            else:  # change color
                self.play_text_color = "white"
                self.draw_rect(x, y, width, height, "black")

    def check_click(self, click_x, click_y, x, y, width, height):
         if x <= click_x <= x + width and y <= click_y <= y + height:
            return True
         else:
            return False

    def game_start(self):
        Game().run() # level_start, best_score

        # Game(PICTURES_HEROES_ANIMATION_SMALL, PICTURES_HEROES_LARGE, DIRECTORY_HEROES_ANIMATION_SMALL_NAME,
        #              DIRECTORY_HEROES_LARGE_NAME).run() # level_start, best_score
        # self.running = True
        # self.pygame_init()

    def draw_texts(self):
        # self.draw_rect(self.play_rect_x, self.play_rect_y,
        #                self.play_rect_width, self.play_rect_height, self.play_rect_color)
        self.draw_text(f"{str(self.best_score)}",
                       self.best_score_text_center_x, self.best_score_text_center_y,
                       self.best_score_and_coins_count_text_color, self.best_score_and_coins_count_text_size)
        self.draw_text(f"{str(self.coins_count)}",
                       self.coins_count_text_center_x, self.coins_count_text_center_y,
                       self.best_score_and_coins_count_text_color, self.best_score_and_coins_count_text_size)
        self.draw_text(f"ИГРАТЬ", self.play_text_center_x, self.play_text_center_y, self.play_text_color, self.play_text_size)
        if self.isdraw_heroes_lock_text:  # сли нужно рисовать текст
            self.draw_text(f"{str(self.set_of_heroes_coins_need)}", self.set_of_heroes_text_center_x, self.set_of_heroes_text_center_y, self.set_of_heroes_text_color, self.set_of_heroes_text_size)
        # self.draw_text(f"Рекорд: {self.best_score}", self.best_score_text_x, self.best_score_text_y, self.best_score_text_color)  # счет

    def draw_text(self, to_write, center_x, center_y, color, size):
        font = pygame.font.Font(f"{self.font_directory}", size)
        text = font.render(f"{to_write}", True, color)
        # text_x = x - text.get_width() // 2
        # text_y = y - text.get_height() // 2
        place = text.get_rect(center=(center_x, center_y))
        self.static_elements_screen.blit(text, place)

    def draw_rect(self, x, y, width, height, color, *radius):
        pygame.draw.rect(self.background_screen, color, (x, y, width, height), 0)

    def load_image(self, name, directory_name, colorkey=None):
        fullname = os.path.join(directory_name, name)
        # если файл не существует, то выходим
        if not os.path.isfile(fullname):
            print(f"Файл с изображением '{fullname}' не найден")
            sys.exit()
        image = pygame.image.load(fullname)
        return image.convert_alpha()


class SelectionMenu:

    def __init__(self, ):
        self.pygame_init()

        # константы
        self.size = SCREEN_SIZE
        self.fps = FPS

        self.aim_size = AIM_SIZE
        self.aim_size_x = AIM_SIZE[0]
        self.aim_size_y = AIM_SIZE[1]
        self.aim_size_x_half = AIM_SIZE_HALF[0]
        self.aim_size_y_half = AIM_SIZE_HALF[1]

        self.main_sprite_directory = SELECTION_MENU_MAIN_SPRITE_DIRECTORY
        self.main_sprite_name = SELECTION_MENU_MAIN_SPRITE_NAME
        self.main_sprite_x = SELECTION_MENU_MAIN_SPRITE_X
        self.main_sprite_y = SELECTION_MENU_MAIN_SPRITE_Y


        self.main_menu_button_x = SELECTION_MENU_MAIN_MENU_BUTTON_X
        self.main_menu_button_y = SELECTION_MENU_MAIN_MENU_BUTTON_Y
        self.main_menu_button_width = SELECTION_MENU_MAIN_MENU_BUTTON_WIDTH
        self.main_menu_button_height = SELECTION_MENU_MAIN_MENU_BUTTON_HEIGHT

        self.main_menu_text_center_x = SELECTION_MENU_MAIN_MENU_TEXT_CENTER_X
        self.main_menu_text_center_y = SELECTION_MENU_MAIN_MENU_TEXT_CENTER_Y
        self.main_menu_text_color = SELECTION_MENU_MAIN_MENU_TEXT_COLOR

        self.restart_button_x = SELECTION_MENU_RESTART_BUTTON_X
        self.restart_button_y = SELECTION_MENU_RESTART_BUTTON_Y
        self.restart_button_width = SELECTION_MENU_RESTART_BUTTON_WIDTH
        self.restart_button_height = SELECTION_MENU_RESTART_BUTTON_HEIGHT

        self.restart_text_center_x = SELECTION_MENU_RESTART_TEXT_CENTER_X
        self.restart_text_center_y = SELECTION_MENU_RESTART_TEXT_CENTER_Y
        self.restart_text_color = SELECTION_MENU_RESTART_TEXT_COLOR

        self.main_menu_and_restart_text_size = SELECTION_MENU_MAIN_MENU_AND_RESTART_TEXT_SIZE

        self.font_directory = FONT_DIRECTORY

        # экраны
        self.background_screen = pygame.display.set_mode(self.size)
        self.static_elements_screen = pygame.display.set_mode(self.size)
        self.aim_screen = pygame.display.set_mode(self.size)

        self.clock = pygame.time.Clock()

        # группы спрайтов
        self.aim_sprites_group = pygame.sprite.Group()
        self.aim_sprite = pygame.sprite.Sprite()  # создадим спрайт
        self.aim_sprite.image = self.load_image("aim2.png", "data")  # определим его вид
        self.aim_sprite.rect = self.aim_sprite.image.get_rect()  # и размеры
        self.aim_sprites_group.add(self.aim_sprite)  # добавим спрайт в группу

        self.static_elements_sprites_group = pygame.sprite.Group()

        # создаем спрайты
        self.main_sprite = pygame.sprite.Sprite()
        self.main_sprite.image = self.load_image(f"{self.main_sprite_name}", f"{self.main_sprite_directory}")  # определим его вид
        self.main_sprite.rect = self.main_sprite.image.get_rect()  # и размеры
        self.main_sprite.rect.x = self.main_sprite_x
        self.main_sprite.rect.y = self.main_sprite_y
        self.static_elements_sprites_group.add(self.main_sprite)  # добавим спрайт в группу

        self.start_game = False
        self.exit = False
        self.running = True

        # self.pictures_heroes_animation_small = pictures_heroes_animation_small
        # self.pictures_heroes_large = pictures_heroes_large
        #
        # self.directory_heroes_animation_small_name = DIRECTORY_HEROES_ANIMATION_SMALL_NAME
        # self.directory_heroes_large_name = directory_heroes_large_name
        self.isgame_start = False
        self.ismain_menu = False

        if self.running:
            self.run()
        # self.delta_time = 1  # секунд
        # self.level_time = 200  # секунд
        #
        # self.ismiss = True  # нужно ли уменьшать время

    def run(self):
        while self.running:
            self.background_screen.fill('white')
            self.restart_text_color = SELECTION_MENU_RESTART_TEXT_COLOR
            self.main_menu_text_color = SELECTION_MENU_MAIN_MENU_TEXT_COLOR

            mouse_x, mouse_y = pygame.mouse.get_pos()
            aim_x, aim_y = mouse_x, mouse_y
            self.check_coords((mouse_x, mouse_y))

            self.static_elements_sprites_group.draw(self.static_elements_screen)
            self.draw()

            if pygame.mouse.get_focused():
                pygame.mouse.set_visible(False)

                self.aim_sprite.rect.x = aim_x - self.aim_size_x_half  # 25 - половина размера прицела
                self.aim_sprite.rect.y = aim_y - self.aim_size_y_half  # 25 - половина размера прицела
                self.aim_sprites_group.draw(self.aim_screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    # print(board.get_click(event.pos))  # вывод координат клетки ad
                    self.check_coords(event.pos, True)

            self.clock.tick(self.fps)
            pygame.display.flip()

        if self.isgame_start:
            self.game_start()
            # self.running = False
        elif self.ismain_menu:
            self.main_menu()
        else:
            self.pygame_quit()

    def pygame_quit(self):
        pygame.quit()

    def pygame_init(self):
        pygame.init()

    def check_coords(self, pos, button_down=False):
        click_x, click_y = pos
        self.check_restart_button(click_x, click_y, button_down)
        self.check_main_menu_button(click_x, click_y, button_down)

    def check_restart_button(self, click_x, click_y, button_down):
        width, height = self.restart_button_width, self.restart_button_height
        x, y = self.restart_button_x, self.restart_button_y
        if self.check_click(click_x, click_y, x, y, width, height):
            if button_down:  # buttondown
                self.isgame_start = True
                self.running = False
            else:  # change color
                self.restart_text_color = "white"
                self.draw_rect(x, y, width, height, "black")

    def check_main_menu_button(self, click_x, click_y, button_down):
        width, height = self.main_menu_button_width, self.main_menu_button_height
        x, y = self.main_menu_button_x, self.main_menu_button_y
        if self.check_click(click_x, click_y, x, y, width, height):
            if button_down:  # buttondown
                self.ismain_menu = True
                self.running = False
            else:  # change color
                self.main_menu_text_color = "white"
                self.draw_rect(x, y, width, height, "black")

    def check_click(self, click_x, click_y, x, y, width, height):
         if x <= click_x <= x + width and y <= click_y <= y + height:
            return True
         else:
            return False

    def game_start(self):
        # Game(PICTURES_HEROES_ANIMATION_SMALL, PICTURES_HEROES_LARGE, DIRECTORY_HEROES_ANIMATION_SMALL_NAME,
        #      DIRECTORY_HEROES_LARGE_NAME, self.level_start).run() # level_start, best_score
        MainMenu.game_start()
        # self.running = True
        # self.pygame_init()

    def main_menu(self):
        MainMenu()

    def draw(self):
        self.draw_text(f"Меню",
                       self.main_menu_text_center_x, self.main_menu_text_center_y,
                       self.main_menu_text_color, self.main_menu_and_restart_text_size)
        self.draw_text(f"Рестарт",
                       self.restart_text_center_x, self.restart_text_center_y,
                       self.restart_text_color, self.main_menu_and_restart_text_size)
        # self.draw_text(f"{str(self.time)}", self.time_text_center_x, self.time_text_center_y, self.time_text_color, self.time_text_size)

    def draw_text(self, to_write, center_x, center_y, color, size):
        font = pygame.font.Font(f"{self.font_directory}", size)
        text = font.render(f"{to_write}", True, color)
        # text_x = x - text.get_width() // 2
        # text_y = y - text.get_height() // 2
        place = text.get_rect(center=(center_x, center_y))
        self.static_elements_screen.blit(text, place)

    def draw_rect(self, x, y, width, height, color, *radius):
        pygame.draw.rect(self.background_screen, color, (x, y, width, height), 0)

    def load_image(self, name, directory_name, colorkey=None):
        fullname = os.path.join(directory_name, name)
        # если файл не существует, то выходим
        if not os.path.isfile(fullname):
            print(f"Файл с изображением '{fullname}' не найден")
            sys.exit()
        image = pygame.image.load(fullname)
        return image.convert_alpha()


class Game:

    def __init__(self):  # , , pictures_heroes_large, directory_heroes_animation_small_name,
                 # directory_heroes_large_name level_start, best_score

        self.size = SCREEN_SIZE
        self.fps = FPS
        self.v = 0

        self.aim_size = AIM_SIZE
        self.aim_size_x = AIM_SIZE[0]
        self.aim_size_y = AIM_SIZE[1]
        self.aim_size_x_half = AIM_SIZE_HALF[0]
        self.aim_size_y_half = AIM_SIZE_HALF[1]

        self.level = 1
        self.min_level = GAME_HEROES_MIN_V
        self.max_level = GAME_HEROES_MAX_LEVEL

        # self.screen = pygame.display.set_mode(self.size)
        # self.screen2 = pygame.display.set_mode(self.size)
        # self.screen3 = pygame.display.set_mode(self.size)
        # self.screen4 = pygame.display.set_mode(self.size)

        self.background_screen = pygame.display.set_mode(self.size)
        self.static_elements_screen = pygame.display.set_mode(self.size)
        self.heroes_sprites_screen = pygame.display.set_mode(self.size)
        self.aim_screen = pygame.display.set_mode(self.size)
        self.black_rect_screen = pygame.display.set_mode(self.size)

        self.black_rect_level = GAME_BLACK_RECT_LEVEL
        self.cover_surf = pygame.Surface((850, 850))
        self.cover_surf.set_colorkey((255, 255, 255))

        self.white_circle_radius = 400

        self.clock = pygame.time.Clock()

        self.aim_sprites_group = pygame.sprite.Group()
        self.aim_sprite = pygame.sprite.Sprite()  # создадим спрайт
        self.aim_sprite.image = self.load_image("aim2.png", "data")  # определим его вид
        self.aim_sprite.rect = self.aim_sprite.image.get_rect()  # и размеры
        self.aim_sprites_group.add(self.aim_sprite)  # добавим спрайт в группу

        self.heroes_sprites_group = pygame.sprite.Group()

        self.isupdate_level = False
        self.running = True
        self.score = 0

        self.get_from_db()

        # self.pictures_heroes_animation_small = pictures_heroes_animation_small
        # self.pictures_heroes_large = pictures_heroes_large

        self.pictures_heroes_animation_small = []
        self.pictures_heroes_large = []

        # self.pictures_heroes_animation_small = ""
        # self.pictures_heroes_large = ""

        self.directory_heroes_animation_small_name = ""
        self.directory_heroes_large_name = ""

        self.delta_time = 5  # на сколько секунд увеличится время при попадании
        self.level_time = 20  # секунд
        self.penalty = 0

        self.font_directory = FONT_DIRECTORY

        self.time_penalty_text_delta_y = GAME_TIME_PENALTY_TEXT_DELTA_Y
        self.time_penalty_text_delta_y = GAME_TIME_PENALTY_TEXT_DELTA_Y
        self.time_penalty_text_color = GAME_TIME_PENALTY_TEXT_COLOR
        self.time_penalty_text_size = GAME_TIME_PENALTY_TEXT_SIZE
        self.isdraw_time_penalty_text = False

        self.ismiss = True  # нужно ли уменьшать время
        # MainMenu()

        self.quit = False

    def run(self):
        self.update_level(self.level)
        i = 0  # счетчик обновления смайла
        start_ticks = pygame.time.get_ticks()  # starter tick
        time_penalty_text_start_tick = pygame.time.get_ticks()
        info_board = InfoBoard(self.static_elements_screen, self.score, self.best_score, self.level_time)
        while self.running:
            self.background_screen.fill('white')

            self.ismiss = True  # нужно ли уменьшать время
            self.level_time = min(59, max(1, self.level_time))

            seconds = round(self.level_time + self.penalty - (pygame.time.get_ticks() - start_ticks) / 1000)
            if seconds <= 0:
                self.update_db()
                self.running = False
            else:
                seconds_res = time.gmtime(seconds)
                current_level_time = time.strftime("%S", seconds_res)

            mouse_x, mouse_y = pygame.mouse.get_pos()
            aim_x, aim_y = mouse_x, mouse_y

            if self.score > self.black_rect_level:
                k = 4000
                self.white_circle_radius = min(400, max(70, k / max(1, self.score)))
                self.cover_surf.fill((0, 0, 0))
                pygame.draw.circle(self.cover_surf, (255, 255, 255), (aim_x, aim_y), self.white_circle_radius)
                # self.cover_surf.set_alpha(300)

            self.heroes_sprites_group.draw(self.heroes_sprites_screen)

            # штраф отрисовка
            if self.isdraw_time_penalty_text:
                if (pygame.time.get_ticks() - time_penalty_text_start_tick) / 1000 < 0.2:
                    time_penalty_text_center_x, time_penalty_text_center_y = aim_x, aim_y + self.time_penalty_text_delta_y
                    self.draw_text(f"-{str(self.delta_time)}", time_penalty_text_center_x, time_penalty_text_center_y,
                                   self.time_penalty_text_color, self.time_penalty_text_size)  # ШТРАФ
                else:
                    self.isdraw_time_penalty_text = False

            if pygame.mouse.get_focused():
                pygame.mouse.set_visible(False)
                self.aim_sprite.rect.x = aim_x - self.aim_size_x_half  # 25 - половина размера прицела
                self.aim_sprite.rect.y = aim_y - self.aim_size_y_half  # 25 - половина размера прицела
                self.aim_sprites_group.draw(self.aim_screen)

            if int(self.score) > int(self.best_score):
                self.best_score = self.score


            info_board.draw(current_level_time, self.score, self.coins_count, self.best_score)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.update_db()
                    self.running = False
                    self.quit = True

                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.heroes_sprites_group.update(event)
            # счетчик обновления картинок анимации
            i += 1
            i %= 7
            for hero in self.heroes_sprites_group:
                if i == 6:
                    hero.update_image()
                if hero.ismiss() and self.ismiss:  # при промахе
                    # self.level_time -= 5
                    self.penalty -= 5
                    self.isdraw_time_penalty_text = True
                    self.ismiss = False  # уменьшили время, уже не нужно
                    time_penalty_text_start_tick = pygame.time.get_ticks()  # штраф

                if not hero.isupdate_level():
                    hero.unmiss()  # убрать флаг об уменьшении времени у всех героев
                    hero.move()
                else:
                    self.isupdate_level = True

                    self.score += 1
                    self.penalty = 0
                    self.coins_count += 1

                    start_ticks = pygame.time.get_ticks()
                    time_penalty_text_start_tick = pygame.time.get_ticks()

                    self.create_level()
                    self.create_v()
                    break

            # удалить спрайты смайлов и обновить уровень
            if self.isupdate_level:
                self.remove_heroes(self.heroes_sprites_group)
                self.update_level(self.level)

                self.isupdate_level = False
                self.isdraw_time_penalty_text = False

            # условие появления черного экрана
            if self.score > self.black_rect_level:
                self.black_rect_screen.blit(self.cover_surf, (0, 0))

            self.clock.tick(self.fps)
            pygame.display.flip()

        if not self.quit:
            SelectionMenu()
            # MainMenu()
        # /pygame.quit()

    def game_start(self):
        self.running = True

    def game_quit(self):
        pygame.quit()

    def create_level(self):
        #  сначала парабола до 14 потом прямая
        self.level = min(self.max_level, min(196, self.score ** 2 + 1) + 10 * max(0, (self.score - 14)))

    def create_v(self):
        # self.v = self.level / 2
        self.v = max(GAME_HEROES_MIN_V, min(GAME_HEROES_MAX_V, min(200, GAME_HEROES_MIN_V + 70 * self.score ** 0.5))) // FPS

    def get_from_db(self):
        directory = DB_DIRECTORY
        name = DB_NAME
        fullname = os.path.join(directory, name)
        con = sqlite3.connect(fullname)
        cur = con.cursor()
        result = cur.execute(f"""SELECT * FROM {name.split('.')[0]}""").fetchall()
        self.set_of_heroes = result[0][2]
        self.coins_count = result[0][1]
        self.best_score = result[0][0]
        con.commit()

    def update_db(self):
        directory = DB_DIRECTORY
        name = DB_NAME
        fullname = os.path.join(directory, name)
        con = sqlite3.connect(fullname)
        cur = con.cursor()
        result = cur.execute(f"""SELECT * FROM {name.split('.')[0]}""").fetchall()[0]
        # sql = """UPDATE statistics SET best_score = """ + str(max(int(self.score), int(result[0])))
        sql = """UPDATE statistics SET best_score = """ + str(self.best_score)
        cur.execute(sql)
        sql = """UPDATE statistics SET coins = """ + str(self.coins_count)
        cur.execute(sql)
        sql = """UPDATE statistics SET collection_of_heroes = """ + str(self.set_of_heroes)
        cur.execute(sql)
        con.commit()

    # def draw_info_board(self):
    def load_image(self, name, directory_name, colorkey=None):
        fullname = os.path.join(directory_name, name)
        # если файл не существует, то выходим
        if not os.path.isfile(fullname):
            print(f"Файл с изображением '{fullname}' не найден")
            sys.exit()
        image = pygame.image.load(fullname)
        return image.convert_alpha()

    def remove_heroes(self, sprites_group):
        for hero in sprites_group:
            hero.remove(sprites_group)

    def update_level(self, heroes_count):
        wanted = True
        table_info = True
        image_wanted, image_wanted_large, images_not_wanted = self.choose_picture()
        Hero(self.heroes_sprites_group, wanted, self.level, self.v, image_wanted, image_wanted_large, images_not_wanted, table_info)
        for i in range(heroes_count):
            Hero(self.heroes_sprites_group, wanted, self.level, self.v, image_wanted, image_wanted_large, images_not_wanted)
            wanted = False
            table_info = False

    def get_pictures(self):
        pictures_heroes_animation_small, pictures_heroes_large = [], []
        self.directory_heroes_animation_small_name = f"data\heroes_{self.set_of_heroes}\heroes_animation_small"
        self.directory_heroes_large_name = f"data\heroes_{self.set_of_heroes}\heroes_large"
        for file in glob.glob(f'{self.directory_heroes_animation_small_name}\*.png'):
            pictures_heroes_animation_small.append(file.split("\\")[-1])
        for file in glob.glob(f'{self.directory_heroes_large_name}\*.png'):
            pictures_heroes_large.append(file.split("\\")[-1])
        return pictures_heroes_animation_small, pictures_heroes_large

    def choose_picture(self, *pictures_used):
        # pictures = self.pictures_heroes_animation_small[:]
        pictures_heroes_animation_small, pictures_heroes_large = self.get_pictures()
        pictures = pictures_heroes_animation_small[:]
        # directory_heroes_animation_small_name = self.directory_heroes_animation_small_name  # директория с фреймами для анимации
        # directory_heroes_large_name = self.directory_heroes_large_name

        # if pictures_used:
        #     for picture in pictures_used:
        #         if picture in pictures:
        #             pictures.remove(picture)
        pictures_count = 3
        pictures_to_use = rnd.sample(pictures, pictures_count)

        picture_wanted = pictures_to_use[0]
        picture_wanted_large = picture_wanted.split('_')[1] + '_large.png'
        pictures_not_wanted = pictures_to_use[1:3]

        # print(pictures_to_use)
        # print(picture_wanted, picture_wanted_large)
        # print(pictures_not_wanted)
        # pictures_not_wanted = self.choose_pictures_not_wanted(pictures, self.level)
        # for picture_not_wanted in pictures_not_wanted:
        #     pictures.remove(picture_not_wanted)
        # picture_wanted = pictures[rnd.randrange(len(pictures))]
        # picture_wanted_large = picture_wanted.split('_')[1] + '_large.png'
        images_not_wanted = [self.load_image(picture, self.directory_heroes_animation_small_name) for picture in pictures_not_wanted]
        image_wanted = self.load_image(picture_wanted, self.directory_heroes_animation_small_name)
        image_wanted_large = self.load_image(picture_wanted_large, self.directory_heroes_large_name)

        return image_wanted, image_wanted_large, images_not_wanted

    # def choose_pictures_not_wanted(self, pictures, level):
    #     #  подается список названий картинок и из них рандомно выбирается 2
    #     pictures = pictures[:]
    #     pictures_not_wanted = []
    #     # pictures_count = min(level, len(pictures) - 1)
    #     pictures_count = 2
    #     # print(pictures_count)
    #     try:
    #         for n in range(pictures_count):
    #             picture_not_wanted = pictures[rnd.randrange(len(pictures))]
    #             pictures_not_wanted.append(picture_not_wanted)
    #             pictures.remove(picture_not_wanted)
    #         return pictures_not_wanted
    #     except Exception as e:
    #         print(e)

    def draw_text(self, to_write, center_x, center_y, color, size):
        font = pygame.font.Font(f"{self.font_directory}", size)
        text = font.render(f"{to_write}", True, color)
        # text_x = x - text.get_width() // 2
        # text_y = y - text.get_height() // 2
        place = text.get_rect(center=(center_x, center_y))
        self.aim_screen.blit(text, place)


class Hero(pygame.sprite.Sprite):
    # color_hero_not_wanted, color_hero_wanted = Game.choose_color("data\smiles_1")
    # image_not_wanted = Game.load_image(color_hero_not_wanted, "data\smiles_1")
    # image_wanted = Game.load_image(color_hero_wanted, "data\smiles_1")

    def __init__(self, heroes_sprites_group, wanted, level, v, image_wanted, image_wanted_large, images_not_wanted, table_info=False):
        # НЕОБХОДИМО вызвать конструктор родительского класса Sprite.
        # Это очень важно !!!
        super().__init__(heroes_sprites_group)

        # image_wanted, image_not_wanted, color_hero_wanted, color_hero_not_wanted = self.change_color()
        # self.color_hero_wanted, self.color_hero_not_wanted = color_hero_wanted, color_hero_not_wanted

        self.heroes_sprites_group = heroes_sprites_group

        self.update_level = False
        self.miss = False

        self.level = level
        self.table_info = table_info
        self.wanted = wanted
        self.v = v

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

    def update_position(self):
        if self.table_info:
            self.rect.x, self.rect.y = 950, 75
        else:
            self.rect.x = rnd.randrange(70, GAME_FIELD_WIDTH)
            self.rect.y = rnd.randrange(70, GAME_FILED_HEIGHT)

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
                # #     hero.update_position()
                # self.score += 1
                # self.level = self.score ** 2 + 1
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
            # x, y = self.rect.x, self.rect.y
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

        # self.vx = int([rnd.randint(-self.v, -self.v // 3), rnd.randint(self.v // 3, self.v) ][rnd.randrange(1)]) #  + rnd.uniform(-rnd.random(), rnd.random())
        # --------------------------------------------
        # if self.v:
        #     self.vx = min(0.7 * self.v, round([- 0.25 - rnd.randint(-self.v + self.v // 3, -self.v // 3), 0.25 + rnd.randint(self.v // 3, self.v - self.v // 3)][rnd.randrange(1)] + rnd.uniform(-rnd.random(), rnd.random()), 2))
        # else:
        #     self.vx = 0
        # # self.vx = int(rnd.randrange(-self.v, self.v) + rnd.uniform(-rnd.random(), rnd.random()))
        # self.vy = round(sqrt((self.v ** 2 - self.vx ** 2)), 2)
        # --------------------------------------------
        self.vx = int([rnd.randint(-self.v, -self.v // 3), rnd.randint(self.v // 3, self.v)][rnd.randrange(1)])
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


class InfoBoard:

    def __init__(self, screen, score, best_score, current_level_time):
        # self.screen = screen
        self.size = SCREEN_SIZE
        self.fps = FPS

        self.score = score
        self.best_score = best_score

        # экраны
        self.static_elements_screen = screen

        self.line_x = INFO_BOARD_LINE_X
        self.line_y = INFO_BOARD_LINE_Y
        self.line_height = HEIGHT

        self.main_sprite_directory = INFO_BOARD_MAIN_SPRITE_DIRECTORY
        self.main_sprite_name = INFO_BOARD_MAIN_SPRITE_NAME
        self.main_sprite_x = INFO_BOARD_MAIN_SPRITE_X
        self.main_sprite_y = INFO_BOARD_MAIN_SPRITE_Y

        self.time_text_center_x = INFO_BOARD_TIME_TEXT_CENTER_X
        self.time_text_center_y = INFO_BOARD_TIME_TEXT_CENTER_Y
        self.time_text_color = INFO_BOARD_TIME_TEXT_DEFAULT_COLOR

        self.score_text_center_x = INFO_BOARD_SCORE_TEXT_CENTER_X
        self.score_text_center_y = INFO_BOARD_SCORE_TEXT_CENTER_Y
        self.score_text_color = INFO_BOARD_SCORE_TEXT_DEFAULT_COLOR

        self.coins_count_text_center_x = INFO_BOARD_COINS_COUNT_TEXT_CENTER_X
        self.coins_count_text_center_y = INFO_BOARD_COINS_COUNT_TEXT_CENTER_Y
        self.coins_count_text_color = INFO_BOARD_COINS_COUNT_TEXT_COLOR

        self.best_score_text_center_x = INFO_BOARD_BEST_SCORE_TEXT_CENTER_X
        self.best_score_text_center_y = INFO_BOARD_BEST_SCORE_TEXT_CENTER_Y
        self.best_score_text_color = INFO_BOARD_BEST_SCORE_TEXT_COLOR

        self.table_info_main_sprites_group = pygame.sprite.Group()

        self.main_sprite = pygame.sprite.Sprite()
        self.main_sprite.image = self.load_image(f"{self.main_sprite_name}",
                                                  f"{self.main_sprite_directory}")  # определим его вид
        self.main_sprite.rect = self.main_sprite.image.get_rect()  # и размеры
        self.main_sprite.rect.x = self.main_sprite_x
        self.main_sprite.rect.y = self.main_sprite_y
        self.table_info_main_sprites_group.add(self.main_sprite)  # доба

        self.current_level_time = current_level_time

        self.text_size = INFO_BOARD_TEXT_SIZE

        self.font_directory = FONT_DIRECTORY
        # self.draw()
        # print(score)

    def draw(self, time, score, coins_count, best_score):
        self.table_info_main_sprites_group.draw(self.static_elements_screen)

        self.draw_line(self.line_x, self.line_y, self.line_height, "black")

        self.change_time_text_color(time)
        self.change_score_text_color(score, best_score)
        random_size = False
        if int(time) <= 5:
            random_size = True
        self.draw_text(f"00:{time}", self.time_text_center_x, self.time_text_center_y, self.time_text_color, self.text_size, random_size, int(time))
        self.draw_text(f"{score}", self.score_text_center_x, self.score_text_center_y, self.score_text_color, self.text_size)
        self.draw_text(f"{best_score}", self.best_score_text_center_x, self.best_score_text_center_y, self.best_score_text_color, self.text_size)
        self.draw_text(f"{coins_count}", self.coins_count_text_center_x, self.coins_count_text_center_y, self.coins_count_text_color,
                       self.text_size)

    def change_time_text_color(self, time):
        default_r, default_g, default_b = INFO_BOARD_TIME_TEXT_DEFAULT_COLOR
        final_r, final_g, final_b = INFO_BOARD_TIME_TEXT_FINAL_COLOR

        min_r, min_g, min_b = min(default_r, final_r), min(default_g, final_g), min(default_b, final_b)
        max_r, max_g, max_b = max(default_r, final_r), max(default_g, final_g), max(default_b, final_b)

        start_time = INFO_BOARD_TIME_TEXT_START_TIME
        min_time = INFO_BOARD_TIME_TEXT_MIN_TIME

        msc = int(time) * 100
        # r = int(71 + (184 / 1500) * (2000 - msc))
        # g = int(255 - (184 / 1500) * (2000 - msc))
        r = max(min_r, min(max_r, int(min_r + ((max_r - min_r) / ((start_time - min_time) * 100)) * (start_time * 100 - msc))))
        g = max(min_g, min(max_g, int(max_g - ((max_g - min_g) / ((start_time - min_time) * 100)) * (start_time * 100 - msc))))
        #g = max_g - int(((max_g - min_g) / (start_time - min_time) * 100) * (start_time * 100 - msc))
        b = max_b
        self.time_text_color = (r, g, b)

    def change_score_text_color(self, score, best_score):
        #print(score, best_score)
        default_r, default_g, default_b = INFO_BOARD_SCORE_TEXT_DEFAULT_COLOR
        final_r, final_g, final_b = INFO_BOARD_SCORE_TEXT_FINAL_COLOR

        min_r, min_g, min_b = min(default_r, final_r), min(default_g, final_g), min(default_b, final_b)
        max_r, max_g, max_b = max(default_r, final_r), max(default_g, final_g), max(default_b, final_b)

        r = max(min_r, min(max_r, int(max_r - (max_r - min_r) / best_score * score)))
        g = max_g
        b = max(min_b, min(max_b, int(min_b + (max_b - min_b) / best_score * score)))
        self.score_text_color = r, g, b

    def draw_line(self, x, y, height, color):
        pygame.draw.line(self.static_elements_screen, color, [x, 0], [x, height], 7)

    def draw_rect(self, x, y, width, height, color, *radius):
        pygame.draw.rect(self.static_elements_screen, color, (x, y, width, height), 6)

    def draw_text(self, to_write, center_x, center_y, color, size, random_size=False, *args):
        font = pygame.font.Font(f"{self.font_directory}", size)
        text = font.render(f"{to_write}", True, color)
        # text_x = x - text.get_width() // 2
        # text_y = y - text.get_height() // 2
        if random_size:
            if args:
                delta = (-2.5 / 6) * int(args[0]) + 2.5
            center_x += rnd.uniform(-delta, delta)
            center_y += rnd.uniform(-delta, delta)
        place = text.get_rect(center=(center_x, center_y))
        self.static_elements_screen.blit(text, place)

    def load_image(self, name, directory_name, colorkey=None):
        fullname = os.path.join(directory_name, name)
        # если файл не существует, то выходим
        if not os.path.isfile(fullname):
            print(f"Файл с изображением '{fullname}' не найден")
            sys.exit()
        image = pygame.image.load(fullname)
        return image.convert_alpha()

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
    # level_start, best_score = 100, 1
    MainMenu() 
#     Game(PICTURES_HEROES_ANIMATION_SMALL, PICTURES_HEROES_LARGE, DIRECTORY_HEROES_ANIMATION_SMALL_NAME,
# DIRECTORY_HEROES_LARGE_NAME, level_start, best_score).run()
