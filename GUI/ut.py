from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication
from yz2 import Ui_MainWindow  
import time, threading
import queue
import sys 
  
# class mywindow(QMainWindow):  
#     def __init__(self):  
#         super(mywindow,self).__init__()  
#         self.new=Ui_MainWindow()  
#         self.new.setupUi(self)  

# from PyQt5 import QtWidgets  
# from untitled import Ui_Form  
  
global restTime
restTime =[0,0,0]


class mywindow(QMainWindow,Ui_MainWindow):  
	_expeditionNumber=QtCore.pyqtSignal(list)
	tasklist = queue.PriorityQueue(maxsize=-1)		
	def __init__(self):
		super(mywindow,self).__init__()  
		self.setupUi(self)  
		self.timer=QtCore.QTimer()
		self.lcdNumber.display("00:00")
		self.lcdNumber_2.display("00:00")
		self.lcdNumber_3.display("00:00")
#----------------------------------------------------------------
#slot and signal
		self.pushButton.clicked.connect(self.getNumber)
		self.pushButton_2.clicked.connect(self.stopEvent)

		self._expeditionNumber.connect(self.emitExpedition)	

		self.timer.timeout.connect(self.countTime)
#----------------------------------------------------------------	
#initial event loop thread
		t = threading.Thread(target = self.eventLoop)
		t.setDaemon(True)
		t.start()

	def eventLoop(self):
		while True:	
			if self.tasklist.empty():
				print('sleeping')
				time.sleep(1)
			else:
				task = self.tasklist.get()
				print('get task:%s'%task)

	def getNumber(self):
		status = [self.checkBox.checkState()*0.5*self.spinBox.value(),\
					self.checkBox_2.checkState()*0.5*self.spinBox_2.value(),\
					self.checkBox_3.checkState()*0.5*self.spinBox_3.value(),]
		status = list(map(int,status))
		self._expeditionNumber.emit(status)
		self.timer.start(1000)

	def emitExpedition(self, status):
		#此处应该用QThread改写为多线程。
		global restTime
		restTime=[100,30,46]
		for i in status:
			if i !=0:
				self.tasklist.put('goyuanzheng(%d)'%i,10)
		print('远征分别为:',status)
		
	def stopEvent(self):
		self.tasklist.put('stop!',1)
#----------------------------------------------------------------
	def countTime(self):
		global restTime
		t = list(map(lambda x: "%02d:%02d" % (x/60,x%60),restTime))
		self.lcdNumber.display(t[0])
		self.lcdNumber_2.display(t[1])
		self.lcdNumber_3.display(t[2])
		for i in restTime:
			if i != 0:
				restTime[restTime.index(i)]=i-1

	def showRestTime(self):
		pass

if __name__=="__main__":  

	app=QtWidgets.QApplication(sys.argv)  
	myshow=mywindow()
	myshow.show()
	sys.exit(app.exec_())
 
    # sys.exit(app.exec_())

