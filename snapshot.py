from PIL import ImageGrab
import numpy as np
import cv2

def getSnapshot(rect):
	bbox = rect
	image = ImageGrab.grab(bbox)
	return image

def save(img,name):
	im = np.asarray(img)
	cv2.imwrite(name,im)