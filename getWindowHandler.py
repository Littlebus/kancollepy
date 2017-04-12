import win32gui
import snapshot
import win32con
import cv2
import numpy as np
from PIL import Image
'''
accept name of window
return a rect of window
'''
def getwindow(name):
	handler = win32gui.FindWindow(None, name)
	window = win32gui.GetWindowRect(handler)
	rect = (window[0], window[1], window[2] - window[0], window[3] - window[1])
	return window

'''
accept the name of window
return a image in numpy array
'''
def getPlayarea(name):
	rect = getwindow(name)
	im = snapshot.getSnapshot(rect)
	im.save("E:\\cole.jpg")
	numpyim = np.asarray(im)
	return numpyim

def show(im):
	cv2.imshow('image', im)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

if __name__ == '__main__':
	handler = win32gui.FindWindow(None,'poi')
	win32gui.SetForegroundWindow(handler)
	print(handler)
	# handler = win32gui.GetWindow(handler,win32con.GW_CHILD)
	# print(handler)
	# handler = win32gui.GetNextWindow()
	window = win32gui.GetWindowRect(handler)
	rect = (window[0], window[1], window[2] - window[0], window[3] - window[1])
	print(rect)
	im = snapshot.getSnapshot(rect)
	im = np.asarray(im)
	show(im)

	# im = getPlayarea('poi')
	# cv2.imwrite("E:\\collection.jpg", im)
	# cv2.imshow('image',im)
	# im = Image.fromarray(np.uint8(im))
	# im.save("E:\\real.jpg")
	# cv2.waitKey(0)
	# cv2.destroyAllWindows()