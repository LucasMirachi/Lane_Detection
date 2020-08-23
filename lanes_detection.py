#Importing the libraries
import cv2
import numpy as np

def canny(img):
	# Converting the image's color channel from RGB to Grayscale
    gray = cv2.cvtColor(src=img, code=cv2.COLOR_RGB2GRAY)
    # To apply a GaussionBlur with a 5x5 Kernel to "smooth" the image
    blur = cv2.GaussianBlur(src=gray,ksize=(5, 5),sigmaX=10)
    # To define the upper and lower tresholds for Canny Filter
    median_pixel_value = np.median(img)
    lower=int(max(0,0.7*median_pixel_value))
    upper = int(min(255, 1.3*median_pixel_value))
    canny = cv2.Canny(image=gray, threshold1=lower, threshold2=upper)
    return canny

def region_of_interest(canny):
	# PS: the video size I used is actually (1080, 1920, 3) 
    height = canny.shape[0]
    width = canny.shape[1]
    mask = np.zeros_like(canny)
 
    polygon = np.array([[
    (175, height),
    (750, 700),
    (1100, 700),
    (1750, height),]], np.int32)
 	#So far, we've created a black image with a white polygon that involves the area we want to show. Now, we'll have to make a "bitwise &" operation
    cv2.fillPoly(mask, polygon, 255)
    masked_image = cv2.bitwise_and(canny, mask)
    return masked_image

def display_lines(img,lines):
    line_image = np.zeros_like(img)
    # To loop through lines
    if lines is not None: #To check if the 'lines' array is not empty
        for line in lines:
            for x1, y1, x2, y2 in line:
            	# To take each line that we're interacting and draw them into our blank image line_image
                cv2.line(img=line_image,pt1=(x1,y1),pt2=(x2,y2),color=(0,0,255),thickness=10)
    return line_image

def make_points(image, line):
    slope, intercept = line
    #To define where the detected lines will be drawn on the video
    y1 = int(image.shape[0])     # bottom of the video -or- height of the image 
    y2 = int(y1*6.45/10)         # slightly lower than the middle
    x1 = int((y1 - intercept)/slope)
    x2 = int((y2 - intercept)/slope)
    return [[x1, y1, x2, y2]]
 
def average_slope_intercept(image, lines):
	#left_fit contains the coordinates of the averaged lines on the left and right_fit contains the coordinates of the averaged lines on the right
    left_fit    = []
    right_fit   = []
    if lines is None:
        return None
    for line in lines:
        for x1, y1, x2, y2 in line:
            fit = np.polyfit(x=(x1,x2), y=(y1,y2), deg=1)
            slope = fit[0]
            intercept = fit[1]
            # According to the cartesian coordinates and the equation y = mx+b, if the slope is negative, it belongs to the left line (because the values of y are decreasing) and if slope is positive, it belongs to the right line 
            if slope < 0: # y is reversed in image
                left_fit.append((slope, intercept))
            else:
                right_fit.append((slope, intercept))
    # add more weight to longer lines
    if len(left_fit) and len(right_fit):
    	left_fit_average  = np.average(left_fit, axis=0)
    	right_fit_average = np.average(right_fit, axis=0)
    	left_line  = make_points(image, left_fit_average)
    	right_line = make_points(image, right_fit_average)
    	averaged_lines = [left_line, right_line]
    	return averaged_lines
 
cap = cv2.VideoCapture("lanes_video.mp4")
while(cap.isOpened()):
	#To return every video-frame from our capture, we must create a loop
    _, frame = cap.read()
    #cropped_image = region_of_interest(frame) -> To visualize the mask and tweak the mask coordenates
    canny_image = canny(frame)
    cropped_canny = region_of_interest(canny_image)
    lines = cv2.HoughLinesP(cropped_canny, 2, np.pi/180, 100, np.array([]), minLineLength=40,maxLineGap=5)
    averaged_lines = average_slope_intercept(frame, lines)
    line_image = display_lines(frame, averaged_lines)
    combo_image = cv2.addWeighted(src1=frame, alpha=0.8, src2=line_image, beta=1, gamma=1)
    cv2.imshow("result", combo_image)
   	#Instead of waiting for the whole video to end so we can close it, we can end the loop with the command
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()