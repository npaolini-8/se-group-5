from PySide6.QtWidgets import (QLineEdit, QDockWidget, QCheckBox,
QVBoxLayout, QWidget, QPushButton, QLabel, QTableWidget,
QTableWidgetItem, QHBoxLayout, QRadioButton, QTableWidgetSelectionRange, QSizePolicy)
from PySide6.QtCore import Qt
from PySide6.QtGui import QBrush, QColor
from item_inspector import ItemInspectorWidget

class ItemTableWidget(QTableWidget):
    def __init__(self,  warehouse, itemCatalogWidget):
        super().__init__()
        self.itemCatalogWidget = itemCatalogWidget
        self.warehouse = warehouse
        self.verticalHeader().setVisible(False)
        #colTitles = self.warehouse.item_column_titles()  #Gets list of values that items have
        self.setColumnCount(11)
        self.keyHeaderNames = ['id', 'Name', 'Description', 'Model Number',
        'Brand', 'Active?', 'Last modified', 'Last modified by', 'Increment', 'Items']
        self.keyHeaders = ['_id', 'Name', 'Description', 'Model Number',
        'Brand', 'isActive', 'Date modified', 'Last modified by', 'Barcode Increment', 'Items']
        self.customHeaders = ['Stock']
        headers = self.keyHeaderNames + self.customHeaders
        self.setHorizontalHeaderLabels(headers)
        self.cellClicked.connect(self.cell_was_clicked)
        self.currentItemChanged.connect(self.cell_was_changed)
        #self.setRangeSelected(QTableWidgetSelectionRange(0, 0, 2, 2), True)
        #self.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)

    #@override
    def cell_was_clicked(self, row, column):
        self.item(row, column).setSelected(False)

    def cell_was_changed(self, current, previous):

        for i in range(self.columnCount()):
            if previous != None:
                self.item(previous.row(), i).setBackground(QBrush(QColor(0, 0, 0, 0)))
            if current != None:
                self.item(current.row(), i).setBackground(QBrush(QColor(91, 46, 242, 100)))
                self.itemCatalogWidget.itemInspectorWidget.update_item(self.item(current.row(), 1).text())  #Grab name value

