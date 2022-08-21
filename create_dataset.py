import os

base_dir = r'C:\Users\masua\Downloads\Cimat\BSR_bsds500\BSR\BSDS500\data'
source_dir = 'images'
dest_dir = 'images_gray'

sets = ['test', 'train', 'val']

for dname in sets:
    print(os.listdir(os.path.join(base_dir, source_dir, dname)))