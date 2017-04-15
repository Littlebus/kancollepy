import Match, snapshot, click, win32gui
import getWindowHandler as gw
import cv2
import WRjson as json
import time

plrect = (0,0)
pos = 0
point = 0
source = 0




def pointaddrect(point,rect2):
	return (point[0]+rect2[0],point[1]+rect2[1],point[0]+rect2[2],point[1]+rect2[3])
def pointaddpoint(point1, point2):
	return (point1[0]+point2[0], point1[1]+point2[1])
def absrect(pos):
	return pointaddrect(plarea[0:2], pos)
def abspoint(pos):
	return pointaddpoint(plarea[0:2], pos)
def backToMugang():
	pt = abspoint(point['back'])
	click.click(*pt)


def goyuanzheng(number):
	yzid = source['yuanzheng_number']
	target = yzid[number-1]
	imgt = cv2.imread(target)
	# gw.show(imgt)
	threshold = pos['threshold']
	print(threshold)
	areas = pos['yuanzheng']
	sign = True
	for i in areas:
		# print(i)
		rect = absrect(i)
		# print('rect',rect)
		imgs = gw.img2array(snapshot.getSnapshot(rect))
		# gw.show(imgs)
		judge,thresh = Match.judgematch(imgs,imgt,threshold)
		print(i,thresh)
		# print(areas.index(i))
		if judge:
			# print('match succeed: %d!'%number)
			pt = abspoint(point['yuanzheng_number'][areas.index(i)])
			click.click(*pt)
			res = check()
			if not res:
				print('have left')
				backToMugang()
				return
			sign = False
			break
	if sign:
		backToMugang()		



def check():
	path = source['yuanzheng_status'][0]
	rect = absrect(pos['yuanzheng_status'])

	time.sleep(1)
	imgs = gw.img2array(snapshot.getSnapshot(rect))
	# gw.show(imgs)
	imgt = cv2.imread(path)
	# gw.show(imgt)
	judge, thresh = Match.judgematch(imgs,imgt,pos['threshold'])
	print(judge,thresh)
	if judge:
		return False
	return True

if __name__ == '__main__': 
	# a = []
	# for i in range(40):
	# 	a.append('source/image/yuanzheng%d.png'%(i+1))
	# b = {'yuanzheng_number':a}
	# json.store('source.json',b)
	
	
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

	plim = snapshot.getSnapshot(wdrect)
	plim = gw.img2array(plim)

	plrect = gw.getplayarea(plim)
	plarea = pointaddrect(wdrect[0:2],plrect)

	pos = json.load('source/json/pos.json')
	point = json.load('source/json/clickpoint.json')
	source = json.load('source/json/source.json')

	chujiarea = tuple(pos['chuji'])
	chujiarea = pointaddrect(plarea[0:2],chujiarea)

	
	imgs = cv2.imread('source/image/chuji-button.png')
	imgt = gw.img2array(snapshot.getSnapshot(chujiarea))

	judge,thresh = Match.judgematch(imgs,plim,pos['threshold'])
	print(thresh)
	if judge:
		click.click(*pointaddpoint(plarea[0:2],point['chuji']))
		time.sleep(2)
		click.click(*pointaddpoint(plarea[0:2],point['yuanzheng']))
		time.sleep(2)
		goyuanzheng(2)

