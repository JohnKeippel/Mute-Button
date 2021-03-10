import time
import board
import usb_hid
import adafruit_dotstar
#import gc
from digitalio import DigitalInOut, Direction, Pull
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

# get the dotstar led just for funsies...
led = adafruit_dotstar.DotStar(board.APA102_SCK, board.APA102_MOSI, 1)
led.brightness = .2

# switches get stitches? - [all inputs, pull UP for switches (requires built in pull up resistor of course)]
os_switch = DigitalInOut(board.D0)
os_switch.direction = Direction.INPUT
os_switch.pull = Pull.UP

app_switch = DigitalInOut(board.D1)
app_switch.direction = Direction.INPUT
app_switch.pull = Pull.UP

y_m_switch = DigitalInOut(board.D3)
y_m_switch.direction = Direction.INPUT
y_m_switch.pull = Pull.UP

g_m_switch = DigitalInOut(board.D4)
g_m_switch.direction = Direction.INPUT
g_m_switch.pull = Pull.UP

# create a keyboard object - [key codes - https://circuitpython.readthedocs.io/projects/hid/en/latest/api.html]
kbd = Keyboard(usb_hid.devices)

# debug available mem
#print(gc.mem_free())

# loop de loop...
while True:
    # hand...
    if not y_m_switch.value:
        # os
        if not os_switch.value:
            # windows
            if not app_switch.value:
                # teams
                kbd.send(Keycode.LEFT_CONTROL, Keycode.LEFT_SHIFT, Keycode.K)
                #print("windows, teams, hand")
            else:
                # zoom
                kbd.send(Keycode.LEFT_ALT, Keycode.Y)
                #print("windows, zoom, hand")
        else:
            # macos
            if not app_switch.value:
                # teams
                kbd.send(Keycode.LEFT_GUI, Keycode.LEFT_SHIFT, Keycode.K)
                #print("mac, teams, hand")
            else:
                # zoom
                kbd.send(Keycode.LEFT_ALT, Keycode.Y)
                #print("mac, zoom, hand")

        # make the led yellow to indicate the last command sent
        led[0] = (255, 255, 0)  

        # cheap debounce for the momentary switch
        time.sleep(.2)      

    # mute
    if not g_m_switch.value:
        # os
        if not os_switch.value:
            # windows
            if not app_switch.value:
                # teams
                kbd.send(Keycode.LEFT_CONTROL, Keycode.LEFT_SHIFT, Keycode.M)
                #print("windows, teams, mute")
            else:
                # zoom
                kbd.send(Keycode.LEFT_ALT, Keycode.A)
                #print("windows, zoom, mute")
        else:
            # macos
            if not app_switch.value:
                # teams
                kbd.send(Keycode.LEFT_GUI, Keycode.LEFT_SHIFT, Keycode.M)
                #print("mac, teams, mute")
            else:
                # zoom
                kbd.send(Keycode.LEFT_GUI, Keycode.LEFT_SHIFT, Keycode.A)
                #print("mac, zoom, mute")

        # make the led yellow to indicate the last command sent
        led[0] = (0, 255, 0)

        # cheap debounce for the momentary switches
        time.sleep(.2)

    # release all keys
    kbd.release_all()

# zoom
    # mac
        # mute - Command + Shift + A [KEY_LEFT_GUI] ✅
        # hand - Option + Y ✅
    # windows
        # mute - Alt + A ✅
        # hand - Alt + Y ✅
# teams
    # mac
        # mute - Command + Shift + M ✅
        # hand - Command + Shift + K ✅
    # windows
        # mute - Ctrl + Shift + M ✅
        # hand - Ctrl + Shift + K ✅