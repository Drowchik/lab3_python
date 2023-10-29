import sys
import os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import Qt
from task_1 import run1
import task_2 
import task_3
import task_5

class ScrollLabel(QScrollArea):
    def __init__(self, *args, **kwargs):
        QScrollArea.__init__(self, *args, **kwargs)
        self.setWidgetResizable(True)
        text = QWidget(self)
        self.setWidget(text)
        lay = QVBoxLayout(text)
        self.label = QLabel(text)
        self.label.setWordWrap(True)
        lay.addWidget(self.label)

    def setText(self, text):
        self.label.setText(text)
        
class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.setStyleSheet(
            "background:#fec7d7; color: #fffffe; font-weight:bold; border-radius: 5px;")

    def initUI(self):
        
        self.setWindowTitle('6212 - lab_3')
        QToolTip.setFont(QFont('SansSerif', 10))
        self.setWindowTitle('6212 - lab3')
        self.setWindowIcon(QIcon('home.png'))
        
        self.button = QPushButton('Create CSV-Dataset', self)
        self.button.adjustSize()
        self.button.clicked.connect(self.click_csv)
        self.button.setStyleSheet("background:#0e172c; border-radius: 5px; min-width: 300px; min-height: 100px;")
        
        self.button_dataset = QPushButton('Create Dataset-Copy', self)
        self.button_dataset.adjustSize()
        self.button_dataset.clicked.connect(self.click_dataset)
        self.button_dataset.setStyleSheet("background:#0e172c; border-radius: 5px; min-width: 300px; min-height: 100px;")
        
        
        self.button_dataset2 = QPushButton('Create Dataset-Copy2', self)
        self.button_dataset2.adjustSize()
        self.button_dataset2.clicked.connect(self.click_dataset_copy)
        self.button_dataset2.setStyleSheet("background:#0e172c; border-radius: 5px; min-width: 300px; min-height: 100px;")
        
        self.button_rating1 = QPushButton('1', self)
        self.button_rating1.setStyleSheet("background:#0e172c; border-radius: 5px; min-width: 150px; min-height: 70px;")

        self.button_rating2 = QPushButton('2', self)
        self.button_rating2.setStyleSheet("background:#0e172c; border-radius: 5px; min-width: 150px; min-height: 70px;")
        self.button_rating3 = QPushButton('3', self)
        self.button_rating3.setStyleSheet("background:#0e172c; border-radius: 5px; min-width: 150px; min-height: 70px;")
        self.button_rating4 = QPushButton('4', self)
        self.button_rating4.setStyleSheet("background:#0e172c; border-radius: 5px; min-width: 150px; min-height: 70px;")
        self.button_rating5 = QPushButton('5', self)
        self.button_rating5.setStyleSheet("background:#0e172c; border-radius: 5px; min-width: 150px; min-height: 70px;")
        
        
        self.review_label = ScrollLabel(self)
        self.review_label.setStyleSheet("background:#d9d4e7;  border: 5px solid #0e172c")
        
        
        layout = QGridLayout()
        self.setLayout(layout)
        
        layout.addWidget(self.button, 0, 0)
        layout.addWidget(self.button_dataset, 0, 1, 1, 3)
        layout.addWidget(self.button_dataset2, 0, 4)
        layout.addWidget(self.review_label, 1, 0, 3, 5)
        
        layout.addWidget(self.button_rating1, 5, 0)
        layout.addWidget(self.button_rating2, 5, 1)
        layout.addWidget(self.button_rating3, 5, 2)
        layout.addWidget(self.button_rating4, 5, 3)
        layout.addWidget(self.button_rating5, 5, 4)
        
        # self.setGeometry(300, 300, 1200, 200)
        self.show()

    def click_csv(self):
        dialog = QDialog(self)
        dialog.setWindowTitle('Create file CSV')
        dialog.setFixedSize(300, 100)
        path_label = QLabel("Choose path:", dialog)
        path_label.setStyleSheet('color: #0e172c')
        self.folderpath = 'введите путь'
        self.path_line_edit = QLineEdit(dialog)
        self.path_line_edit.setEnabled(False)
        self.path_line_edit.setStyleSheet("background:#f9f8fc; border-radius: 5px; color: #0e172c;")
        
        browse_button = QPushButton("Browse", dialog)
        browse_button.clicked.connect(self.select_folder)
        browse_button.setStyleSheet("background:#0e172c; border-radius: 5px;")
        browse_button.adjustSize()
        
        create_button = QPushButton("Сreate CSV", dialog)
        create_button.setStyleSheet("background:#0e172c; border-radius: 5px;")
        create_button.clicked.connect(self.click_create_csv1)
        create_button.adjustSize()
        
        
        layout = QVBoxLayout()
        layout.addWidget(path_label)
        layout.addWidget(self.path_line_edit)
        layout.addWidget(browse_button)
        layout.addWidget(create_button)
        dialog.setLayout(layout)

        dialog.exec_()


    def select_folder(self):
        self.folderpath = (QFileDialog.getExistingDirectory(self, 'Select Folder')).replace('/', '\\')
        self.path_line_edit.setText(self.folderpath)

    def create_dataset_copy(self):
        task_2.copy_info(self.folderpath)
    
    def create_dataset_copy2(self):
        print('asdas')
        task_3.run3(self.folderpath)
        
    def click_dataset(self):
        dialog = QDialog(self)
        dialog.setWindowTitle('Create dataset_copy')
        dialog.setFixedSize(350, 130)
        path_label = QLabel("Choose path:", dialog)
        path_label.setStyleSheet('color: #0e172c')
        self.folderpath = ''
        self.path_line_edit = QLineEdit(dialog)
        self.path_line_edit.setEnabled(False)
        self.path_line_edit.setStyleSheet("background:#f9f8fc; border-radius: 5px; color: #0e172c;")
        
        browse_button = QPushButton("Browse", dialog)
        browse_button.clicked.connect(self.select_folder)
        browse_button.setStyleSheet("background:#0e172c; border-radius: 5px;")
        browse_button.adjustSize()
        
        dataset_button = QPushButton("Сreate dataset", dialog)
        dataset_button.setStyleSheet("background:#0e172c; border-radius: 5px;")
        dataset_button.clicked.connect(self.create_dataset_copy)
        dataset_button.adjustSize()
        
        create_button = QPushButton("Сreate CSV", dialog)
        create_button.setStyleSheet("background:#0e172c; border-radius: 5px;")
        create_button.clicked.connect(self.click_create_csv2)
        create_button.adjustSize()
        
        
        layout = QVBoxLayout()
        layout.addWidget(path_label)
        layout.addWidget(self.path_line_edit)
        layout.addWidget(browse_button)
        layout.addWidget(create_button)
        layout.addWidget(dataset_button)
        dialog.setLayout(layout)

        dialog.exec_()
        
        
    def click_dataset_copy(self):
        dialog = QDialog(self)
        dialog.setWindowTitle('Create dataset_copy3')
        dialog.setFixedSize(350, 130)
        path_label = QLabel("Choose path:", dialog)
        path_label.setStyleSheet('color: #0e172c')
        self.folderpath = ''
        self.path_line_edit = QLineEdit(dialog)
        self.path_line_edit.setEnabled(False)
        self.path_line_edit.setStyleSheet("background:#f9f8fc; border-radius: 5px; color: #0e172c;")
        
        browse_button = QPushButton("Browse", dialog)
        browse_button.clicked.connect(self.select_folder)
        browse_button.setStyleSheet("background:#0e172c; border-radius: 5px;")
        browse_button.adjustSize()
        
        dataset_button = QPushButton("Сreate dataset", dialog)
        dataset_button.setStyleSheet("background:#0e172c; border-radius: 5px;")
        dataset_button.clicked.connect(self.create_dataset_copy2)
        dataset_button.adjustSize()
        
        create_button = QPushButton("Сreate CSV", dialog)
        create_button.setStyleSheet("background:#0e172c; border-radius: 5px;")
        create_button.clicked.connect(self.click_create_csv2)
        create_button.adjustSize()
        
        
        layout = QVBoxLayout()
        layout.addWidget(path_label)
        layout.addWidget(self.path_line_edit)
        layout.addWidget(browse_button)
        layout.addWidget(create_button)
        layout.addWidget(dataset_button)
        dialog.setLayout(layout)

        dialog.exec_()
        
    def click_create_csv1(self):
        if 'dataset' in self.folderpath:
            run1(self.folderpath)
        else:
            ErrorMessageBox(self, "Please choose directory with dataset")
            
    def click_create_csv2(self):
        if 'dataset' in self.folderpath:
            task_2.run2()
        else:
            ErrorMessageBox(self, "Please choose directory with dataset")
            


class ErrorMessageBox:
    def __init__(self, parent, text:str):
        message_box = QMessageBox(parent)
        message_box.setText(text)
        ok_button = message_box.addButton(QMessageBox.Ok)
        ok_button.setStyleSheet("background:#0e172c; border-radius: 5px; min-width: 100px;")
        message_box.setStyleSheet('color: #0e172c')
        message_box.exec_()
  
        
def application(): 
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
    
    
if __name__ == '__main__':
    application() 