import os
import re

clippings_path = "/Path/to/Your/My Clippings.txt"
export_path = "/Where/you/want/to/put/"

re_pattern = r'Location\s\d{1,5}-?\d{1,5}'

f = open(clippings_path, "r+", encoding='utf-8')

try:
    os.makedirs(export_path)
except FileExistsError:
    # directory already exists
    print("Directory already exists.")
    pass

while True:
    clipping_blocks = []
    for i in range(0,5):
        line = f.readline()
        if not line:
            exit()
        clipping_blocks.append(line)
    book_clippings = open('{}{}.txt'.format(export_path, clipping_blocks[0]), 'a+')
    location_extract = re.search(re_pattern, clipping_blocks[1])[0]
    book_clippings.write(f'{clipping_blocks[3]}highlighted at {location_extract}' + '\n\n')
    book_clippings.close()