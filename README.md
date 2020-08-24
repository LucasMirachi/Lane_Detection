# Lane Detection with OpenCV
The objective of this project is to create a lane detector algorithm using Python and computer vision techniques. 


![](https://raw.githubusercontent.com/LucasMirachi/Lane_Detection/master/Images/detected_avg_lines.gif)

## Setup
For this project, the following libraries were used:
1. [Python 3.8.5](https://www.python.org/downloads/) - Latest Python version by the time the project was created
2. [Numpy](https://numpy.org/)
3. [OpenCV](https://opencv.org/releases/)

## Image Preprocessing
The video used was filmed by me in my hometown located in Belo Horizonte - Brazil. Its a 
![](https://raw.githubusercontent.com/LucasMirachi/Lane_Detection/master/Images/base_video.gif)

### Convert to Grayscale
RGB images have 3 color channels (Reg, Green, Blue). In order to use less computational power, before applying the Canny Filter, one technique used is to transform the 3-Color-Channel RGB image into a 1-Color-Channel Grayscale image.

![](https://raw.githubusercontent.com/LucasMirachi/Lane_Detection/master/Images/gray.gif)

### Apply Blur with Gaussian Filter
When applying the Canny Filter for edge detection, it is easily affected by noise and, to reduce this noise and make the image smoother, we apply a Blur
![](https://raw.githubusercontent.com/LucasMirachi/Lane_Detection/master/Images/blur.gif)

### Apply Canny Filter

![](https://raw.githubusercontent.com/LucasMirachi/Lane_Detection/master/Images/canny.gif)

## Highliting the Region of Interest

![](https://raw.githubusercontent.com/LucasMirachi/Lane_Detection/master/Images/mask.gif)

### Criacao das linhas

![](https://raw.githubusercontent.com/LucasMirachi/Lane_Detection/master/Images/lines.gif)

### Average Lines
![](https://raw.githubusercontent.com/LucasMirachi/Lane_Detection/master/Images/detected_avg_lines.gif)


This project is part of the Udacity Self-Driving Car Nanodegree, and much of the code is leveraged from the lecture notes.
