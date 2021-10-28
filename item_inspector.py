from PySide6.QtWidgets import (QMainWindow, QTextEdit, QLineEdit,
QDockWidget, QCheckBox, QVBoxLayout, QWidget, QPushButton, QLabel, QSizePolicy, QTableWidget,
QTableWidgetItem, QHBoxLayout, QStackedLayout, QButtonGroup, QRadioButton)
from PySide6.QtCore import Qt, QTimer,QRunnable, Slot, Signal, QObject, QThread
from PySide6.QtGui import QAction
from ssl import CERT_NONE
from time import sleep
from sys import exit, argv


class ItemInspectorWidget(QWidget):
    def __init__(self, warehouse, itemCatalogWidget):
        super().__init__()
        self.itemCatalogWidget = itemCatalogWidget
        self.currentItemName = None
        self.warehouse = warehouse
        layout = QVBoxLayout()
        self.setMaximumSize(375, 1000)

        self.titleLbl = QLabel("Selected Item: " + str(self.currentItemName))
        self.titleLbl.setMaximumHeight(50)

        self.containerEdit = QLineEdit()
        self.containerEdit.setPlaceholderText("Container name")

        self.addItemBtn = QPushButton("Manually add sub-item")
        self.addItemBtn.clicked.connect(self.try_add_item)

        self.errorLbl = QLabel("")
        self.errorLbl.setMaximumHeight(50)
        self.errorLbl.setStyleSheet("color: red;")

        layout.addWidget(self.titleLbl)
        layout.addWidget(self.containerEdit)
        layout.addWidget(self.addItemBtn)
        layout.addWidget(self.errorLbl)

        layout.setContentsMargins(30, 30, 30, 30)

        self.setLayout(layout)


        #self.addStretch(1)

    def update_item(self, itemName):
        self.currentItemName = itemName
        self.titleLbl.setText("Selected Item: " + str(self.currentItemName))

    def try_add_item(self):
        if len(self.containerEdit.text()) > 0 and self.currentItemName != None:
            barcode = self.warehouse.create_sub_item(self.currentItemName, self.containerEdit.text())
            self.errorLbl.setStyleSheet("color: green;")
            self.errorLbl.setText('Barcode: ' + barcode + ' successfully added to database.')
            self.containerEdit.clear()
            self.itemCatalogWidget.normal_refresh_item_table()
        else:
            self.errorLbl.setStyleSheet("color: red;")
            self.errorLbl.setText('One or more fields are empty. Cannot add item.')
