from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_OrdersWindow(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(800, 600)
        self.verticalLayoutWidget = QWidget(Dialog)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 50, 201, 541))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout.addWidget(self.label)

        self.order_type_text = QTextBrowser(self.verticalLayoutWidget)
        self.order_type_text.setObjectName(u"order_type_text")
        self.order_type_text.setMaximumSize(QSize(16777215, 50))

        self.verticalLayout.addWidget(self.order_type_text)

        self.label_2 = QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout.addWidget(self.label_2)

        self.client_text = QTextBrowser(self.verticalLayoutWidget)
        self.client_text.setObjectName(u"client_text")
        self.client_text.setMaximumSize(QSize(16777215, 50))

        self.verticalLayout.addWidget(self.client_text)

        self.select_btn = QPushButton(self.verticalLayoutWidget)
        self.select_btn.setObjectName(u"select_btn")
        self.select_btn.setMinimumSize(QSize(0, 100))

        self.verticalLayout.addWidget(self.select_btn)

        self.remove_btn = QPushButton(self.verticalLayoutWidget)
        self.remove_btn.setObjectName(u"remove_btn")
        self.remove_btn.setMinimumSize(QSize(0, 100))

        self.verticalLayout.addWidget(self.remove_btn)

        self.horizontalLayoutWidget = QWidget(Dialog)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(220, 10, 561, 581))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.items_need_tbl = QTableView(self.horizontalLayoutWidget)
        self.items_need_tbl.setObjectName(u"items_need_tbl")

        self.horizontalLayout.addWidget(self.items_need_tbl)

        self.containers_tbl = QTableView(self.horizontalLayoutWidget)
        self.containers_tbl.setObjectName(u"containers_tbl")

        self.horizontalLayout.addWidget(self.containers_tbl)

        self.selected_tbl = QTableView(self.horizontalLayoutWidget)
        self.selected_tbl.setObjectName(u"selected_tbl")

        self.horizontalLayout.addWidget(self.selected_tbl)

        self.return_btn = QPushButton(Dialog)
        self.return_btn.setObjectName(u"return_btn")
        self.return_btn.setGeometry(QRect(10, 10, 121, 34))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"   Order Type:", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"   Client:", None))
        self.select_btn.setText(QCoreApplication.translate("Dialog", u"Select", None))
        self.remove_btn.setText(QCoreApplication.translate("Dialog", u"Remove", None))
        self.return_btn.setText(QCoreApplication.translate("Dialog", u"Return", None))
    # retranslateUi



class OrdersWindow(QDialog):
    def __init__(self, warehouse_controller):
        super(OrdersWindow, self).__init__()
        self.ui = Ui_OrdersWindow()
        self.ui.setupUi(self)
        self.warehouse_controller = warehouse_controller
        self.init_buttons()

    def init_buttons(self):
        self.ui.return_btn.clicked.connect(self.return_clicked)

    def get_order_type(self):
        pass

    def get_client(self):
        pass

    def return_clicked(self):
        self.warehouse_controller.switch_to(self, 'main')
