from typing import List
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QShowEvent, QCloseEvent
from PyQt5.QtWidgets import QMainWindow, QWidget, QPushButton, QLineEdit, QLabel, QRadioButton
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QHeaderView, QAbstractItemView, QMessageBox
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QGroupBox, QSizePolicy
from ThinqAPI import ThinqAPI
from Device import *


class ThinqGUI(QMainWindow):
    _thinqAPI: ThinqAPI
    _dev_list: List[DeviceCommon]

    def __init__(self, parent=None):
        super().__init__(parent)
        self._btnStartAPI = QPushButton('START')
        self._btnStopAPI = QPushButton('STOP')
        self._tableDeviceList = QTableWidget()
        self._editDeviceId = QLineEdit()
        self._editDataKey = QLineEdit()
        self._editDataValue = QLineEdit()
        self._radioValueInt = QRadioButton('Integer')
        self._radioValueFloat = QRadioButton('Float')
        self._btnSendCommand = QPushButton('SEND COMMAND')
        self._dev_list = list()
        self.initControl()
        self.initLayout()
        self.setWindowTitle('ThinQ GUI')
        self.resize(600, 600)

    def initLayout(self):
        central = QWidget(self)
        self.setCentralWidget(central)

        vbox = QVBoxLayout(central)
        vbox.setContentsMargins(4, 4, 4, 4)
        vbox.setSpacing(4)

        subwgt = QWidget()
        subwgt.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        hbox = QHBoxLayout(subwgt)
        hbox.setContentsMargins(0, 0, 0, 0)
        hbox.setSpacing(4)
        hbox.addWidget(self._btnStartAPI)
        hbox.addWidget(self._btnStopAPI)
        hbox.addWidget(QWidget())
        vbox.addWidget(subwgt)

        subwgt = QWidget()
        subwgt.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        hbox = QHBoxLayout(subwgt)
        hbox.setContentsMargins(0, 0, 0, 0)
        hbox.setSpacing(4)
        lbl = QLabel('Device List')
        hbox.addWidget(lbl)
        hbox.addWidget(QWidget(self))
        vbox.addWidget(subwgt)
        vbox.addWidget(self._tableDeviceList)

        grbox = QGroupBox('Device Control')
        vbox_gr = QVBoxLayout(grbox)
        vbox_gr.setContentsMargins(4, 6, 4, 4)
        vbox_gr.setSpacing(4)
        subwgt = QWidget()
        subwgt.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        hbox = QHBoxLayout(subwgt)
        hbox.setContentsMargins(0, 0, 0, 0)
        hbox.setSpacing(4)
        lbl = QLabel('Device ID')
        lbl.setFixedWidth(70)
        hbox.addWidget(lbl)
        hbox.addWidget(self._editDeviceId)
        vbox_gr.addWidget(subwgt)
        subwgt = QWidget()
        subwgt.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        hbox = QHBoxLayout(subwgt)
        hbox.setContentsMargins(0, 0, 0, 0)
        hbox.setSpacing(4)
        lbl = QLabel('Data Key')
        lbl.setFixedWidth(70)
        hbox.addWidget(lbl)
        hbox.addWidget(self._editDataKey)
        vbox_gr.addWidget(subwgt)
        subwgt = QWidget()
        subwgt.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        hbox = QHBoxLayout(subwgt)
        hbox.setContentsMargins(0, 0, 0, 0)
        hbox.setSpacing(4)
        lbl = QLabel('Data Value')
        lbl.setFixedWidth(70)
        hbox.addWidget(lbl)
        hbox.addWidget(self._editDataValue)
        self._radioValueInt.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.MinimumExpanding)
        hbox.addWidget(self._radioValueInt)
        self._radioValueFloat.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.MinimumExpanding)
        hbox.addWidget(self._radioValueFloat)
        vbox_gr.addWidget(subwgt)
        subwgt = QWidget()
        subwgt.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        hbox = QHBoxLayout(subwgt)
        hbox.setContentsMargins(0, 0, 0, 0)
        hbox.setSpacing(4)
        hbox.addWidget(self._btnSendCommand)
        vbox_gr.addWidget(subwgt)
        vbox.addWidget(grbox)

    def initControl(self):
        self._btnStartAPI.clicked.connect(self.onClickBtnStartAPI)
        self._btnStopAPI.clicked.connect(self.onClickBtnStopAPI)
        self._editDeviceId.setReadOnly(True)
        self._btnSendCommand.clicked.connect(self.onClickBtnSendCommand)
        self._radioValueInt.setChecked(True)
        self.initTableDeviceList()

    def initTableDeviceList(self):
        hHeaderLabels = ['Type', 'Id', 'Model', 'Alias', 'Platform']
        self._tableDeviceList.setColumnCount(len(hHeaderLabels))
        self._tableDeviceList.setHorizontalHeaderLabels(hHeaderLabels)
        self._tableDeviceList.verticalHeader().hide()
        hHeader = self._tableDeviceList.horizontalHeader()
        hHeader.setSectionResizeMode(0, QHeaderView.ResizeToContents)
        hHeader.setSectionResizeMode(1, QHeaderView.Stretch)
        hHeader.setSectionResizeMode(2, QHeaderView.ResizeToContents)
        hHeader.setSectionResizeMode(3, QHeaderView.ResizeToContents)
        hHeader.setSectionResizeMode(4, QHeaderView.ResizeToContents)
        self._tableDeviceList.setSelectionMode(QAbstractItemView.SingleSelection)
        self._tableDeviceList.setSelectionBehavior(QAbstractItemView.SelectRows)
        self._tableDeviceList.itemSelectionChanged.connect(self.onTableDeviceListItemSelectionChanged)
        self._tableDeviceList.setWordWrap(False)

    def release(self):
        if self._thinqAPI is not None:
            self._thinqAPI.release()

    def setThinqApiInstance(self, thinq: ThinqAPI):
        self._thinqAPI = thinq
        self._thinqAPI.sig_dev_info_list.connect(self.onThinqApiDeviceListCallback)
        self._thinqAPI.sig_request_failed.connect(self.onThinqApiRequestFailed)

    def startAPI(self):
        if self._thinqAPI is not None:
            self._thinqAPI.start()

    def stopAPI(self):
        if self._thinqAPI is not None:
            self._thinqAPI.stop()

    def showEvent(self, a0: QShowEvent):
        pass

    def closeEvent(self, a0: QCloseEvent):
        self.release()

    def onClickBtnStartAPI(self):
        if self._thinqAPI is not None:
            self._thinqAPI.start()

    def onClickBtnStopAPI(self):
        if self._thinqAPI is not None:
            self._thinqAPI.stop()

    def createDeviceInstance(self, dev_info: dict) -> DeviceCommon:
        deviceType: DeviceType = DeviceType(int(dev_info.get('deviceType', '0')))
        if deviceType is DeviceType.AirConditioner:
            device = AirConditioner(dev_info, self._thinqAPI)
        elif deviceType is DeviceType.AirPurifier:
            device = AirPurifier(dev_info, self._thinqAPI)
        elif deviceType is DeviceType.Dehumidifier:
            device = Dehumidifier(dev_info, self._thinqAPI)
        elif deviceType is DeviceType.Dryer:
            device = Dryer(dev_info, self._thinqAPI)
        elif deviceType is DeviceType.RobotCleaner:
            device = RobotCleaner(dev_info, self._thinqAPI)
        elif deviceType is DeviceType.Styler:
            device = Styler(dev_info, self._thinqAPI)
        elif deviceType is DeviceType.Washer:
            device = Washer(dev_info, self._thinqAPI)
        else:
            device = DeviceCommon(dev_info, self._thinqAPI)
        return device

    def onThinqApiDeviceListCallback(self, dev_info_list: list):
        self._dev_list.clear()
        self._dev_list = [self.createDeviceInstance(x) for x in dev_info_list]

        self._tableDeviceList.clearContents()
        self._tableDeviceList.setRowCount(len(self._dev_list))
        for r, dev in enumerate(self._dev_list):
            item = QTableWidgetItem()
            item.setFlags(Qt.ItemFlags(int(item.flags()) ^ Qt.ItemIsEditable))
            item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            item.setText(f'{dev.deviceType.value}')
            self._tableDeviceList.setItem(r, 0, item)
            item = QTableWidgetItem()
            item.setFlags(Qt.ItemFlags(int(item.flags()) ^ Qt.ItemIsEditable))
            item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            item.setText(f'{dev.deviceId}')
            self._tableDeviceList.setItem(r, 1, item)
            item = QTableWidgetItem()
            item.setFlags(Qt.ItemFlags(int(item.flags()) ^ Qt.ItemIsEditable))
            item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            item.setText(f'{dev.modelName}')
            self._tableDeviceList.setItem(r, 2, item)
            item = QTableWidgetItem()
            item.setFlags(Qt.ItemFlags(int(item.flags()) ^ Qt.ItemIsEditable))
            item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            item.setText(f'{dev.alias}')
            self._tableDeviceList.setItem(r, 3, item)
            item = QTableWidgetItem()
            item.setFlags(Qt.ItemFlags(int(item.flags()) ^ Qt.ItemIsEditable))
            item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            item.setText(f'{dev.platformType}')
            self._tableDeviceList.setItem(r, 4, item)

    def onThinqApiRequestFailed(self, code: int, message: str):
        QMessageBox.warning(self, "Error", f"Request Failed ({code})\n{message}", QMessageBox.Ok)

    def onTableDeviceListItemSelectionChanged(self):
        selected = self._tableDeviceList.selectedItems()
        if len(selected) > 0:
            row = selected[0].row()
            dev = self._dev_list[row]
            dev_id = dev.deviceId
            self._editDeviceId.setText(dev_id)

    def onClickBtnSendCommand(self):
        try:
            dev_id = self._editDeviceId.text()
            find = list(filter(lambda x: x.deviceId == dev_id, self._dev_list))
            if len(find) == 1:
                device = find[0]
                data_key = self._editDataKey.text()
                if self._radioValueFloat.isChecked():
                    data_value = float(self._editDataValue.text())
                else:
                    data_value = int(self._editDataValue.text())
                device.sendCommand(data_key, data_value)
        except Exception as e:
            print(f'onClickBtnSendCommand::error::{e}')
