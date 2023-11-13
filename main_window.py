import sys
import os

import task_2
import task_3
import task_5

from task_1 import run1

from PyQt5.QtWidgets import (QMessageBox, QFileDialog, QWidget, QLabel, QApplication, QPushButton,
                             QToolTip, QVBoxLayout, QGridLayout, QScrollArea, QDialog, QLineEdit)
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import Qt


class ScrollLabel(QScrollArea):
    def __init__(self, *args, **kwargs) -> None:
        """
            Сreates a window for viewing reviews

            Returns:
            None
        """
        QScrollArea.__init__(self, *args, **kwargs)
        self.setWidgetResizable(True)
        text = QWidget(self)
        self.setWidget(text)
        lay = QVBoxLayout(text)
        self.label = QLabel(text)
        self.label.setWordWrap(True)
        lay.addWidget(self.label)
        self.label.setFont(QFont("SansSerif", 18))

    def setText(self, text: str) -> None:
        """
        Sets the text

        Args:
            text (str): _description_

        Returns:
        None

        """
        self.label.setText(text)


class ErrorMessageBox:
    def __init__(self, parent: QWidget, text: str) -> None:
        """
        Args:
            parent (QWidget): the main class for creating an error window
            text (str): error text

            Creates an error window

            Returns:
            None
        """
        print(type(parent))
        message_box = QMessageBox(parent)
        message_box.setText(text)
        ok_button = message_box.addButton(QMessageBox.Ok)
        ok_button.setStyleSheet(
            "background:#0e172c; border-radius: 5px; min-width: 100px;")
        message_box.setStyleSheet('color: #0e172c')
        message_box.exec_()


