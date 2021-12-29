import glob
from game_settings import *

PICTURES_HEROES_ANIMATION_SMALL = []
PICTURES_HEROES_LARGE = []
for file in glob.glob(f'{DIRECTORY_HEROES_ANIMATION_SMALL_NAME}\*.png'):
    PICTURES_HEROES_ANIMATION_SMALL.append(file.split("\\")[-1])
for file in glob.glob(f'{DIRECTORY_HEROES_LARGE_NAME}\*.png'):
    PICTURES_HEROES_LARGE.append(file.split("\\")[-1])
# print(PICTURES)