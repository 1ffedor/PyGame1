import glob

COLORS = []
for file in glob.glob('data\smiles_1\*.png'):
    COLORS.append(file.split("\\")[-1])
print(COLORS)

