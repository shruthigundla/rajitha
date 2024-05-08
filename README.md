
## crop1
DRAWING BOUNDING BOXES
crop
![7622202030987_f306535d741c9148dc458acbbc887243_L_493](https://github.com/shruthigundla/rajitha/assets/169051447/94bdd867-d9d5-4104-81d7-646a625c7bf0)

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

## histogram
A histogram is a visual representation of the distribution of quantitative data.Histograms are commonly used in image processing and computer vision for tasks like analyzing pixel intensity distributions.

![avngers](https://github.com/shruthigundla/rajitha/assets/169051447/8b364903-bae5-4598-a42f-f2f6b619220a)



LIBRARIES USED:
```
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
```
These are the libraries we used in histogram ,numpy is used for numerical computing.
cv2 is  provides various tools and algorithms for image and video processing
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

## iterate
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



## video
python script to capture video from webcam


LIBRARIES USED
```
# import the opencv library 
import cv2
```
openCV (Open Source Computer Vision Library) is an open-source computer vision and machine learning software library. It's widely used for various tasks such as image and video processing, object detection and tracking, face recognition, and more.
cv2 is  provides various tools and algorithms for image and video processing
  
```  
# define a video capture object 
vid = cv2.VideoCapture(0) 
```
IT is used to capture video frames from a camera. It allows you to access video streams from various sources, including video files, image sequences, and cameras.

while(True): 


``` 
    # Capture the video frame 
    # by frame 
    ret, frame = vid.read()
```

 It is used to capture video frames from the camera stream using the VideoCapture object we created. The captured frame, represented as a NumPy array. Each element of the array contains the pixel values of the corresponding pixel in the frame.
  
  

 ```
    # Display the resulting frame 
    cv2.imshow('frame', frame)
```

here we displayed the resulting frame in a window with the title 'frame'.

    
```
    # the 'q' button is set as the 
    # quitting button you may use any 
    # desired button of your choice 
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break
```
here q is used to quit the program .after complition of the video.

  ```
# After the loop release the cap object 
vid.release() 
# Destroy all the windows 
cv2.destroyAllWindows()
```
it states that after the loop displays the frames from the all video streams it is imporatant to distroy other additionally created windows.

