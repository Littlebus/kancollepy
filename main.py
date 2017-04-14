import Match, snapshot, click, win32gui
import getWindowHandler as gw
import cv2
import WRjson as json


def pointaddrect(point,rect2):
	return (point[0]+rect2[0],point[1]+rect2[1],point[0]+rect2[2],point[1]+rect2[3])
def pointaddpoint(point1, point2):
	return (point1[0]+point2[0], point1[1]+point2[1])

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

	plim = snapshot.getSnapshot(wdrect)
	plim = gw.img2array(plim)

	plrect = gw.getplayarea(plim)
	plarea = pointaddrect(wdrect[0:2],plrect)

	pos = json.load('source/json/pos.json')
	point = json.load('source/json/clickpoint.json')

	chujiarea = tuple(pos['chuji'])
	chujiarea = pointaddrect(plarea[0:2],chujiarea)

	imgs = cv2.imread('source/image/chuji-button.png')
	# imgt = gw.img2array(snapshot.getSnapshot(chujiarea))

	judge,thresh = Match.judgematch(imgs,plim,pos['threshold'])
	print(thresh)
	if judge:
		click.click(*pointaddpoint(plarea[0:2],point['chuji']))