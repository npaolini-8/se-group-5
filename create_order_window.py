from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

class Ui_CreateOrder(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(800, 600)
        self.return_btn = QPushButton(Dialog)
        self.return_btn.setObjectName(u"return_btn")
        self.return_btn.setGeometry(QRect(20, 10, 75, 24))
        self.horizontalLayoutWidget = QWidget(Dialog)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 40, 221, 51))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.incoming_radio = QRadioButton(self.horizontalLayoutWidget)
        self.incoming_radio.setObjectName(u"incoming_radio")

        self.horizontalLayout.addWidget(self.incoming_radio)

        self.outgoing_radio = QRadioButton(self.horizontalLayoutWidget)
        self.outgoing_radio.setObjectName(u"outgoing_radio")

        self.horizontalLayout.addWidget(self.outgoing_radio)

        self.verticalLayoutWidget = QWidget(Dialog)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 100, 311, 481))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.search_bar_line = QLineEdit(self.verticalLayoutWidget)
        self.search_bar_line.setObjectName(u"search_bar_line")

        self.verticalLayout.addWidget(self.search_bar_line)

        self.search_tbl = QTableWidget(self.verticalLayoutWidget)
        self.search_tbl.setObjectName(u"search_tbl")

        self.verticalLayout.addWidget(self.search_tbl)

        self.add_to_order_btn = QPushButton(Dialog)
        self.add_to_order_btn.setObjectName(u"add_to_order_btn")
        self.add_to_order_btn.setGeometry(QRect(330, 290, 161, 51))
        self.verticalLayoutWidget_3 = QWidget(Dialog)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(500, 100, 281, 481))
        self.verticalLayout_3 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.verticalLayoutWidget_3)
        self.label.setObjectName(u"label")

        self.verticalLayout_3.addWidget(self.label)

        self.order_items_tbl = QTableWidget(self.verticalLayoutWidget_3)
        self.order_items_tbl.setObjectName(u"order_items_tbl")

        self.verticalLayout_3.addWidget(self.order_items_tbl)

        self.client_line = QLineEdit(Dialog)
        self.client_line.setObjectName(u"client_line")
        self.client_line.setGeometry(QRect(240, 40, 211, 51))
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(250, 20, 49, 16))
        self.submit_order_btn = QPushButton(Dialog)
        self.submit_order_btn.setObjectName(u"submit_order_btn")
        self.submit_order_btn.setGeometry(QRect(500, 40, 281, 51))
        self.verticalLayoutWidget_4 = QWidget(Dialog)
        self.verticalLayoutWidget_4.setObjectName(u"verticalLayoutWidget_4")
        self.verticalLayoutWidget_4.setGeometry(QRect(330, 150, 161, 133))
        self.verticalLayout_4 = QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.plus_btn = QPushButton(self.verticalLayoutWidget_4)
        self.plus_btn.setObjectName(u"plus_btn")

        self.verticalLayout_4.addWidget(self.plus_btn)

        self.count_line = QLineEdit(self.verticalLayoutWidget_4)
        self.count_line.setObjectName(u"count_line")
        self.count_line.setAlignment(Qt.AlignCenter)
        self.count_line.setReadOnly(True)

        self.verticalLayout_4.addWidget(self.count_line)

        self.minus_btn = QPushButton(self.verticalLayoutWidget_4)
        self.minus_btn.setObjectName(u"minus_btn")

        self.verticalLayout_4.addWidget(self.minus_btn)

        self.remove_from_order_btn = QPushButton(Dialog)
        self.remove_from_order_btn.setObjectName(u"remove_from_order_btn")
        self.remove_from_order_btn.setGeometry(QRect(330, 350, 161, 51))
        self.info_label = QLabel(Dialog)
        self.info_label.setObjectName(u"info_label")
        self.info_label.setGeometry(QRect(500, 10, 281, 16))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.return_btn.setText(QCoreApplication.translate("Dialog", u"Return", None))
        self.incoming_radio.setText(QCoreApplication.translate("Dialog", u"Incoming", None))
        self.outgoing_radio.setText(QCoreApplication.translate("Dialog", u"Outgoing", None))
        self.search_bar_line.setPlaceholderText(QCoreApplication.translate("Dialog", u"Search Bar...", None))
        self.add_to_order_btn.setText(QCoreApplication.translate("Dialog", u"Add to Order", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Order Contents", None))
        self.client_line.setPlaceholderText(QCoreApplication.translate("Dialog", u"Insert Client...", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Client", None))
        self.submit_order_btn.setText(QCoreApplication.translate("Dialog", u"Submit Order", None))
        self.plus_btn.setText(QCoreApplication.translate("Dialog", u"+", None))
        self.count_line.setText(QCoreApplication.translate("Dialog", u"0", None))
        self.count_line.setPlaceholderText("")
        self.minus_btn.setText(QCoreApplication.translate("Dialog", u"-", None))
        self.remove_from_order_btn.setText(QCoreApplication.translate("Dialog", u"Remove from Order", None))
        self.info_label.setText("")
    # retranslateUi


class CreateOrderWindow(QDialog):
    def __init__(self, warehouse_controller):
        super(CreateOrderWindow, self).__init__()
        self.ui = Ui_CreateOrder()
        self.ui.setupUi(self)
        self.warehouse_controller = warehouse_controller
        self.init_buttons()
        self.init_tables()
        self.ui.search_bar_line.textChanged.connect(self.filter_table)

    def init_buttons(self):
        self.ui.return_btn.clicked.connect(self.return_clicked)
        self.ui.add_to_order_btn.clicked.connect(self.add_to_order)
        self.ui.remove_from_order_btn.clicked.connect(self.remove_from_order)
        self.plus_minus_btn = QButtonGroup()
        self.plus_minus_btn.addButton(self.ui.plus_btn)
        self.plus_minus_btn.addButton(self.ui.minus_btn)
        self.plus_minus_btn.buttonClicked.connect(self.choose_amount)
        self.ui.submit_order_btn.clicked.connect(self.create_order)
        self.ui.incoming_radio.clicked.connect(self.radio_checked)
        self.ui.outgoing_radio.clicked.connect(self.radio_checked)

    def radio_checked(self):
        self.ui.order_items_tbl.setRowCount(0)
        self.ui.order_items_tbl.insertRow(self.ui.order_items_tbl.rowCount())
        self.ui.client_line.setText('')
        self.init_table(self.ui.search_tbl, self.warehouse_controller.get_items())

    def return_clicked(self):
        self.warehouse_controller.switch_to(self, 'main')

    def filter_table(self):
        filter_string = self.ui.search_bar_line.text()
        for row in range(self.ui.search_tbl.rowCount()):
            filtered = False
            for column in range(self.ui.search_tbl.columnCount()):
                item = self.ui.search_tbl.item(row, column)
                if filter_string.lower() in item.text().lower():
                    filtered = True
                    break
            self.ui.search_tbl.setRowHidden(row, not filtered)

    def add_to_order(self):
        if self.ui.outgoing_radio.isChecked():
            try:
                row = self.ui.search_tbl.currentRow()
                item_col0 = QTableWidgetItem(self.ui.search_tbl.item(row, 0))
                item_col1 = QTableWidgetItem(self.ui.search_tbl.item(row, 1))

                if int(self.ui.count_line.text()) > 0:
                    if self.ui.order_items_tbl.item(0, 0) is None or self.ui.order_items_tbl.item(0, 0).text() == '':
                        if int(item_col1.text()) != 0:
                            if int(item_col1.text()) >= int(self.ui.count_line.text()):
                                self.ui.order_items_tbl.setItem(0, 0, item_col0)
                                amountItem = QTableWidgetItem(self.ui.count_line.text())
                                self.ui.order_items_tbl.setItem(0, 1, amountItem)
                                newStockItem = QTableWidgetItem(str(int(item_col1.text())-int(self.ui.count_line.text())))
                                self.ui.search_tbl.setItem(row, 1, newStockItem)
                    else:
                        if int(item_col1.text()) != 0:
                            if int(item_col1.text()) >= int(self.ui.count_line.text()):
                                self.ui.order_items_tbl.insertRow(self.ui.order_items_tbl.rowCount())
                                self.ui.order_items_tbl.setItem(self.ui.order_items_tbl.rowCount()-1, 0, item_col0)
                                amountItem = QTableWidgetItem(self.ui.count_line.text())
                                self.ui.order_items_tbl.setItem(self.ui.order_items_tbl.rowCount()-1, 1, amountItem)
                                newStockItem = QTableWidgetItem(str(int(item_col1.text())-int(self.ui.count_line.text())))
                                self.ui.search_tbl.setItem(row, 1, newStockItem)
            except ValueError: # This error comes up when you haven't selected an item yet.
                pass
        elif self.ui.incoming_radio.isChecked():
            try:
                row = self.ui.search_tbl.currentRow()
                item_col0 = QTableWidgetItem(self.ui.search_tbl.item(row, 0))
                item_col1 = QTableWidgetItem(self.ui.search_tbl.item(row, 1))
                if int(self.ui.count_line.text()) > 0:
                    if self.ui.order_items_tbl.item(0, 0) is None or self.ui.order_items_tbl.item(0, 0).text() == '':
                        self.ui.order_items_tbl.setItem(0, 0, item_col0)
                        amountItem = QTableWidgetItem(self.ui.count_line.text())
                        self.ui.order_items_tbl.setItem(0, 1, amountItem)
                    else:
                        self.ui.order_items_tbl.insertRow(self.ui.order_items_tbl.rowCount())
                        self.ui.order_items_tbl.setItem(self.ui.order_items_tbl.rowCount()-1, 0, item_col0)
                        amountItem = QTableWidgetItem(self.ui.count_line.text())
                        self.ui.order_items_tbl.setItem(self.ui.order_items_tbl.rowCount()-1, 1, amountItem)
            except ValueError: # This error comes up when you haven't selected an item yet.
                pass

    def remove_from_order(self):
        try:
            order_row = self.ui.order_items_tbl.currentRow()
            restock_amount = int(self.ui.order_items_tbl.item(order_row, 1).text())
            search_item_string = self.ui.order_items_tbl.item(order_row, 0).text()
            search_items = self.ui.search_tbl.findItems(search_item_string, Qt.MatchContains)
            if search_items:
                item = search_items[0]
                item_row = item.row()
                current_stock = int(self.ui.search_tbl.item(item_row, 1).text())
                newStockItem = QTableWidgetItem(str(current_stock+restock_amount))
                self.ui.search_tbl.setItem(item_row, 1, newStockItem)
            self.ui.order_items_tbl.removeRow(order_row)

            if self.ui.order_items_tbl.rowCount() == 0:
                self.ui.order_items_tbl.insertRow(self.ui.order_items_tbl.rowCount())
        except AttributeError: # This error comes up when there's nothing to remove.
            pass

    def choose_amount(self, btn):
        if self.ui.outgoing_radio.isChecked():
            try:
                current_amount = int(self.ui.count_line.text())
                row = self.ui.search_tbl.currentRow()
                item_col1 = QTableWidgetItem(self.ui.search_tbl.item(row, 1))
                if btn.objectName() == 'plus_btn':
                    if current_amount < int(item_col1.text()):
                        self.ui.count_line.setText(str(current_amount+1))
                elif btn.objectName() == 'minus_btn':
                    if current_amount > 0:
                        self.ui.count_line.setText(str(current_amount-1))
            except ValueError: # This error comes up when you haven't selected an item yet.
                pass
        elif self.ui.incoming_radio.isChecked():
            try:
                current_amount = int(self.ui.count_line.text())
                row = self.ui.search_tbl.currentRow()
                if btn.objectName() == 'plus_btn':
                    self.ui.count_line.setText(str(current_amount+1))
                elif btn.objectName() == 'minus_btn':
                    self.ui.count_line.setText(str(current_amount-1))
            except ValueError: # This error comes up when you haven't selected an item yet.
                pass

    def create_order(self):
        if self.ui.incoming_radio.isChecked():
            order_type = 'Incoming'
        elif self.ui.outgoing_radio.isChecked():
            order_type = 'Outgoing'
        client = self.ui.client_line.text()
        order_id = self.warehouse_controller.create_order(order_type, client, 'Pending')
        for row in range(self.ui.order_items_tbl.rowCount()):
            item_name = self.ui.order_items_tbl.item(row, 0).text()
            item_count = int(self.ui.order_items_tbl.item(row,  1).text())
            self.warehouse_controller.warehouse.add_to_order(order_id, item_name, item_count, order_type)

        self.ui.order_items_tbl.setRowCount(0)
        self.ui.order_items_tbl.insertRow(self.ui.order_items_tbl.rowCount())
        self.ui.client_line.setText('')
        self.ui.incoming_radio.setChecked(False)
        self.ui.outgoing_radio.setChecked(False)
        self.ui.info_label.setStyleSheet("color: green;")
        self.ui.info_label.setText(f"Submitted Order ID: {order_id}")

    def init_table(self, table, list):
        col_count = 0
        row_count = 0
        headers = []

        if len(list) > 0:
            col_count = len(list[0].keys())
            headers = list[0].keys()
            row_count = len(list)

        table.setColumnCount(col_count)
        table.setRowCount(row_count)
        table.verticalHeader().setVisible(False)
        table.setHorizontalHeaderLabels(headers)

        for i in range(len(list)):
            count = 0
            for key in list[i]:
                item = QTableWidgetItem(list[i][key].__str__())
                #item.setFlags(Qt.ItemIsDragEnabled)
                item.setFlags(item.flags() ^ Qt.ItemIsEditable)
                table.setItem(i, count, item)
                count += 1

    def refresh_table(self):
        self.init_table(self.ui.search_tbl, self.warehouse_controller.get_items())

    def init_tables(self):
        self.ui.search_tbl.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.ui.search_tbl.setSelectionMode(QAbstractItemView.SingleSelection)
        self.ui.order_items_tbl.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.ui.order_items_tbl.setSelectionMode(QAbstractItemView.SingleSelection)


        items=[{'Item Name': '', 'Stock': ''}]
        self.init_table(self.ui.search_tbl, self.warehouse_controller.get_items())
        self.init_table(self.ui.order_items_tbl, items)

        header = self.ui.search_tbl.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.Stretch)
        header.setSectionResizeMode(1, QHeaderView.Stretch)

        header = self.ui.order_items_tbl.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.Stretch)
        header.setSectionResizeMode(1, QHeaderView.Stretch)

        def clear_amount():
            self.ui.count_line.setText('0')

        self.ui.search_tbl.clicked.connect(clear_amount)
