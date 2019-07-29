# Image_processing
#reading and obtein information from an image.
from skimage.filters import laplace
from scipy.ndimage import variance
import cv2 
import numpy as np
import pandas as pd
from skimage.color import rgb2gray
from skimage.restoration import estimate_sigma
from skimage.transform import resize
import datetime
import sys
import os
from joblib import load
import networking

def get_info_from_image (image): 	
	
	if len(image.shape) == 3: # convert image to gray scale
		img=rgb2gray(image)
		
	x1 = variance(laplace(img, ksize=3)) # return variance of laplancian 
	x2 = estimate_sigma(img) # returns Noise 
	
	return x1, x2

def show(text,image,x1):
	
	#image = resize(image, (400,600) )
	cv2.putText(image, "{}: {:.2f}".format(text, x1), (10, 31), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 256), 3)
	cv2.imshow("Image", image)
	cv2.waitKey(0)
	#cv2.imwrite("%s - %s.jpg" %ip, %now.strftime("%Y-%m-%d %H:%M"), img,CV_IMWRITE_JPEG_QUALITY)	
	#vidcap.release()
	cv2.destroyAllWindows()
	

def blury_or_not(x1,x2):
	
	r = networking.requests_to(x1,x2)
	text = "CLEAR"
	if r == 1 :
		text = "BLURRY"
	return text

def main_folder(path,chk_state):
	results =[]
	
	#os.chdir(path)
	for image in os.listdir(path):
		img_path = os.path.join(path,image)
		img = cv2.imread(img_path)
		x1, x2= get_info_from_image(img)
		text = blury_or_not(x1,x2)
		if chk_state :
			show(text,img,x1)
		temp_results =[image,text]
		results.append(temp_results)

	array=np.array(results)
	labels = ["File", "Focus State"]
	report = pd.DataFrame(array, columns=labels)
	return report

def process(password, ip,chk_state):
	vidcap = cv2.VideoCapture("rtsp://admin:%s@%s:554/CH001" %(password,ip))
	now=datetime.datetime.now()
	
	if vidcap.isOpened():
				
		success, image = vidcap.read()
		x1, x2= get_info_from_image(image)
		text = blury_or_not(x1,x2)
        
		if chk_state:
			show(text,image,x1)
	temp_results = [ip,now.strftime("%Y-%m-%d %H:%M"),text]
    
	return temp_results