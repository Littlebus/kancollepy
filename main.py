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
			res = checkYZstatus()
			if not res:
				print('have left')
				time = checkRestTime('yz')
				backToMugang()
				return
			sign = False
			break
	if sign:
		backToMugang()		


'''
检查远征是否已经出发：
必须在已经点击数字后进行
'''
def checkYZstatus():
	path = source['yuanzheng_status'][0]
	rect = absrect(pos['yuanzheng_status'])

	time.sleep(1)
	#获得按钮区域
	imgs = gw.img2array(snapshot.getSnapshot(rect))
	imgt = cv2.imread(path)
	judge, thresh = Match.judgematch(imgs,imgt,pos['threshold'])
	print(judge,thresh)
	if judge:
		return False
	return True

def checkRestTime(area):
	if area == 'yz':
		#从文件中读取模板
		imgt = []
		path = source['yuanzheng_time']
		for i in path:
			imgt.append(cv2.imread(i))
			# gw.show(cv2.imread(i))
		# imgt = imgt[::-1]
		#用map获得绝对位置
		rect = pos['yuanzheng_time_digit']
		rect = list(map(absrect,rect))
		# print(rect)
		# rect = rect[::-1]
		time_wd = []
		for i in rect:
			imgs = gw.img2array(snapshot.getSnapshot(i))
			# gw.show(imgs)
			sign = True
			# print(len(imgt))
			thresh = []
			# print('h')
			for j in range(len(imgt)):
				# print(type(template))
				# gw.show(template)
				judge, thresht = Match.judgematch(imgs,imgt[j],0.03)
				thresh.append(thresht)
				# if judge:
				# 	sign = False
				# 	time_wd.append(9-j)
				# 	break
			# print(rect.index(i),thresh)
			min_thresh = min(thresh)
			# print(min_thresh)
			if min_thresh>0.04:
				return False,[]
			else:
				time_wd.append(thresh.index(min_thresh))
		# print(time_wd)
		return True, time_wd
	elif area == 'rq':
		return True
	else:
		return False

			
			

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

	res, rest_time = checkRestTime('yz')
	print(res,rest_time)

'''
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
'''
