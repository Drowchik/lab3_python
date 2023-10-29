import sys
import os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont, QIcon
from task_1 import run1
import task_2 
import task_3

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
        self.button.move(50, 50)
        self.button.adjustSize()
        self.button.clicked.connect(self.click_csv)
        self.button.setStyleSheet("background:#0e172c; border-radius: 5px; min-width: 300px;")
        
        self.button_dataset = QPushButton('Create Dataset-Copy', self)
        self.button_dataset.move(450, 50)
        self.button_dataset.adjustSize()
        self.button_dataset.clicked.connect(self.click_dataset)
        self.button_dataset.setStyleSheet("background:#0e172c; border-radius: 5px; min-width: 300px;")
        
        
        self.button_dataset2 = QPushButton('Create Dataset-Copy2', self)
        self.button_dataset2.move(850, 50)
        self.button_dataset2.adjustSize()
        self.button_dataset2.clicked.connect(self.click_dataset)
        self.button_dataset2.setStyleSheet("background:#0e172c; border-radius: 5px; min-width: 300px;")
        
        self.setGeometry(300, 300, 1200, 200)
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
        create_button.clicked.connect(self.click_create_csv)
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
        create_button.clicked.connect(self.click_create_csv)
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
        create_button.clicked.connect(self.click_create_csv)
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
            task_2.run2(self.folderpath)
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

    sys.exit(app.exec_())
    
    
if __name__ == '__main__':
    application() 