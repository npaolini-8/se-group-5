from typing import Final
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QTableWidget, QTableWidgetItem,
    QTextEdit, QVBoxLayout, QWidget, QAbstractItemView, QHeaderView)
# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'items_windowZAjOeB.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QTableWidget, QTableWidgetItem,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_ItemWindow(object):
    def setupUi(self, ItemWindow):
        if not ItemWindow.objectName():
            ItemWindow.setObjectName(u"ItemWindow")
        ItemWindow.resize(810, 600)
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ItemWindow.sizePolicy().hasHeightForWidth())
        ItemWindow.setSizePolicy(sizePolicy)
        ItemWindow.setStyleSheet(u"background-color: #295B63;")
        self.return_btn = QPushButton(ItemWindow)
        self.return_btn.setObjectName(u"return_btn")
        self.return_btn.setGeometry(QRect(10, 10, 75, 24))
        self.return_btn.setStyleSheet(u"\n"
"color: #B6E3F0;")
        self.verticalLayoutWidget = QWidget(ItemWindow)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 70, 251, 441))
        self.item_search_vlayout = QVBoxLayout(self.verticalLayoutWidget)
        self.item_search_vlayout.setObjectName(u"item_search_vlayout")
        self.item_search_vlayout.setContentsMargins(0, 0, 0, 0)
        self.item_search_line = QLineEdit(self.verticalLayoutWidget)
        self.item_search_line.setObjectName(u"item_search_line")
        self.item_search_line.setStyleSheet(u"background-color: #4395a3;\n"
"color: white;\n"
"\n"
"font-size: 12px;")

        self.item_search_vlayout.addWidget(self.item_search_line)

        self.item_table = QTableWidget(self.verticalLayoutWidget)
        self.item_table.setObjectName(u"item_table")
        self.item_table.setStyleSheet(u"background-color: #526c75;\n"
"color: #B6E3F0;\n"
"border-radius: 10px;\n"
"font-size: 12px;")

        self.item_search_vlayout.addWidget(self.item_table)

        self.verticalLayoutWidget_2 = QWidget(ItemWindow)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(270, 69, 270, 441))
        self.item_info_vlayout = QVBoxLayout(self.verticalLayoutWidget_2)
        self.item_info_vlayout.setObjectName(u"item_info_vlayout")
        self.item_info_vlayout.setContentsMargins(0, 0, 0, 0)
        self.new_item_type_btn = QPushButton(self.verticalLayoutWidget_2)
        self.new_item_type_btn.setObjectName(u"new_item_type_btn")
        self.new_item_type_btn.setStyleSheet(u"\n"
"color: #B6E3F0;\n"
"\n"
"font-size: 12px;")

        self.item_info_vlayout.addWidget(self.new_item_type_btn)

        self.edit_label = QLabel(self.verticalLayoutWidget_2)
        self.edit_label.setObjectName(u"edit_label")
        self.edit_label.setAlignment(Qt.AlignCenter)

        self.item_info_vlayout.addWidget(self.edit_label)

        self.item_name_line = QLineEdit(self.verticalLayoutWidget_2)
        self.item_name_line.setObjectName(u"item_name_line")
        self.item_name_line.setMinimumSize(QSize(0, 25))
        self.item_name_line.setStyleSheet(u"background-color: #526c75;\n"
"color: #B6E3F0;\n"
"\n"
"font-size: 12px;")

        self.item_info_vlayout.addWidget(self.item_name_line)

        self.item_desc = QTextEdit(self.verticalLayoutWidget_2)
        self.item_desc.setObjectName(u"item_desc")
        self.item_desc.setStyleSheet(u"background-color: #526c75;\n"
"color: #B6E3F0;\n"
"border-radius: 15px;\n"
"font-size: 12px;")
        self.item_desc.setCursorWidth(0)
        self.item_desc.setPlaceholderText(u"0")

        self.item_info_vlayout.addWidget(self.item_desc)

        self.item_model = QLineEdit(self.verticalLayoutWidget_2)
        self.item_model.setObjectName(u"item_model")
        self.item_model.setStyleSheet(u"background-color: #526c75;\n"
"color: #B6E3F0;\n"
"\n"
"font-size: 12px;")

        self.item_info_vlayout.addWidget(self.item_model)

        self.item_brand = QLineEdit(self.verticalLayoutWidget_2)
        self.item_brand.setObjectName(u"item_brand")
        self.item_brand.setStyleSheet(u"background-color: #526c75;\n"
"color: #B6E3F0;\n"
"\n"
"font-size: 12px;")

        self.item_info_vlayout.addWidget(self.item_brand)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.len_lbl = QLabel(self.verticalLayoutWidget_2)
        self.len_lbl.setObjectName(u"len_lbl")
        self.len_lbl.setStyleSheet(u"\n"
"color: white;\n"
"\n"
"")

        self.horizontalLayout_2.addWidget(self.len_lbl)

        self.widthLbl = QLabel(self.verticalLayoutWidget_2)
        self.widthLbl.setObjectName(u"widthLbl")
        self.widthLbl.setStyleSheet(u"color: white;")

        self.horizontalLayout_2.addWidget(self.widthLbl)

        self.depth_lbl = QLabel(self.verticalLayoutWidget_2)
        self.depth_lbl.setObjectName(u"depth_lbl")
        self.depth_lbl.setStyleSheet(u"color: white;")

        self.horizontalLayout_2.addWidget(self.depth_lbl)

        self.weight_lbl = QLabel(self.verticalLayoutWidget_2)
        self.weight_lbl.setObjectName(u"weight_lbl")
        self.weight_lbl.setStyleSheet(u"color: white;")

        self.horizontalLayout_2.addWidget(self.weight_lbl)


        self.item_info_vlayout.addLayout(self.horizontalLayout_2)

        self.item_phys_atts_hlayout = QHBoxLayout()
        self.item_phys_atts_hlayout.setObjectName(u"item_phys_atts_hlayout")
        self.item_length = QLineEdit(self.verticalLayoutWidget_2)
        self.item_length.setObjectName(u"item_length")
        self.item_length.setStyleSheet(u"background-color: #526c75;\n"
"color: #B6E3F0;\n"
"\n"
"font-size: 12px;")

        self.item_phys_atts_hlayout.addWidget(self.item_length)

        self.item_width = QLineEdit(self.verticalLayoutWidget_2)
        self.item_width.setObjectName(u"item_width")
        self.item_width.setStyleSheet(u"background-color: #526c75;\n"
"color: #B6E3F0;\n"
"\n"
"font-size: 12px;")

        self.item_phys_atts_hlayout.addWidget(self.item_width)

        self.item_depth = QLineEdit(self.verticalLayoutWidget_2)
        self.item_depth.setObjectName(u"item_depth")
        self.item_depth.setStyleSheet(u"background-color: #526c75;\n"
"color: #B6E3F0;\n"
"\n"
"font-size: 12px;")

        self.item_phys_atts_hlayout.addWidget(self.item_depth)

        self.item_weight = QLineEdit(self.verticalLayoutWidget_2)
        self.item_weight.setObjectName(u"item_weight")
        self.item_weight.setStyleSheet(u"background-color: #526c75;\n"
"color: #B6E3F0;\n"
"\n"
"font-size: 12px;")

        self.item_phys_atts_hlayout.addWidget(self.item_weight)


        self.item_info_vlayout.addLayout(self.item_phys_atts_hlayout)

        self.active_pending_lo = QHBoxLayout()
        self.active_pending_lo.setObjectName(u"active_pending_lo")
        self.active_check = QCheckBox(self.verticalLayoutWidget_2)
        self.active_check.setObjectName(u"active_check")
        self.active_check.setStyleSheet(u"\n"
"color: #B6E3F0;")

        self.active_pending_lo.addWidget(self.active_check)

        self.pending_lbl = QLabel(self.verticalLayoutWidget_2)
        self.pending_lbl.setObjectName(u"pending_lbl")
        self.pending_lbl.setStyleSheet(u"color: white;")

        self.active_pending_lo.addWidget(self.pending_lbl)

        self.pending_shipment_line = QLineEdit(self.verticalLayoutWidget_2)
        self.pending_shipment_line.setObjectName(u"pending_shipment_line")
        self.pending_shipment_line.setStyleSheet(u"background-color: #526c75;\n"
"color: #B6E3F0;\n"
"\n"
"font-size: 12px;")

        self.active_pending_lo.addWidget(self.pending_shipment_line)


        self.item_info_vlayout.addLayout(self.active_pending_lo)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.item_info_vlayout.addItem(self.verticalSpacer)

        self.error_label = QLabel(self.verticalLayoutWidget_2)
        self.error_label.setObjectName(u"error_label")
        self.error_label.setAlignment(Qt.AlignCenter)

        self.item_info_vlayout.addWidget(self.error_label)

        self.save_item_btn = QPushButton(self.verticalLayoutWidget_2)
        self.save_item_btn.setObjectName(u"save_item_btn")
        self.save_item_btn.setStyleSheet(u"\n"
"color: #B6E3F0;\n"
"\n"
"font-size: 12px;")

        self.item_info_vlayout.addWidget(self.save_item_btn)

        self.verticalLayoutWidget_3 = QWidget(ItemWindow)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(550, 70, 252, 441))
        self.barcode_info_vlayout = QVBoxLayout(self.verticalLayoutWidget_3)
        self.barcode_info_vlayout.setObjectName(u"barcode_info_vlayout")
        self.barcode_info_vlayout.setContentsMargins(0, 0, 0, 0)
        self.barcode_ops_hlayout = QHBoxLayout()
        self.barcode_ops_hlayout.setObjectName(u"barcode_ops_hlayout")
        self.barcode_count_lbl = QLineEdit(self.verticalLayoutWidget_3)
        self.barcode_count_lbl.setObjectName(u"barcode_count_lbl")
        self.barcode_count_lbl.setStyleSheet(u"background-color: #526c75;\n"
"color: #B6E3F0;\n"
"\n"
"font-size: 12px;")

        self.barcode_ops_hlayout.addWidget(self.barcode_count_lbl)

        self.new_barcode_btn = QPushButton(self.verticalLayoutWidget_3)
        self.new_barcode_btn.setObjectName(u"new_barcode_btn")
        self.new_barcode_btn.setStyleSheet(u"\n"
"color: #B6E3F0;")

        self.barcode_ops_hlayout.addWidget(self.new_barcode_btn)

        self.delete_item_btn = QPushButton(self.verticalLayoutWidget_3)
        self.delete_item_btn.setObjectName(u"delete_item_btn")
        self.delete_item_btn.setStyleSheet(u"\n"
"color: #B6E3F0;")

        self.barcode_ops_hlayout.addWidget(self.delete_item_btn)


        self.barcode_info_vlayout.addLayout(self.barcode_ops_hlayout)

        self.barcode_search_line = QLineEdit(self.verticalLayoutWidget_3)
        self.barcode_search_line.setObjectName(u"barcode_search_line")
        self.barcode_search_line.setStyleSheet(u"background-color: #4395a3;\n"
"color: white;\n"
"\n"
"font-size: 12px;")

        self.barcode_info_vlayout.addWidget(self.barcode_search_line)

        self.barcode_table = QTableWidget(self.verticalLayoutWidget_3)
        self.barcode_table.setObjectName(u"barcode_table")
        self.barcode_table.setStyleSheet(u"background-color: #526c75;\n"
"color: #B6E3F0;\n"
"border-radius: 10px;\n"
"font-size: 12px;")

        self.barcode_info_vlayout.addWidget(self.barcode_table)


        self.retranslateUi(ItemWindow)

        QMetaObject.connectSlotsByName(ItemWindow)
    # setupUi

    def retranslateUi(self, ItemWindow):
        ItemWindow.setWindowTitle(QCoreApplication.translate("ItemWindow", u"Item Manipulation", None))
        self.return_btn.setText(QCoreApplication.translate("ItemWindow", u"Return", None))
        self.item_search_line.setPlaceholderText(QCoreApplication.translate("ItemWindow", u"Search for an Item...", None))
        self.new_item_type_btn.setText(QCoreApplication.translate("ItemWindow", u"Create New Item Type", None))
        self.edit_label.setText("")
        self.item_name_line.setText("")
        self.item_name_line.setPlaceholderText(QCoreApplication.translate("ItemWindow", u"Item Name", None))
        self.item_model.setPlaceholderText(QCoreApplication.translate("ItemWindow", u"Model #", None))
        self.item_brand.setPlaceholderText(QCoreApplication.translate("ItemWindow", u"Brand", None))
        self.len_lbl.setText(QCoreApplication.translate("ItemWindow", u"Length", None))
        self.widthLbl.setText(QCoreApplication.translate("ItemWindow", u"Width", None))
        self.depth_lbl.setText(QCoreApplication.translate("ItemWindow", u"Depth", None))
        self.weight_lbl.setText(QCoreApplication.translate("ItemWindow", u"Weight", None))
        self.item_length.setPlaceholderText(QCoreApplication.translate("ItemWindow", u"Length", None))
        self.item_width.setPlaceholderText(QCoreApplication.translate("ItemWindow", u"Width", None))
        self.item_depth.setPlaceholderText(QCoreApplication.translate("ItemWindow", u"Depth", None))
        self.item_weight.setPlaceholderText(QCoreApplication.translate("ItemWindow", u"Weight", None))
        self.active_check.setText(QCoreApplication.translate("ItemWindow", u"Active Item", None))
        self.pending_lbl.setText(QCoreApplication.translate("ItemWindow", u"Pending Shipment:", None))
        self.pending_shipment_line.setPlaceholderText(QCoreApplication.translate("ItemWindow", u"Pending", None))
        self.error_label.setText("")
        self.save_item_btn.setText(QCoreApplication.translate("ItemWindow", u"Save Item Type", None))
        self.barcode_count_lbl.setText(QCoreApplication.translate("ItemWindow", u"1", None))
        self.new_barcode_btn.setText(QCoreApplication.translate("ItemWindow", u"Create New Item", None))
        self.delete_item_btn.setText(QCoreApplication.translate("ItemWindow", u"Remove Item", None))
        self.barcode_search_line.setPlaceholderText(QCoreApplication.translate("ItemWindow", u"Search for a Barcode...", None))
    # retranslateUi




