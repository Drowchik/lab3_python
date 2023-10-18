import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QFileDialog, QToolTip
from PyQt5.QtGui import QIcon, QFont


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        QToolTip.setFont(QFont('SansSerif', 10))
        self.setGeometry(300, 300, 500, 420)
        self.setWindowTitle('Lab3-6212')
        self.setWindowIcon(QIcon('home.png'))
        btn = QPushButton("Create CSV", self)
        btn.setToolTip('This button creates an annotation')
        btn.resize(btn.sizeHint())
        btn.move(50, 50)

        # folderpath = QFileDialog.getExistingDirectory(self, 'Select Folder')
        # print(folderpath)
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())