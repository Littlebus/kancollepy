import getWindowHandler as gw
import snapshot as ss
import WRjson as json
from main import *
import time

if __name__ == '__main__':
	wdhandler = gw.getwindowhandle('poi')
	cd = gw.getchildhandle(wdhandler)

	if len(cd) > 4:
		print('poi isn\'t running')

	wdrect = 0

	for i in cd:
		wdrect = win32gui.GetWindowRect(i)
		if wdrect[0] != wdrect[2] and wdrect[1] != wdrect[3]:
			wdhandler = i
			break

	wdrect=wdrect
	win32gui.SetForegroundWindow(wdhandler)

	wdim = snapshot.getSnapshot(wdrect)
	wdim = gw.img2array(wdim)


	plrect = gw.getplayarea(wdim)
	plarea = pointaddrect(wdrect[0:2],plrect)
	plim = snapshot.getSnapshot(plarea)
	plim = gw.img2array(plim)
	# cv2.imwrite('source/image/waiting1.png',plim)

	pos = json.load('source/json/pos.json')
	point = json.load('source/json/clickpoint.json')
	source = json.load('source/json/source.json')
	
	# yuanzhengarea = pos['yuanzheng']
	yz = source['yuanzheng_time']
	# image = gw.img2array(snapshot.getSnapshot(plarea))
	# cv2.imwrite('source/image/yuanzheng_page2.png',image)

	for i in yz:
		img = cv2.imread(i)
		img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
		cv2.imwrite(i,img)
	# t = pointaddrect(plarea[0:2],yuanzheng_status)
	# for i in range(10):
	a = "source/image/yuanzheng_00.png"
	# img = ss.getSnapshot(t)
	# ss.save(img,a)
	# time.sleep(1)

	# abc = yuanzheng_status[-1]

	# print(yuanzhengarea)
	# for i in range(len(yuanzhengarea)):
	# 	t = pointaddrect(plarea[0:2],yuanzhengarea[i])
	# 	# print(t)
	# 	a = "source/image/yuanzheng_unknow%d.png"%(i+1)
	# 	# print(a)
	# 	img = ss.getSnapshot(t)
	# 	# print(type(img),type(a))
	# 	ss.save(img,a)

	# print(yuanzhengarea)

	# judge,thresh = Match.judgematch(imgs,plim,pos['threshold'])
	# print(thresh)
	# if judge:
		# click.click(*pointaddpoint(plarea[0:2],point['chuji']))