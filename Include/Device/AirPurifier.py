from DeviceCommon import DeviceCommon


class AirPurifier(DeviceCommon):
    def setActive(self, active: bool):
        if self.platformType == 'thinq2':
            self.sendCommand('airState.operation', int(active))
        else:
            self.sendCommand('Operation', int(active))

    def setTargetState(self, state: int):
        if self.platformType == 'thinq2':
            self.sendCommand('airState.opMode', state)
        else:
            self.sendCommand('OpMode', state)

    def setRotationSpeed(self, speed: int):
        if self.platformType == 'thinq2':
            self.sendCommand('airState.windStrength', speed)
        else:
            self.sendCommand('WindStrength', speed)

    def setSwingMode(self, swing: bool):
        if self.platformType == 'thinq2':
            self.sendCommand('airState.circulate.rotate', int(swing))
        else:
            self.sendCommand('CirculateDir', int(swing))

    def setLight(self, onoff: bool):
        if self.platformType == 'thinq2':
            self.sendCommand('airState.lightingState.signal', int(onoff))
        else:
            self.sendCommand('SignalLighting', int(onoff))
