FPS = 60

SCREEN_SIZE = (1200, 800)
WIDTH, HEIGHT = 1200, 800

AIM_SIZE = (35, 35)
AIM_SIZE_HALF = (AIM_SIZE[0] // 2, AIM_SIZE[1] // 2)

DB_DIRECTORY = "data"
DB_NAME = "statistics.db"

FONT_DIRECTORY = "data\Sansus.ttf"

HEROES_MAIN_DIRECTORY = "data"
HEROES_DIRECTORIES = ""


# --- MAIN MENU ---
# # кнопка играть
# MAIN_MENU_PLAY_TEXT_X = 600
# MAIN_MENU_PLAY_TEXT_Y = 400
#
# MAIN_MENU_PLAY_TEXT_COLOR = "black"
#
#
# MAIN_MENU_PLAY_RECT_WIDTH = 300
# MAIN_MENU_PLAY_RECT_HEIGHT = 100
#
# MAIN_MENU_PLAY_RECT_X = 450
# MAIN_MENU_PLAY_RECT_Y = 350
#
# MAIN_MENU_PLAY_RECT_COLOR = "black"


# рекорд текст
# MAIN_MENU_BEST_SCORE_TEXT_X = 450
# MAIN_MENU_BEST_SCORE_TEXT_Y = 350
#
# MAIN_MENU_BEST_SCORE_TEXT_COLOR = "black"  # 4747ff


DIRECTORY_HEROES_ANIMATION_SMALL_NAME = r"data\heroes_1\heroes_animation_small"
DIRECTORY_HEROES_LARGE_NAME = r"data\heroes_1\heroes_large"



LEVEL_START = 1


##--------------------------------------

# шрифт Sansus Webiss...
# название левый верхний угол
MAIN_MENU_TITLE_SPRITE_DIRECTORY = r"data\main_menu"
MAIN_MENU_TITLE_SPRITE_NAME = "title.png"

MAIN_MENU_TITLE_SPRITE_X = 200
MAIN_MENU_TITLE_SPRITE_Y = 100


# рекорд и монеты верхний левый
MAIN_MENU_BEST_SCORE_AND_COINS_SPRITE_DIRECTORY = r"data\main_menu"
MAIN_MENU_BEST_SCORE_AND_COINS_SPRITE_NAME = "best_score_and_coins.png"

MAIN_MENU_BEST_SCORE_AND_COINS_SPRITE_X = 200
MAIN_MENU_BEST_SCORE_AND_COINS_SPRITE_Y = 200

# рекорд число центр
MAIN_MENU_BEST_SCORE_TEXT_CENTER_X = 450
MAIN_MENU_BEST_SCORE_TEXT_CENTER_Y = 300

# монет число центр
MAIN_MENU_COINS_COUNT_TEXT_CENTER_X = 750
MAIN_MENU_COINS_COUNT_TEXT_CENTER_Y = 300

MAIN_MENU_BEST_SCORE_AND_COINS_COUNT_TEXT_COLOR = (71, 71, 225) #"4747ff"

MAIN_MENU_BEST_SCORE_AND_COINS_COUNT_TEXT_SIZE = 40


# кнопка играть
MAIN_MENU_PLAY_SPRITE_DIRECTORY = r"data\main_menu"
MAIN_MENU_PLAY_SPRITE_NAME = "play2.png"

MAIN_MENU_PLAY_SPRITE_X = 450
MAIN_MENU_PLAY_SPRITE_Y = 350

MAIN_MENU_PLAY_SPRITE_WIGHT = 300
MAIN_MENU_PLAY_SPRITE_HEIGHT = 100

# текст играть
MAIN_MENU_PLAY_TEXT_CENTER_X = 601
MAIN_MENU_PLAY_TEXT_CENTER_Y = 407
MAIN_MENU_PLAY_TEXT_COLOR = "black"
MAIN_MENU_PLAY_TEXT_SIZE = 80


# набор смайлов текст и квадрат
MAIN_MENU_SET_OF_HEROES_SPRITE_DIRECTORY = r"data\main_menu"
MAIN_MENU_SET_OF_HEROES_SPRITE_NAME = "set_of_smiles.png"

MAIN_MENU_SET_OF_HEROES_SPRITE_X = 400
MAIN_MENU_SET_OF_HEROES_SPRITE_Y = 500

# картинка блокировки
MAIN_MENU_SET_OF_HEROES_LOCK_DIRECTORY = r"data\main_menu"
MAIN_MENU_SET_OF_HEROES_LOCK_SPRITE_NAME = "set_of_smiles_lock.png"

MAIN_MENU_SET_OF_HEROES_LOCK_SPRITE_X = 500
MAIN_MENU_SET_OF_HEROES_LOCK_SPRITE_Y = 500

# текст
MAIN_MENU_SET_OF_HEROES_LOCK_TEXT_CENTER_X = 750
MAIN_MENU_SET_OF_HEROES_LOCK_TEXT_CENTER_Y = 300

MAIN_MENU_SET_OF_HEROES_LOCK_TEXT_COLOR = (71, 71, 225) #"4747ff"

MAIN_MENU_SET_OF_HEROES_LOCK_TEXT_SIZE = 40

# стрелки

# левая
MAIN_MENU_ARROW_LEFT_SPRITE_DIRECTORY = r"data\main_menu"
MAIN_MENU_ARROW_LEFT_SPRITE_NAME = "arrow_left.png"

MAIN_MENU_ARROW_LEFT_SPRITE_X = 450
MAIN_MENU_ARROW_LEFT_SPRITE_Y = 634

# правая
MAIN_MENU_ARROW_RIGHT_SPRITE_DIRECTORY = r"data\main_menu"
MAIN_MENU_ARROW_RIGHT_SPRITE_NAME = "arrow_right.png"

MAIN_MENU_ARROW_RIGHT_SPRITE_X = 700
MAIN_MENU_ARROW_RIGHT_SPRITE_Y = 634



# --------------------------------
# GAME
GAME_FIELD_WIDTH = 800 - 50
GAME_FILED_HEIGHT = HEIGHT - 50
GAME_FIELD = (GAME_FIELD_WIDTH, GAME_FILED_HEIGHT)

GAME_HEROES_MIN_V = 59
GAME_HEROES_MAX_V = 280

GAME_HEROES_MIN_LEVEL = 1
GAME_HEROES_MAX_LEVEL = 500

GAME_BLACK_RECT_LEVEL = 10

# --------------------------
# INFO BOARD
# --- INFO BOARD ---
INFO_BOARD_LINE_X = GAME_FIELD_WIDTH + 100
INFO_BOARD_LINE_Y = GAME_FILED_HEIGHT + 100


INFO_BOARD_MAIN_SPRITE_DIRECTORY = r"data\info_board"
INFO_BOARD_MAIN_SPRITE_NAME = "info.png"

INFO_BOARD_MAIN_SPRITE_X = 850
INFO_BOARD_MAIN_SPRITE_Y = 0


INFO_BOARD_TIME_TEXT_CENTER_X = 945
INFO_BOARD_TIME_TEXT_CENTER_Y = 400

INFO_BOARD_TIME_TEXT_DEFAULT_COLOR = (71, 255, 71)  #47ff47
INFO_BOARD_TIME_TEXT_FINAL_COLOR = (255, 71, 71)

INFO_BOARD_TIME_TEXT_START_TIME = 20  # начиная с какой секунды будет меняться цвет
INFO_BOARD_TIME_TEXT_MIN_TIME = 5  # при таком значении цвет полностью поменяется


INFO_BOARD_SCORE_TEXT_CENTER_X = 1105
INFO_BOARD_SCORE_TEXT_CENTER_Y = 400

INFO_BOARD_SCORE_TEXT_DEFAULT_COLOR = (255, 71, 71)  # ff4747
INFO_BOARD_SCORE_TEXT_FINAL_COLOR = (71, 71, 255)


INFO_BOARD_COINS_COUNT_TEXT_CENTER_X = 945
INFO_BOARD_COINS_COUNT_TEXT_CENTER_Y = 500

INFO_BOARD_COINS_COUNT_TEXT_COLOR = (71, 71, 255)  #4747ff


INFO_BOARD_BEST_SCORE_TEXT_CENTER_X = 1105
INFO_BOARD_BEST_SCORE_TEXT_CENTER_Y = 500

INFO_BOARD_BEST_SCORE_TEXT_COLOR = (71, 71, 255)  #4747ff

INFO_BOARD_TEXT_SIZE = 30