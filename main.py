from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
import sys
import cpp_gui

class ExampleApp(QtWidgets.QMainWindow, cpp_gui.Ui_MainWindow):
    def __init__(self, parent=None):
        super(ExampleApp, self).__init__(parent)
        self.setupUi(self)

        self.btnDraw.clicked.connect(self.gridFrame.setStateDraw)
        self.btnErase.clicked.connect(self.gridFrame.setStateErase)
        self.btnSetStart.clicked.connect(self.gridFrame.setStateStartPoint)
        self.btnCalculatePath.clicked.connect(self.gridFrame.calculatePath)

        self.actionSave.triggered.connect(self.gridFrame.saveData)
        self.actiontest_path.triggered.connect(self.gridFrame.testLoad)

def main():
    app = QApplication(sys.argv)
    form = ExampleApp()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()
