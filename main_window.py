import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont, QIcon
from task_1 import main


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('6212 - lab_3')
        QToolTip.setFont(QFont('SansSerif', 10))
        self.setWindowTitle('6212 - lab3')
        self.setWindowIcon(QIcon('home.png'))
        button = QPushButton('Button', self)
        button.resize(button.sizeHint())
        button.move(50, 50)
        button.clicked.connect(self.click_csv)

        self.setGeometry(300, 300, 300, 200)
        self.show()

    def click_csv(self):
        dialog = QDialog(self)
        dialog.setWindowTitle('Create file CSV')
        
        path_label = QLabel("Choose path:", dialog)
        self.path_line_edit = QLineEdit(dialog)
        browse_button = QPushButton("Browse", dialog)
        browse_button.clicked.connect(self.select_folder)
        create_button = QPushButton("Сreate CSV", dialog)
        create_button.clicked.connect(self.click_create)
        dialog.setGeometry(400, 400, 200, 100)
        
        layout = QVBoxLayout()
        layout.addWidget(path_label)
        layout.addWidget(self.path_line_edit)
        layout.addWidget(browse_button)
        layout.addWidget(create_button)
        dialog.setLayout(layout)

        dialog.exec_()

    def select_folder(self):
        self.folderpath = QFileDialog.getExistingDirectory(self, 'Select Folder')
        self.path_line_edit.setText(self.folderpath)

    def click_create(self):
        if 'dataset' in self.folderpath:
            main(self.folderpath)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()

    sys.exit(app.exec_())
