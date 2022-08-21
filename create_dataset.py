import os
from PIL import Image, ImageOps

base_dir = r'C:\Users\masua\Downloads\Cimat\BSR_bsds500\BSR\BSDS500\data'
source_dir = 'images'
dest_dir = 'grayscale'

sets = ['test', 'train', 'val']

for dname in sets:
    for fname in [name for name in os.listdir(os.path.join(base_dir, source_dir, dname)) if name[-3:] == 'jpg']:
        image = Image.open(os.path.join(base_dir, source_dir, dname, fname))
        grayscale = ImageOps.grayscale(image)
        grayscale.save(os.path.join(base_dir, dest_dir, dname, fname))