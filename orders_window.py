# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'order_processing_windowKfhlWW.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QDialog, QGroupBox,
    QHeaderView, QLCDNumber, QLabel, QPushButton,
    QRadioButton, QSizePolicy, QStackedWidget, QTableWidget,
    QTableWidgetItem, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(814, 600)
        self.return_btn = QPushButton(Dialog)
        self.return_btn.setObjectName(u"return_btn")
        self.return_btn.setGeometry(QRect(10, 10, 121, 34))
        self.complete_btn = QPushButton(Dialog)
        self.complete_btn.setObjectName(u"complete_btn")
        self.complete_btn.setGeometry(QRect(10, 520, 251, 71))
        self.groupBox = QGroupBox(Dialog)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 70, 251, 441))
        self.orders_tbl = QTableWidget(self.groupBox)
        self.orders_tbl.setObjectName(u"orders_tbl")
        self.orders_tbl.setGeometry(QRect(0, 20, 251, 441))
        font = QFont()
        font.setPointSize(8)
        self.orders_tbl.setFont(font)
        self.in_radio = QRadioButton(self.groupBox)
        self.in_radio.setObjectName(u"in_radio")
        self.in_radio.setGeometry(QRect(50, 0, 81, 20))
        self.in_radio.setFont(font)
        self.in_radio.setChecked(True)
        self.out_radio = QRadioButton(self.groupBox)
        self.out_radio.setObjectName(u"out_radio")
        self.out_radio.setGeometry(QRect(130, 0, 91, 20))
        self.out_radio.setFont(font)
        self.groupBox_2 = QGroupBox(Dialog)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(290, 70, 251, 441))
        self.items_tbl = QTableWidget(self.groupBox_2)
        self.items_tbl.setObjectName(u"items_tbl")
        self.items_tbl.setGeometry(QRect(0, 20, 251, 441))
        self.items_tbl.setFont(font)
        self.stacked_widget = QStackedWidget(Dialog)
        self.stacked_widget.setObjectName(u"stacked_widget")
        self.stacked_widget.setGeometry(QRect(570, 90, 231, 421))
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.save_count_btn = QPushButton(self.page)
        self.save_count_btn.setObjectName(u"save_count_btn")
        self.save_count_btn.setEnabled(True)
        self.save_count_btn.setGeometry(QRect(0, 100, 231, 41))
        self.groupBox_4 = QGroupBox(self.page)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(0, 0, 231, 81))
        self.minus_btn = QPushButton(self.groupBox_4)
        self.minus_btn.setObjectName(u"minus_btn")
        self.minus_btn.setGeometry(QRect(0, 20, 61, 61))
        font1 = QFont()
        font1.setPointSize(36)
        self.minus_btn.setFont(font1)
        self.incoming_lcd_count = QLCDNumber(self.groupBox_4)
        self.incoming_lcd_count.setObjectName(u"incoming_lcd_count")
        self.incoming_lcd_count.setGeometry(QRect(60, 20, 111, 61))
        self.incoming_lcd_count.setMode(QLCDNumber.Dec)
        self.incoming_lcd_count.setSegmentStyle(QLCDNumber.Flat)
        self.plus_btn = QPushButton(self.groupBox_4)
        self.plus_btn.setObjectName(u"plus_btn")
        self.plus_btn.setGeometry(QRect(170, 20, 61, 61))
        font2 = QFont()
        font2.setPointSize(28)
        self.plus_btn.setFont(font2)
        self.stacked_widget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.groupBox_3 = QGroupBox(self.page_2)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(0, 150, 231, 271))
        self.barcodes_tbl = QTableWidget(self.groupBox_3)
        self.barcodes_tbl.setObjectName(u"barcodes_tbl")
        self.barcodes_tbl.setGeometry(QRect(0, 20, 231, 251))
        self.barcodes_tbl.setFont(font)
        self.barcodes_tbl.setSelectionMode(QAbstractItemView.SingleSelection)
        self.save_barcodes_btn = QPushButton(self.page_2)
        self.save_barcodes_btn.setObjectName(u"save_barcodes_btn")
        self.save_barcodes_btn.setEnabled(True)
        self.save_barcodes_btn.setGeometry(QRect(0, 100, 231, 41))
        self.groupBox_5 = QGroupBox(self.page_2)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setGeometry(QRect(0, 0, 231, 81))
        self.outgoing_lcd_count = QLCDNumber(self.groupBox_5)
        self.outgoing_lcd_count.setObjectName(u"outgoing_lcd_count")
        self.outgoing_lcd_count.setGeometry(QRect(0, 20, 231, 61))
        self.outgoing_lcd_count.setMode(QLCDNumber.Dec)
        self.outgoing_lcd_count.setSegmentStyle(QLCDNumber.Flat)
        self.stacked_widget.addWidget(self.page_2)
        self.error_lbl = QLabel(Dialog)
        self.error_lbl.setObjectName(u"error_lbl")
        self.error_lbl.setGeometry(QRect(270, 540, 531, 31))
        font3 = QFont()
        font3.setPointSize(22)
        self.error_lbl.setFont(font3)

        self.retranslateUi(Dialog)

        self.stacked_widget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.return_btn.setText(QCoreApplication.translate("Dialog", u"Return", None))
        self.complete_btn.setText(QCoreApplication.translate("Dialog", u"Complete Order", None))
        self.groupBox.setTitle(QCoreApplication.translate("Dialog", u"Orders", None))
        self.in_radio.setText(QCoreApplication.translate("Dialog", u"Incoming", None))
        self.out_radio.setText(QCoreApplication.translate("Dialog", u"Outgoing", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Dialog", u"Items in Order", None))
        self.save_count_btn.setText(QCoreApplication.translate("Dialog", u"Save Present Item Count", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("Dialog", u"Items Present", None))
        self.minus_btn.setText(QCoreApplication.translate("Dialog", u"-", None))
        self.plus_btn.setText(QCoreApplication.translate("Dialog", u"+", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Dialog", u"Barcodes", None))
        self.save_barcodes_btn.setText(QCoreApplication.translate("Dialog", u"Save Barcode Selections", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("Dialog", u"Items Present", None))
        self.error_lbl.setText("")
    # retranslateUi





from PySide6.QtWidgets import QAbstractItemView


class OrdersWindow(QDialog):
    def __init__(self, warehouse_controller):
        super(OrdersWindow, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.warehouse_controller = warehouse_controller
        self.lcds_empty = False
        self.init_connects()
        self.init_tables()
        self.reset_to_start_state(set_radios = True, incoming = True)
        self.edited_orders = {}
        self.order_warning_present = False

    def init_tables(self):
        self.init_table(self.ui.orders_tbl, ['Order', 'Client', 'Item Count'])
        header = self.ui.orders_tbl.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.Stretch)
        header.setSectionResizeMode(1, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QHeaderView.Stretch)
        #self.refresh_table(self.ui.orders_tbl, self.get_orders_item_list())

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

    def init_table(self, table, col_labels):
        col_count = len(col_labels)
        table.setColumnCount(col_count)
        table.verticalHeader().setVisible(False)
        table.setHorizontalHeaderLabels(col_labels)
        table.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        table.setSelectionMode(QAbstractItemView.SingleSelection)
        table.setSortingEnabled(True)

    def init_connects(self):
        self.ui.return_btn.clicked.connect(self.return_clicked)
        self.ui.in_radio.toggled.connect(self.in_radio_toggled)
        self.ui.out_radio.toggled.connect(self.out_radio_toggled)

        self.ui.orders_tbl.clicked.connect(self.order_selected)
        self.ui.items_tbl.clicked.connect(self.item_selected)
        self.ui.barcodes_tbl.clicked.connect(self.barcode_selected)

        self.ui.minus_btn.clicked.connect(self.minus_clicked)
        self.ui.plus_btn.clicked.connect(self.plus_clicked)

        self.ui.save_barcodes_btn.clicked.connect(self.save_barcodes_clicked)
        self.ui.save_count_btn.clicked.connect(self.save_count_clicked)

        self.ui.complete_btn.clicked.connect(self.complete_clicked)

    def set_error(self, msg, color = 'red'):
        self.ui.error_lbl.setStyleSheet("color: "+ color + ";")
        self.ui.error_lbl.setText(msg)


    def all_items_done(self):
        done = True
        for i in range(self.ui.items_tbl.rowCount()):
            done = done and (str(self.ui.items_tbl.item(i, 3).text()) == 'Yes')
        return done

    def all_items_filled(self):
        filled = True
        for i in range(self.ui.items_tbl.rowCount()):
            filled = filled and (str(self.ui.items_tbl.item(i, 1).text()) == str(self.ui.items_tbl.item(i, 2).text()))
        return filled

    def complete_order(self):
        try:
            order_row = self.ui.orders_tbl.currentRow()
            id = str(self.ui.orders_tbl.item(order_row, 0).text())
            order = self.warehouse_controller.get_order(id)

            order_type = order['Order Type']
            for i in range(self.ui.items_tbl.rowCount()):
                item_name = self.ui.items_tbl.item(i, 0).text()
                if order_type == 'Incoming':
                    items_to_add = int(self.ui.items_tbl.item(i, 2).text())
                    for j in range(items_to_add):
                        self.warehouse_controller.create_sub_item(item_name)
                elif order_type == 'Outgoing':
                    added_dict = self.edited_orders[id][item_name][1]
                    barcodes_to_add = []
                    for barcode in added_dict:
                        if added_dict[barcode] == 'Yes':
                            barcodes_to_add.append(barcode)
                    for barcode in barcodes_to_add:
                        self.warehouse_controller.delete_sub_item(item_name, barcode)

            self.warehouse_controller.complete_order(id)
            self.set_error('Order completed', color='green')
            self.reset_to_start_state(set_radios = False, incoming = self.is_incoming_checked())
        except:
            self.set_error('Please select an order first', color='red')



    def complete_clicked(self):
        if self.all_items_done():
            if self.all_items_filled():
                self.complete_order()
            else:
                if self.order_warning_present:
                    self.complete_order()
                else:
                    self.order_warning_present = True
                    self.set_error('Warning - Not all items specified are accounted for. Press Complete again if this is intended.', color='yellow')
        else:
            self.set_error('All items of order must be marked as done.', color='red')



    def save_barcodes_clicked(self):
        order_row = self.ui.orders_tbl.currentRow()
        id = str(self.ui.orders_tbl.item(order_row, 0).text())
        if not id in self.edited_orders:
            self.edited_orders[id] = {}
        item_row = self.ui.items_tbl.currentRow()
        item_name = str(self.ui.items_tbl.item(item_row, 0).text())

        added_dict = {}
        for i in range(self.ui.barcodes_tbl.rowCount()):
            added_dict[str(self.ui.barcodes_tbl.item(i, 0).text())] = str(self.ui.barcodes_tbl.item(i, 1).text())
        self.edited_orders[id][item_name] = (str(int(self.ui.incoming_lcd_count.value())), added_dict)

        #self.set_item(self.ui.items_tbl, 2, item_row, self.edited_orders[id][item_name][0])
        self.set_item(self.ui.items_tbl, 3, item_row, 'Yes')


    def save_count_clicked(self):
        order_row = self.ui.orders_tbl.currentRow()
        id = str(self.ui.orders_tbl.item(order_row, 0).text())
        if not id in self.edited_orders:
            self.edited_orders[id] = {}
        item_row = self.ui.items_tbl.currentRow()
        item_name = str(self.ui.items_tbl.item(item_row, 0).text())

        self.edited_orders[id][item_name] = (str(int(self.ui.incoming_lcd_count.value())), None)

        self.set_item(self.ui.items_tbl, 2, item_row, self.edited_orders[id][item_name][0])
        self.set_item(self.ui.items_tbl, 3, item_row, 'Yes')


    def return_clicked(self):
        self.warehouse_controller.switch_to(self, 'main')

    def in_radio_toggled(self):
        self.reset_to_start_state(set_radios = False, incoming = True)

    def out_radio_toggled(self):
        self.reset_to_start_state(set_radios = False, incoming = False)

    def order_selected(self, item):
        self.order_warning_present = False
        row = item.row()
        id = self.ui.orders_tbl.item(row, 0).text()
        order = self.warehouse_controller.get_order(id)
        self.refresh_items_table()
        self.clear_table(self.ui.barcodes_tbl)
        self.clear_all_lcds()
        self.ui.error_lbl.setText('')

    def refresh_items_table(self):
        order_row = self.ui.orders_tbl.currentRow()
        id = str(self.ui.orders_tbl.item(order_row, 0).text())
        order = self.warehouse_controller.get_order(id)
        table_contents = self.get_items(order)

        if id in self.edited_orders:
            items = self.edited_orders[id]
            for i in range(len(table_contents[0])):
                if table_contents[0][i] in items.keys():
                    table_contents[2][i] = items[table_contents[0][i]][0]
                    table_contents[3][i] = 'Yes'
        self.refresh_table(self.ui.items_tbl, table_contents)

    def refresh_barcodes_table(self, barcodes):
        order_row = self.ui.orders_tbl.currentRow()
        id = str(self.ui.orders_tbl.item(order_row, 0).text())

        item_row = self.ui.items_tbl.currentRow()
        item_name = str(self.ui.items_tbl.item(item_row, 0).text())

        table_contents = [barcodes, ['No'] * len(barcodes)]


        if id in self.edited_orders and item_name in self.edited_orders[id]:
            barcodes_dict = self.edited_orders[id][item_name][1]
            for i in range(len(table_contents[0])):
                if table_contents[0][i] in barcodes_dict.keys():
                    table_contents[1][i] = barcodes_dict[table_contents[0][i]]
        self.refresh_table(self.ui.barcodes_tbl, table_contents)


    def item_selected(self, item):
        row = item.row()
        name = self.ui.items_tbl.item(row, 0).text()
        order_row = self.ui.orders_tbl.currentRow()
        id = self.ui.orders_tbl.item(order_row, 0).text()
        order = self.warehouse_controller.get_order(id)
        idx = 0
        for i in range (len(order['Order Items'])):
            if order['Order Items'][i]['Item Name'] == name:
                idx = i
                break

        base_item = order['Order Items'][idx]
        if self.is_incoming_checked():
            self.ui.stacked_widget.setCurrentIndex(0)
        else:
            self.ui.stacked_widget.setCurrentIndex(1)
            barcodes = self.warehouse_controller.get_barcodes(base_item['Item Name'])
            self.refresh_barcodes_table(barcodes)



        self.ui.incoming_lcd_count.display(self.ui.items_tbl.item(row, 1).text())
        self.ui.outgoing_lcd_count.display(self.ui.items_tbl.item(row, 2).text())
        self.lcds_empty = False
        self.ui.save_barcodes_btn.setEnabled(True)
        self.ui.save_count_btn.setEnabled(True)

    def barcode_selected(self, item):
        row = item.row()
        is_added = self.ui.barcodes_tbl.item(row, 1).text()
        item_row = self.ui.items_tbl.currentRow()


        if is_added == 'No':
            self.set_item(self.ui.barcodes_tbl, 1, row, 'Yes')
            self.set_item(self.ui.items_tbl, 2, item_row, str(int(self.ui.items_tbl.item(item_row, 2).text()) + 1))
        else:
            self.set_item(self.ui.barcodes_tbl, 1, row, 'No')
            self.set_item(self.ui.items_tbl, 2, item_row, str(int(self.ui.items_tbl.item(item_row, 2).text()) - 1))
            #self.ui.items_tbl.item(item_row, 1).text()

        current_item_count = self.ui.items_tbl.item(item_row, 2).text()
        self.ui.outgoing_lcd_count.display(current_item_count)


    def minus_clicked(self):
        if self.ui.incoming_lcd_count.value() != 0 and not self.lcds_empty:
            self.ui.incoming_lcd_count.display(self.ui.incoming_lcd_count.value() - 1)

    def plus_clicked(self):
        if not self.lcds_empty:
            self.ui.incoming_lcd_count.display(self.ui.incoming_lcd_count.value() + 1)


    def get_items(self, order):
        item_dicts = self.warehouse_controller.get_items_from_order(order)
        items = []
        counts = []
        addeds = []
        dones = []
        for item in item_dicts:
            items.append(item['Item Name'])
            counts.append(str(item['Count']))
            addeds.append(0)
            dones.append('No')
        return [items, counts, addeds, dones]

    def is_incoming_checked(self):
        return self.ui.in_radio.isChecked()

    def get_orders_item_list(self, incoming):
        orders = None
        if incoming:
            orders = self.warehouse_controller.get_incoming_orders_raw()
        else:
            orders = self.warehouse_controller.get_outgoing_orders_raw()

        item_list = []
        order_ids = []
        clients = []
        num_items = []
        for order in orders:
            order_ids.append(order['_id'])
            clients.append(order['Client'])
            count = 0
            for item in order['Order Items']:
                count += item['Count']
            num_items.append(str(count))
        item_list.append(order_ids)
        item_list.append(clients)
        item_list.append(num_items)
        return item_list

    def clear_table(self, table):
        table.clearContents()
        table.setRowCount(0)

    def clear_all_tables(self):
        self.clear_table(self.ui.orders_tbl)
        self.clear_table(self.ui.items_tbl)
        self.clear_table(self.ui.barcodes_tbl)

    def clear_all_lcds(self):
        self.ui.incoming_lcd_count.display(None)
        self.ui.outgoing_lcd_count.display(None)
        self.lcds_empty = True
        self.ui.save_barcodes_btn.setEnabled(False)
        self.ui.save_count_btn.setEnabled(False)


    def reset_to_start_state(self, set_radios = True, incoming = True):
        self.clear_all_tables()
        self.refresh_orders_table(incoming)
        self.clear_all_lcds()
        if incoming:
            if set_radios:
                self.ui.in_radio.setChecked(True)
                self.ui.out_radio.setChecked(False)
            self.ui.stacked_widget.setCurrentIndex(0)
        else:
            if set_radios:
                self.ui.in_radio.setChecked(False)
                self.ui.out_radio.setChecked(True)
            self.ui.stacked_widget.setCurrentIndex(1)

    def refresh_orders_table(self, incoming):
        self.refresh_table(self.ui.orders_tbl, self.get_orders_item_list(incoming))

    def set_item(self, table, x, y, value):
        item = QTableWidgetItem(value)
        item.setFlags(item.flags() and ~Qt.ItemIsEditable)
        item.setTextAlignment(Qt.AlignCenter)
        table.setItem(y, x, item)


    def refresh_table(self, table, item_lists):
        table.clearContents()
        if len(item_lists) == 0 or len(item_lists[0]) == 0:
            table.setRowCount(0)
            return
        table.setRowCount(len(item_lists[0]))
        for i in range(len(item_lists)):
            for j in range(len(item_lists[0])):
                self.set_item(table, i, j, str(item_lists[i][j]))
