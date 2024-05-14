
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--image_path", help = "Enter the path of your image")
parser.add_argument("--out_dir", help = "name of output directory where you want to save your output")

args = vars (parser.parse_args())
image =cv.imread(args['image_path'])

img = cv.imread('bird.jpg')
assert img is not None, "file could not be read, check with os.path.exists()" 
color = ('b','g','r')
for i,col in enumerate(color):
 histr = cv.calcHist([img],[i],None,[256],[0,256])
 plt.plot(histr,color = col)
 plt.xlim([0,256])
plt.show()
