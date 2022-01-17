import sys

data = list(map(str.strip, sys.stdin))
print(data)
for el in data:
    if el and not '#' in el:
        print(f"""self.{el.split()[0].lower().split("selection_menu_")[1]} = {el.split()[0]}""")