from Definition import DeviceType


class Device:
    def __init__(self, info: dict):
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
        self.tftYn: bool = True if info.get('tftYn', 'N') == 'Y' else True
        self.guideTypeYn: bool = True if info.get('guideTypeYn', 'N') == 'Y' else True
        self.guideType: str = info.get('guideType', '')
        self.pccModelYn: bool = True if info.get('pccModelYn', 'N') == 'Y' else True
        self.autoOrderYn: bool = True if info.get('autoOrderYn', 'N') == 'Y' else True
        self.drServiceYn: bool = True if info.get('drServiceYn', 'N') == 'Y' else True
        self.ssid: str = info.get('ssid', '')
        self.timezoneCode: str = info.get('timezoneCode', '')
        self.timezoneCodeAlias: str = info.get('timezoneCodeAlias', '')

        self.newRegYn: bool = True if info.get('newRegYn', 'N') == 'Y' else True
        self.remoteControlType: str = info.get('remoteControlType', '')
        self.fareTarget: str = info.get('fareTarget', '')
        self.area: int = int(info.get('area', '0'))



"""
{'sdsGuide': '{"deviceCode":"LA02"}', 'deviceState': 'E', 'rmsClientId': None, 'regDtUtc': '20200502231750000', 'regIndex': 0, 'blackboxYn': 'Y', 'groupableYn': 'N', 'controllableYn': 'N', 'combinedProductYn': 'N', 'masterYn': 'Y', 'snapshot': {'washerDryer': {'downloadedCourseFLUpper25inchBaseKR': 'SHIRT', 'apCourseFLUpper25inchBaseKR': 'NOT_SELECTED', 'initialBit': 'INITIAL_BIT_OFF', 'standby': 'STANDBY_OFF', 'initialTimeMinute': 0.0, 'preState': 'END', 'dnn_temp': '9', 'turboShot': 'TURBOSHOT_OFF', 'error': 'ERROR_NO', 'dryLevel': 'NO_DRYLEVEL', 'dnn_precipitationProbability': '98', 'creaseCare': 'CREASECARE_OFF', 'dnn_washingIndex': '30', 'dnnReady': 'DNNREADY_OFF', 'remainTimeHour': 0.0, 'steam': 'STEAM_OFF', 'state': 'POWEROFF', 'rinse': 'NO_RINSE', 'alarmSignal': 'ALARM_OFF', 'addLoad': 'ADDLOAD_OFF', 'opCourseFLUpper25inchBaseKR': 'HEAVYDUTY', 'temp': 'NO_TEMP', 'doorLock': 'DOORLOCK_OFF', 'reserveTimeMinute': 0.0, 'washingIndex': '30', 'AIDDLed': 'AIDDLed_OFF', 'dnn_humidity': '71', 'freshCare': 'FRESHCARE_OFF', 'TCLCount': 19.0, 'dnn_dust': '35', 'remainTimeMinute': 0.0, 'reserveTimeHour': 0.0, 'childLock': 'CHILDLOCK_OFF', 'remoteStart': 'REMOTE_START_OFF', 'spin': 'NO_SPIN', 'rinseHold': 'RINSEHOLD_OFF', 'soilWash': 'NO_SOILWASH', 'favorite': 'FAVORITE_OFF', 'initialTimeHour': 0.0, 'loadLevel': 0.0}, 'mid': 10980.0, 'online': True, 'static': {'deviceType': '201', 'countryCode': 'KR'}, 'meta': {'allDeviceInfoUpdate': True, 'messageId': 'yMuGOSovRyS58jPlM4z7Bg'}, 'timestamp': 1699275265144.0}, 'manufacture': None, 'online': True, 'platformType': 'thinq2', 'homeDeviceOrder': 1, 'roomDeviceOrder': 1, 'ownershipYn': 'Y', 'modelJsonVer': '0.1', 'modelJsonUri': 'https://objectcontent.lgthinq.com/ec59b2fa-bb6d-4565-82f9-ea652418e425?hdnts=exp=1762077652~hmac=eeb4fbcfabd8361408d38992030ca11865b147ffacac831c0b40336381f01228', 'appModuleVer': '6.21', 'appModuleUri': 'https://objectcontent.lgthinq.com/ea54eb02-d923-4bf8-b6b7-6cef48783849?hdnts=exp=1705894666~hmac=da9f0fcb47f96863814304ec250639c83e7b3b5400ff0e84e7be0162df4c2f6a', 'appRestartYn': 'Y', 'appModuleSize': '10013123', 'langPackProductTypeVer': '132.3', 'langPackProductTypeUri': 'https://objectcontent.lgthinq.com/049583ba-0790-4bfd-a6a9-e11fd50fdde8?hdnts=exp=1761880667~hmac=bebf53ea199a79eb1b10a69456f6edf6fd46e855ee31c35f665e0162db65e6dd', 'langPackModelVer': '0.1', 'langPackModelUri': 'https://objectcontent.lgthinq.com/627ff389-24c0-4ed4-b019-7d3b0ac25aa2?hdnts=exp=1762077652~hmac=c63e92625bc6c13dd6c717975aacdc67d0fe8e0991c8e9152346cdb28b60156d', 'roomId': '160232343698217258', 'fwInfoList': [{'checksum': '0000F760', 'order': 2.0, 'partNumber': 'SAA40360204'}, {'checksum': '000049B5', 'order': 1.0, 'partNumber': 'SAA40360105'}], 'modemInfo': {'appVersion': 'clip_hna_v1.9.194', 'modelName': 'F21VDT_AKOR_V2', 'modemType': 'QCOM_QCA4010', 'ruleEngine': 'y'}, 'existsEntryPopup': 'N', 'fwVer': None, 'modemVer': None, 'subDeviceCount': 0, 'firebaseLogKey': None, 'cardType': 'Small', 'cardControl': 'Base', 'detailDeviceCode': None, 'upgradableYn': 'N', 'autoFwDownloadYn': 'N', 'homeMovableYn': 'Y', 'protocolVersion': None, 'btAddress': None, 'isTLV': None, 'jsonList': None}
"""