class ItemsWindow(QDialog):
    new_item_string: Final = "Creating a New Item Type"

    def __init__(self, warehouse_controller):
        super(ItemsWindow, self).__init__()
        self.ui = Ui_ItemWindow()
        self.ui.setupUi(self)
        self.warehouse_controller = warehouse_controller
        self.init_buttons()
        self.init_item_table()
        self.init_barcode_table()
        self.ui.item_search_line.textChanged.connect(self.filter_items)
        self.ui.barcode_search_line.textChanged.connect(self.filter_barcodes)
        self.ui.item_table.clicked.connect(self.select_item)
        self.ui.barcode_table.clicked.connect(self.barcode_clicked)
        self.curr_barcode = ""
        self.ui.edit_label.setText(self.new_item_string)
        self.ui.active_check.setChecked(True)

    def init_buttons(self):
        self.ui.return_btn.clicked.connect(self.return_clicked)
        self.ui.new_item_type_btn.clicked.connect(self.new_item_type_clicked)
        self.ui.save_item_btn.clicked.connect(self.save_item)
        self.ui.new_barcode_btn.clicked.connect(self.new_barcode_btn_clicked)
        self.ui.delete_item_btn.clicked.connect(self.delete_item_btn_clicked)

    #hardcoded the headers, sorry!
    def init_item_table(self):
        self.ui.item_table.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.ui.item_table.setSelectionMode(QAbstractItemView.SingleSelection)

        self.refresh_items()
        #taken from tony in create_order :)
        # col_count = 0
        # headers = []

        # if len(self.items) > 0:
        #     col_count = len(self.items[0].keys())
        #     headers = self.items[0].keys()

        self.ui.item_table.setColumnCount(3)
        self.ui.item_table.setHorizontalHeaderLabels(["Item Name", "Stock", "Pending"])
        header = self.ui.item_table.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.Stretch)
        header.setSectionResizeMode(1, QHeaderView.Stretch)
        header.setSectionResizeMode(2, QHeaderView.ResizeToContents)

        self.refresh_item_table()

    def init_barcode_table(self):
        self.ui.barcode_table.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.ui.barcode_table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.ui.barcode_table.setColumnCount(2)
        self.ui.barcode_table.setHorizontalHeaderLabels(["Barcode", "Status"])
        header = self.ui.barcode_table.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QHeaderView.ResizeToContents)

    def return_clicked(self):
        self.warehouse_controller.switch_to(self, 'main')

    def refresh_items(self):
        self.items = self.warehouse_controller.get_all_items()
        self.curr_item = ""

    def refresh_item_table(self):
        self.refresh_items()
        self.ui.item_table.setRowCount(len(self.items))

        i = 0
        for item in self.items:
            # j = 0
            # for key in item.keys():
            #     self.ui.item_table.setItem(i, j, QTableWidgetItem(item[key].__str__()))
            #     j += 1

            name_item = QTableWidgetItem(item['Name'])
            stock_item = QTableWidgetItem(str(len(item['Items'])))
            pending_item = QTableWidgetItem(str(item['Pending Shipment']))
            name_item.setFlags(name_item.flags() ^ Qt.ItemIsEditable)
            stock_item.setFlags(stock_item.flags() ^ Qt.ItemIsEditable)
            pending_item.setFlags(pending_item.flags() ^ Qt.ItemIsEditable)


            self.ui.item_table.setItem( i, 0, name_item)
            self.ui.item_table.setItem( i, 1, stock_item)
            self.ui.item_table.setItem( i, 2, pending_item)
            #print(item['Pending Shipment'])


            i += 1

    def filter_items(self):
        filter_string = self.ui.item_search_line.text()

        for row in range(self.ui.item_table.rowCount()):
            if filter_string.lower() in self.ui.item_table.item(row,0).text().lower():
                filtered = False
            else:
                filtered = True
            self.ui.item_table.setRowHidden(row, filtered)

    def filter_barcodes(self):
        filter_string = self.ui.barcode_search_line.text()

        for row in range(self.ui.barcode_table.rowCount()):
            if filter_string.lower() in self.ui.barcode_table.item(row,0).text().lower():
                filtered = False
            else:
                filtered = True
            self.ui.barcode_table.setRowHidden(row, filtered)


    def select_item(self,item):
        row = item.row()

        item = self.ui.item_table.item(row,0).text()
        self.curr_item = item
        self.curr_barcode = ""
        self.ui.item_name_line.setText(item)
        self.ui.edit_label.setText("Editing: " + item)
        self.set_error("", True)
        #clear dimension fields to account for null cases
        self.ui.item_length.setText("")
        self.ui.item_width.setText("")
        self.ui.item_depth.setText("")
        self.ui.item_weight.setText("")

        for db_item in self.items:
            if db_item['Name'] == item:
                item_info = db_item
                break

        #required fields will not have keyerror checking
        self.ui.active_check.setChecked(item_info['isActive'])
        self.ui.item_desc.setText(item_info['Description'])
        self.ui.item_model.setText(item_info["Model Number"])
        self.ui.item_brand.setText(item_info['Brand'])
        self.ui.pending_shipment_line.setText(str(item_info["Pending Shipment"]))
        self.ui.pending_shipment_line.setReadOnly(False)
        self.refresh_barcode_table(item_info["Items"])

        #error checking for non-required fields, also for old data
        try:
            if item_info["Length"] is not None:
                self.ui.item_length.setText(str(item_info["Length"]))
            if item_info["Width"] is not None:
                self.ui.item_width.setText(str(item_info["Width"]))
            if item_info["Depth"] is not None:
                self.ui.item_depth.setText(str(item_info["Depth"]))
            if item_info["Weight"] is not None:
                self.ui.item_weight.setText(str(item_info["Weight"]))
        except KeyError:
            pass

    def refresh_barcode_table(self, items):
        self.ui.barcode_table.setRowCount(len(items))

        i = 0
        for item in items:
            barcode_item = QTableWidgetItem(item["Barcode"])
            status_item = QTableWidgetItem(item["Status"])
            barcode_item.setFlags(barcode_item.flags() ^ Qt.ItemIsEditable)
            status_item.setFlags(status_item.flags() ^ Qt.ItemIsEditable)
            self.ui.barcode_table.setItem(i, 0, barcode_item)
            self.ui.barcode_table.setItem(i, 1, status_item)
            i +=  1

    def clear_form(self, mode="normal"):
        self.ui.edit_label.setText(self.new_item_string)
        self.ui.item_name_line.setText("")
        self.ui.item_desc.clear()
        self.ui.item_brand.setText("")
        self.ui.item_model.setText("")
        self.ui.item_length.setText("")
        self.ui.item_width.setText("")
        self.ui.item_depth.setText("")
        self.ui.item_weight.setText("")
        self.ui.pending_shipment_line.setText("")
        self.ui.active_check.setChecked(True)
        self.ui.barcode_table.setRowCount(0)
        self.ui.error_label.setText("")

        if mode == "normal":
            self.ui.item_search_line.setText("")


    def new_item_type_clicked(self):
        if not(self.warehouse_controller.access_check("Supervisor")):
            self.set_error("Insufficient Access",False)
        else:
            self.clear_form("new")
            self.curr_item = ""
            self.curr_barcode = ""
            self.ui.edit_label.setText(self.new_item_string)
            self.ui.pending_shipment_line.setText("0")
            self.ui.pending_shipment_line.setReadOnly(True)
            self.ui.item_name_line.setFocus()

    def set_error(self,error, good):
        self.ui.error_label.setText(error)
        if good:
            self.ui.error_label.setStyleSheet("color: green;")
        else:
            self.ui.error_label.setStyleSheet("color: red;")

    def save_item(self):

        if not(self.warehouse_controller.access_check("Supervisor")):
            self.set_error("Insufficient Access",False)
        else:

            #try/catch for catching non-numerical input into dimensions/weight
            #try:
                #required fields
                item_name = self.ui.item_name_line.text()
                item_desc = self.ui.item_desc.toPlainText()
                item_model = self.ui.item_model.text()
                item_brand = self.ui.item_brand.text()
                item_active = self.ui.active_check.isChecked()

                #dimension and weight fields not required, check before casting
                #set to None to ensure type reliability in DB, dont want to set empty strings
                dim_ok = True

                item_length = self.ui.item_length.text()
                if item_length != "":
                    try:
                        item_length = float(item_length)
                    except ValueError:
                        dim_ok = False
                else:
                    item_length = None

                item_width = self.ui.item_width.text()
                if item_width != "":
                    try:
                        item_width = float(item_width)
                    except ValueError:
                        dim_ok = False
                else:
                    item_width = None

                item_depth = self.ui.item_depth.text()
                if item_depth != "":
                    try:
                        item_depth = float(item_depth)
                    except ValueError:
                        dim_ok = False
                else:
                    item_depth = None

                item_weight = self.ui.item_weight.text()
                #if item_weight is not None or item_weight != "":
                if item_weight != "":
                    try:
                        item_weight = float(item_weight)
                    except ValueError:
                        dim_ok = False
                else:
                    item_weight = None

                pending_shipment = self.ui.pending_shipment_line.text()
                if pending_shipment != "":
                    try:
                        pending_shipment = int(pending_shipment)
                    except ValueError:
                        dim_ok = False
                else:
                    pending_shipment = None


                if dim_ok == False:
                    self.set_error("Dimensions/Weight/Pending must be Numbers",False)

                #required field checks
                elif item_desc is None or item_desc == "":
                    self.set_error("Item Description Required",False)
                elif item_model is None or item_model == "":
                    self.set_error("Model Information Required",False)
                elif item_brand is None or item_brand == "":
                    self.set_error("Item Brand Required",False)
                elif item_name is None or item_name == "":
                    self.set_error("Item Name Required",False)
                elif pending_shipment == "":
                    self.set_error("Pending Shipment is required",False)
                else: #required fields correct, check cases (I think you get some duplicated code either way you do this)
                    if self.curr_item == "": #new item being created
                        if self.warehouse_controller.validate_new_item_name(item_name) != "OK":
                            self.set_error("Item Name in Use",False)
                        else: #input validated, create new item type
                            self.warehouse_controller.create_new_item(item_name,item_desc,item_model,item_brand,item_active,item_weight=item_weight,item_length=item_length,item_width=item_width,item_depth=item_depth)
                            self.clear_form()
                            self.refresh_item_table()
                            self.set_error("New Item Created: " + item_name, True)
                    else: #editing existing item, cases separated for informative messaging
                        if self.curr_item != item_name: #change item name case
                            if self.warehouse_controller.validate_new_item_name(item_name) != "OK":
                                self.set_error("Item Name in Use",False)
                            else: #new username OK
                                self.warehouse_controller.edit_item(self.curr_item,item_desc=item_desc,item_model=item_model,item_brand=item_brand,isActive=item_active,item_weight=item_weight,item_length=item_length,item_width=item_width,item_depth=item_depth, new_name=item_name,pending=pending_shipment)
                                self.clear_form()
                                self.set_error(self.curr_item + " updated to: " + item_name,True)
                                self.refresh_item_table()
                        else: #edit existing item, no item name change
                            self.warehouse_controller.edit_item(self.curr_item,item_desc=item_desc,item_model=item_model,item_brand=item_brand,isActive=item_active,item_weight=item_weight,item_length=item_length,item_width=item_width,item_depth=item_depth,pending=pending_shipment)
                            self.clear_form()
                            self.set_error(self.curr_item + " updated!",True)
                            self.refresh_item_table()


            #except ValueError:
            #    self.set_error("Dimensions and Weight must be Numbers")

    def barcode_clicked(self,barcode):
        row = barcode.row()
        self.curr_barcode = self.ui.barcode_table.item(row,0).text()

    def new_barcode_btn_clicked(self):
        if not(self.warehouse_controller.access_check("Supervisor")):
            self.set_error("Insufficient Access",False)
        else:
            if self.curr_item == "": #make sure an item is selected
                self.set_error("Select a pre-existing item type",False)
            #elif not(self.ui.barcode_count_lbl.text().isdigit()):
            elif self.warehouse_controller.parseable_int_str(self.ui.barcode_count_lbl.text()) is not True:
                self.set_error("Count must be a Non-Zero Number",False)
            else:
                #add appropriate number of subitems
                count = int(self.ui.barcode_count_lbl.text())
                for x in range(count):
                    self.warehouse_controller.create_sub_item(self.curr_item)

                #update barcode table, need to go out to the DB because of unpredictable increments
                new_barcode_list = self.warehouse_controller.get_item(self.curr_item)["Items"]
                self.refresh_barcode_table(new_barcode_list)
                #manually update item main table to reduce query frequency
                #DESYNC POTENTIAL
                row = self.find_item_in_table(self.curr_item)
                item_count = int(self.ui.item_table.item(row,1).text())
                self.ui.item_table.setItem(row,1,QTableWidgetItem(str(item_count+count))) #changed from +1
                # need to edit the stored item list to maintain consistency
                for i in range(len(self.items)):
                    if self.items[i]["Name"] == self.curr_item:
                        #barcode = self.ui.barcode_table.item(self.ui.barcode_table.rowCount()-1, 0).text()
                        #self.items[i]["Items"].append({"Barcode": barcode,"Container":None,"Status":"Available"})
                        self.items[i]["Items"] = new_barcode_list

                if count == 1:
                    self.set_error("New " + self.curr_item + " created!",True)
                else:
                    self.ui.barcode_count_lbl.setText("1")
                    self.set_error( str(count) + " new " + self.curr_item + "s created!",True)


    def find_item_in_table(self, item_name):
        index = -1
        for i in range(self.ui.item_table.rowCount()):
            if self.ui.item_table.item(i, 0).text() == item_name:
                index = i
                break
        return index

    def delete_item_btn_clicked(self):
        if not(self.warehouse_controller.access_check("Supervisor")):
            self.set_error("Insufficient Access",False)
        else:
            if self.curr_item == "":
                self.set_error("Please select a pre-existing item",False)
            elif self.curr_barcode == "":
                self.set_error("Please select a barcode to delete",False)
            else:
                self.warehouse_controller.delete_sub_item(self.curr_item,self.curr_barcode)
                new_barcode_list = self.warehouse_controller.get_item(self.curr_item)["Items"]
                self.refresh_barcode_table(new_barcode_list)
                #manually update item main table to reduce query frequency
                #DESYNC POTENTIAL
                row = self.find_item_in_table(self.curr_item)
                item_count = int(self.ui.item_table.item(row,1).text())
                self.ui.item_table.setItem(row,1,QTableWidgetItem(str(item_count-1)))
                # need to edit the stored item list to maintain consistency
                for i in range(len(self.items)):
                    if self.items[i]["Name"] == self.curr_item:
                        for j in range(len(self.items[i]["Items"])):
                            if self.items[i]["Items"][j]["Barcode"] == self.curr_barcode:
                                del self.items[i]["Items"][j]
                                break
                        break
                self.set_error(self.curr_barcode + " deleted!",True)
                self.curr_barcode = ""
