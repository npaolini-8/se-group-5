from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

class Ui_ItemWindow(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(800, 600)
        self.verticalLayoutWidget = QWidget(Dialog)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 60, 160, 521))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.create_item_btn = QPushButton(self.verticalLayoutWidget)
        self.create_item_btn.setObjectName(u"create_item_btn")
        self.create_item_btn.setMinimumSize(QSize(0, 80))

        self.verticalLayout.addWidget(self.create_item_btn)

        self.modify_item_btn = QPushButton(self.verticalLayoutWidget)
        self.modify_item_btn.setObjectName(u"modify_item_btn")
        self.modify_item_btn.setMinimumSize(QSize(0, 80))

        self.verticalLayout.addWidget(self.modify_item_btn)

        self.remove_item_btn = QPushButton(self.verticalLayoutWidget)
        self.remove_item_btn.setObjectName(u"remove_item_btn")
        self.remove_item_btn.setMinimumSize(QSize(0, 80))

        self.verticalLayout.addWidget(self.remove_item_btn)

        self.verticalLayoutWidget_2 = QWidget(Dialog)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(170, 10, 601, 571))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.search_bar_line = QLineEdit(self.verticalLayoutWidget_2)
        self.search_bar_line.setObjectName(u"search_bar_line")

        self.horizontalLayout.addWidget(self.search_bar_line)

        self.search_btn = QPushButton(self.verticalLayoutWidget_2)
        self.search_btn.setObjectName(u"search_btn")

        self.horizontalLayout.addWidget(self.search_btn)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.items_tbl = QTableView(self.verticalLayoutWidget_2)
        self.items_tbl.setObjectName(u"items_tbl")

        self.verticalLayout_2.addWidget(self.items_tbl)

        self.return_btn = QPushButton(Dialog)
        self.return_btn.setObjectName(u"return_btn")
        self.return_btn.setGeometry(QRect(20, 10, 131, 34))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.create_item_btn.setText(QCoreApplication.translate("Dialog", u"Create Item", None))
        self.modify_item_btn.setText(QCoreApplication.translate("Dialog", u"Modify Item", None))
        self.remove_item_btn.setText(QCoreApplication.translate("Dialog", u"Remove Item", None))
        self.search_bar_line.setText("")
        self.search_bar_line.setPlaceholderText(QCoreApplication.translate("Dialog", u"Search Bar...", None))
        self.search_btn.setText(QCoreApplication.translate("Dialog", u"PushButton", None))
        self.return_btn.setText(QCoreApplication.translate("Dialog", u"Return", None))
    # retranslateUi

class ItemsWindow(QDialog):
    def __init__(self, warehouse_controller):
        super(ItemsWindow, self).__init__()
        self.ui = Ui_ItemWindow()
        self.ui.setupUi(self)
        self.warehouse_controller = warehouse_controller
        self.init_buttons()

    def init_buttons(self):
        self.ui.return_btn.clicked.connect(self.return_clicked)


    def return_clicked(self):
        self.warehouse_controller.switch_to(self, 'main')