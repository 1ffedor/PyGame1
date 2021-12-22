import glob
from game_settings import *

PICTURES = []
for file in glob.glob(f'{DIRECTORY_NAME}\*.png'):
    PICTURES.append(file.split("\\")[-1])
print(PICTURES)

