import win32gui
import snapshot
import win32con
import cv2
import numpy as np
from PIL import Image


'''
全局信息：
窗口名称
当前状态
'''

def getwindowhandle(name):
	return win32gui.FindWindow(None,name)


def getchildhandle(handle):
	c = []
	win32gui.EnumChildWindows(handle,lambda x,y:y.append(x),c)
	return c


'''
accept name of window
return a rect of window
'''
def getwindowrect(handler):
	window = win32gui.GetWindowRect(handler)
	# rect = (window[0], window[1], window[2], window[3])
	# rect = (window[0]+8, window[1]+31, window[2], window[3])
	return window

'''
receive image
return numpy array
'''
def img2array(img):
	return np.asarray(img)

'''
receive image in numpy array
show the image
'''
def show(im):
	cv2.imshow('image', im)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

'''
receive numpy array image of window
return play area rectangular as to window
'''
def getplayarea(img):
	#find in first row
	for i in range(800):
		if img[0][i][0] != img[0][i+1][0] or img[0][i][1] != img[0][i+1][1] or img[0][i][2] != img[0][i+1][2]:
			return (i,0,i+800,480)
	for i in range(480):
		if img[i][0][0] != img[i+1][0][0] or img[i][0][1] != img[i+1][0][1] or img[i][0][2] != img[i+1][0][2]:
			return (0,i,800,i+480)
	return None