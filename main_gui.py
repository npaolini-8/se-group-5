from PySide6.QtWidgets import (QMainWindow, QTextEdit, QLineEdit,
QDockWidget, QCheckBox, QVBoxLayout, QWidget, QPushButton, QLabel, QSizePolicy, QTableWidget,
QTableWidgetItem, QHBoxLayout, QStackedLayout, QButtonGroup, QRadioButton)
from PySide6.QtCore import Qt, QTimer,QRunnable, Slot, Signal, QObject, QThread
from PySide6.QtGui import QAction
from ssl import CERT_NONE
from time import sleep
from sys import exit, argv
from database_funcs import Warehouse
from utils import WorkerSignals, Worker
from login_gui import LoginMainWindow
from item_catalog import ItemCatalogWidget

#Main gui that holds all gui elements
class MainWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.warehouse = app.warehouse
        self.init_window_props() #Set window title, dimensions, location
        self.init_central_widget()
        self.init_dock_widgets()
        self.init_menu()

    def try_add_item(self):
        if len(self.idEdit.text()) > 0 and len(self.modelNumberEdit.text()) > 0 and len(self.brandEdit.text()) > 0 and len(self.descriptionEdit.toPlainText()) > 0:
            if self.warehouse.find_item(self.idEdit.text()) == None:  #If item id doesn't already exist
                self.warehouse.create_main_item(self.idEdit.text(), self.descriptionEdit.toPlainText(), self.modelNumberEdit.text(), self.brandEdit.text())
                self.errorLbl.setStyleSheet("color: green;")
                self.errorLbl.setText(self.idEdit.text() + ' successfully added to database.')
                self.idEdit.clear()
                self.modelNumberEdit.clear()
                self.brandEdit.clear()
                self.descriptionEdit.clear()
                self.refresh_item_table()
            else:
                self.errorLbl.setStyleSheet("color: red;")
                self.errorLbl.setText(self.idEdit.text() + ' already exists. Cannot add item.')
        else:
            self.errorLbl.setStyleSheet("color: red;")
            self.errorLbl.setText('One or more fields are empty. Cannot add item.')

    def init_central_widget(self):
        layout = QVBoxLayout()
        addItemBtn = QPushButton("Add Item to Database")
        addItemBtn.clicked.connect(self.try_add_item)
        #Username and Password LineEdits
        self.idEdit = QLineEdit()
        self.idEdit.setPlaceholderText("_id")
        self.modelNumberEdit = QLineEdit()
        self.modelNumberEdit.setPlaceholderText("Model Number")
        self.brandEdit = QLineEdit()
        self.brandEdit.setPlaceholderText("Brand")
        self.descriptionEdit = QTextEdit()
        self.descriptionEdit.setPlaceholderText("Description")
        self.errorLbl = QLabel("")
        self.errorLbl.setMaximumHeight(50)
        self.errorLbl.setStyleSheet("color: red;")

        layout.addWidget(self.errorLbl)
        layout.addWidget(addItemBtn)
        layout.addWidget(self.idEdit)
        layout.addWidget(self.modelNumberEdit)
        layout.addWidget(self.brandEdit)
        layout.addWidget(self.descriptionEdit)
        layout.addStretch(1)
        container_widget = QWidget()
        container_widget.setLayout(layout)
        self.setCentralWidget(container_widget)


    def init_dock_widgets(self):
        #Place item catalog widget on bottom dock
        self.itemCatalog = ItemCatalogWidget("Item Catalog", self.warehouse)
        self.addDockWidget(Qt.BottomDockWidgetArea, self.itemCatalog)
        self.resizeDocks([self.itemCatalog], [self.dimensions[1] * 0.45], Qt.Vertical)


    def init_window_props(self):
        self.setWindowTitle('Warehouse System Control Panel')
        geometry = self.screen().availableGeometry()
        self.dimensions = (geometry.width() * 0.6, geometry.height() * 0.6)
        self.resize(self.dimensions[0], self.dimensions[1])
        self.move((geometry.width() - self.dimensions[0]) / 2, (geometry.height() - self.dimensions[1]) / 2)

    def bottomDockInvert(self):
        self.bottomDockWidget.setVisible(not self.bottomDockWidget.isVisible())

    def init_menu(self):
        file = self.menuBar().addMenu("File")
        edit = self.menuBar().addMenu("Edit")
        view = self.menuBar().addMenu("View")

        bottomDockAction = QAction("Item catalog", self)
        bottomDockAction.setStatusTip("Pane to browse item list")
        bottomDockAction.setCheckable(True)
        bottomDockAction.triggered.connect(self.bottomDockInvert)
        view.addAction(bottomDockAction)
