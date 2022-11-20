# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'GUI.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from pyqtgraph import PlotWidget


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1013, 740)
        MainWindow.setMinimumSize(QSize(0, 0))
        MainWindow.setWindowOpacity(0.500000000000000)
        MainWindow.setDocumentMode(False)
        self.actionVersion = QAction(MainWindow)
        self.actionVersion.setObjectName(u"actionVersion")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_8 = QGridLayout(self.centralwidget)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tab_1 = QWidget()
        self.tab_1.setObjectName(u"tab_1")
        self.gridLayout_2 = QGridLayout(self.tab_1)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_5 = QLabel(self.tab_1)
        self.label_5.setObjectName(u"label_5")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy1)

        self.gridLayout_2.addWidget(self.label_5, 0, 0, 1, 1)

        self.label = QLabel(self.tab_1)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 1)

        self.sb__consumptionYear = QSpinBox(self.tab_1)
        self.sb__consumptionYear.setObjectName(u"sb__consumptionYear")
        self.sb__consumptionYear.setMaximum(20000)
        self.sb__consumptionYear.setValue(5840)

        self.gridLayout_2.addWidget(self.sb__consumptionYear, 1, 1, 1, 1)

        self.label_3 = QLabel(self.tab_1)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 1, 2, 1, 1)

        self.label_2 = QLabel(self.tab_1)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 2, 0, 1, 1)

        self.sb_rateHeat = QSpinBox(self.tab_1)
        self.sb_rateHeat.setObjectName(u"sb_rateHeat")
        self.sb_rateHeat.setValue(70)

        self.gridLayout_2.addWidget(self.sb_rateHeat, 2, 1, 1, 1)

        self.label_4 = QLabel(self.tab_1)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_2.addWidget(self.label_4, 2, 2, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.tw_consumption = QTableWidget(self.tab_1)
        if (self.tw_consumption.columnCount() < 1):
            self.tw_consumption.setColumnCount(1)
        __qtablewidgetitem = QTableWidgetItem()
        self.tw_consumption.setHorizontalHeaderItem(0, __qtablewidgetitem)
        if (self.tw_consumption.rowCount() < 12):
            self.tw_consumption.setRowCount(12)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tw_consumption.setVerticalHeaderItem(0, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tw_consumption.setVerticalHeaderItem(1, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tw_consumption.setVerticalHeaderItem(2, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tw_consumption.setVerticalHeaderItem(3, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tw_consumption.setVerticalHeaderItem(4, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tw_consumption.setVerticalHeaderItem(5, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tw_consumption.setVerticalHeaderItem(6, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tw_consumption.setVerticalHeaderItem(7, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tw_consumption.setVerticalHeaderItem(8, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tw_consumption.setVerticalHeaderItem(9, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tw_consumption.setVerticalHeaderItem(10, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tw_consumption.setVerticalHeaderItem(11, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tw_consumption.setItem(0, 0, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tw_consumption.setItem(1, 0, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tw_consumption.setItem(2, 0, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tw_consumption.setItem(3, 0, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tw_consumption.setItem(4, 0, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tw_consumption.setItem(5, 0, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tw_consumption.setItem(6, 0, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tw_consumption.setItem(7, 0, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tw_consumption.setItem(8, 0, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tw_consumption.setItem(9, 0, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tw_consumption.setItem(10, 0, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tw_consumption.setItem(11, 0, __qtablewidgetitem24)
        self.tw_consumption.setObjectName(u"tw_consumption")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.tw_consumption.sizePolicy().hasHeightForWidth())
        self.tw_consumption.setSizePolicy(sizePolicy2)
        self.tw_consumption.setRowCount(12)
        self.tw_consumption.horizontalHeader().setMinimumSectionSize(70)
        self.tw_consumption.horizontalHeader().setDefaultSectionSize(80)
        self.tw_consumption.horizontalHeader().setStretchLastSection(True)
        self.tw_consumption.verticalHeader().setStretchLastSection(False)

        self.horizontalLayout.addWidget(self.tw_consumption)

        self.tw_sun = QTableWidget(self.tab_1)
        if (self.tw_sun.columnCount() < 1):
            self.tw_sun.setColumnCount(1)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.tw_sun.setHorizontalHeaderItem(0, __qtablewidgetitem25)
        if (self.tw_sun.rowCount() < 12):
            self.tw_sun.setRowCount(12)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.tw_sun.setVerticalHeaderItem(0, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.tw_sun.setVerticalHeaderItem(1, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.tw_sun.setVerticalHeaderItem(2, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.tw_sun.setVerticalHeaderItem(3, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.tw_sun.setVerticalHeaderItem(4, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.tw_sun.setVerticalHeaderItem(5, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.tw_sun.setVerticalHeaderItem(6, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.tw_sun.setVerticalHeaderItem(7, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.tw_sun.setVerticalHeaderItem(8, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.tw_sun.setVerticalHeaderItem(9, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.tw_sun.setVerticalHeaderItem(10, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.tw_sun.setVerticalHeaderItem(11, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.tw_sun.setItem(0, 0, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        self.tw_sun.setItem(1, 0, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        self.tw_sun.setItem(2, 0, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        self.tw_sun.setItem(3, 0, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        self.tw_sun.setItem(4, 0, __qtablewidgetitem42)
        __qtablewidgetitem43 = QTableWidgetItem()
        self.tw_sun.setItem(5, 0, __qtablewidgetitem43)
        __qtablewidgetitem44 = QTableWidgetItem()
        self.tw_sun.setItem(6, 0, __qtablewidgetitem44)
        __qtablewidgetitem45 = QTableWidgetItem()
        self.tw_sun.setItem(7, 0, __qtablewidgetitem45)
        __qtablewidgetitem46 = QTableWidgetItem()
        self.tw_sun.setItem(8, 0, __qtablewidgetitem46)
        __qtablewidgetitem47 = QTableWidgetItem()
        self.tw_sun.setItem(9, 0, __qtablewidgetitem47)
        __qtablewidgetitem48 = QTableWidgetItem()
        self.tw_sun.setItem(10, 0, __qtablewidgetitem48)
        __qtablewidgetitem49 = QTableWidgetItem()
        self.tw_sun.setItem(11, 0, __qtablewidgetitem49)
        self.tw_sun.setObjectName(u"tw_sun")
        sizePolicy2.setHeightForWidth(self.tw_sun.sizePolicy().hasHeightForWidth())
        self.tw_sun.setSizePolicy(sizePolicy2)
        self.tw_sun.setRowCount(12)
        self.tw_sun.horizontalHeader().setMinimumSectionSize(70)
        self.tw_sun.horizontalHeader().setDefaultSectionSize(80)
        self.tw_sun.horizontalHeader().setStretchLastSection(True)
        self.tw_sun.verticalHeader().setStretchLastSection(False)

        self.horizontalLayout.addWidget(self.tw_sun)


        self.gridLayout_2.addLayout(self.horizontalLayout, 3, 0, 1, 3)

        self.tabWidget.addTab(self.tab_1, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.gridLayout_3 = QGridLayout(self.tab_4)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.lbl_unit_areaPanel = QLabel(self.tab_4)
        self.lbl_unit_areaPanel.setObjectName(u"lbl_unit_areaPanel")

        self.gridLayout_3.addWidget(self.lbl_unit_areaPanel, 5, 2, 1, 1)

        self.lbl_areaPanel = QLabel(self.tab_4)
        self.lbl_areaPanel.setObjectName(u"lbl_areaPanel")

        self.gridLayout_3.addWidget(self.lbl_areaPanel, 5, 0, 1, 1)

        self.pb_addPower = QPushButton(self.tab_4)
        self.pb_addPower.setObjectName(u"pb_addPower")
        icon = QIcon()
        icon.addFile(u"Images/plus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_addPower.setIcon(icon)

        self.gridLayout_3.addWidget(self.pb_addPower, 1, 2, 1, 1)

        self.lbl_unit_area = QLabel(self.tab_4)
        self.lbl_unit_area.setObjectName(u"lbl_unit_area")

        self.gridLayout_3.addWidget(self.lbl_unit_area, 4, 2, 1, 1)

        self.dsb_powerPanel = QDoubleSpinBox(self.tab_4)
        self.dsb_powerPanel.setObjectName(u"dsb_powerPanel")
        self.dsb_powerPanel.setMaximum(100.000000000000000)
        self.dsb_powerPanel.setSingleStep(0.050000000000000)

        self.gridLayout_3.addWidget(self.dsb_powerPanel, 6, 1, 1, 1)

        self.cb_power = QComboBox(self.tab_4)
        self.cb_power.addItem("")
        self.cb_power.setObjectName(u"cb_power")

        self.gridLayout_3.addWidget(self.cb_power, 1, 0, 1, 2)

        self.tw_addPower = QTableWidget(self.tab_4)
        if (self.tw_addPower.columnCount() < 3):
            self.tw_addPower.setColumnCount(3)
        __qtablewidgetitem50 = QTableWidgetItem()
        self.tw_addPower.setHorizontalHeaderItem(0, __qtablewidgetitem50)
        __qtablewidgetitem51 = QTableWidgetItem()
        self.tw_addPower.setHorizontalHeaderItem(1, __qtablewidgetitem51)
        __qtablewidgetitem52 = QTableWidgetItem()
        self.tw_addPower.setHorizontalHeaderItem(2, __qtablewidgetitem52)
        self.tw_addPower.setObjectName(u"tw_addPower")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.tw_addPower.sizePolicy().hasHeightForWidth())
        self.tw_addPower.setSizePolicy(sizePolicy3)
        self.tw_addPower.setMinimumSize(QSize(0, 100))
        self.tw_addPower.setMaximumSize(QSize(16777215, 1000000))
        self.tw_addPower.horizontalHeader().setMinimumSectionSize(300)
        self.tw_addPower.horizontalHeader().setDefaultSectionSize(300)
        self.tw_addPower.horizontalHeader().setStretchLastSection(False)
        self.tw_addPower.verticalHeader().setMinimumSectionSize(15)
        self.tw_addPower.verticalHeader().setDefaultSectionSize(30)
        self.tw_addPower.verticalHeader().setStretchLastSection(False)

        self.gridLayout_3.addWidget(self.tw_addPower, 3, 0, 1, 4)

        self.pb_savePower = QPushButton(self.tab_4)
        self.pb_savePower.setObjectName(u"pb_savePower")
        icon1 = QIcon()
        icon1.addFile(u"Images/save.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_savePower.setIcon(icon1)

        self.gridLayout_3.addWidget(self.pb_savePower, 7, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_2, 1, 3, 1, 1)

        self.lbl_surface = QLabel(self.tab_4)
        self.lbl_surface.setObjectName(u"lbl_surface")

        self.gridLayout_3.addWidget(self.lbl_surface, 4, 0, 1, 1)

        self.line = QFrame(self.tab_4)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout_3.addWidget(self.line, 2, 0, 1, 4)

        self.dsb_area = QDoubleSpinBox(self.tab_4)
        self.dsb_area.setObjectName(u"dsb_area")
        self.dsb_area.setMaximum(1000.000000000000000)

        self.gridLayout_3.addWidget(self.dsb_area, 4, 1, 1, 1)

        self.label_7 = QLabel(self.tab_4)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_3.addWidget(self.label_7, 0, 0, 1, 1)

        self.lbl_unit_power = QLabel(self.tab_4)
        self.lbl_unit_power.setObjectName(u"lbl_unit_power")

        self.gridLayout_3.addWidget(self.lbl_unit_power, 6, 2, 1, 1)

        self.dsb_areaPanel = QDoubleSpinBox(self.tab_4)
        self.dsb_areaPanel.setObjectName(u"dsb_areaPanel")

        self.gridLayout_3.addWidget(self.dsb_areaPanel, 5, 1, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 485, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_3, 8, 0, 1, 1)

        self.lbl_power = QLabel(self.tab_4)
        self.lbl_power.setObjectName(u"lbl_power")

        self.gridLayout_3.addWidget(self.lbl_power, 6, 0, 1, 1)

        self.tabWidget.addTab(self.tab_4, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_4 = QGridLayout(self.tab_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.lbl_countBat = QLabel(self.tab_2)
        self.lbl_countBat.setObjectName(u"lbl_countBat")

        self.gridLayout_4.addWidget(self.lbl_countBat, 3, 0, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(584, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_3, 1, 3, 1, 1)

        self.label_8 = QLabel(self.tab_2)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_4.addWidget(self.label_8, 0, 0, 1, 1)

        self.cb_storage = QComboBox(self.tab_2)
        self.cb_storage.addItem("")
        self.cb_storage.addItem("")
        self.cb_storage.addItem("")
        self.cb_storage.setObjectName(u"cb_storage")

        self.gridLayout_4.addWidget(self.cb_storage, 1, 0, 1, 2)

        self.sb_countBat = QSpinBox(self.tab_2)
        self.sb_countBat.setObjectName(u"sb_countBat")
        self.sb_countBat.setMaximum(9999)
        self.sb_countBat.setValue(20)

        self.gridLayout_4.addWidget(self.sb_countBat, 3, 1, 1, 1)

        self.pb_addStorage = QPushButton(self.tab_2)
        self.pb_addStorage.setObjectName(u"pb_addStorage")
        self.pb_addStorage.setIcon(icon)

        self.gridLayout_4.addWidget(self.pb_addStorage, 1, 2, 1, 1)

        self.lbl_unit_volumeSalt = QLabel(self.tab_2)
        self.lbl_unit_volumeSalt.setObjectName(u"lbl_unit_volumeSalt")

        self.gridLayout_4.addWidget(self.lbl_unit_volumeSalt, 7, 2, 1, 1)

        self.lbl_volumeSalt = QLabel(self.tab_2)
        self.lbl_volumeSalt.setObjectName(u"lbl_volumeSalt")

        self.gridLayout_4.addWidget(self.lbl_volumeSalt, 7, 0, 1, 1)

        self.lbl_unit_selfDischarge = QLabel(self.tab_2)
        self.lbl_unit_selfDischarge.setObjectName(u"lbl_unit_selfDischarge")

        self.gridLayout_4.addWidget(self.lbl_unit_selfDischarge, 6, 2, 1, 1)

        self.lbl_unitPressure = QLabel(self.tab_2)
        self.lbl_unitPressure.setObjectName(u"lbl_unitPressure")

        self.gridLayout_4.addWidget(self.lbl_unitPressure, 9, 2, 1, 1)

        self.lbl_unit_capacity = QLabel(self.tab_2)
        self.lbl_unit_capacity.setObjectName(u"lbl_unit_capacity")

        self.gridLayout_4.addWidget(self.lbl_unit_capacity, 5, 2, 1, 1)

        self.lbl_cap = QLabel(self.tab_2)
        self.lbl_cap.setObjectName(u"lbl_cap")

        self.gridLayout_4.addWidget(self.lbl_cap, 5, 0, 1, 1)

        self.lbl_unit_energySalt = QLabel(self.tab_2)
        self.lbl_unit_energySalt.setObjectName(u"lbl_unit_energySalt")

        self.gridLayout_4.addWidget(self.lbl_unit_energySalt, 8, 2, 1, 1)

        self.dsb_discharge = QDoubleSpinBox(self.tab_2)
        self.dsb_discharge.setObjectName(u"dsb_discharge")
        self.dsb_discharge.setValue(20.000000000000000)

        self.gridLayout_4.addWidget(self.dsb_discharge, 6, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer, 12, 0, 1, 1)

        self.cb_pressure = QComboBox(self.tab_2)
        self.cb_pressure.addItem("")
        self.cb_pressure.addItem("")
        self.cb_pressure.addItem("")
        self.cb_pressure.setObjectName(u"cb_pressure")

        self.gridLayout_4.addWidget(self.cb_pressure, 9, 1, 1, 1)

        self.dsb_energySalt = QDoubleSpinBox(self.tab_2)
        self.dsb_energySalt.setObjectName(u"dsb_energySalt")
        self.dsb_energySalt.setMaximum(1000.000000000000000)
        self.dsb_energySalt.setValue(10.000000000000000)

        self.gridLayout_4.addWidget(self.dsb_energySalt, 7, 1, 1, 1)

        self.lbl_unit_voltage = QLabel(self.tab_2)
        self.lbl_unit_voltage.setObjectName(u"lbl_unit_voltage")

        self.gridLayout_4.addWidget(self.lbl_unit_voltage, 4, 2, 1, 1)

        self.lbl_selfDischargeRate = QLabel(self.tab_2)
        self.lbl_selfDischargeRate.setObjectName(u"lbl_selfDischargeRate")

        self.gridLayout_4.addWidget(self.lbl_selfDischargeRate, 6, 0, 1, 1)

        self.lbl_pressure = QLabel(self.tab_2)
        self.lbl_pressure.setObjectName(u"lbl_pressure")

        self.gridLayout_4.addWidget(self.lbl_pressure, 9, 0, 1, 1)

        self.tw_addStorage = QTableWidget(self.tab_2)
        if (self.tw_addStorage.columnCount() < 3):
            self.tw_addStorage.setColumnCount(3)
        __qtablewidgetitem53 = QTableWidgetItem()
        self.tw_addStorage.setHorizontalHeaderItem(0, __qtablewidgetitem53)
        __qtablewidgetitem54 = QTableWidgetItem()
        self.tw_addStorage.setHorizontalHeaderItem(1, __qtablewidgetitem54)
        __qtablewidgetitem55 = QTableWidgetItem()
        self.tw_addStorage.setHorizontalHeaderItem(2, __qtablewidgetitem55)
        self.tw_addStorage.setObjectName(u"tw_addStorage")
        sizePolicy3.setHeightForWidth(self.tw_addStorage.sizePolicy().hasHeightForWidth())
        self.tw_addStorage.setSizePolicy(sizePolicy3)
        self.tw_addStorage.setMinimumSize(QSize(0, 100))
        self.tw_addStorage.setMaximumSize(QSize(16777215, 1000000))
        self.tw_addStorage.horizontalHeader().setMinimumSectionSize(120)
        self.tw_addStorage.horizontalHeader().setDefaultSectionSize(250)
        self.tw_addStorage.horizontalHeader().setStretchLastSection(True)
        self.tw_addStorage.verticalHeader().setMinimumSectionSize(15)
        self.tw_addStorage.verticalHeader().setDefaultSectionSize(30)
        self.tw_addStorage.verticalHeader().setStretchLastSection(False)

        self.gridLayout_4.addWidget(self.tw_addStorage, 2, 0, 1, 4)

        self.lbl_voltage = QLabel(self.tab_2)
        self.lbl_voltage.setObjectName(u"lbl_voltage")

        self.gridLayout_4.addWidget(self.lbl_voltage, 4, 0, 1, 1)

        self.pb_saveStorage = QPushButton(self.tab_2)
        self.pb_saveStorage.setObjectName(u"pb_saveStorage")
        self.pb_saveStorage.setIcon(icon1)

        self.gridLayout_4.addWidget(self.pb_saveStorage, 11, 0, 1, 1)

        self.lbl_energySalt = QLabel(self.tab_2)
        self.lbl_energySalt.setObjectName(u"lbl_energySalt")

        self.gridLayout_4.addWidget(self.lbl_energySalt, 8, 0, 1, 1)

        self.dsb_voltage = QDoubleSpinBox(self.tab_2)
        self.dsb_voltage.setObjectName(u"dsb_voltage")
        self.dsb_voltage.setValue(12.000000000000000)

        self.gridLayout_4.addWidget(self.dsb_voltage, 4, 1, 1, 1)

        self.dsb_energyMCube = QDoubleSpinBox(self.tab_2)
        self.dsb_energyMCube.setObjectName(u"dsb_energyMCube")
        self.dsb_energyMCube.setMaximum(2000.000000000000000)
        self.dsb_energyMCube.setValue(300.000000000000000)

        self.gridLayout_4.addWidget(self.dsb_energyMCube, 8, 1, 1, 1)

        self.dsb_capacity = QDoubleSpinBox(self.tab_2)
        self.dsb_capacity.setObjectName(u"dsb_capacity")
        self.dsb_capacity.setMaximum(1000.000000000000000)
        self.dsb_capacity.setValue(290.000000000000000)

        self.gridLayout_4.addWidget(self.dsb_capacity, 5, 1, 1, 1)

        self.lbl_volumeHydrogen = QLabel(self.tab_2)
        self.lbl_volumeHydrogen.setObjectName(u"lbl_volumeHydrogen")

        self.gridLayout_4.addWidget(self.lbl_volumeHydrogen, 10, 0, 1, 1)

        self.lbl_unitVolumHydrogen = QLabel(self.tab_2)
        self.lbl_unitVolumHydrogen.setObjectName(u"lbl_unitVolumHydrogen")

        self.gridLayout_4.addWidget(self.lbl_unitVolumHydrogen, 10, 2, 1, 1)

        self.dsb_volumeHydrogen = QDoubleSpinBox(self.tab_2)
        self.dsb_volumeHydrogen.setObjectName(u"dsb_volumeHydrogen")
        self.dsb_volumeHydrogen.setMaximum(200.000000000000000)
        self.dsb_volumeHydrogen.setValue(10.000000000000000)

        self.gridLayout_4.addWidget(self.dsb_volumeHydrogen, 10, 1, 1, 1)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.tab_5.sizePolicy().hasHeightForWidth())
        self.tab_5.setSizePolicy(sizePolicy4)
        self.gridLayout = QGridLayout(self.tab_5)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pb_nextStorage = QPushButton(self.tab_5)
        self.pb_nextStorage.setObjectName(u"pb_nextStorage")
        icon2 = QIcon()
        icon2.addFile(u"Images/right.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_nextStorage.setIcon(icon2)

        self.gridLayout.addWidget(self.pb_nextStorage, 0, 6, 1, 1)

        self.sb_animateTimeStorage = QSpinBox(self.tab_5)
        self.sb_animateTimeStorage.setObjectName(u"sb_animateTimeStorage")
        self.sb_animateTimeStorage.setMaximum(20000)
        self.sb_animateTimeStorage.setValue(200)

        self.gridLayout.addWidget(self.sb_animateTimeStorage, 0, 4, 1, 1)

        self.pb_previousStorage = QPushButton(self.tab_5)
        self.pb_previousStorage.setObjectName(u"pb_previousStorage")
        icon3 = QIcon()
        icon3.addFile(u"Images/left.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_previousStorage.setIcon(icon3)

        self.gridLayout.addWidget(self.pb_previousStorage, 0, 0, 1, 1)

        self.graph_hydrogen = PlotWidget(self.tab_5)
        self.graph_hydrogen.setObjectName(u"graph_hydrogen")
        sizePolicy5 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.graph_hydrogen.sizePolicy().hasHeightForWidth())
        self.graph_hydrogen.setSizePolicy(sizePolicy5)

        self.gridLayout.addWidget(self.graph_hydrogen, 3, 0, 1, 7)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 2, 1, 1)

        self.lbl_startStorage = QLabel(self.tab_5)
        self.lbl_startStorage.setObjectName(u"lbl_startStorage")

        self.gridLayout.addWidget(self.lbl_startStorage, 0, 1, 1, 1)

        self.graph_salt = PlotWidget(self.tab_5)
        self.graph_salt.setObjectName(u"graph_salt")
        sizePolicy5.setHeightForWidth(self.graph_salt.sizePolicy().hasHeightForWidth())
        self.graph_salt.setSizePolicy(sizePolicy5)

        self.gridLayout.addWidget(self.graph_salt, 2, 0, 1, 7)

        self.pb_animateStorage = QPushButton(self.tab_5)
        self.pb_animateStorage.setObjectName(u"pb_animateStorage")
        icon4 = QIcon()
        icon4.addFile(u"Images/clap.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_animateStorage.setIcon(icon4)

        self.gridLayout.addWidget(self.pb_animateStorage, 0, 3, 1, 1)

        self.graph_battery = PlotWidget(self.tab_5)
        self.graph_battery.setObjectName(u"graph_battery")
        sizePolicy5.setHeightForWidth(self.graph_battery.sizePolicy().hasHeightForWidth())
        self.graph_battery.setSizePolicy(sizePolicy5)

        self.gridLayout.addWidget(self.graph_battery, 1, 0, 1, 7)

        self.label_9 = QLabel(self.tab_5)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout.addWidget(self.label_9, 0, 5, 1, 1)

        self.tabWidget.addTab(self.tab_5, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_5 = QGridLayout(self.tab)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_4, 0, 2, 1, 1)

        self.label_6 = QLabel(self.tab)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_5.addWidget(self.label_6, 0, 7, 1, 1)

        self.pb_previousPower = QPushButton(self.tab)
        self.pb_previousPower.setObjectName(u"pb_previousPower")
        self.pb_previousPower.setIcon(icon3)

        self.gridLayout_5.addWidget(self.pb_previousPower, 0, 0, 1, 1)

        self.lbl_startPower = QLabel(self.tab)
        self.lbl_startPower.setObjectName(u"lbl_startPower")

        self.gridLayout_5.addWidget(self.lbl_startPower, 0, 1, 1, 1)

        self.pb_nextPower = QPushButton(self.tab)
        self.pb_nextPower.setObjectName(u"pb_nextPower")
        self.pb_nextPower.setIcon(icon2)

        self.gridLayout_5.addWidget(self.pb_nextPower, 0, 8, 1, 1)

        self.graph_panels = PlotWidget(self.tab)
        self.graph_panels.setObjectName(u"graph_panels")
        sizePolicy4.setHeightForWidth(self.graph_panels.sizePolicy().hasHeightForWidth())
        self.graph_panels.setSizePolicy(sizePolicy4)

        self.gridLayout_5.addWidget(self.graph_panels, 1, 0, 1, 9)

        self.pb_animatePower = QPushButton(self.tab)
        self.pb_animatePower.setObjectName(u"pb_animatePower")
        self.pb_animatePower.setIcon(icon4)

        self.gridLayout_5.addWidget(self.pb_animatePower, 0, 3, 1, 1)

        self.sb_animateTimePower = QSpinBox(self.tab)
        self.sb_animateTimePower.setObjectName(u"sb_animateTimePower")
        self.sb_animateTimePower.setMaximum(20000)
        self.sb_animateTimePower.setValue(200)

        self.gridLayout_5.addWidget(self.sb_animateTimePower, 0, 6, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayout_7 = QGridLayout(self.tab_3)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.pb_nextBilan = QPushButton(self.tab_3)
        self.pb_nextBilan.setObjectName(u"pb_nextBilan")
        self.pb_nextBilan.setIcon(icon2)

        self.gridLayout_7.addWidget(self.pb_nextBilan, 0, 6, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_5, 0, 2, 1, 1)

        self.graph_bilan = PlotWidget(self.tab_3)
        self.graph_bilan.setObjectName(u"graph_bilan")
        sizePolicy4.setHeightForWidth(self.graph_bilan.sizePolicy().hasHeightForWidth())
        self.graph_bilan.setSizePolicy(sizePolicy4)

        self.gridLayout_7.addWidget(self.graph_bilan, 1, 0, 1, 7)

        self.lbl_startBilan = QLabel(self.tab_3)
        self.lbl_startBilan.setObjectName(u"lbl_startBilan")

        self.gridLayout_7.addWidget(self.lbl_startBilan, 0, 1, 1, 1)

        self.sb_animateTimeBilan = QSpinBox(self.tab_3)
        self.sb_animateTimeBilan.setObjectName(u"sb_animateTimeBilan")
        self.sb_animateTimeBilan.setMaximum(20000)
        self.sb_animateTimeBilan.setValue(200)
        self.sb_animateTimeBilan.setDisplayIntegerBase(10)

        self.gridLayout_7.addWidget(self.sb_animateTimeBilan, 0, 4, 1, 1)

        self.pb_animateBilan = QPushButton(self.tab_3)
        self.pb_animateBilan.setObjectName(u"pb_animateBilan")
        self.pb_animateBilan.setIcon(icon4)

        self.gridLayout_7.addWidget(self.pb_animateBilan, 0, 3, 1, 1)

        self.pb_previousBilan = QPushButton(self.tab_3)
        self.pb_previousBilan.setObjectName(u"pb_previousBilan")
        self.pb_previousBilan.setIcon(icon3)

        self.gridLayout_7.addWidget(self.pb_previousBilan, 0, 0, 1, 1)

        self.label_10 = QLabel(self.tab_3)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_7.addWidget(self.label_10, 0, 5, 1, 1)

        self.tabWidget.addTab(self.tab_3, "")

        self.gridLayout_8.addWidget(self.tabWidget, 0, 0, 1, 2)

        self.pb_run = QPushButton(self.centralwidget)
        self.pb_run.setObjectName(u"pb_run")
        palette = QPalette()
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(46, 194, 126, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(96, 255, 182, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush2)
        brush3 = QBrush(QColor(71, 224, 154, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        brush4 = QBrush(QColor(23, 97, 63, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush4)
        brush5 = QBrush(QColor(31, 129, 84, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        brush6 = QBrush(QColor(255, 255, 255, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush6)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush6)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush)
        brush7 = QBrush(QColor(150, 224, 190, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush7)
        brush8 = QBrush(QColor(255, 255, 220, 255))
        brush8.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush8)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        brush9 = QBrush(QColor(239, 239, 239, 255))
        brush9.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush9)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush6)
        brush10 = QBrush(QColor(202, 202, 202, 255))
        brush10.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush10)
        brush11 = QBrush(QColor(159, 159, 159, 255))
        brush11.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush11)
        brush12 = QBrush(QColor(184, 184, 184, 255))
        brush12.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush12)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush9)
        brush13 = QBrush(QColor(118, 118, 118, 255))
        brush13.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush13)
        brush14 = QBrush(QColor(247, 247, 247, 255))
        brush14.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush14)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush8)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush6)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        brush15 = QBrush(QColor(177, 177, 177, 255))
        brush15.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush15)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush14)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush8)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush)
        self.pb_run.setPalette(palette)

        self.gridLayout_8.addWidget(self.pb_run, 1, 1, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_6, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1013, 22))
        self.menuFichiers = QMenu(self.menubar)
        self.menuFichiers.setObjectName(u"menuFichiers")
        self.menuA_propos = QMenu(self.menubar)
        self.menuA_propos.setObjectName(u"menuA_propos")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFichiers.menuAction())
        self.menubar.addAction(self.menuA_propos.menuAction())
        self.menuA_propos.addAction(self.actionVersion)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Application stockage", None))
        self.actionVersion.setText(QCoreApplication.translate("MainWindow", u"Version", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:22pt; font-weight:700;\">Installation solaire \u00e0 Kujjijak</span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Energie annuelle", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"kWh", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Pourcentage du chauffage", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"%", None))
        ___qtablewidgetitem = self.tw_consumption.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Energie consomm\u00e9e (kWh)", None));
        ___qtablewidgetitem1 = self.tw_consumption.verticalHeaderItem(0)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Janvier", None));
        ___qtablewidgetitem2 = self.tw_consumption.verticalHeaderItem(1)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"F\u00e9vrier", None));
        ___qtablewidgetitem3 = self.tw_consumption.verticalHeaderItem(2)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Mars", None));
        ___qtablewidgetitem4 = self.tw_consumption.verticalHeaderItem(3)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Avril", None));
        ___qtablewidgetitem5 = self.tw_consumption.verticalHeaderItem(4)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Mai", None));
        ___qtablewidgetitem6 = self.tw_consumption.verticalHeaderItem(5)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Juin", None));
        ___qtablewidgetitem7 = self.tw_consumption.verticalHeaderItem(6)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Juillet", None));
        ___qtablewidgetitem8 = self.tw_consumption.verticalHeaderItem(7)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Aout", None));
        ___qtablewidgetitem9 = self.tw_consumption.verticalHeaderItem(8)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Septembre", None));
        ___qtablewidgetitem10 = self.tw_consumption.verticalHeaderItem(9)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Octobre", None));
        ___qtablewidgetitem11 = self.tw_consumption.verticalHeaderItem(10)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Novembre", None));
        ___qtablewidgetitem12 = self.tw_consumption.verticalHeaderItem(11)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"D\u00e9cembre", None));

        __sortingEnabled = self.tw_consumption.isSortingEnabled()
        self.tw_consumption.setSortingEnabled(False)
        ___qtablewidgetitem13 = self.tw_consumption.item(0, 0)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"590", None));
        ___qtablewidgetitem14 = self.tw_consumption.item(1, 0)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"542", None));
        ___qtablewidgetitem15 = self.tw_consumption.item(2, 0)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"560", None));
        ___qtablewidgetitem16 = self.tw_consumption.item(3, 0)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"472", None));
        ___qtablewidgetitem17 = self.tw_consumption.item(4, 0)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"436", None));
        ___qtablewidgetitem18 = self.tw_consumption.item(5, 0)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"407", None));
        ___qtablewidgetitem19 = self.tw_consumption.item(6, 0)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"413", None));
        ___qtablewidgetitem20 = self.tw_consumption.item(7, 0)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"420", None));
        ___qtablewidgetitem21 = self.tw_consumption.item(8, 0)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"439", None));
        ___qtablewidgetitem22 = self.tw_consumption.item(9, 0)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"491", None));
        ___qtablewidgetitem23 = self.tw_consumption.item(10, 0)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"520", None));
        ___qtablewidgetitem24 = self.tw_consumption.item(11, 0)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"551", None));
        self.tw_consumption.setSortingEnabled(__sortingEnabled)

        ___qtablewidgetitem25 = self.tw_sun.horizontalHeaderItem(0)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"Ensoleillement (h)", None));
        ___qtablewidgetitem26 = self.tw_sun.verticalHeaderItem(0)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"Janvier", None));
        ___qtablewidgetitem27 = self.tw_sun.verticalHeaderItem(1)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"F\u00e9vrier", None));
        ___qtablewidgetitem28 = self.tw_sun.verticalHeaderItem(2)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"Mars", None));
        ___qtablewidgetitem29 = self.tw_sun.verticalHeaderItem(3)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"Avril", None));
        ___qtablewidgetitem30 = self.tw_sun.verticalHeaderItem(4)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"Mai", None));
        ___qtablewidgetitem31 = self.tw_sun.verticalHeaderItem(5)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"Juin", None));
        ___qtablewidgetitem32 = self.tw_sun.verticalHeaderItem(6)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"Juillet", None));
        ___qtablewidgetitem33 = self.tw_sun.verticalHeaderItem(7)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"Aout", None));
        ___qtablewidgetitem34 = self.tw_sun.verticalHeaderItem(8)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"Septembre", None));
        ___qtablewidgetitem35 = self.tw_sun.verticalHeaderItem(9)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MainWindow", u"Octobre", None));
        ___qtablewidgetitem36 = self.tw_sun.verticalHeaderItem(10)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("MainWindow", u"Novembre", None));
        ___qtablewidgetitem37 = self.tw_sun.verticalHeaderItem(11)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("MainWindow", u"D\u00e9cembre", None));

        __sortingEnabled1 = self.tw_sun.isSortingEnabled()
        self.tw_sun.setSortingEnabled(False)
        ___qtablewidgetitem38 = self.tw_sun.item(0, 0)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("MainWindow", u"1.2", None));
        ___qtablewidgetitem39 = self.tw_sun.item(1, 0)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("MainWindow", u"3.4", None));
        ___qtablewidgetitem40 = self.tw_sun.item(2, 0)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("MainWindow", u"5.5", None));
        ___qtablewidgetitem41 = self.tw_sun.item(3, 0)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("MainWindow", u"7.5", None));
        ___qtablewidgetitem42 = self.tw_sun.item(4, 0)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("MainWindow", u"6.4", None));
        ___qtablewidgetitem43 = self.tw_sun.item(5, 0)
        ___qtablewidgetitem43.setText(QCoreApplication.translate("MainWindow", u"6.3", None));
        ___qtablewidgetitem44 = self.tw_sun.item(6, 0)
        ___qtablewidgetitem44.setText(QCoreApplication.translate("MainWindow", u"6.9", None));
        ___qtablewidgetitem45 = self.tw_sun.item(7, 0)
        ___qtablewidgetitem45.setText(QCoreApplication.translate("MainWindow", u"5.2", None));
        ___qtablewidgetitem46 = self.tw_sun.item(8, 0)
        ___qtablewidgetitem46.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem47 = self.tw_sun.item(9, 0)
        ___qtablewidgetitem47.setText(QCoreApplication.translate("MainWindow", u"1.8", None));
        ___qtablewidgetitem48 = self.tw_sun.item(10, 0)
        ___qtablewidgetitem48.setText(QCoreApplication.translate("MainWindow", u"1.5", None));
        ___qtablewidgetitem49 = self.tw_sun.item(11, 0)
        ___qtablewidgetitem49.setText(QCoreApplication.translate("MainWindow", u"0.7", None));
        self.tw_sun.setSortingEnabled(__sortingEnabled1)

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), QCoreApplication.translate("MainWindow", u"R\u00e9sidence", None))
        self.lbl_unit_areaPanel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>m<span style=\" vertical-align:super;\">2</span></p></body></html>", None))
        self.lbl_areaPanel.setText(QCoreApplication.translate("MainWindow", u"Surface d'un panneau", None))
        self.pb_addPower.setText(QCoreApplication.translate("MainWindow", u"  Ajouter", None))
        self.lbl_unit_area.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>m<span style=\" vertical-align:super;\">2</span></p></body></html>", None))
        self.cb_power.setItemText(0, QCoreApplication.translate("MainWindow", u"Panneaux solaires", None))

        ___qtablewidgetitem50 = self.tw_addPower.horizontalHeaderItem(0)
        ___qtablewidgetitem50.setText(QCoreApplication.translate("MainWindow", u"Moyens de production", None));
        self.pb_savePower.setText(QCoreApplication.translate("MainWindow", u"  Enregistrer", None))
        self.lbl_surface.setText(QCoreApplication.translate("MainWindow", u"Surface", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Liste des moyens de production", None))
        self.lbl_unit_power.setText(QCoreApplication.translate("MainWindow", u"kW", None))
        self.lbl_power.setText(QCoreApplication.translate("MainWindow", u"Puissance cr\u00eate", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"Productions", None))
        self.lbl_countBat.setText(QCoreApplication.translate("MainWindow", u"Nombre de batteries", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Liste des moyens de stockage", None))
        self.cb_storage.setItemText(0, QCoreApplication.translate("MainWindow", u"Batterie_plomb", None))
        self.cb_storage.setItemText(1, QCoreApplication.translate("MainWindow", u"Sel", None))
        self.cb_storage.setItemText(2, QCoreApplication.translate("MainWindow", u"Hydrog\u00e8ne", None))

        self.pb_addStorage.setText(QCoreApplication.translate("MainWindow", u"  Ajouter", None))
        self.lbl_unit_volumeSalt.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>m<span style=\" vertical-align:super;\">3</span></p></body></html>", None))
        self.lbl_volumeSalt.setText(QCoreApplication.translate("MainWindow", u"Volume de sel", None))
        self.lbl_unit_selfDischarge.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.lbl_unitPressure.setText(QCoreApplication.translate("MainWindow", u"bars", None))
        self.lbl_unit_capacity.setText(QCoreApplication.translate("MainWindow", u"Ah", None))
        self.lbl_cap.setText(QCoreApplication.translate("MainWindow", u"Capacit\u00e9 d'une batterie", None))
        self.lbl_unit_energySalt.setText(QCoreApplication.translate("MainWindow", u"kWh", None))
        self.cb_pressure.setItemText(0, QCoreApplication.translate("MainWindow", u"700", None))
        self.cb_pressure.setItemText(1, QCoreApplication.translate("MainWindow", u"500", None))
        self.cb_pressure.setItemText(2, QCoreApplication.translate("MainWindow", u"300", None))

        self.lbl_unit_voltage.setText(QCoreApplication.translate("MainWindow", u"V", None))
        self.lbl_selfDischargeRate.setText(QCoreApplication.translate("MainWindow", u"Autod\u00e9charge", None))
        self.lbl_pressure.setText(QCoreApplication.translate("MainWindow", u"Pression de l'hydrog\u00e8ne", None))
        ___qtablewidgetitem51 = self.tw_addStorage.horizontalHeaderItem(0)
        ___qtablewidgetitem51.setText(QCoreApplication.translate("MainWindow", u"Moyens de stockage", None));
        self.lbl_voltage.setText(QCoreApplication.translate("MainWindow", u"Tension des batteries", None))
        self.pb_saveStorage.setText(QCoreApplication.translate("MainWindow", u"Enregistrer", None))
        self.lbl_energySalt.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Energie par m<span style=\" vertical-align:super;\">3</span></p></body></html>", None))
        self.lbl_volumeHydrogen.setText(QCoreApplication.translate("MainWindow", u"Volume d'hydrog\u00e8ne", None))
        self.lbl_unitVolumHydrogen.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>m<span style=\" vertical-align:super;\">3</span></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Stockage", None))
        self.pb_nextStorage.setText(QCoreApplication.translate("MainWindow", u"Mois suivant", None))
        self.pb_previousStorage.setText(QCoreApplication.translate("MainWindow", u"Mois pr\u00e9c\u00e9dent", None))
        self.lbl_startStorage.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>D\u00e9but de la simulation au mois de Janvier</p></body></html>", None))
        self.pb_animateStorage.setText(QCoreApplication.translate("MainWindow", u"Animer", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"(ms)", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"R\u00e9sultats stockage", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"(ms)", None))
        self.pb_previousPower.setText(QCoreApplication.translate("MainWindow", u"Mois pr\u00e9c\u00e9dent", None))
        self.lbl_startPower.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>D\u00e9but de la simulation au mois de Janvier</p></body></html>", None))
        self.pb_nextPower.setText(QCoreApplication.translate("MainWindow", u"Mois suivant", None))
        self.pb_animatePower.setText(QCoreApplication.translate("MainWindow", u"Animer", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"R\u00e9sultats de production", None))
        self.pb_nextBilan.setText(QCoreApplication.translate("MainWindow", u"Mois suivant", None))
        self.lbl_startBilan.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>D\u00e9but de la simulation au mois de Janvier</p></body></html>", None))
        self.pb_animateBilan.setText(QCoreApplication.translate("MainWindow", u"Animer", None))
        self.pb_previousBilan.setText(QCoreApplication.translate("MainWindow", u"Mois pr\u00e9c\u00e9dent", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"(ms)", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Bilan \u00e9nerg\u00e9tique", None))
        self.pb_run.setText(QCoreApplication.translate("MainWindow", u"Simuler (F5)", None))
        self.menuFichiers.setTitle(QCoreApplication.translate("MainWindow", u"Fichiers", None))
        self.menuA_propos.setTitle(QCoreApplication.translate("MainWindow", u"A propos", None))
    # retranslateUi

