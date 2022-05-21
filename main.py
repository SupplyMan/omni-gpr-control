from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
import sys
import cpp_gui
import requests

class ExampleApp(QtWidgets.QMainWindow, cpp_gui.Ui_MainWindow):
	def __init__(self, parent=None):
		super(ExampleApp, self).__init__(parent)
		self.setupUi(self)

		self.btnDraw.clicked.connect(self.gridFrame.setStateDraw)
		self.btnErase.clicked.connect(self.gridFrame.setStateErase)
		self.btnClearGrid.clicked.connect(self.gridFrame.clearGrid)
		self.btnSetStart.clicked.connect(self.gridFrame.setStateStartPoint)

		self.btnCalculatePath.clicked.connect(self.sendPath)
		self.btnRectPath.clicked.connect(self.sendRect)

		self.actionSave.triggered.connect(self.gridFrame.saveData)
		self.actiontest_path.triggered.connect(self.gridFrame.testLoad)

		self.status_timeout = 5000

	def sendRect(self):
		data = {"id":117, "width":self.sbWidth.value(), "length":self.sbLength.value(), "resolution":self.sbCellResolution.value()}

		try:
			r = requests.post("http://" + self.txtIPAddress.text() + ":5000/rect", json=data, headers={"Content-Type": "application/json"})
			if r.status_code == 200:
				self.statusbar.showMessage("Command sent successfully.", self.status_timeout)
			else:
				self.statusbar.showMessage("ERROR: Flask server response" + r.status_code, self.status_timeout)
		except:
			self.statusbar.showMessage("ERROR: Failed to send command to robot. Please check connection and try again.", self.status_timeout)

	def sendPath(self):
		try:
			moves = self.gridFrame.calculatePath()
		except:
			self.statusbar.showMessage("ERROR: No start point set.", self.status_timeout)
			return

		if len(moves) == 0:
			self.statusbar.showMessage("ERROR: Generated graph contains zero moves. Please connect path area to start point.", self.status_timeout)
			return

		data = {"id":117, "moves":moves, "resolution":self.sbCellResolution.value()}

		try:
			r = requests.post("http://" + self.txtIPAddress.text() + ":5000/path", json=data, headers={"Content-Type": "application/json"})
			if r.status_code == 200:
				self.statusbar.showMessage("Command sent successfully.", self.status_timeout)
			else:
				self.statusbar.showMessage("ERROR: Flask server response" + r.status_code, self.status_timeout)
		except:
			self.statusbar.showMessage("ERROR: Failed to send command to robot. Please check connection and try again.", self.status_timeout)

def main():
	app = QApplication(sys.argv)
	form = ExampleApp()
	form.show()
	app.exec_()

if __name__ == '__main__':
	main()
