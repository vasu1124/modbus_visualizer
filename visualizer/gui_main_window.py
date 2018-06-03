# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ui_files/modbus_visualizer.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1068, 823)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        MainWindow.setDockNestingEnabled(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.mainFrame = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainFrame.sizePolicy().hasHeightForWidth())
        self.mainFrame.setSizePolicy(sizePolicy)
        self.mainFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mainFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mainFrame.setObjectName("mainFrame")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.mainFrame)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.pollingSettingsGroupBox = QtWidgets.QGroupBox(self.mainFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pollingSettingsGroupBox.sizePolicy().hasHeightForWidth())
        self.pollingSettingsGroupBox.setSizePolicy(sizePolicy)
        self.pollingSettingsGroupBox.setObjectName("pollingSettingsGroupBox")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.pollingSettingsGroupBox)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.updateTimeSpinBox = QtWidgets.QSpinBox(self.pollingSettingsGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.updateTimeSpinBox.sizePolicy().hasHeightForWidth())
        self.updateTimeSpinBox.setSizePolicy(sizePolicy)
        self.updateTimeSpinBox.setMinimum(1)
        self.updateTimeSpinBox.setMaximum(999999)
        self.updateTimeSpinBox.setObjectName("updateTimeSpinBox")
        self.gridLayout_4.addWidget(self.updateTimeSpinBox, 1, 6, 1, 1)
        self.stopPollingPushButton = QtWidgets.QPushButton(self.pollingSettingsGroupBox)
        self.stopPollingPushButton.setEnabled(False)
        self.stopPollingPushButton.setObjectName("stopPollingPushButton")
        self.gridLayout_4.addWidget(self.stopPollingPushButton, 2, 4, 1, 1)
        self.startRegisterLabel = QtWidgets.QLabel(self.pollingSettingsGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.startRegisterLabel.sizePolicy().hasHeightForWidth())
        self.startRegisterLabel.setSizePolicy(sizePolicy)
        self.startRegisterLabel.setObjectName("startRegisterLabel")
        self.gridLayout_4.addWidget(self.startRegisterLabel, 0, 2, 1, 1)
        self.numberOfRegistersLabel = QtWidgets.QLabel(self.pollingSettingsGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.numberOfRegistersLabel.sizePolicy().hasHeightForWidth())
        self.numberOfRegistersLabel.setSizePolicy(sizePolicy)
        self.numberOfRegistersLabel.setObjectName("numberOfRegistersLabel")
        self.gridLayout_4.addWidget(self.numberOfRegistersLabel, 0, 4, 1, 1)
        self.startPollingPushButton = QtWidgets.QPushButton(self.pollingSettingsGroupBox)
        self.startPollingPushButton.setObjectName("startPollingPushButton")
        self.gridLayout_4.addWidget(self.startPollingPushButton, 2, 2, 1, 1)
        self.numberOfRegistersSpinBox = QtWidgets.QSpinBox(self.pollingSettingsGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.numberOfRegistersSpinBox.sizePolicy().hasHeightForWidth())
        self.numberOfRegistersSpinBox.setSizePolicy(sizePolicy)
        self.numberOfRegistersSpinBox.setToolTip("")
        self.numberOfRegistersSpinBox.setMinimum(1)
        self.numberOfRegistersSpinBox.setMaximum(100)
        self.numberOfRegistersSpinBox.setObjectName("numberOfRegistersSpinBox")
        self.gridLayout_4.addWidget(self.numberOfRegistersSpinBox, 1, 4, 1, 1)
        self.startRegisterSpinBox = QtWidgets.QSpinBox(self.pollingSettingsGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.startRegisterSpinBox.sizePolicy().hasHeightForWidth())
        self.startRegisterSpinBox.setSizePolicy(sizePolicy)
        self.startRegisterSpinBox.setMaximum(65535)
        self.startRegisterSpinBox.setProperty("value", 0)
        self.startRegisterSpinBox.setObjectName("startRegisterSpinBox")
        self.gridLayout_4.addWidget(self.startRegisterSpinBox, 1, 2, 1, 1)
        self.registerTypeComboBox = QtWidgets.QComboBox(self.pollingSettingsGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.registerTypeComboBox.sizePolicy().hasHeightForWidth())
        self.registerTypeComboBox.setSizePolicy(sizePolicy)
        self.registerTypeComboBox.setObjectName("registerTypeComboBox")
        self.registerTypeComboBox.addItem("")
        self.registerTypeComboBox.addItem("")
        self.registerTypeComboBox.addItem("")
        self.registerTypeComboBox.addItem("")
        self.gridLayout_4.addWidget(self.registerTypeComboBox, 1, 0, 1, 1)
        self.singlePollPushButton = QtWidgets.QPushButton(self.pollingSettingsGroupBox)
        self.singlePollPushButton.setObjectName("singlePollPushButton")
        self.gridLayout_4.addWidget(self.singlePollPushButton, 2, 0, 1, 1)
        self.updateTimeLabel = QtWidgets.QLabel(self.pollingSettingsGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.updateTimeLabel.sizePolicy().hasHeightForWidth())
        self.updateTimeLabel.setSizePolicy(sizePolicy)
        self.updateTimeLabel.setObjectName("updateTimeLabel")
        self.gridLayout_4.addWidget(self.updateTimeLabel, 0, 6, 1, 1)
        self.registerTypeLabel = QtWidgets.QLabel(self.pollingSettingsGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.registerTypeLabel.sizePolicy().hasHeightForWidth())
        self.registerTypeLabel.setSizePolicy(sizePolicy)
        self.registerTypeLabel.setObjectName("registerTypeLabel")
        self.gridLayout_4.addWidget(self.registerTypeLabel, 0, 0, 1, 1)
        self.writeAllPushButton = QtWidgets.QPushButton(self.pollingSettingsGroupBox)
        self.writeAllPushButton.setEnabled(False)
        self.writeAllPushButton.setObjectName("writeAllPushButton")
        self.gridLayout_4.addWidget(self.writeAllPushButton, 2, 6, 1, 1)
        self.gridLayout_3.addWidget(self.pollingSettingsGroupBox, 2, 0, 1, 1)
        self.displaySettingsGroupBox = QtWidgets.QGroupBox(self.mainFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.displaySettingsGroupBox.sizePolicy().hasHeightForWidth())
        self.displaySettingsGroupBox.setSizePolicy(sizePolicy)
        self.displaySettingsGroupBox.setObjectName("displaySettingsGroupBox")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.displaySettingsGroupBox)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.wordEndianessComboBox = QtWidgets.QComboBox(self.displaySettingsGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.wordEndianessComboBox.sizePolicy().hasHeightForWidth())
        self.wordEndianessComboBox.setSizePolicy(sizePolicy)
        self.wordEndianessComboBox.setObjectName("wordEndianessComboBox")
        self.wordEndianessComboBox.addItem("")
        self.wordEndianessComboBox.addItem("")
        self.gridLayout_7.addWidget(self.wordEndianessComboBox, 1, 3, 1, 1)
        self.byteEndianessComboBox = QtWidgets.QComboBox(self.displaySettingsGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.byteEndianessComboBox.sizePolicy().hasHeightForWidth())
        self.byteEndianessComboBox.setSizePolicy(sizePolicy)
        self.byteEndianessComboBox.setObjectName("byteEndianessComboBox")
        self.byteEndianessComboBox.addItem("")
        self.byteEndianessComboBox.addItem("")
        self.gridLayout_7.addWidget(self.byteEndianessComboBox, 1, 1, 1, 1)
        self.dataTypeComboBox = QtWidgets.QComboBox(self.displaySettingsGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dataTypeComboBox.sizePolicy().hasHeightForWidth())
        self.dataTypeComboBox.setSizePolicy(sizePolicy)
        self.dataTypeComboBox.setObjectName("dataTypeComboBox")
        self.dataTypeComboBox.addItem("")
        self.dataTypeComboBox.addItem("")
        self.dataTypeComboBox.addItem("")
        self.dataTypeComboBox.addItem("")
        self.dataTypeComboBox.addItem("")
        self.gridLayout_7.addWidget(self.dataTypeComboBox, 0, 1, 1, 1)
        self.byteEndiannessLabel = QtWidgets.QLabel(self.displaySettingsGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.byteEndiannessLabel.sizePolicy().hasHeightForWidth())
        self.byteEndiannessLabel.setSizePolicy(sizePolicy)
        self.byteEndiannessLabel.setObjectName("byteEndiannessLabel")
        self.gridLayout_7.addWidget(self.byteEndiannessLabel, 1, 0, 1, 1, QtCore.Qt.AlignRight)
        self.dataTypeLabel = QtWidgets.QLabel(self.displaySettingsGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dataTypeLabel.sizePolicy().hasHeightForWidth())
        self.dataTypeLabel.setSizePolicy(sizePolicy)
        self.dataTypeLabel.setObjectName("dataTypeLabel")
        self.gridLayout_7.addWidget(self.dataTypeLabel, 0, 0, 1, 1, QtCore.Qt.AlignRight)
        self.wordEndiannessLabel = QtWidgets.QLabel(self.displaySettingsGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.wordEndiannessLabel.sizePolicy().hasHeightForWidth())
        self.wordEndiannessLabel.setSizePolicy(sizePolicy)
        self.wordEndiannessLabel.setObjectName("wordEndiannessLabel")
        self.gridLayout_7.addWidget(self.wordEndiannessLabel, 1, 2, 1, 1, QtCore.Qt.AlignRight)
        self.numberBaseLabel = QtWidgets.QLabel(self.displaySettingsGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.numberBaseLabel.sizePolicy().hasHeightForWidth())
        self.numberBaseLabel.setSizePolicy(sizePolicy)
        self.numberBaseLabel.setObjectName("numberBaseLabel")
        self.gridLayout_7.addWidget(self.numberBaseLabel, 0, 2, 1, 1, QtCore.Qt.AlignRight)
        self.numberBaseComboBox = QtWidgets.QComboBox(self.displaySettingsGroupBox)
        self.numberBaseComboBox.setObjectName("numberBaseComboBox")
        self.numberBaseComboBox.addItem("")
        self.numberBaseComboBox.addItem("")
        self.numberBaseComboBox.addItem("")
        self.numberBaseComboBox.addItem("")
        self.gridLayout_7.addWidget(self.numberBaseComboBox, 0, 3, 1, 1)
        self.gridLayout_3.addWidget(self.displaySettingsGroupBox, 2, 1, 1, 1)
        self.networkSettingsGroupBox = QtWidgets.QGroupBox(self.mainFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.networkSettingsGroupBox.sizePolicy().hasHeightForWidth())
        self.networkSettingsGroupBox.setSizePolicy(sizePolicy)
        self.networkSettingsGroupBox.setObjectName("networkSettingsGroupBox")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.networkSettingsGroupBox)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.tcpRadioButton = QtWidgets.QRadioButton(self.networkSettingsGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tcpRadioButton.sizePolicy().hasHeightForWidth())
        self.tcpRadioButton.setSizePolicy(sizePolicy)
        self.tcpRadioButton.setChecked(True)
        self.tcpRadioButton.setObjectName("tcpRadioButton")
        self.gridLayout_5.addWidget(self.tcpRadioButton, 0, 1, 1, 1)
        self.serialRadioButton = QtWidgets.QRadioButton(self.networkSettingsGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.serialRadioButton.sizePolicy().hasHeightForWidth())
        self.serialRadioButton.setSizePolicy(sizePolicy)
        self.serialRadioButton.setObjectName("serialRadioButton")
        self.gridLayout_5.addWidget(self.serialRadioButton, 3, 1, 1, 1)
        self.serialSettingsGroupBox = QtWidgets.QGroupBox(self.networkSettingsGroupBox)
        self.serialSettingsGroupBox.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.serialSettingsGroupBox.sizePolicy().hasHeightForWidth())
        self.serialSettingsGroupBox.setSizePolicy(sizePolicy)
        self.serialSettingsGroupBox.setCheckable(False)
        self.serialSettingsGroupBox.setObjectName("serialSettingsGroupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.serialSettingsGroupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.serialPortComboBox = QtWidgets.QComboBox(self.serialSettingsGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.serialPortComboBox.sizePolicy().hasHeightForWidth())
        self.serialPortComboBox.setSizePolicy(sizePolicy)
        self.serialPortComboBox.setMinimumSize(QtCore.QSize(100, 0))
        self.serialPortComboBox.setObjectName("serialPortComboBox")
        self.gridLayout_2.addWidget(self.serialPortComboBox, 1, 1, 1, 1)
        self.serialPortLabel = QtWidgets.QLabel(self.serialSettingsGroupBox)
        self.serialPortLabel.setObjectName("serialPortLabel")
        self.gridLayout_2.addWidget(self.serialPortLabel, 0, 1, 1, 1)
        self.serialProtocolLabel = QtWidgets.QLabel(self.serialSettingsGroupBox)
        self.serialProtocolLabel.setObjectName("serialProtocolLabel")
        self.gridLayout_2.addWidget(self.serialProtocolLabel, 0, 0, 1, 1)
        self.serialProtocolComboBox = QtWidgets.QComboBox(self.serialSettingsGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.serialProtocolComboBox.sizePolicy().hasHeightForWidth())
        self.serialProtocolComboBox.setSizePolicy(sizePolicy)
        self.serialProtocolComboBox.setMinimumSize(QtCore.QSize(100, 0))
        self.serialProtocolComboBox.setObjectName("serialProtocolComboBox")
        self.serialProtocolComboBox.addItem("")
        self.serialProtocolComboBox.addItem("")
        self.serialProtocolComboBox.addItem("")
        self.gridLayout_2.addWidget(self.serialProtocolComboBox, 1, 0, 1, 1)
        self.serialBaudRateLabel = QtWidgets.QLabel(self.serialSettingsGroupBox)
        self.serialBaudRateLabel.setObjectName("serialBaudRateLabel")
        self.gridLayout_2.addWidget(self.serialBaudRateLabel, 0, 2, 1, 1)
        self.serialParityLabel = QtWidgets.QLabel(self.serialSettingsGroupBox)
        self.serialParityLabel.setObjectName("serialParityLabel")
        self.gridLayout_2.addWidget(self.serialParityLabel, 0, 5, 1, 1)
        self.serialParityComboBox = QtWidgets.QComboBox(self.serialSettingsGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.serialParityComboBox.sizePolicy().hasHeightForWidth())
        self.serialParityComboBox.setSizePolicy(sizePolicy)
        self.serialParityComboBox.setMinimumSize(QtCore.QSize(69, 0))
        self.serialParityComboBox.setObjectName("serialParityComboBox")
        self.serialParityComboBox.addItem("")
        self.serialParityComboBox.addItem("")
        self.serialParityComboBox.addItem("")
        self.gridLayout_2.addWidget(self.serialParityComboBox, 1, 5, 1, 1)
        self.serialByteSizeComboBox = QtWidgets.QComboBox(self.serialSettingsGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.serialByteSizeComboBox.sizePolicy().hasHeightForWidth())
        self.serialByteSizeComboBox.setSizePolicy(sizePolicy)
        self.serialByteSizeComboBox.setMinimumSize(QtCore.QSize(69, 0))
        self.serialByteSizeComboBox.setIconSize(QtCore.QSize(16, 16))
        self.serialByteSizeComboBox.setObjectName("serialByteSizeComboBox")
        self.serialByteSizeComboBox.addItem("")
        self.serialByteSizeComboBox.addItem("")
        self.serialByteSizeComboBox.addItem("")
        self.serialByteSizeComboBox.addItem("")
        self.gridLayout_2.addWidget(self.serialByteSizeComboBox, 1, 4, 1, 1)
        self.serialStopBitsLabel = QtWidgets.QLabel(self.serialSettingsGroupBox)
        self.serialStopBitsLabel.setObjectName("serialStopBitsLabel")
        self.gridLayout_2.addWidget(self.serialStopBitsLabel, 0, 3, 1, 1)
        self.serialByteSizeLabel = QtWidgets.QLabel(self.serialSettingsGroupBox)
        self.serialByteSizeLabel.setObjectName("serialByteSizeLabel")
        self.gridLayout_2.addWidget(self.serialByteSizeLabel, 0, 4, 1, 1)
        self.serialStopBitsComboBox = QtWidgets.QComboBox(self.serialSettingsGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.serialStopBitsComboBox.sizePolicy().hasHeightForWidth())
        self.serialStopBitsComboBox.setSizePolicy(sizePolicy)
        self.serialStopBitsComboBox.setMinimumSize(QtCore.QSize(69, 0))
        self.serialStopBitsComboBox.setObjectName("serialStopBitsComboBox")
        self.serialStopBitsComboBox.addItem("")
        self.serialStopBitsComboBox.addItem("")
        self.gridLayout_2.addWidget(self.serialStopBitsComboBox, 1, 3, 1, 1)
        self.timeoutLabel = QtWidgets.QLabel(self.serialSettingsGroupBox)
        self.timeoutLabel.setObjectName("timeoutLabel")
        self.gridLayout_2.addWidget(self.timeoutLabel, 0, 6, 1, 1)
        self.timoutSpinBox = QtWidgets.QDoubleSpinBox(self.serialSettingsGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.timoutSpinBox.sizePolicy().hasHeightForWidth())
        self.timoutSpinBox.setSizePolicy(sizePolicy)
        self.timoutSpinBox.setMinimumSize(QtCore.QSize(69, 0))
        self.timoutSpinBox.setSingleStep(1.0)
        self.timoutSpinBox.setProperty("value", 3.0)
        self.timoutSpinBox.setObjectName("timoutSpinBox")
        self.gridLayout_2.addWidget(self.timoutSpinBox, 1, 6, 1, 1)
        self.serialBaudRateSpinBox = QtWidgets.QSpinBox(self.serialSettingsGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.serialBaudRateSpinBox.sizePolicy().hasHeightForWidth())
        self.serialBaudRateSpinBox.setSizePolicy(sizePolicy)
        self.serialBaudRateSpinBox.setMinimumSize(QtCore.QSize(80, 0))
        self.serialBaudRateSpinBox.setMaximum(999999)
        self.serialBaudRateSpinBox.setProperty("value", 19200)
        self.serialBaudRateSpinBox.setObjectName("serialBaudRateSpinBox")
        self.gridLayout_2.addWidget(self.serialBaudRateSpinBox, 1, 2, 1, 1)
        self.gridLayout_5.addWidget(self.serialSettingsGroupBox, 4, 1, 1, 1)
        self.tcpSettingsGroupBox = QtWidgets.QGroupBox(self.networkSettingsGroupBox)
        self.tcpSettingsGroupBox.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tcpSettingsGroupBox.sizePolicy().hasHeightForWidth())
        self.tcpSettingsGroupBox.setSizePolicy(sizePolicy)
        self.tcpSettingsGroupBox.setObjectName("tcpSettingsGroupBox")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.tcpSettingsGroupBox)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.tcpHostLabel = QtWidgets.QLabel(self.tcpSettingsGroupBox)
        self.tcpHostLabel.setObjectName("tcpHostLabel")
        self.gridLayout_6.addWidget(self.tcpHostLabel, 0, 0, 1, 1)
        self.tcpPortLabel = QtWidgets.QLabel(self.tcpSettingsGroupBox)
        self.tcpPortLabel.setObjectName("tcpPortLabel")
        self.gridLayout_6.addWidget(self.tcpPortLabel, 0, 1, 1, 1)
        self.tcpHostLineEdit = QtWidgets.QLineEdit(self.tcpSettingsGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tcpHostLineEdit.sizePolicy().hasHeightForWidth())
        self.tcpHostLineEdit.setSizePolicy(sizePolicy)
        self.tcpHostLineEdit.setObjectName("tcpHostLineEdit")
        self.gridLayout_6.addWidget(self.tcpHostLineEdit, 1, 0, 1, 1)
        self.tcpPortLineEdit = QtWidgets.QLineEdit(self.tcpSettingsGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tcpPortLineEdit.sizePolicy().hasHeightForWidth())
        self.tcpPortLineEdit.setSizePolicy(sizePolicy)
        self.tcpPortLineEdit.setMaximumSize(QtCore.QSize(50, 16777215))
        self.tcpPortLineEdit.setObjectName("tcpPortLineEdit")
        self.gridLayout_6.addWidget(self.tcpPortLineEdit, 1, 1, 1, 1)
        self.gridLayout_5.addWidget(self.tcpSettingsGroupBox, 2, 1, 1, 1)
        self.gridLayout_3.addWidget(self.networkSettingsGroupBox, 0, 0, 1, 2, QtCore.Qt.AlignLeft)
        self.pollTable = QtWidgets.QTableWidget(self.mainFrame)
        self.pollTable.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pollTable.sizePolicy().hasHeightForWidth())
        self.pollTable.setSizePolicy(sizePolicy)
        self.pollTable.setMinimumSize(QtCore.QSize(0, 0))
        self.pollTable.setMaximumSize(QtCore.QSize(1050, 350))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        self.pollTable.setFont(font)
        self.pollTable.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.pollTable.setShowGrid(True)
        self.pollTable.setGridStyle(QtCore.Qt.SolidLine)
        self.pollTable.setColumnCount(10)
        self.pollTable.setObjectName("pollTable")
        self.pollTable.setRowCount(10)
        item = QtWidgets.QTableWidgetItem()
        self.pollTable.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.pollTable.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.pollTable.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.pollTable.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.pollTable.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.pollTable.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.pollTable.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.pollTable.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.pollTable.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.pollTable.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.pollTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.pollTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.pollTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.pollTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.pollTable.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.pollTable.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.pollTable.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.pollTable.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.pollTable.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.pollTable.setHorizontalHeaderItem(9, item)
        self.pollTable.horizontalHeader().setVisible(True)
        self.pollTable.horizontalHeader().setCascadingSectionResizes(False)
        self.pollTable.verticalHeader().setSortIndicatorShown(False)
        self.pollTable.verticalHeader().setStretchLastSection(False)
        self.gridLayout_3.addWidget(self.pollTable, 3, 0, 1, 2)
        self.consoleTextEdit = QtWidgets.QTextEdit(self.mainFrame)
        self.consoleTextEdit.setEnabled(True)
        self.consoleTextEdit.setMinimumSize(QtCore.QSize(0, 71))
        self.consoleTextEdit.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.consoleTextEdit.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.consoleTextEdit.setReadOnly(True)
        self.consoleTextEdit.setTextInteractionFlags(QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.consoleTextEdit.setObjectName("consoleTextEdit")
        self.gridLayout_3.addWidget(self.consoleTextEdit, 4, 0, 1, 2)
        self.gridLayout.addWidget(self.mainFrame, 0, 1, 1, 1, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1068, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        self.serialParityComboBox.setCurrentIndex(2)
        self.serialByteSizeComboBox.setCurrentIndex(3)
        self.tcpRadioButton.clicked['bool'].connect(self.tcpSettingsGroupBox.setEnabled)
        self.serialRadioButton.clicked['bool'].connect(self.tcpSettingsGroupBox.setDisabled)
        self.serialRadioButton.clicked['bool'].connect(self.serialSettingsGroupBox.setEnabled)
        self.tcpRadioButton.clicked['bool'].connect(self.serialSettingsGroupBox.setDisabled)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Modbus Visualizer"))
        self.pollingSettingsGroupBox.setTitle(_translate("MainWindow", "Polling Settings"))
        self.stopPollingPushButton.setText(_translate("MainWindow", "Stop Polling"))
        self.startRegisterLabel.setText(_translate("MainWindow", "Start Register"))
        self.numberOfRegistersLabel.setText(_translate("MainWindow", "Number of Registers"))
        self.startPollingPushButton.setText(_translate("MainWindow", "Start Polling"))
        self.registerTypeComboBox.setItemText(0, _translate("MainWindow", "Coils"))
        self.registerTypeComboBox.setItemText(1, _translate("MainWindow", "Discrete Inputs"))
        self.registerTypeComboBox.setItemText(2, _translate("MainWindow", "Input Registers"))
        self.registerTypeComboBox.setItemText(3, _translate("MainWindow", "Holding Registers"))
        self.singlePollPushButton.setText(_translate("MainWindow", "Single Poll"))
        self.updateTimeLabel.setText(_translate("MainWindow", "Update Time"))
        self.registerTypeLabel.setText(_translate("MainWindow", "Register Type"))
        self.writeAllPushButton.setText(_translate("MainWindow", "Write all Requests"))
        self.displaySettingsGroupBox.setTitle(_translate("MainWindow", "Display Settings"))
        self.wordEndianessComboBox.setItemText(0, _translate("MainWindow", "MSW, LSW"))
        self.wordEndianessComboBox.setItemText(1, _translate("MainWindow", "LSW, MSW"))
        self.byteEndianessComboBox.setItemText(0, _translate("MainWindow", "MSB, LSB"))
        self.byteEndianessComboBox.setItemText(1, _translate("MainWindow", "LSB, MSB"))
        self.dataTypeComboBox.setItemText(0, _translate("MainWindow", "Unsigned Short"))
        self.dataTypeComboBox.setItemText(1, _translate("MainWindow", "Signed Short"))
        self.dataTypeComboBox.setItemText(2, _translate("MainWindow", "Float"))
        self.dataTypeComboBox.setItemText(3, _translate("MainWindow", "Unsigned Long"))
        self.dataTypeComboBox.setItemText(4, _translate("MainWindow", "Signed Long"))
        self.byteEndiannessLabel.setText(_translate("MainWindow", "Byte Order"))
        self.dataTypeLabel.setText(_translate("MainWindow", "Data Type"))
        self.wordEndiannessLabel.setText(_translate("MainWindow", "Word Order"))
        self.numberBaseLabel.setText(_translate("MainWindow", "Number Base"))
        self.numberBaseComboBox.setItemText(0, _translate("MainWindow", "Decimal"))
        self.numberBaseComboBox.setItemText(1, _translate("MainWindow", "Hexadecimal"))
        self.numberBaseComboBox.setItemText(2, _translate("MainWindow", "Binary"))
        self.numberBaseComboBox.setItemText(3, _translate("MainWindow", "Octal"))
        self.networkSettingsGroupBox.setTitle(_translate("MainWindow", "Network Settings"))
        self.tcpRadioButton.setText(_translate("MainWindow", "TCP"))
        self.serialRadioButton.setText(_translate("MainWindow", "Serial"))
        self.serialSettingsGroupBox.setTitle(_translate("MainWindow", "Modbus Serial Settings"))
        self.serialPortLabel.setText(_translate("MainWindow", "Port"))
        self.serialProtocolLabel.setText(_translate("MainWindow", "Protocol"))
        self.serialProtocolComboBox.setItemText(0, _translate("MainWindow", "RTU"))
        self.serialProtocolComboBox.setItemText(1, _translate("MainWindow", "ASCII"))
        self.serialProtocolComboBox.setItemText(2, _translate("MainWindow", "Binary"))
        self.serialBaudRateLabel.setText(_translate("MainWindow", "Baudrate"))
        self.serialParityLabel.setText(_translate("MainWindow", "Parity"))
        self.serialParityComboBox.setCurrentText(_translate("MainWindow", "None"))
        self.serialParityComboBox.setItemText(0, _translate("MainWindow", "Even"))
        self.serialParityComboBox.setItemText(1, _translate("MainWindow", "Odd"))
        self.serialParityComboBox.setItemText(2, _translate("MainWindow", "None"))
        self.serialByteSizeComboBox.setCurrentText(_translate("MainWindow", "8"))
        self.serialByteSizeComboBox.setItemText(0, _translate("MainWindow", "5"))
        self.serialByteSizeComboBox.setItemText(1, _translate("MainWindow", "6"))
        self.serialByteSizeComboBox.setItemText(2, _translate("MainWindow", "7"))
        self.serialByteSizeComboBox.setItemText(3, _translate("MainWindow", "8"))
        self.serialStopBitsLabel.setText(_translate("MainWindow", "Stop Bits"))
        self.serialByteSizeLabel.setText(_translate("MainWindow", "Byte Size"))
        self.serialStopBitsComboBox.setItemText(0, _translate("MainWindow", "1"))
        self.serialStopBitsComboBox.setItemText(1, _translate("MainWindow", "2"))
        self.timeoutLabel.setText(_translate("MainWindow", "Timeout"))
        self.tcpSettingsGroupBox.setTitle(_translate("MainWindow", "Modbus TCP Settings"))
        self.tcpHostLabel.setText(_translate("MainWindow", "Host"))
        self.tcpPortLabel.setText(_translate("MainWindow", "Port"))
        self.tcpHostLineEdit.setText(_translate("MainWindow", "127.0.0.1"))
        self.tcpPortLineEdit.setText(_translate("MainWindow", "502"))
        self.pollTable.setSortingEnabled(False)
        item = self.pollTable.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "+0"))
        item = self.pollTable.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "+1"))
        item = self.pollTable.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "+2"))
        item = self.pollTable.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "+3"))
        item = self.pollTable.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "+4"))
        item = self.pollTable.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "+5"))
        item = self.pollTable.verticalHeaderItem(6)
        item.setText(_translate("MainWindow", "+6"))
        item = self.pollTable.verticalHeaderItem(7)
        item.setText(_translate("MainWindow", "+7"))
        item = self.pollTable.verticalHeaderItem(8)
        item.setText(_translate("MainWindow", "+8"))
        item = self.pollTable.verticalHeaderItem(9)
        item.setText(_translate("MainWindow", "+9"))
        item = self.pollTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.pollTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "2"))
        item = self.pollTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "3"))
        item = self.pollTable.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "4"))
        item = self.pollTable.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "5"))
        item = self.pollTable.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "6"))
        item = self.pollTable.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "7"))
        item = self.pollTable.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "8"))
        item = self.pollTable.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "9"))
        item = self.pollTable.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "10"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))

