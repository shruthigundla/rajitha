<<<<<<< HEAD

## CROP1
DRAWING BOUNDING BOXES
crop
![image](https://github.com/shruthigundla/rajitha/assets/169051447/db96c4cc-e34f-42fd-9933-9af754bd69e6)

```LIBRARIES USED
```

```
import os
import csv
from PIL import Image, ImageDraw
import argparse
```

parser = argparse.ArgumentParser()

parser.add_argument("--image_path", help = "Enter the path of your image")

parser.add_argument("--csv", help = "your csv file path , which has bounding box values")

parser.add_argument("--out_dir", help = "name of output directory where you want to save your output")

args = parser.parse_args()

image_dir = args.image_path

csv_file = args.csv

output_dir = args.out_dir




# csv_file = "/home/shruthi-gundla/Downloads/7622202030987_bounding_box.csv"
# image_dir = "/home/shruthi-gundla/Downloads/7622202030987"
# output_dir = "/home/shruthi-gundla/Downloads/7622202030987_with_boxes"


os.makedirs(output_dir, exist_ok=True)


```
def draw_boxes(image, boxes):
    draw = ImageDraw.Draw(image)
    for box in boxes:
        left = int(box['left'])
        top = int(box['top'])
        right = int(box['right'])
        bottom = int(box['bottom'])
        draw.rectangle([left, top, right, bottom], outline="red")
    return image
```
here we are drawing coordinates to the image on top , bottom, left and right side of the images after that moified image is retuned.

```
def crop_image(image, boxes):
    cropped_images = []
    for box in boxes:
        left = int(box['left'])
        top = int(box['top'])
        right = int(box['right'])
        bottom = int(box['bottom'])
        cropped_img = image.crop((left, top, right, bottom))
        cropped_images.append(cropped_img)
    return cropped_images
```
here we are cropinng the images where we drawn rectangular boxes to them ,on top , bottom,left and right sides of the images are cropped and then croped images are returned 

```
with open(csv_file, 'r') as file:
    csv_reader = csv.DictReader(file)
    print(csv_reader)
    for row in csv_reader:
        # print(row)
        # print(type(row))
        print(row["filename"])
```
it opens the csv file and then reads the dictonary.then here row and type of row in file name is printed.

   ```
 for row in csv_reader:
       image_name = row['filename']
       image_path = os.path.join(image_dir, image_name)
       output_path = os.path.join(output_dir, image_name)
       image = Image.open(image_path)
       boxes = [{'left': row['xmin'], 'top': row['ymin'], 'right': row['xmax'], 'bottom': row['ymax']}]
       cropped_images = crop_image(image, boxes)
       for i, cropped_img in enumerate(cropped_images):
        cropped_img.save(os.path.join(output_dir, f"{i}_{image_name}"))  
       full_image_with_boxes = draw_boxes(image, boxes)
       full_image_with_boxes.save(os.path.join(output_dir, f"full_{image_name}"))
```
here we are saving the images where we drawn coordinates and croped them.


```
![image](https://github.com/shruthigundla/rajitha/assets/169051447/e4c811fa-f237-419a-bc61-cd93129ad11f)

...

## HISTOGRAM
A histogram is a visual representation of the distribution of quantitative data.Histograms are commonly used in image processing and computer vision for tasks like analyzing pixel intensity distributions.

![avngers](https://github.com/shruthigundla/rajitha/assets/169051447/8b364903-bae5-4598-a42f-f2f6b619220a)



```
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
import argparse
```

parser = argparse.ArgumentParser()
parser.add_argument("--image_path", help = "Enter the path of your image")
parser.add_argument("--out_dir", help = "name of output directory where you want to save your output")

args = vars (parser.parse_args())
image =cv.imread(args['image_path'])

```
img = cv.imread('bird.jpg')
```
by using imread function we are reading the details of the image.

```
assert img is not None, "file could not be read, check with os.path.exists()" 
```
if the image is not read then code will not read and return error.

```
color = ('b','g','r')
for i,col in enumerate(color):
 histr = cv.calcHist([img],[i],None,[256],[0,256])
 plt.plot(histr,color = col)
 plt.xlim([0,256])
plt.show()
```
histogram caluculate the colour of blue, green and red channels and plot the colour of the histogram and sets the limits and shows there.







![histogram images main](https://github.com/shruthigundla/rajitha/assets/169051447/1c5db1e2-ef7d-4275-99b3-732041a700f8)

## ITERATE
Writing a program to iterate the first ten numbers,and in each iteration, printing the sum of current and previous numbers.

import argparse

parser = argparse.ArgumentParser()
parser.add_argument ('--number', help = "enter the numbers")
args = parser.parse_args()

```
num = list(range(10))
```
here list of numbers 0 to 9 is given

```
previousNum = 0
```
previous number value assigned is equal to 0

```
for i in num:
    sum = previousNum + i
```
here we are caluculating sum of crrent number (i) and previous number

  ```
  print('Current Number '+ str(i) + 'Previous Number ' + str(previousNum) + 'is ' + str(sum))
    previousNum=i
```
here we are printing previous and current numbers.



## VIDEO


https://github.com/shruthigundla/rajitha/assets/169051447/2e8d6174-8b9f-4a35-888a-fc224049a07c



=======
>>>>>>> dff9bd7... first commit
