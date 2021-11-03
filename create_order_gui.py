# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitledAwbIwJ.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

import sys
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QDialog, QApplication
from PyQt6.uic import loadUi
from database_funcs import Warehouse

warehouse = Warehouse()

class CreateOrder(QDialog):
    def __init__(self):
        super(CreateOrder, self).__init__()
        self.ui = loadUi("create_order.ui", self)
        self.create_order_btn.clicked.connect(self.create_order_click)
        self.order_id = ""

    def create_order_click(self):
        order_type = self.order_type_cb.currentText()
        client = self.client_tb.text()
        status = 'Pending'
        self.order_id = warehouse.create_order(order_type, client, status)
        self.move_to_screen_addtocart()

    def move_to_screen_addtocart(self):
        addtocart = AddToCart(self.order_id)
        widget.addWidget(addtocart)
        widget.setCurrentIndex(widget.currentIndex()+1)

class AddToCart(QDialog):
    def __init__(self, order_id):
        self.order_id = order_id
        super(AddToCart, self).__init__()
        self.ui = loadUi("add_to_order.ui", self)
        self.add_to_order_btn.clicked.connect(self.add_to_order_click)

    def add_to_order_click(self):
        item_name = self.item_name_tb.text()
        count = self.count_sb.value()
        warehouse.add_to_order(self.order_id, item_name, count)


app = QApplication(sys.argv)
mainwindow = CreateOrder()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(300)
widget.setFixedHeight(150)
widget.show()
app.exec()