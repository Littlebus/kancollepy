# import cv2
import win32api,win32con

MOUSEEVENTF_MOVE = 0x0001#      移动鼠标 
MOUSEEVENTF_LEFTDOWN = 0x0002# 模拟鼠标左键按下 
MOUSEEVENTF_LEFTUP = 0x0004# 模拟鼠标左键抬起 
MOUSEEVENTF_RIGHTDOWN = 0x0008# 模拟鼠标右键按下 
MOUSEEVENTF_RIGHTUP = 0x0010# 模拟鼠标右键抬起 
MOUSEEVENTF_MIDDLEDOWN = 0x0020# 模拟鼠标中键按下 
MOUSEEVENTF_MIDDLEUP = 0x0040# 模拟鼠标中键抬起 
MOUSEEVENTF_ABSOLUTE = 0x8000# 标示是否采用绝对坐标 

def pixelx(x):
	return int((x/1920)*65535)

def pixely(y):
	return int((y/1080)*65535)

def click(x,y):
	win32api.mouse_event(MOUSEEVENTF_ABSOLUTE|MOUSEEVENTF_MOVE,pixelx(x),pixely(y),0,0)
	win32api.mouse_event(MOUSEEVENTF_LEFTDOWN,0,0,0,0)
	win32api.mouse_event(MOUSEEVENTF_LEFTUP,0,0,0,0)
	

click(1910,10)




# img = cv2.imread("test.jpg")
# cv2.namedWindow("Image")
# cv2.imshow("Image", img)
# cv2.waitKey(0)