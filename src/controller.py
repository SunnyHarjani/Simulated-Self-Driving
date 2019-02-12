import pyvjoy
import time

MIN_THROTTLE = 0x0000
NEUTRAL_THROTTLE = 0x4000
MAX_THROTTLE = 0x8000

sticks = [pyvjoy.HID_USAGE_X, pyvjoy.HID_USAGE_Y, pyvjoy.HID_USAGE_Z,
          pyvjoy.HID_USAGE_RX, pyvjoy.HID_USAGE_RY, pyvjoy.HID_USAGE_RZ]

class controller:
    def __init__(self, deviceID=1):
        self.joystick = pyvjoy.VJoyDevice(deviceID)
        self.reset()

    def reset(self):
        for stick in sticks:
            self.joystick.set_axis(stick, NEUTRAL_THROTTLE)

    def moveForward(self, power):
        print('FORWARD')
        self.joystick.set_axis(pyvjoy.HID_USAGE_Z, int((NEUTRAL_THROTTLE - MIN_THROTTLE) * power) + MIN_THROTTLE)
        #self.joystick.set_axis(pyvjoy.HID_USAGE_Z, 0x3000)
        self.joystick.set_axis(pyvjoy.HID_USAGE_X, NEUTRAL_THROTTLE)

    def moveBackward(self, power):
        print('BACK')
        self.joystick.set_axis(pyvjoy.HID_USAGE_Z, int((MAX_THROTTLE - NEUTRAL_THROTTLE) * power) + NEUTRAL_THROTTLE)
        #self.joystick.set_axis(pyvjoy.HID_USAGE_Z, 0x5000)
        self.joystick.set_axis(pyvjoy.HID_USAGE_X, NEUTRAL_THROTTLE)

    def moveLeft(self, power):
        print('LEFT')
        self.joystick.set_axis(pyvjoy.HID_USAGE_X, int((NEUTRAL_THROTTLE - MIN_THROTTLE) * power) + MIN_THROTTLE)
        self.joystick.set_axis(pyvjoy.HID_USAGE_Z, 0x3000)
        #self.joystick.set_axis(pyvjoy.HID_USAGE_X, 0x3000)

    def moveRight(self, power):
        print('RIGHT')
        self.joystick.set_axis(pyvjoy.HID_USAGE_X, int((MAX_THROTTLE - NEUTRAL_THROTTLE) * power) + NEUTRAL_THROTTLE)
        self.joystick.set_axis(pyvjoy.HID_USAGE_Z, 0x3000)
        #self.joystick.set_axis(pyvjoy.HID_USAGE_X, 0x5000)

    def main(self):
        self.moveForward(0.25)
        while(True):
            self.moveLeft(0.5)
            time.sleep(1)
            self.moveRight(0.5)
            time.sleep(1)

if __name__ == "__main__":
    controller.main()