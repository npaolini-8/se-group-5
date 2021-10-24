from PySide6.QtWidgets import (QLineEdit, QDockWidget, QCheckBox,
QVBoxLayout, QWidget, QPushButton, QLabel, QTableWidget,
QTableWidgetItem, QHBoxLayout, QRadioButton)

#Item catalog custom widget
#For displaying table of current items in database
#Allows for sorting of table by value
#Allows to search for an item by string
class ItemCatalogWidget(QDockWidget):
    def __init__(self, title, warehouse):
        super().__init__(title)
        self.warehouse = warehouse
        layout = QVBoxLayout()
        searchLayout = QHBoxLayout()
        orderLayout = QHBoxLayout()

        #Create and setup item table
        self.itemTable = QTableWidget()
        self.itemTable.verticalHeader().setVisible(False)
        colTitles = self.warehouse.item_column_titles()  #Gets list of values that items have
        self.itemTable.setColumnCount(10)
        self.itemTable.setHorizontalHeaderLabels(['id', 'Description', 'Model Number', 'Brand', 'Active?', 'Last modified', 'Last modified by', 'Increment', 'Items', 'Stock'])
        #self.itemTable.horizontalHeader().setStretchLastSection(True)

        #Create radio buttons for sorting
        self.idCheck = QRadioButton("id")
        self.descriptionCheck = QRadioButton("Description")
        self.modelCheck = QRadioButton("Model Number")
        self.brandCheck = QRadioButton("Brand")
        self.dateCheck = QRadioButton("Most recently modified")
        self.subCheck = QRadioButton("Stock")
        self.idCheck.setChecked(True)

        self.idCheck.clicked.connect(self.updateSearchPlaceholder)
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
        searchLayout.addWidget(QPushButton("Search"))
        #searchLayout.addWidget(self.descriptionCheck)

        #Add all radio buttons to a layout
        orderLayout.addWidget(QLabel("Field to search by: "))
        orderLayout.addWidget(self.idCheck)
        orderLayout.addWidget(self.descriptionCheck)
        orderLayout.addWidget(self.modelCheck)
        orderLayout.addWidget(self.brandCheck)
        orderLayout.addWidget(self.dateCheck)
        orderLayout.addWidget(self.subCheck)

        self.sortBtn = QPushButton("Sort by id")
        self.sortBtn.clicked.connect(self.refresh_item_table)
        orderLayout.addWidget(self.sortBtn)

        searchLayout.addStretch(1)
        orderLayout.addStretch(1)

        layout.addLayout(orderLayout)
        layout.addLayout(searchLayout)
        layout.addWidget(self.itemTable)

        container_widget = QWidget()
        container_widget.setLayout(layout)
        self.setWidget(container_widget)
        self.refresh_item_table()

    def updateSearchPlaceholder(self):
        if self.idCheck.isChecked():
            self.searchLine.setPlaceholderText("id")
            self.sortBtn.setText("Sort by id")
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

    #Refresh item list in gui
    def refresh_item_table(self):
        self.itemTable.clearContents()
        items = self.warehouse.get_items()
        self.itemTable.setRowCount(len(items))

        if self.idCheck.isChecked():
            items = sorted(items, key=lambda x:x['_id'])
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
            for key in items[i].keys():
                self.itemTable.setItem(i, count, QTableWidgetItem(items[i][key].__str__()))
                count += 1
            self.itemTable.setItem(i, count, QTableWidgetItem(str(len(items[i]['Items']))))
