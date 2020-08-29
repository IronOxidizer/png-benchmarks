from pathlib import Path
from PIL import Image
from os import remove

non_png = [path for path in Path(".").rglob("*/*") if not path.name.endswith(".png")]

for path in non_png:
    new_path = str(path).rsplit(".", 1)
    new_path[-1] = ".png"
    im = Image.open(path)
    im.save(''.join(new_path))
    print("Created " + ''.join(new_path))


for path in non_png:
    remove(path)
    
