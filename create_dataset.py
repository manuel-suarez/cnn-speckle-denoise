import os
import cv2
import numpy as np
from skimage.util import random_noise

base_dir = r'C:\Users\masua\Downloads\Cimat\BSR_bsds500\BSR\BSDS500\data'
source_dir = 'images'
dest_dir = 'grayscale'
noise_dir = 'noise'

sets = ['test', 'train', 'val']

for dname in sets:
    for fname in [name for name in os.listdir(os.path.join(base_dir, source_dir, dname)) if name[-3:] == 'jpg']:
        image = cv2.imread(os.path.join(base_dir, source_dir, dname, fname), cv2.IMREAD_GRAYSCALE)
        # Grayscale
        cv2.imwrite(os.path.join(base_dir, dest_dir, dname, fname), image)
        # Noise
        noise_img = random_noise(image, mode='s&p', amount=0.3)
        noise_img = np.array(255*noise_img, dtype='uint8')
        cv2.imwrite(os.path.join(base_dir, noise_dir, dname, fname), noise_img)