#Item catalog custom widget
#For displaying table of current items in database
#Allows for sorting of table by value
#Allows to search for an item by string
class ItemCatalogWidget(QDockWidget):
    def __init__(self, title, warehouse):
        super().__init__(title)
        self.warehouse = warehouse

        mainLayout = QHBoxLayout()
        leftLayout = QVBoxLayout()
        rightLayout = QVBoxLayout()
        addLayout = QVBoxLayout()
        searchLayout = QHBoxLayout()
        orderLayout = QHBoxLayout()

        #Create and setup item table
        self.itemTable = ItemTableWidget(self.warehouse, self)
        self.itemInspectorWidget = ItemInspectorWidget(self.warehouse, self)
        #self.itemTable.horizontalHeader().setStretchLastSection(True)
        #Create radio buttons for sorting
        self.idCheck = QRadioButton("id")
        self.nameCheck = QRadioButton("Name")
        self.descriptionCheck = QRadioButton("Description")
        self.modelCheck = QRadioButton("Model Number")
        self.brandCheck = QRadioButton("Brand")
        self.dateCheck = QRadioButton("Most recently modified")
        self.subCheck = QRadioButton("Stock")
        self.idCheck.setChecked(True)

        self.idCheck.clicked.connect(self.updateSearchPlaceholder)
        self.nameCheck.clicked.connect(self.updateSearchPlaceholder)
        self.descriptionCheck.clicked.connect(self.updateSearchPlaceholder)
        self.modelCheck.clicked.connect(self.updateSearchPlaceholder)
        self.brandCheck.clicked.connect(self.updateSearchPlaceholder)
        self.dateCheck.clicked.connect(self.updateSearchPlaceholder)
        self.subCheck.clicked.connect(self.updateSearchPlaceholder)

        #Add items to searchLayout
        searchLayout.addWidget(QLabel("Search for: "))
        self.searchLine = QLineEdit()
        self.searchLine.setPlaceholderText("id")
        searchLayout.addWidget(self.searchLine)
        self.searchBtn = QPushButton("Search")
        self.searchBtn.clicked.connect(self.search_clicked)
        searchLayout.addWidget(self.searchBtn)
        #searchLayout.addWidget(self.descriptionCheck)

        #Add all radio buttons to a layout
        orderLayout.addWidget(QLabel("Field to search by: "))
        orderLayout.addWidget(self.idCheck)
        orderLayout.addWidget(self.nameCheck)
        orderLayout.addWidget(self.descriptionCheck)
        orderLayout.addWidget(self.modelCheck)
        orderLayout.addWidget(self.brandCheck)
        orderLayout.addWidget(self.dateCheck)
        orderLayout.addWidget(self.subCheck)

        self.sortBtn = QPushButton("Sort by id")
        self.sortBtn.clicked.connect(self.normal_refresh_item_table)
        orderLayout.addWidget(self.sortBtn)

        searchLayout.addStretch(1)
        orderLayout.addStretch(1)

        leftLayout.addLayout(orderLayout)
        leftLayout.addLayout(searchLayout)
        leftLayout.addWidget(self.itemTable)

        rightLayout.addWidget(self.itemInspectorWidget)

        mainLayout.addLayout(leftLayout)
        mainLayout.addLayout(rightLayout)

        container_widget = QWidget()
        container_widget.setLayout(mainLayout)
        self.setWidget(container_widget)
        self.normal_refresh_item_table()

    def get_search(self, key, string):
        results = []
        items = self.warehouse.get_items()
        for item in items:
            if string.upper() in str(item[key]).upper():
                results.append(item)
        return results

    def search_clicked(self):
        result = []

        if self.idCheck.isChecked():
            result = self.get_search('_id', self.searchLine.text())
        elif self.nameCheck.isChecked():
            result = self.get_search('Name', self.searchLine.text())
        elif self.descriptionCheck.isChecked():
            result = self.get_search('Description', self.searchLine.text())
        elif self.modelCheck.isChecked():
            result = self.get_search('Model Number', self.searchLine.text())
        elif self.brandCheck.isChecked():
            result = self.get_search('Brand', self.searchLine.text())
        elif self.dateCheck.isChecked():
            result = self.get_search('Date Modified', self.searchLine.text())
        #elif self.subCheck.isChecked():
            #result = self.get_search('Items', self.searchLine.text())

        self.refresh_item_table(result)

    def updateSearchPlaceholder(self):
        if self.idCheck.isChecked():
            self.searchLine.setPlaceholderText("id")
            self.sortBtn.setText("Sort by id")
        elif self.nameCheck.isChecked():
            self.searchLine.setPlaceholderText("name")
            self.sortBtn.setText("Sort by name")
        elif self.descriptionCheck.isChecked():
            self.searchLine.setPlaceholderText("description")
            self.sortBtn.setText("Sort by description")
        elif self.modelCheck.isChecked():
            self.searchLine.setPlaceholderText("model number")
            self.sortBtn.setText("Sort by model number")
        elif self.brandCheck.isChecked():
            self.searchLine.setPlaceholderText("brand")
            self.sortBtn.setText("Sort by brand")
        elif self.dateCheck.isChecked():
            self.searchLine.setPlaceholderText("date")
            self.sortBtn.setText("Sort by date")
        elif self.subCheck.isChecked():
            self.searchLine.setPlaceholderText("stock")
            self.sortBtn.setText("Sort by stock")

    def normal_refresh_item_table(self):
        self.refresh_item_table(self.warehouse.get_items())

    #Refresh item list in gui
    def refresh_item_table(self, items):
        self.itemTable.clearContents()
        self.itemTable.setRowCount(len(items))

        if self.idCheck.isChecked():
            items = sorted(items, key=lambda x:x['_id'])
        elif self.nameCheck.isChecked():
            items = sorted(items, key=lambda x:x['Name'])
        elif self.descriptionCheck.isChecked():
            items = sorted(items, key=lambda x:x['Description'])
        elif self.modelCheck.isChecked():
            items = sorted(items, key=lambda x:x['Model Number'])
        elif self.brandCheck.isChecked():
            items = sorted(items, key=lambda x:x['Brand'])
        elif self.dateCheck.isChecked():
            items = sorted(items, key=lambda x:x['Date modified'], reverse=True)
        elif self.subCheck.isChecked():
            items = sorted(items, key=lambda x:len(x['Items']), reverse=True)

        for i in range(len(items)):
            count = 0
            for key in self.itemTable.keyHeaders:
                item = QTableWidgetItem(items[i][key].__str__())
                item.setFlags(item.flags() & ~Qt.ItemIsEditable & ~Qt.ItemIsSelectable)
                self.itemTable.setItem(i, count, item)
                count += 1
            item = QTableWidgetItem(str(len(items[i]['Items'])))
            item.setFlags(item.flags() & ~Qt.ItemIsEditable & ~Qt.ItemIsSelectable)
            self.itemTable.setItem(i, count, item)
            count += 1