class Example(QWidget):

    def __init__(self) -> None:
        """
            Creates a base window

            Returns:
            None
        """

        super().__init__()
        self.initUI()
        self.setStyleSheet(
            "background:#fec7d7; color: #fffffe; font-weight:bold; border-radius: 5px;")

    def initUI(self) -> None:
        """
            Design designer

            Returns:
            None
        """
        QToolTip.setFont(QFont('SansSerif', 10))
        self.setWindowTitle('6212 - lab3')
        self.setWindowIcon(QIcon('home.png'))

        self.button = QPushButton('Create CSV-Dataset', self)
        self.button.clicked.connect(self.click_csv)
        self.button.setStyleSheet(
            "background:#0e172c; border-radius: 5px; min-width: 300px; min-height: 100px;")

        self.button_dataset = QPushButton('Create Dataset-Copy', self)
        self.button_dataset.clicked.connect(self.click_dataset)
        self.button_dataset.setStyleSheet(
            "background:#0e172c; border-radius: 5px; min-width: 300px; min-height: 100px;")

        self.button_dataset2 = QPushButton('Create Dataset-Copy2', self)
        self.button_dataset2.clicked.connect(self.click_dataset_copy)
        self.button_dataset2.setStyleSheet(
            "background:#0e172c; border-radius: 5px; min-width: 300px; min-height: 100px;")

        self.button_rating1 = QPushButton('1', self)
        self.button_rating1.setStyleSheet(
            "background:#0e172c; border-radius: 5px; min-width: 150px; min-height: 70px;")
        self.button_rating1.clicked.connect(self.get_next_review_1)

        self.button_rating2 = QPushButton('2', self)
        self.button_rating2.setStyleSheet(
            "background:#0e172c; border-radius: 5px; min-width: 150px; min-height: 70px;")
        self.button_rating2.clicked.connect(self.get_next_review_2)

        self.button_rating3 = QPushButton('3', self)
        self.button_rating3.setStyleSheet(
            "background:#0e172c; border-radius: 5px; min-width: 150px; min-height: 70px;")
        self.button_rating3.clicked.connect(self.get_next_review_3)

        self.button_rating4 = QPushButton('4', self)
        self.button_rating4.setStyleSheet(
            "background:#0e172c; border-radius: 5px; min-width: 150px; min-height: 70px;")
        self.button_rating4.clicked.connect(self.get_next_review_4)

        self.button_rating5 = QPushButton('5', self)
        self.button_rating5.setStyleSheet(
            "background:#0e172c; border-radius: 5px; min-width: 150px; min-height: 70px;")
        self.button_rating5.clicked.connect(self.get_next_review_5)

        self.review = ScrollLabel(self)
        self.review.setStyleSheet("background:#d9d4e7; color: #0e172c;")

        layout = QGridLayout()
        self.setLayout(layout)

        layout.addWidget(self.button_dataset, 0, 0)
        layout.addWidget(self.button, 0, 1, 1, 3)
        layout.addWidget(self.button_dataset2, 0, 4)
        layout.addWidget(self.review, 1, 0, 3, 5)

        layout.addWidget(self.button_rating1, 5, 0)
        layout.addWidget(self.button_rating2, 5, 1)
        layout.addWidget(self.button_rating3, 5, 2)
        layout.addWidget(self.button_rating4, 5, 3)
        layout.addWidget(self.button_rating5, 5, 4)

        self.show()

    def get_next_review_1(self) -> None:
        """
            Iterates reviews, rating 1

            Returns:
            None
        """
        try:
            with open(next(self.rating_iter1), 'r', encoding='utf-8') as file:
                self.review.setText(''.join(file.readlines()))
        except StopIteration:
            self.rating_iter1 = task_5.Iterator1(self.folderpath, str(1))
            ErrorMessageBox(self, 'something went wrong')

    def get_next_review_2(self) -> None:
        """
            Iterates reviews, rating 2

            Returns:
            None
        """
        try:
            with open(next(self.rating_iter2), 'r', encoding='utf-8') as file:
                self.review.setText(''.join(file.readlines()))
        except StopIteration:
            self.rating_iter2 = task_5.Iterator1(self.folderpath, str(2))
            ErrorMessageBox(self, 'something went wrong')

    def get_next_review_3(self) -> None:
        """
            Iterates reviews, rating 3

            Returns:
            None
        """
        try:
            with open(next(self.rating_iter3), 'r', encoding='utf-8') as file:
                self.review.setText(''.join(file.readlines()))
        except StopIteration:
            self.rating_iter3 = task_5.Iterator1(self.folderpath, str(3))
            ErrorMessageBox(self, 'something went wrong')

    def get_next_review_4(self) -> None:
        """
            Iterates reviews, rating 4

            Returns:
            None
        """
        try:
            with open(next(self.rating_iter4), 'r', encoding='utf-8') as file:
                self.review.setText(''.join(file.readlines()))
        except StopIteration:
            self.rating_iter4 = task_5.Iterator1(self.folderpath, str(4))
            ErrorMessageBox(self, 'something went wrong')

    def get_next_review_5(self) -> None:
        """
            Iterates reviews, rating 5

            Returns:
            None
        """
        try:
            with open(next(self.rating_iter5), 'r', encoding='utf-8') as file:
                self.review.setText(''.join(file.readlines()))
        except StopIteration:
            self.rating_iter5 = task_5.Iterator1(self.folderpath, str(5))
            ErrorMessageBox(self, 'something went wrong')

    def click_csv(self) -> None:
        """
            Creates a window for creating a csv file

            Returns:
            None
        """
        dialog = QDialog(self)
        dialog.setWindowTitle('Create file CSV')
        dialog.setFixedSize(300, 100)
        path_label = QLabel("Choose path:", dialog)
        path_label.setStyleSheet('color: #0e172c')
        self.folderpath = 'Введите путь'
        self.path_line_edit = QLineEdit(dialog)
        self.path_line_edit.setEnabled(False)
        self.path_line_edit.setStyleSheet(
            "background:#f9f8fc; border-radius: 5px; color: #0e172c;")

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

    def select_folder(self) -> None:
        """
            Saving the path for the folder.

            Returns:
            None
        """
        self.folderpath = (QFileDialog.getExistingDirectory(
            self, 'Select Folder')).replace('/', '\\')
        self.path_line_edit.setText(self.folderpath)
        if 'dataset' in self.folderpath:
            self.rating_iter1 = task_5.Iterator1(self.folderpath, str(1))
            self.rating_iter2 = task_5.Iterator1(self.folderpath, str(2))
            self.rating_iter3 = task_5.Iterator1(self.folderpath, str(3))
            self.rating_iter4 = task_5.Iterator1(self.folderpath, str(4))
            self.rating_iter5 = task_5.Iterator1(self.folderpath, str(5))
        else:
            ErrorMessageBox(self, "Please choose directory with dataset")

    def select_save_folder(self) -> None:
        """
            Saving the path for the folder where we will save the new dataset

            Returns:
            None
        """
        self.save_folderpath = (QFileDialog.getExistingDirectory(
            self, 'Select Folder')).replace('/', '\\')
        self.path_save_line_edit.setText(self.save_folderpath)

    def create_dataset_copy(self) -> None:
        """
            Сreates a folder

            Returns:
            None
        """
        if 'dataset' in self.folderpath:
            task_2.copy_info(self.folderpath, self.save_folderpath)
        else:
            ErrorMessageBox(self, "Please choose directory with dataset")

    def create_dataset_copy2(self) -> None:
        """
            Creates a dataset copy version 2

            Returns:
            None
        """
        if 'dataset' in self.folderpath:
            task_3.run3(self.folderpath, self.save_folderpath)
        else:
            ErrorMessageBox(self, "Please choose directory with dataset")

    def click_dataset(self) -> None:
        """
            Creates a window for creating a copy of the dataset

            Returns:
            None
        """
        dialog = QDialog(self)
        dialog.setWindowTitle('Create dataset_copy')
        dialog.setFixedSize(350, 150)
        path_label = QLabel("Choose path:", dialog)
        path_label.setStyleSheet('color: #0e172c')
        self.folderpath = ''
        self.path_line_edit = QLineEdit(dialog)
        self.path_line_edit.setEnabled(False)
        self.path_line_edit.setStyleSheet(
            "background:#f9f8fc; border-radius: 5px; color: #0e172c;")

        self.path_save_line_edit = QLineEdit(dialog)
        self.path_save_line_edit.setEnabled(False)
        self.path_save_line_edit.setStyleSheet(
            "background:#f9f8fc; border-radius: 5px; color: #0e172c;")

        browse_button = QPushButton("Browse", dialog)
        browse_button.clicked.connect(self.select_folder)
        browse_button.setStyleSheet("background:#0e172c; border-radius: 5px;")
        browse_button.adjustSize()

        browse_save_button = QPushButton("Browse path to save", dialog)
        browse_save_button.clicked.connect(self.select_save_folder)
        browse_save_button.setStyleSheet(
            "background:#0e172c; border-radius: 5px;")
        browse_save_button.adjustSize()

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
        layout.addWidget(self.path_save_line_edit)
        layout.addWidget(browse_save_button)
        layout.addWidget(browse_button)
        layout.addWidget(create_button)
        layout.addWidget(dataset_button)
        dialog.setLayout(layout)

        dialog.exec_()

    def click_dataset_copy(self) -> None:
        """
            Creates a window for creating a copy of the dataset copy

            Returns:
            None
        """
        dialog = QDialog(self)
        dialog.setWindowTitle('Create dataset_copy3')
        dialog.setFixedSize(350, 130)
        path_label = QLabel("Choose path:", dialog)
        path_label.setStyleSheet('color: #0e172c')
        self.folderpath = ''
        self.path_line_edit = QLineEdit(dialog)
        self.path_line_edit.setEnabled(False)
        self.path_line_edit.setStyleSheet(
            "background:#f9f8fc; border-radius: 5px; color: #0e172c;")

        self.path_save_line_edit = QLineEdit(dialog)
        self.path_save_line_edit.setEnabled(False)
        self.path_save_line_edit.setStyleSheet(
            "background:#f9f8fc; border-radius: 5px; color: #0e172c;")

        browse_button = QPushButton("Browse", dialog)
        browse_button.clicked.connect(self.select_folder)
        browse_button.setStyleSheet("background:#0e172c; border-radius: 5px;")
        browse_button.adjustSize()

        browse_save_button = QPushButton("Browse path to save", dialog)
        browse_save_button.clicked.connect(self.select_save_folder)
        browse_save_button.setStyleSheet(
            "background:#0e172c; border-radius: 5px;")
        browse_save_button.adjustSize()

        dataset_button = QPushButton("Сreate dataset and CSV", dialog)
        dataset_button.setStyleSheet("background:#0e172c; border-radius: 5px;")
        dataset_button.clicked.connect(self.create_dataset_copy2)
        dataset_button.adjustSize()

        layout = QVBoxLayout()
        layout.addWidget(path_label)
        layout.addWidget(self.path_line_edit)
        layout.addWidget(self.path_save_line_edit)
        layout.addWidget(browse_save_button)
        layout.addWidget(browse_button)
        layout.addWidget(dataset_button)
        dialog.setLayout(layout)

        dialog.exec_()

    def click_create_csv1(self) -> None:
        """
            A csv file is being created

            Returns:
            None
        """
        if 'dataset' in self.folderpath:
            run1(self.folderpath)
        else:
            ErrorMessageBox(self, "Please choose directory with dataset")

    def click_create_csv2(self) -> None:
        """
            A csv copy file is being created

            Returns:
            None
        """
        if 'dataset' in self.folderpath:
            task_2.run2()
        else:
            ErrorMessageBox(self, "Please choose directory with dataset")


def application() -> None:
    """
        Сreates a base window

        Returns:
        None
    """
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    application()
