from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication
from yz import Ui_MainWindow  
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
  
class mywindow(QMainWindow,Ui_MainWindow):  
	_signal=QtCore.pyqtSignal(list)
	tasklist = queue.PriorityQueue(maxsize=-1)		
	def __init__(self):
		super(mywindow,self).__init__()  
		self.setupUi(self)  
		t = threading.Thread(target = self.eventLoop)
		t.setDaemon(True)
		t.start()
		self.pushButton.clicked.connect(self.forwardYznumber)
		self.pushButton_2.clicked.connect(self.stopEvent)
		self._signal.connect(self.yz)


	def eventLoop(self):

		while True:
			self.lcdNumber.display("24:31")
			if self.tasklist.empty():
				# print('1,',self.spinBox.value())
				# print('2,',self.spinBox_2.value())
				# print('3,',self.spinBox_3.value())
				
				time.sleep(1)
			else:
				task = self.tasklist.get()
				print('get task:%s'%task)

	def forwardYznumber(self):
		status = [self.checkBox.checkState()*0.5*self.spinBox.value(),\
					self.checkBox_2.checkState()*0.5*self.spinBox_2.value(),\
					self.checkBox_3.checkState()*0.5*self.spinBox_3.value(),]
		status = list(map(int,status))
		self._signal.emit(status)

	def yz(self, status):
		#此处应该用QThread改写为多线程。
		time.sleep(1)
		for i in status:
			if i !=0:
				self.tasklist.put('goyuanzheng(%d)'%i,10)
		# print('远征分别为:',status)
	def stopEvent(self):
		self.tasklist.put('stop!',1)


if __name__=="__main__":  

	app=QtWidgets.QApplication(sys.argv)  
	myshow=mywindow()
	myshow.show()
	sys.exit(app.exec_())
 
    # sys.exit(app.exec_())  