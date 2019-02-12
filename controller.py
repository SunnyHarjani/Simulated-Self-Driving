import pyvjoy
import time

sticks = [pyvjoy.HID_USAGE_X, pyvjoy.HID_USAGE_Y, pyvjoy.HID_USAGE_Z,
          pyvjoy.HID_USAGE_RX, pyvjoy.HID_USAGE_RY, pyvjoy.HID_USAGE_RZ]

def reset():
    for stick in sticks:
        j.set_axis(stick, 0x4000)

j = pyvjoy.VJoyDevice(1)
reset()
j.set_axis(pyvjoy.HID_USAGE_Z, 0x3000)
while(True):
    print('LEFT')
    j.set_axis(pyvjoy.HID_USAGE_X, 0x2000)
    time.sleep(1)
    print('RIGHT')
    j.set_axis(pyvjoy.HID_USAGE_X, 0x6000)
    time.sleep(1)