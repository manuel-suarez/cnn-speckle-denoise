import os
import cv2

base_dir = r'C:\Users\masua\Downloads\Cimat\BSR_bsds500\BSR\BSDS500\data'
source_dir = 'images'
dest_dir = 'grayscale'

sets = ['test', 'train', 'val']

for dname in sets:
    for fname in [name for name in os.listdir(os.path.join(base_dir, source_dir, dname)) if name[-3:] == 'jpg']:
        image = cv2.imread(os.path.join(base_dir, source_dir, dname, fname), cv2.IMREAD_GRAYSCALE)
        cv2.imwrite(os.path.join(base_dir, dest_dir, dname, fname), image)