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


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(992, 740)
        MainWindow.setMinimumSize(QSize(0, 0))
        MainWindow.setWindowOpacity(0.500000000000000)
        MainWindow.setDocumentMode(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 2, 2, 1, 1)

        self.pb_openPort = QPushButton(self.centralwidget)
        self.pb_openPort.setObjectName(u"pb_openPort")
        palette = QPalette()
        brush = QBrush(QColor(138, 226, 52, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush)
        self.pb_openPort.setPalette(palette)

        self.gridLayout.addWidget(self.pb_openPort, 2, 1, 1, 1)

        self.pb_progressBar = QProgressBar(self.centralwidget)
        self.pb_progressBar.setObjectName(u"pb_progressBar")
        self.pb_progressBar.setValue(0)

        self.gridLayout.addWidget(self.pb_progressBar, 2, 3, 1, 1)

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab_1 = QWidget()
        self.tab_1.setObjectName(u"tab_1")
        self.gridLayout_2 = QGridLayout(self.tab_1)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_2 = QLabel(self.tab_1)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 2, 0, 1, 1)

        self.label = QLabel(self.tab_1)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 1)

        self.label_4 = QLabel(self.tab_1)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_2.addWidget(self.label_4, 2, 3, 1, 1)

        self.label_5 = QLabel(self.tab_1)
        self.label_5.setObjectName(u"label_5")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.label_5, 0, 0, 1, 4)

        self.label_3 = QLabel(self.tab_1)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 1, 3, 1, 1)

        self.tw_consumption = QTableWidget(self.tab_1)
        if (self.tw_consumption.columnCount() < 12):
            self.tw_consumption.setColumnCount(12)
        __qtablewidgetitem = QTableWidgetItem()
        self.tw_consumption.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tw_consumption.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tw_consumption.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tw_consumption.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tw_consumption.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tw_consumption.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tw_consumption.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tw_consumption.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tw_consumption.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tw_consumption.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tw_consumption.setHorizontalHeaderItem(10, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tw_consumption.setHorizontalHeaderItem(11, __qtablewidgetitem11)
        if (self.tw_consumption.rowCount() < 1):
            self.tw_consumption.setRowCount(1)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tw_consumption.setItem(0, 0, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tw_consumption.setItem(0, 1, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tw_consumption.setItem(0, 2, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tw_consumption.setItem(0, 3, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tw_consumption.setItem(0, 4, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tw_consumption.setItem(0, 5, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tw_consumption.setItem(0, 6, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tw_consumption.setItem(0, 7, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tw_consumption.setItem(0, 8, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tw_consumption.setItem(0, 9, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tw_consumption.setItem(0, 10, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tw_consumption.setItem(0, 11, __qtablewidgetitem23)
        self.tw_consumption.setObjectName(u"tw_consumption")
        self.tw_consumption.setRowCount(1)
        self.tw_consumption.horizontalHeader().setMinimumSectionSize(70)
        self.tw_consumption.horizontalHeader().setDefaultSectionSize(80)
        self.tw_consumption.horizontalHeader().setStretchLastSection(True)
        self.tw_consumption.verticalHeader().setStretchLastSection(True)

        self.gridLayout_2.addWidget(self.tw_consumption, 3, 0, 1, 4)

        self.sb__consumptionYear = QSpinBox(self.tab_1)
        self.sb__consumptionYear.setObjectName(u"sb__consumptionYear")
        self.sb__consumptionYear.setMaximum(20000)
        self.sb__consumptionYear.setValue(5840)

        self.gridLayout_2.addWidget(self.sb__consumptionYear, 1, 1, 1, 1)

        self.sb_rateHeat = QSpinBox(self.tab_1)
        self.sb_rateHeat.setObjectName(u"sb_rateHeat")
        self.sb_rateHeat.setValue(70)

        self.gridLayout_2.addWidget(self.sb_rateHeat, 2, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 4, 0, 1, 1)

        self.tabWidget.addTab(self.tab_1, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayout_5 = QGridLayout(self.tab_3)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.tw_sun = QTableWidget(self.tab_3)
        if (self.tw_sun.columnCount() < 12):
            self.tw_sun.setColumnCount(12)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tw_sun.setHorizontalHeaderItem(0, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.tw_sun.setHorizontalHeaderItem(1, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.tw_sun.setHorizontalHeaderItem(2, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.tw_sun.setHorizontalHeaderItem(3, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.tw_sun.setHorizontalHeaderItem(4, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.tw_sun.setHorizontalHeaderItem(5, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.tw_sun.setHorizontalHeaderItem(6, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.tw_sun.setHorizontalHeaderItem(7, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.tw_sun.setHorizontalHeaderItem(8, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.tw_sun.setHorizontalHeaderItem(9, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.tw_sun.setHorizontalHeaderItem(10, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.tw_sun.setHorizontalHeaderItem(11, __qtablewidgetitem35)
        if (self.tw_sun.rowCount() < 1):
            self.tw_sun.setRowCount(1)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.tw_sun.setVerticalHeaderItem(0, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.tw_sun.setItem(0, 0, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.tw_sun.setItem(0, 1, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        self.tw_sun.setItem(0, 2, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        self.tw_sun.setItem(0, 3, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        self.tw_sun.setItem(0, 4, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        self.tw_sun.setItem(0, 5, __qtablewidgetitem42)
        __qtablewidgetitem43 = QTableWidgetItem()
        self.tw_sun.setItem(0, 6, __qtablewidgetitem43)
        __qtablewidgetitem44 = QTableWidgetItem()
        self.tw_sun.setItem(0, 7, __qtablewidgetitem44)
        __qtablewidgetitem45 = QTableWidgetItem()
        self.tw_sun.setItem(0, 8, __qtablewidgetitem45)
        __qtablewidgetitem46 = QTableWidgetItem()
        self.tw_sun.setItem(0, 9, __qtablewidgetitem46)
        __qtablewidgetitem47 = QTableWidgetItem()
        self.tw_sun.setItem(0, 10, __qtablewidgetitem47)
        __qtablewidgetitem48 = QTableWidgetItem()
        self.tw_sun.setItem(0, 11, __qtablewidgetitem48)
        self.tw_sun.setObjectName(u"tw_sun")

        self.gridLayout_5.addWidget(self.tw_sun, 1, 0, 1, 1)

        self.label_6 = QLabel(self.tab_3)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_5.addWidget(self.label_6, 0, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_2, 2, 0, 1, 1)

        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.gridLayout_3 = QGridLayout(self.tab_4)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.dsb_areaPanel = QDoubleSpinBox(self.tab_4)
        self.dsb_areaPanel.setObjectName(u"dsb_areaPanel")

        self.gridLayout_3.addWidget(self.dsb_areaPanel, 5, 1, 1, 1)

        self.dsb_volume = QDoubleSpinBox(self.tab_4)
        self.dsb_volume.setObjectName(u"dsb_volume")

        self.gridLayout_3.addWidget(self.dsb_volume, 6, 1, 1, 1)

        self.lbl_volume = QLabel(self.tab_4)
        self.lbl_volume.setObjectName(u"lbl_volume")

        self.gridLayout_3.addWidget(self.lbl_volume, 6, 0, 1, 1)

        self.label_7 = QLabel(self.tab_4)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_3.addWidget(self.label_7, 0, 0, 1, 1)

        self.lbl_surface = QLabel(self.tab_4)
        self.lbl_surface.setObjectName(u"lbl_surface")

        self.gridLayout_3.addWidget(self.lbl_surface, 4, 0, 1, 1)

        self.tw_addPower = QTableWidget(self.tab_4)
        if (self.tw_addPower.columnCount() < 3):
            self.tw_addPower.setColumnCount(3)
        __qtablewidgetitem49 = QTableWidgetItem()
        self.tw_addPower.setHorizontalHeaderItem(0, __qtablewidgetitem49)
        __qtablewidgetitem50 = QTableWidgetItem()
        self.tw_addPower.setHorizontalHeaderItem(1, __qtablewidgetitem50)
        __qtablewidgetitem51 = QTableWidgetItem()
        self.tw_addPower.setHorizontalHeaderItem(2, __qtablewidgetitem51)
        self.tw_addPower.setObjectName(u"tw_addPower")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tw_addPower.sizePolicy().hasHeightForWidth())
        self.tw_addPower.setSizePolicy(sizePolicy1)
        self.tw_addPower.setMinimumSize(QSize(0, 100))
        self.tw_addPower.setMaximumSize(QSize(16777215, 1000000))
        self.tw_addPower.horizontalHeader().setMinimumSectionSize(120)
        self.tw_addPower.horizontalHeader().setDefaultSectionSize(250)
        self.tw_addPower.horizontalHeader().setStretchLastSection(True)
        self.tw_addPower.verticalHeader().setMinimumSectionSize(15)
        self.tw_addPower.verticalHeader().setDefaultSectionSize(30)
        self.tw_addPower.verticalHeader().setStretchLastSection(False)

        self.gridLayout_3.addWidget(self.tw_addPower, 3, 0, 1, 4)

        self.lbl_unit_area = QLabel(self.tab_4)
        self.lbl_unit_area.setObjectName(u"lbl_unit_area")

        self.gridLayout_3.addWidget(self.lbl_unit_area, 4, 2, 1, 1)

        self.pb_addPower = QPushButton(self.tab_4)
        self.pb_addPower.setObjectName(u"pb_addPower")

        self.gridLayout_3.addWidget(self.pb_addPower, 1, 2, 1, 1)

        self.lbl_unit_power = QLabel(self.tab_4)
        self.lbl_unit_power.setObjectName(u"lbl_unit_power")

        self.gridLayout_3.addWidget(self.lbl_unit_power, 7, 2, 1, 1)

        self.lbl_unit_volume = QLabel(self.tab_4)
        self.lbl_unit_volume.setObjectName(u"lbl_unit_volume")

        self.gridLayout_3.addWidget(self.lbl_unit_volume, 6, 2, 1, 1)

        self.lbl_power = QLabel(self.tab_4)
        self.lbl_power.setObjectName(u"lbl_power")

        self.gridLayout_3.addWidget(self.lbl_power, 7, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 485, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_3, 9, 0, 1, 1)

        self.line = QFrame(self.tab_4)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout_3.addWidget(self.line, 2, 0, 1, 4)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_2, 1, 3, 1, 1)

        self.cb_power = QComboBox(self.tab_4)
        self.cb_power.addItem("")
        self.cb_power.setObjectName(u"cb_power")

        self.gridLayout_3.addWidget(self.cb_power, 1, 0, 1, 2)

        self.dsb_powerPanel = QDoubleSpinBox(self.tab_4)
        self.dsb_powerPanel.setObjectName(u"dsb_powerPanel")

        self.gridLayout_3.addWidget(self.dsb_powerPanel, 7, 1, 1, 1)

        self.dsb_area = QDoubleSpinBox(self.tab_4)
        self.dsb_area.setObjectName(u"dsb_area")

        self.gridLayout_3.addWidget(self.dsb_area, 4, 1, 1, 1)

        self.lbl_areaPanel = QLabel(self.tab_4)
        self.lbl_areaPanel.setObjectName(u"lbl_areaPanel")

        self.gridLayout_3.addWidget(self.lbl_areaPanel, 5, 0, 1, 1)

        self.lbl_unit_areaPanel = QLabel(self.tab_4)
        self.lbl_unit_areaPanel.setObjectName(u"lbl_unit_areaPanel")

        self.gridLayout_3.addWidget(self.lbl_unit_areaPanel, 5, 2, 1, 1)

        self.pb_savePower = QPushButton(self.tab_4)
        self.pb_savePower.setObjectName(u"pb_savePower")

        self.gridLayout_3.addWidget(self.pb_savePower, 8, 0, 1, 1)

        self.tabWidget.addTab(self.tab_4, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_4 = QGridLayout(self.tab_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.lbl_selfDischargeRate = QLabel(self.tab_2)
        self.lbl_selfDischargeRate.setObjectName(u"lbl_selfDischargeRate")

        self.gridLayout_4.addWidget(self.lbl_selfDischargeRate, 6, 0, 1, 1)

        self.lbl_volumeSalt = QLabel(self.tab_2)
        self.lbl_volumeSalt.setObjectName(u"lbl_volumeSalt")

        self.gridLayout_4.addWidget(self.lbl_volumeSalt, 7, 0, 1, 1)

        self.tw_addStorage = QTableWidget(self.tab_2)
        if (self.tw_addStorage.columnCount() < 3):
            self.tw_addStorage.setColumnCount(3)
        __qtablewidgetitem52 = QTableWidgetItem()
        self.tw_addStorage.setHorizontalHeaderItem(0, __qtablewidgetitem52)
        __qtablewidgetitem53 = QTableWidgetItem()
        self.tw_addStorage.setHorizontalHeaderItem(1, __qtablewidgetitem53)
        __qtablewidgetitem54 = QTableWidgetItem()
        self.tw_addStorage.setHorizontalHeaderItem(2, __qtablewidgetitem54)
        self.tw_addStorage.setObjectName(u"tw_addStorage")
        sizePolicy1.setHeightForWidth(self.tw_addStorage.sizePolicy().hasHeightForWidth())
        self.tw_addStorage.setSizePolicy(sizePolicy1)
        self.tw_addStorage.setMinimumSize(QSize(0, 100))
        self.tw_addStorage.setMaximumSize(QSize(16777215, 1000000))
        self.tw_addStorage.horizontalHeader().setMinimumSectionSize(120)
        self.tw_addStorage.horizontalHeader().setDefaultSectionSize(250)
        self.tw_addStorage.horizontalHeader().setStretchLastSection(True)
        self.tw_addStorage.verticalHeader().setMinimumSectionSize(15)
        self.tw_addStorage.verticalHeader().setDefaultSectionSize(30)
        self.tw_addStorage.verticalHeader().setStretchLastSection(False)

        self.gridLayout_4.addWidget(self.tw_addStorage, 2, 0, 1, 4)

        self.label_8 = QLabel(self.tab_2)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_4.addWidget(self.label_8, 0, 0, 1, 1)

        self.lbl_cap = QLabel(self.tab_2)
        self.lbl_cap.setObjectName(u"lbl_cap")

        self.gridLayout_4.addWidget(self.lbl_cap, 5, 0, 1, 1)

        self.pb_addStorage = QPushButton(self.tab_2)
        self.pb_addStorage.setObjectName(u"pb_addStorage")

        self.gridLayout_4.addWidget(self.pb_addStorage, 1, 2, 1, 1)

        self.dsb_energySalt = QDoubleSpinBox(self.tab_2)
        self.dsb_energySalt.setObjectName(u"dsb_energySalt")
        self.dsb_energySalt.setValue(10.000000000000000)

        self.gridLayout_4.addWidget(self.dsb_energySalt, 7, 1, 1, 1)

        self.lbl_unit_volumeSalt = QLabel(self.tab_2)
        self.lbl_unit_volumeSalt.setObjectName(u"lbl_unit_volumeSalt")

        self.gridLayout_4.addWidget(self.lbl_unit_volumeSalt, 7, 2, 1, 1)

        self.lbl_countBat = QLabel(self.tab_2)
        self.lbl_countBat.setObjectName(u"lbl_countBat")

        self.gridLayout_4.addWidget(self.lbl_countBat, 3, 0, 1, 1)

        self.pb_saveStorage = QPushButton(self.tab_2)
        self.pb_saveStorage.setObjectName(u"pb_saveStorage")

        self.gridLayout_4.addWidget(self.pb_saveStorage, 9, 0, 1, 1)

        self.lbl_voltage = QLabel(self.tab_2)
        self.lbl_voltage.setObjectName(u"lbl_voltage")

        self.gridLayout_4.addWidget(self.lbl_voltage, 4, 0, 1, 1)

        self.lbl_energySalt = QLabel(self.tab_2)
        self.lbl_energySalt.setObjectName(u"lbl_energySalt")

        self.gridLayout_4.addWidget(self.lbl_energySalt, 8, 0, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(584, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_3, 1, 3, 1, 1)

        self.lbl_unit_energySalt = QLabel(self.tab_2)
        self.lbl_unit_energySalt.setObjectName(u"lbl_unit_energySalt")

        self.gridLayout_4.addWidget(self.lbl_unit_energySalt, 8, 2, 1, 1)

        self.dsb_energyMCube = QDoubleSpinBox(self.tab_2)
        self.dsb_energyMCube.setObjectName(u"dsb_energyMCube")
        self.dsb_energyMCube.setValue(99.989999999999995)

        self.gridLayout_4.addWidget(self.dsb_energyMCube, 8, 1, 1, 1)

        self.cb_storage = QComboBox(self.tab_2)
        self.cb_storage.addItem("")
        self.cb_storage.addItem("")
        self.cb_storage.addItem("")
        self.cb_storage.setObjectName(u"cb_storage")

        self.gridLayout_4.addWidget(self.cb_storage, 1, 0, 1, 2)

        self.dsb_voltage = QDoubleSpinBox(self.tab_2)
        self.dsb_voltage.setObjectName(u"dsb_voltage")

        self.gridLayout_4.addWidget(self.dsb_voltage, 4, 1, 1, 1)

        self.dsb_capacity = QDoubleSpinBox(self.tab_2)
        self.dsb_capacity.setObjectName(u"dsb_capacity")

        self.gridLayout_4.addWidget(self.dsb_capacity, 5, 1, 1, 1)

        self.sb_countBat = QSpinBox(self.tab_2)
        self.sb_countBat.setObjectName(u"sb_countBat")

        self.gridLayout_4.addWidget(self.sb_countBat, 3, 1, 1, 1)

        self.lbl_unit_voltage = QLabel(self.tab_2)
        self.lbl_unit_voltage.setObjectName(u"lbl_unit_voltage")

        self.gridLayout_4.addWidget(self.lbl_unit_voltage, 4, 2, 1, 1)

        self.lbl_unit_capacity = QLabel(self.tab_2)
        self.lbl_unit_capacity.setObjectName(u"lbl_unit_capacity")

        self.gridLayout_4.addWidget(self.lbl_unit_capacity, 5, 2, 1, 1)

        self.lbl_unit_selfDischarge = QLabel(self.tab_2)
        self.lbl_unit_selfDischarge.setObjectName(u"lbl_unit_selfDischarge")

        self.gridLayout_4.addWidget(self.lbl_unit_selfDischarge, 6, 2, 1, 1)

        self.dsb_discharge = QDoubleSpinBox(self.tab_2)
        self.dsb_discharge.setObjectName(u"dsb_discharge")
        self.dsb_discharge.setValue(20.000000000000000)

        self.gridLayout_4.addWidget(self.dsb_discharge, 6, 1, 1, 1)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_8 = QGridLayout(self.tab)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.tabWidget.addTab(self.tab, "")

        self.gridLayout.addWidget(self.tabWidget, 1, 0, 1, 4)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 992, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Application stockage", None))
        self.pb_openPort.setText(QCoreApplication.translate("MainWindow", u"Lancer la simulation", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Pourcentage du chauffage", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Energie annuelle", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:22pt; font-weight:700;\">Installation solaire \u00e0 Kujjijak</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"kWh", None))
        ___qtablewidgetitem = self.tw_consumption.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Janvier", None));
        ___qtablewidgetitem1 = self.tw_consumption.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"F\u00e9vrier", None));
        ___qtablewidgetitem2 = self.tw_consumption.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Mars", None));
        ___qtablewidgetitem3 = self.tw_consumption.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Avril", None));
        ___qtablewidgetitem4 = self.tw_consumption.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Mai", None));
        ___qtablewidgetitem5 = self.tw_consumption.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Juin", None));
        ___qtablewidgetitem6 = self.tw_consumption.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Juillet", None));
        ___qtablewidgetitem7 = self.tw_consumption.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Aout", None));
        ___qtablewidgetitem8 = self.tw_consumption.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Septembre", None));
        ___qtablewidgetitem9 = self.tw_consumption.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Octobre", None));
        ___qtablewidgetitem10 = self.tw_consumption.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Novembre", None));
        ___qtablewidgetitem11 = self.tw_consumption.horizontalHeaderItem(11)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"D\u00e9cembre", None));

        __sortingEnabled = self.tw_consumption.isSortingEnabled()
        self.tw_consumption.setSortingEnabled(False)
        ___qtablewidgetitem12 = self.tw_consumption.item(0, 0)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"590", None));
        ___qtablewidgetitem13 = self.tw_consumption.item(0, 1)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"542", None));
        ___qtablewidgetitem14 = self.tw_consumption.item(0, 2)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"560", None));
        ___qtablewidgetitem15 = self.tw_consumption.item(0, 3)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"472", None));
        ___qtablewidgetitem16 = self.tw_consumption.item(0, 4)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"436", None));
        ___qtablewidgetitem17 = self.tw_consumption.item(0, 5)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"407", None));
        ___qtablewidgetitem18 = self.tw_consumption.item(0, 6)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"413", None));
        ___qtablewidgetitem19 = self.tw_consumption.item(0, 7)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"420", None));
        ___qtablewidgetitem20 = self.tw_consumption.item(0, 8)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"439", None));
        ___qtablewidgetitem21 = self.tw_consumption.item(0, 9)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"491", None));
        ___qtablewidgetitem22 = self.tw_consumption.item(0, 10)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"520", None));
        ___qtablewidgetitem23 = self.tw_consumption.item(0, 11)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"551", None));
        self.tw_consumption.setSortingEnabled(__sortingEnabled)

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), QCoreApplication.translate("MainWindow", u"R\u00e9sidence", None))
        ___qtablewidgetitem24 = self.tw_sun.horizontalHeaderItem(0)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"Janvier", None));
        ___qtablewidgetitem25 = self.tw_sun.horizontalHeaderItem(1)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"F\u00e9vrier", None));
        ___qtablewidgetitem26 = self.tw_sun.horizontalHeaderItem(2)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"Mars", None));
        ___qtablewidgetitem27 = self.tw_sun.horizontalHeaderItem(3)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"Avril", None));
        ___qtablewidgetitem28 = self.tw_sun.horizontalHeaderItem(4)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"Mai", None));
        ___qtablewidgetitem29 = self.tw_sun.horizontalHeaderItem(5)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"Juin", None));
        ___qtablewidgetitem30 = self.tw_sun.horizontalHeaderItem(6)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"Juillet", None));
        ___qtablewidgetitem31 = self.tw_sun.horizontalHeaderItem(7)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"Aout", None));
        ___qtablewidgetitem32 = self.tw_sun.horizontalHeaderItem(8)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"Septembre", None));
        ___qtablewidgetitem33 = self.tw_sun.horizontalHeaderItem(9)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"Octobre", None));
        ___qtablewidgetitem34 = self.tw_sun.horizontalHeaderItem(10)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"Novembre", None));
        ___qtablewidgetitem35 = self.tw_sun.horizontalHeaderItem(11)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MainWindow", u"D\u00e9cembre", None));

        __sortingEnabled1 = self.tw_sun.isSortingEnabled()
        self.tw_sun.setSortingEnabled(False)
        ___qtablewidgetitem36 = self.tw_sun.item(0, 0)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("MainWindow", u"1.2", None));
        ___qtablewidgetitem37 = self.tw_sun.item(0, 1)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("MainWindow", u"3.4", None));
        ___qtablewidgetitem38 = self.tw_sun.item(0, 2)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("MainWindow", u"5.5", None));
        ___qtablewidgetitem39 = self.tw_sun.item(0, 3)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("MainWindow", u"7.5", None));
        ___qtablewidgetitem40 = self.tw_sun.item(0, 4)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("MainWindow", u"6.4", None));
        ___qtablewidgetitem41 = self.tw_sun.item(0, 5)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("MainWindow", u"6.3", None));
        ___qtablewidgetitem42 = self.tw_sun.item(0, 6)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("MainWindow", u"6.9", None));
        ___qtablewidgetitem43 = self.tw_sun.item(0, 7)
        ___qtablewidgetitem43.setText(QCoreApplication.translate("MainWindow", u"5.2", None));
        ___qtablewidgetitem44 = self.tw_sun.item(0, 8)
        ___qtablewidgetitem44.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem45 = self.tw_sun.item(0, 9)
        ___qtablewidgetitem45.setText(QCoreApplication.translate("MainWindow", u"1.8", None));
        ___qtablewidgetitem46 = self.tw_sun.item(0, 10)
        ___qtablewidgetitem46.setText(QCoreApplication.translate("MainWindow", u"1.5", None));
        ___qtablewidgetitem47 = self.tw_sun.item(0, 11)
        ___qtablewidgetitem47.setText(QCoreApplication.translate("MainWindow", u"0.7", None));
        self.tw_sun.setSortingEnabled(__sortingEnabled1)

        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:700;\">Nombre d'heures de soleil moyen par jour pour un mois donn\u00e9e</span></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"M\u00e9t\u00e9o", None))
        self.lbl_volume.setText(QCoreApplication.translate("MainWindow", u"Volume", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Liste des moyens de production", None))
        self.lbl_surface.setText(QCoreApplication.translate("MainWindow", u"Surface", None))
        ___qtablewidgetitem48 = self.tw_addPower.horizontalHeaderItem(0)
        ___qtablewidgetitem48.setText(QCoreApplication.translate("MainWindow", u"Moyens de production", None));
        self.lbl_unit_area.setText(QCoreApplication.translate("MainWindow", u"m^2", None))
        self.pb_addPower.setText(QCoreApplication.translate("MainWindow", u"Ajouter", None))
        self.lbl_unit_power.setText(QCoreApplication.translate("MainWindow", u"kW", None))
        self.lbl_unit_volume.setText(QCoreApplication.translate("MainWindow", u"m^3", None))
        self.lbl_power.setText(QCoreApplication.translate("MainWindow", u"Puissance cr\u00eate", None))
        self.cb_power.setItemText(0, QCoreApplication.translate("MainWindow", u"Panneaux solaires", None))

        self.lbl_areaPanel.setText(QCoreApplication.translate("MainWindow", u"Surface d'un panneau", None))
        self.lbl_unit_areaPanel.setText(QCoreApplication.translate("MainWindow", u"m^2", None))
        self.pb_savePower.setText(QCoreApplication.translate("MainWindow", u"Enregistrer", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"Productions", None))
        self.lbl_selfDischargeRate.setText(QCoreApplication.translate("MainWindow", u"Autod\u00e9charge", None))
        self.lbl_volumeSalt.setText(QCoreApplication.translate("MainWindow", u"Volume", None))
        ___qtablewidgetitem49 = self.tw_addStorage.horizontalHeaderItem(0)
        ___qtablewidgetitem49.setText(QCoreApplication.translate("MainWindow", u"Moyens de stockage", None));
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Liste des moyens de stockage", None))
        self.lbl_cap.setText(QCoreApplication.translate("MainWindow", u"Capacit\u00e9 d'une batterie", None))
        self.pb_addStorage.setText(QCoreApplication.translate("MainWindow", u"Ajouter", None))
        self.lbl_unit_volumeSalt.setText(QCoreApplication.translate("MainWindow", u"m^3", None))
        self.lbl_countBat.setText(QCoreApplication.translate("MainWindow", u"Nombre de batteries", None))
        self.pb_saveStorage.setText(QCoreApplication.translate("MainWindow", u"Enregistrer", None))
        self.lbl_voltage.setText(QCoreApplication.translate("MainWindow", u"Tension des batteries", None))
        self.lbl_energySalt.setText(QCoreApplication.translate("MainWindow", u"Energie par m^3", None))
        self.lbl_unit_energySalt.setText(QCoreApplication.translate("MainWindow", u"kWh", None))
        self.cb_storage.setItemText(0, QCoreApplication.translate("MainWindow", u"Batterie_plomb", None))
        self.cb_storage.setItemText(1, QCoreApplication.translate("MainWindow", u"Hydrog\u00e8ne", None))
        self.cb_storage.setItemText(2, QCoreApplication.translate("MainWindow", u"Sel", None))

        self.lbl_unit_voltage.setText(QCoreApplication.translate("MainWindow", u"V", None))
        self.lbl_unit_capacity.setText(QCoreApplication.translate("MainWindow", u"Ah", None))
        self.lbl_unit_selfDischarge.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Stockage", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"R\u00e9sultats", None))
    # retranslateUi

