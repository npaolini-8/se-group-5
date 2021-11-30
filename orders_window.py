# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'orders_windowrizmNZ.ui'
##
## Created by: Qt User Interface Compiler version 6.2.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QGroupBox, QHeaderView,
    QLCDNumber, QPushButton, QRadioButton, QSizePolicy,
    QTableWidget, QTableWidgetItem)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(800, 600)
        self.return_btn = QPushButton(Dialog)
        self.return_btn.setObjectName(u"return_btn")
        self.return_btn.setGeometry(QRect(10, 10, 121, 34))
        self.complete_btn = QPushButton(Dialog)
        self.complete_btn.setObjectName(u"complete_btn")
        self.complete_btn.setGeometry(QRect(10, 520, 251, 71))
        self.groupBox = QGroupBox(Dialog)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 50, 251, 461))
        self.orders_tbl = QTableWidget(self.groupBox)
        self.orders_tbl.setObjectName(u"orders_tbl")
        self.orders_tbl.setGeometry(QRect(0, 20, 251, 441))
        font = QFont()
        font.setPointSize(8)
        self.orders_tbl.setFont(font)
        self.in_radio = QRadioButton(self.groupBox)
        self.in_radio.setObjectName(u"in_radio")
        self.in_radio.setGeometry(QRect(70, 0, 81, 20))
        self.in_radio.setChecked(True)
        self.out_radio = QRadioButton(self.groupBox)
        self.out_radio.setObjectName(u"out_radio")
        self.out_radio.setGeometry(QRect(160, 0, 91, 20))
        self.groupBox_2 = QGroupBox(Dialog)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(290, 50, 251, 461))
        self.items_tbl = QTableWidget(self.groupBox_2)
        self.items_tbl.setObjectName(u"items_tbl")
        self.items_tbl.setGeometry(QRect(0, 20, 251, 441))
        self.items_tbl.setFont(font)
        self.groupBox_3 = QGroupBox(Dialog)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(580, 50, 201, 451))
        self.barcodes_tbl = QTableWidget(self.groupBox_3)
        self.barcodes_tbl.setObjectName(u"barcodes_tbl")
        self.barcodes_tbl.setGeometry(QRect(0, 20, 201, 431))
        self.barcodes_tbl.setFont(font)
        self.groupBox_4 = QGroupBox(Dialog)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(550, 510, 231, 81))
        self.minus_btn = QPushButton(self.groupBox_4)
        self.minus_btn.setObjectName(u"minus_btn")
        self.minus_btn.setGeometry(QRect(0, 20, 61, 61))
        font1 = QFont()
        font1.setPointSize(36)
        self.minus_btn.setFont(font1)
        self.lcd_count = QLCDNumber(self.groupBox_4)
        self.lcd_count.setObjectName(u"lcd_count")
        self.lcd_count.setGeometry(QRect(60, 20, 111, 61))
        self.lcd_count.setMode(QLCDNumber.Dec)
        self.lcd_count.setSegmentStyle(QLCDNumber.Flat)
        self.plus_btn = QPushButton(self.groupBox_4)
        self.plus_btn.setObjectName(u"plus_btn")
        self.plus_btn.setGeometry(QRect(170, 20, 61, 61))
        font2 = QFont()
        font2.setPointSize(28)
        self.plus_btn.setFont(font2)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.return_btn.setText(QCoreApplication.translate("Dialog", u"Return", None))
        self.complete_btn.setText(QCoreApplication.translate("Dialog", u"Complete Order", None))
        self.groupBox.setTitle(QCoreApplication.translate("Dialog", u"Pending", None))
        self.in_radio.setText(QCoreApplication.translate("Dialog", u"Incoming", None))
        self.out_radio.setText(QCoreApplication.translate("Dialog", u"Outgoing", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Dialog", u"Items in Order", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Dialog", u"Barcodes", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("Dialog", u"Items Present", None))
        self.minus_btn.setText(QCoreApplication.translate("Dialog", u"-", None))
        self.plus_btn.setText(QCoreApplication.translate("Dialog", u"+", None))
    # retranslateUi




    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.return_btn.setText(QCoreApplication.translate("Dialog", u"Return", None))
        self.complete_btn.setText(QCoreApplication.translate("Dialog", u"Complete Order", None))
        self.groupBox.setTitle(QCoreApplication.translate("Dialog", u"Pending", None))
        self.in_radio.setText(QCoreApplication.translate("Dialog", u"Incoming", None))
        self.out_radio.setText(QCoreApplication.translate("Dialog", u"Outgoing", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Dialog", u"Items in Order", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Dialog", u"Barcodes", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("Dialog", u"Items Present", None))
        self.minus_btn.setText(QCoreApplication.translate("Dialog", u"-", None))
        self.plus_btn.setText(QCoreApplication.translate("Dialog", u"+", None))
    # retranslateUi

from PySide6.QtWidgets import QAbstractItemView


class OrdersWindow(QDialog):
    def __init__(self, warehouse_controller):
        super(OrdersWindow, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.warehouse_controller = warehouse_controller
        self.init_buttons()
        self.init_tables()

    def init_buttons(self):
        self.ui.return_btn.clicked.connect(self.return_clicked)

    def init_table(self, table, col_labels):
        col_count = len(col_labels)
        table.setColumnCount(col_count)
        table.verticalHeader().setVisible(False)
        table.setHorizontalHeaderLabels(col_labels)
        table.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        table.setSelectionMode(QAbstractItemView.SingleSelection)

        table.setSortingEnabled(True)





    def init_tables(self):
        self.init_table(self.ui.orders_tbl, ['Order', 'Client', 'Number of Items'])
        header = self.ui.orders_tbl.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.Stretch)
        header.setSectionResizeMode(1, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QHeaderView.ResizeToContents)

        self.init_table(self.ui.items_tbl, ['Item', 'Count', 'Added', 'Done'])
        header = self.ui.items_tbl.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.Stretch)
        header.setSectionResizeMode(1, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(3, QHeaderView.ResizeToContents)

        self.init_table(self.ui.barcodes_tbl, ['Barcode', 'Added?'])
        header = self.ui.barcodes_tbl.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.Stretch)
        header.setSectionResizeMode(1, QHeaderView.ResizeToContents)




    def get_order_type(self):
        pass

    def get_client(self):
        pass

    def return_clicked(self):
        self.warehouse_controller.switch_to(self, 'main')
