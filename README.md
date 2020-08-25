# Lane Detection with OpenCV
The objective of this project is to create a lane lines detection algorithm using Python and computer vision techniques. It is part of the [Complete Self Driving Car Course - Applied Deep Learning](https://www.udemy.com/course/applied-deep-learningtm-the-complete-self-driving-car-course/), and much of the code is leveraged from the lecture notes.

![](https://raw.githubusercontent.com/LucasMirachi/Lane_Detection/master/Images/detected_avg_lines.gif)

## Resources
For this project, the following resources were used:
* [Python 3.8.5](https://www.python.org/downloads/) - Latest Python version by the time the project was created
* [Numpy 1.18.5](https://numpy.org/)
* [OpenCV 4.3.0](https://opencv.org/releases/)
* A video recording of a vehicle moving in a lane street
The video used on the project was filmed by me in my hometown (Belo Horizonte - Brazil). In my conception, it was a interesting one because it contained not only straight and cropped lanes, but it also had shadows from the trees and a little change of the perspective due to a soft uphill on the streed (that makes the lanes look a little more separeted from each other), wich made the line detection a little bit more difficult.
The raw video can be downloaded [here](https://drive.google.com/file/d/1nM4K6CksBFwiSmNYrX8QAB3XzLxWB3TG/view?usp=sharing).

In OpenCV, in order to display the video file, it is needed to create a Video Capture Object and then create a loop to decode and show every video frame 

![](https://raw.githubusercontent.com/LucasMirachi/Lane_Detection/master/Images/base_video.gif)

## Application of the Canny Filter
RGB Color images have, as the name suggests, 3 color channels (Reg, Green, Blue). Before applying the Canny Filter, one technique applyed to use less computational power, is to transform the 3-Color-Channel RGB image into a 1-Color-Channel Grayscale image.

![](https://user-images.githubusercontent.com/44238566/91187477-9707b800-e6c6-11ea-8a54-1e72456e2c9b.png)

![](https://raw.githubusercontent.com/LucasMirachi/Lane_Detection/master/Images/gray.gif)

### Apply Blur with Gaussian Filter
When applying the Canny Filter for edge detection, it is easily affected by noise and, to reduce this noise and make the image smoother, we apply a Blur
![](https://raw.githubusercontent.com/LucasMirachi/Lane_Detection/master/Images/blur.gif)

### Edge detection with Canny

![](https://raw.githubusercontent.com/LucasMirachi/Lane_Detection/master/Images/canny.gif)

## Highliting the Region of Interest

![](https://user-images.githubusercontent.com/44238566/91187539-aa1a8800-e6c6-11ea-8f57-1f2d175de578.png)

![](https://raw.githubusercontent.com/LucasMirachi/Lane_Detection/master/Images/mask.gif)

### Criacao das linhas

![](https://raw.githubusercontent.com/LucasMirachi/Lane_Detection/master/Images/lines.gif)

### Average Lines
![](https://raw.githubusercontent.com/LucasMirachi/Lane_Detection/master/Images/detected_avg_lines.gif)

