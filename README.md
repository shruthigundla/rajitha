
## CROP1
DRAWING BOUNDING BOXES
crop
![image](https://github.com/shruthigundla/rajitha/assets/169051447/db96c4cc-e34f-42fd-9933-9af754bd69e6)




LIBRARIES USED


```
import os
import csv
from PIL import Image, ImageDraw
```


This imports the operating system module,mainly it depends on functionality like reading or writing the files and manipulating paths.
Csv means comma seperated values,It is used to import reading and writing tabular data
PIL used to import images,adds support for opening, manipulating, and saving many different image file formats. 


```
csv_file = "/home/shruthi-gundla/Downloads/7622202030987_bounding_box.csv"
```
Here we are assigning the file path to csv.

```
image_dir = "/home/shruthi-gundla/Downloads/7622202030987"
```
Here we given the path where images are stored

```
output_dir = "/home/shruthi-gundla/Downloads/7622202030987_with_boxes"
```
we are specifying the out put directory path.

```
os.makedirs(output_dir, exist_ok=True)
```
we are creating a directory here.id the directory already exits it doesnot show error



```
def draw_boxes(image, boxes):
    draw = ImageDraw.Draw(image)
    for box in boxes:
        left = int(box['left'])
        top = int(box['top'])
        right = int(box['right'])
        bottom = int(box['bottom'])
        draw.rectangle([left, top, right, bottom], outline="red")
```
here we are defing the function draw_boxes,that draw boxes on image. and we representing the coordinates top-left and bottom-right corners of the bounding box.and a red rectangle is drawn around each bounding box.

```
    return image
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
The boxes argument is a list of dictionaries representing the bounding boxes. Each dictionary contains keys 'left', 'top', 'right', and 'bottom', corresponding to the coordinates of the bounding box.For each bounding box, the coordinates are extracted, converted to integers, and used to croped a region from the input image using the crop() method of the PIL Image object.This function can be used to crop regions of interest from an image based on the provided bounding box coordinates.
    
```
with open(csv_file, 'r') as file:
    csv_reader = csv.DictReader(file)
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
![image](https://github.com/shruthigundla/rajitha/assets/169051447/e4c811fa-f237-419a-bc61-cd93129ad11f)


Bounding box coordinates are extracted from the row and passed to the to crop regions of interest from the image.
Cropped images are saved individually with filenames and bounding boxes are drawn on the original image using the draw_boxes() function.
The original image with bounding boxes drawn is saved with a filename prefix 'full_' followed by the original image filename.

## HISTOGRAM
A histogram is a visual representation of the distribution of quantitative data.Histograms are commonly used in image processing and computer vision for tasks like analyzing pixel intensity distributions.

![avngers](https://github.com/shruthigundla/rajitha/assets/169051447/8b364903-bae5-4598-a42f-f2f6b619220a)



LIBRARIES USED:
```
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
```
These are the libraries we used in histogram ,numpy is used for numerical computing.
cv2 is  provides various tools and algorithms for image and video processing.
from matplotlib import pyplot as plt,which is a plotting library for Python.
.

FUNCTIONS


``` 
img = cv.imread('/home/shruthi-gundla/Downloads/avngers.jpg')
```
This function is from the  (cv2 module) .it is used to read an image file from the specified path.

```
cv.imwrite("/home/shruthi-gundla/Desktop/shruthi/histogramgraph.png",img)
```
This function is from the  (cv2 module) .used to write an image to a file.This is the file path where you want to save the image. It specifies the directory and the filename (histogramgraph.png) of the image file we want to create.

assert img is not None, "file could not be read, check with os.path.exists()"


```
color = ('b','g','r')
```
here we used blue, green and red clour is used

```
for i,col in enumerate(color):
```
 For each pair, i will hold the index of the current color 

```
histr = cv.calcHist([img],[i],None,[256],[0,256])
```
here we  calculated the histogram of the image img along a specific color channel.

```
 plt.plot(histr,color = col)
 ```
we plotted the histogram  with a specific color specified by the variable

```
 plt.xlim([0,256])
 ```
This function from the matplotlib library is used to set the limits of the x-axis.and specifies the lower and upper limits of the x-axis, respectively.

```
plt.show()
```
this function shows the output we made

![histogram images main](https://github.com/shruthigundla/rajitha/assets/169051447/1c5db1e2-ef7d-4275-99b3-732041a700f8)

## ITERATE
Writing a program to iterate the first ten numbers,and in each iteration, printing the sum of current and previous numbers.


```
num = list(range(10))

```

here is the list of ten numbers from 0-9 

```
previousNum = 0
```
this line states that previous num has integer value = 0


```
for i in num:
    sum = previousNum + i
```
here we caluculated the sum of i and previous numbers

    
    
    print('Current Number '+ str(i) + 'Previous Number ' + str(previousNum) + 'is ' + str(sum))
    
   here we printed the current number, the previous number, and the sum of the previous number and the current number.

```
previousNum=i
```
here we can see the updated values which are accumulated by sum of previous numbers



## VIDEO

librares used
```
import imutils 
import cv2 # opencv 모듈
```
import imutils helps in immage processing functions such as translation, rotation, resizing, skeletonization, displaying Matplotlib images,etc
cv2 is  provides various tools and algorithms for image and video processing.

```
video = ""

result_path = ""camera.avi""
```
this states that we given path to save the video

```
if video == "":
    print("[webcam start]")
    vs = cv2.VideoCapture(0)
```
using cv2 function we started capturing the video from webcam


```
else:
    print("[video start]")
    vs = cv2.VideoCapture(video)
```
else refers to of given condition is not satisfied then it will excute the code witthin block.then it stat capturng video using cv2

writer = None


```
while True:
    ret, frame = vs.read
```
here read function refers that loop continuosly reads the frames that are recorded by video.
    
```
    if frame is None:
        break
```
after reading all frames the loop breaks 

```
    frame = imutils.resize(frame, width=320, height=240)
```
by using imutils.resize function size and ratios of the images are adjusted.

    
    ```
    cv2.imshow("frame", frame)
    ```
here the resized image is shown by using open cv

```
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break
```
        by using wait key statment key is presed for 1millisecond and returns valu to key.and If the 'q' key is pressed, the loop is broken using the break statement, and terminate the video capture process.
                                    
  ```
  if writer is None:
        fourcc = cv2.VideoWriter_fourcc(*"MJPG")
        writer = cv2.VideoWriter(result_path, fourcc, 25, (frame.shape[1], frame.shape[0]), True)
  ```

this check if  writer object is none then it is not intialised .so by using cv2 function the line intulises video code by using 'MJPG'.and in result path the video out put is saved. here width and height of videoframes are obtained from the shape of the input frame.

   ```
 if writer is not None:
        writer.write(frame)
```
this line states that if video writer frame is properly intialised then frames are writen to the out put video file

```
vs.release()
```
by using vs.release method the recorded video is released

```
cv2.destroyAllWindows()
```
this function closes all OpenCV windows that are  opened during this program.and cleans the displayed windows which are worked during this program.



