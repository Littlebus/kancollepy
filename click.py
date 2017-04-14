import win32api,win32con,win32gui

# MOUSEEVENTF_MOVE = 0x0001#      移动鼠标 
# MOUSEEVENTF_LEFTDOWN = 0x0002# 模拟鼠标左键按下 
# MOUSEEVENTF_LEFTUP = 0x0004# 模拟鼠标左键抬起 
# MOUSEEVENTF_RIGHTDOWN = 0x0008# 模拟鼠标右键按下 
# MOUSEEVENTF_RIGHTUP = 0x0010# 模拟鼠标右键抬起 
# MOUSEEVENTF_MIDDLEDOWN = 0x0020# 模拟鼠标中键按下 
# MOUSEEVENTF_MIDDLEUP = 0x0040# 模拟鼠标中键抬起 
# MOUSEEVENTF_ABSOLUTE = 0x8000# 标示是否采用绝对坐标 

def pixelx(x, defa=1920):
	return int((x/defa)*65535)

def pixely(y, defa=1080):
	return int((y/defa)*65535)

def click(x,y):
	win32api.mouse_event(win32con.MOUSEEVENTF_ABSOLUTE|win32con.MOUSEEVENTF_MOVE,pixelx(x),pixely(y),0,0)
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0,0,0)
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0,0,0)

# def clickbg(handler, x, y):
# 	rect = win32gui.GetWindowRect(handler)
# 	w = rect[2] - rect[0]
# 	h = rect[3] - rect[1]
# 	print(w,h)
# 	a = win32gui.SendMessage(handler, win32con.MOUSEEVENTF_LEFTDOWN,0, pixelx(x,w) + pixely(y,h)*65535)
# 	b = win32gui.SendMessage(handler, win32con.MOUSEEVENTF_LEFTUP,0, pixelx(x,w) + pixely(y,h)*65535)
# 	a = win32gui.SendMessage(handler, win32con.MOUSEEVENTF_LEFTDOWN,0, pixelx(x,w) + pixely(y,h)*65535)
# 	b = win32gui.SendMessage(handler, win32con.MOUSEEVENTF_LEFTUP,0, pixelx(x,w) + pixely(y,h)*65535)
# 	return a,b