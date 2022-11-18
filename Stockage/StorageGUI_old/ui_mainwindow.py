# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(800, 600)
        self.gridLayout = QGridLayout(Widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(Widget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.tabWidget = QTabWidget(Widget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_2 = QGridLayout(self.tab)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.sb_consumption = QSpinBox(self.tab)
        self.sb_consumption.setObjectName(u"sb_consumption")
        self.sb_consumption.setMaximum(20000)
        self.sb_consumption.setValue(5840)

        self.gridLayout_2.addWidget(self.sb_consumption, 1, 1, 1, 1)

        self.label_4 = QLabel(self.tab)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_2.addWidget(self.label_4, 2, 3, 1, 1)

        self.label_3 = QLabel(self.tab)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 1, 3, 1, 1)

        self.label_5 = QLabel(self.tab)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_2.addWidget(self.label_5, 2, 0, 1, 1)

        self.sb_rateHeater = QSpinBox(self.tab)
        self.sb_rateHeater.setObjectName(u"sb_rateHeater")
        self.sb_rateHeater.setValue(70)

        self.gridLayout_2.addWidget(self.sb_rateHeater, 2, 1, 1, 1)

        self.tw_months = QTableWidget(self.tab)
        self.tw_months.setObjectName(u"tw_months")

        self.gridLayout_2.addWidget(self.tw_months, 5, 0, 1, 4)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 6, 1, 1, 1)

        self.label_2 = QLabel(self.tab)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 0, 0, 2, 1)

        self.line = QFrame(self.tab)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line, 3, 0, 1, 4)

        self.label_6 = QLabel(self.tab)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_2.addWidget(self.label_6, 4, 0, 1, 4)

        self.tabWidget.addTab(self.tab, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.gridLayout_3 = QGridLayout(self.tab_5)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_2, 1, 0, 1, 1)

        self.tableWidget_2 = QTableWidget(self.tab_5)
        self.tableWidget_2.setObjectName(u"tableWidget_2")

        self.gridLayout_3.addWidget(self.tableWidget_2, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_5, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.tabWidget.addTab(self.tab_4, "")

        self.gridLayout.addWidget(self.tabWidget, 1, 0, 1, 1)


        self.retranslateUi(Widget)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Stockage_GUI", None))
        self.label.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p><span style=\" font-size:20pt; font-weight:700;\">Installation solaire</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("Widget", u"%", None))
        self.label_3.setText(QCoreApplication.translate("Widget", u"kWh", None))
        self.label_5.setText(QCoreApplication.translate("Widget", u"Proportion du chauffage", None))
        self.label_2.setText(QCoreApplication.translate("Widget", u"Consommation annuelle", None))
        self.label_6.setText(QCoreApplication.translate("Widget", u"Consommation par mois (kWh)", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Widget", u"R\u00e9sidence", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QCoreApplication.translate("Widget", u"M\u00e9t\u00e9o", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Widget", u"Production d'\u00e9nergie", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("Widget", u"Stockage", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("Widget", u"R\u00e9sultats", None))
    # retranslateUi

