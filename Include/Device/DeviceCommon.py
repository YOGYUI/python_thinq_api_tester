import os
import sys
import json
from typing import Any
from Definition import DeviceType
CURPATH = os.path.dirname(os.path.abspath(__file__))
INCPATH = os.path.dirname(CURPATH)
sys.path.extend([INCPATH])
sys.path = list(set(sys.path))
from Common import Callback
from ThinqAPI import ThinqAPI


class DeviceCommon:
    def __init__(self, info: dict, api: ThinqAPI):
        self._api = api
        self.modelAppType: str = info.get('modelAppType', '')
        self.brandType: str = info.get('brandType', '')
        self.deviceId: str = info.get('deviceId', '')
        self.deviceType: DeviceType = DeviceType(int(info.get('deviceType', '0')))
        self.modelName: str = info.get('modelName', '')
        self.subModelNm: str = info.get('subModelNm', None)
        self.sensorType: str = info.get('sensorType', None)
        self.alias: str = info.get('alias', '')
        self.deviceCode: str = info.get('deviceCode', '')
        self.networkType: int = int(info.get('networkType', '0'))
        self.tftYn: bool = True if info.get('tftYn', 'N') == 'Y' else False
        self.guideTypeYn: bool = True if info.get('guideTypeYn', 'N') == 'Y' else False
        self.guideType: str = info.get('guideType', '')
        self.pccModelYn: bool = True if info.get('pccModelYn', 'N') == 'Y' else False
        self.autoOrderYn: bool = True if info.get('autoOrderYn', 'N') == 'Y' else False
        self.drServiceYn: bool = True if info.get('drServiceYn', 'N') == 'Y' else False
        self.ssid: str = info.get('ssid', '')
        self.timezoneCode: str = info.get('timezoneCode', '')
        self.timezoneCodeAlias: str = info.get('timezoneCodeAlias', '')
        try:
            self.sdsGuide: dict = json.loads(info.get('sdsGuide', '{}'))
        except Exception as e:
            # print(f'{e}, {info.get("sdsGuide")}, {info.get("alias")}')
            self.sdsGuide = dict()
        self.newRegYn: bool = True if info.get('newRegYn', 'N') == 'Y' else True
        self.remoteControlType: str = info.get('remoteControlType', '')
        self.fareTarget: str = info.get('fareTarget', '')
        self.area: int = int(info.get('area', '0'))
        self.deviceState: str = info.get('deviceState', '')
        self.rmsClientId: str = info.get('rmsClientId', '')
        self.regDtUtc: int = int(info.get('regDtUtc', '0'))
        self.regIndex: int = int(info.get('regIndex', '0'))
        self.blackboxYn: bool = True if info.get('blackboxYn', 'N') == 'Y' else False
        self.groupableYn: bool = True if info.get('groupableYn', 'N') == 'Y' else False
        self.controllableYn: bool = True if info.get('controllableYn', 'N') == 'Y' else False
        self.combinedProductYn: bool = True if info.get('combinedProductYn', 'N') == 'Y' else False
        self.masterYn: bool = True if info.get('masterYn', 'N') == 'Y' else False
        self.snapshot: dict = info.get('snapshot', dict())
        self.manufacture: str = info.get('manufacture', '')
        self.online: bool = info.get('online', False)
        self.platformType: str = info.get('platformType', '')
        self.homeDeviceOrder: int = info.get('homeDeviceOrder', 0)
        self.roomDeviceOrder: int = info.get('roomDeviceOrder', 0)
        self.ownershipYn: bool = True if info.get('ownershipYn', 'N') == 'Y' else False
        self.modelJsonVer: str = info.get('modelJsonVer', '0.0')
        self.modelJsonUri: str = info.get('modelJsonUri', '')
        self.appModuleVer: str = info.get('appModuleVer', '0.0')
        self.appModuleUri: str = info.get('appModuleUri', '')
        self.appRestartYn: bool = True if info.get('appRestartYn', 'N') == 'Y' else False
        self.appModuleSize: int = int(info.get('appModuleSize', '0'))
        self.langPackProductTypeVer: str = info.get('langPackProductTypeVer', '0.0')
        self.langPackProductTypeUri: str = info.get('langPackProductTypeUri', '')
        self.langPackModelVer: str = info.get('langPackModelVer', '0.0')
        self.langPackModelUri: str = info.get('langPackModelUri', '')
        self.roomId: str = info.get('roomId', '')
        self.fwInfoList: list = info.get('fwInfoList', list())
        self.modemInfo: dict = info.get('modemInfo', dict())
        self.existsEntryPopup: bool = True if info.get('existsEntryPopup', 'N') == 'Y' else False
        self.fwVer: str = info.get('fwVer', '0.0')
        self.modemVer: str = info.get('modemVer', '0.0')
        self.subDeviceCount: int = info.get('subDeviceCount', 0)
        self.firebaseLogKey: str = info.get('firebaseLogKey', '')
        self.cardType: str = info.get('cardType', '')
        self.cardControl: str = info.get('cardControl', '')
        self.detailDeviceCode: str = info.get('detailDeviceCode', '')
        self.upgradableYn: bool = True if info.get('upgradableYn', 'N') == 'Y' else False
        self.autoFwDownloadYn: bool = True if info.get('autoFwDownloadYn', 'N') == 'Y' else False
        self.homeMovableYn: bool = True if info.get('homeMovableYn', 'N') == 'Y' else False
        self.protocolVersion: str = info.get('protocolVersion', '')
        self.btAddress: str = info.get('btAddress', '')
        self.isTLV: str = info.get('isTLV', '')
        self.jsonList: str = info.get('jsonList', '')

    def sendCommand(self, key: str, value: Any):
        if self.platformType == 'thinq2':
            self._api.sendCommandToDevice(self.deviceId, key, value)
        else:
            self._api.sendCommandToDeviceV1(self.deviceId, key, value)
