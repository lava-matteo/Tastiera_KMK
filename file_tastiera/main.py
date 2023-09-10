import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.extensions.peg_oled_display import Oled,OledDisplayMode,OledReactionType,OledData
from kmk.extensions.lock_status import LockStatus
from kmk.extensions.led import LED
from kmk.modules.layers import Layers
from kmk.extensions.media_keys import MediaKeys
from kmk.handlers.sequences import simple_key_sequence
from kmk.modules.dynamic_sequences import DynamicSequences


#colonne
COL1 = board.GP4
COL2 = board.GP3
COL3 = board.GP2
COL4 = board.GP6
COL5 = board.GP5
COL6 = board.GP1
COL7 = board.GP8
COL8 = board.GP22
COL9 = board.GP9
COL10 = board.GP7
COL11 = board.GP21
COL12 = board.GP20
COL13 = board.GP10
COL14 = board.GP14
COL15 = board.GP15
COL16 = board.GP17
COL17 = board.GP16

#righe
ROW1 = board.GP0
ROW2 = board.GP13
ROW3 = board.GP12
ROW4 = board.GP18
ROW5 = board.GP19
ROW6 = board.GP11

keyboard = KMKKeyboard()

keyboard.extensions.append(MediaKeys())

keyboard.modules.append(Layers())

keyboard.modules.append(DynamicSequences())


keyboard.SDA = board.GP26
keyboard.SCL = board.GP27

leds = LED(led_pin=[board.GP28])

#led blocco maiuscolo
class LEDLockStatus(LockStatus):
    def set_lock_leds(self):
        if self.get_caps_lock():
            leds.set_brightness(50, leds=[0])
        else:
            leds.set_brightness(0, leds=[0])

    def after_hid_send(self, sandbox):
        super().after_hid_send(sandbox)
        if self.report_updated:
            self.set_lock_leds()

keyboard.extensions.append(leds)
keyboard.extensions.append(LEDLockStatus())

oled_ext = Oled(OledData(image={0:OledReactionType.LAYER,1:["layer1.bmp","layer2.bmp","layer3.bmp","layer4.bmp"]}),toDisplay=OledDisplayMode.IMG,flip=False)
keyboard.extensions.append(oled_ext)

#matrice
keyboard.col_pins = (COL1, COL2, COL3, COL4, COL5, COL6, COL7, COL8, COL9, COL10, COL11, COL12, COL13, COL14, COL15, COL16, COL17)
keyboard.row_pins = (ROW1, ROW2, ROW3, ROW4, ROW5, ROW6)
keyboard.diode_orientation = DiodeOrientation.ROW2COL

#macro per task manager
TASK = simple_key_sequence((
    KC.LCTRL(no_release=True),
    KC.LSHIFT(no_release=True),
    KC.ESC,
    KC.LCTRL(no_press=True),
    KC.LSHIFT(no_press=True),
))

#macro programmabile da tastiera
START = simple_key_sequence((
    KC.TG(3),
    KC.RECORD_SEQUENCE(0),
))
STOP = simple_key_sequence((
    KC.STOP_SEQUENCE(0),
    KC.TG(3),
    KC.TO(0)
))



#keymap (da layer 1 a layer 4)
keyboard.keymap = [
    [
     KC.ESC,   KC.TG(3), KC.F1,     KC.F2,    KC.F3,    KC.F4,    KC.F5,    KC.F6,    KC.F7,    KC.F8,    KC.F9,     KC.F10,   KC.F11,   KC.F12,     KC.TRNS,    KC.TRNS,   KC.TRNS,    
     KC.ESC,   KC.TG(1), KC.GRAVE,  KC.N1,    KC.N2,    KC.N3,    KC.N4,    KC.N5,    KC.N6,    KC.N7,    KC.N8,     KC.N9,    KC.N0,    KC.MINUS,   KC.EQUAL,   KC.BSPACE, KC.DEL,
     KC.TG(2), KC.NUBS,  KC.TAB,    KC.Q,     KC.W,     KC.E,     KC.R,     KC.T,     KC.Y,     KC.U,     KC.I,      KC.O,     KC.P,     KC.LBRC,    KC.RBRC,    KC.BSLS,   KC.PSCR,
     KC.UP,    KC.PGUP,  KC.CAPS,   KC.A,     KC.S,     KC.D,     KC.F,     KC.G,     KC.H,     KC.J,     KC.K,      KC.L,     KC.SCLN,  KC.QUOT,    KC.BSLS,    KC.LGUI,   KC.E,
     KC.HOME,  KC.RIGHT, KC.END,    KC.LSHIFT,KC.Z,     KC.X,     KC.C,     KC.V,     KC.B,     KC.N,     KC.M,      KC.COMMA, KC.DOT,   KC.SLASH,   TASK,       KC.ENT,    KC.PLAY_SEQUENCE(0),
     KC.LEFT,  KC.DOWN,  KC.PGDN,   KC.NO,    KC.LCTRL, KC.LALT,  KC.NO,    KC.NO,    KC.NO,    KC.SPACE, KC.MPLY,   KC.NO,    KC.NO,    KC.NO,      KC.RALT,    KC.RCTRL,  KC.NO
     ],
     [
     KC.ESC,   KC.TG(3), KC.F1,     KC.F2,    KC.F3,    KC.F4,    KC.F5,    KC.F6,    KC.F7,    KC.F8,    KC.F9,     KC.F10,   KC.F11,   KC.F12,     KC.TRNS,    KC.TRNS,   KC.TRNS,    
     KC.ESC,   KC.TG(1), KC.GRAVE,  KC.F1,    KC.F2,    KC.F3,    KC.F4,    KC.F5,    KC.F6,    KC.F7,    KC.F8,     KC.F9,    KC.F10,   KC.F11,     KC.F12,     KC.BSPACE, KC.DEL,
     KC.TG(2), KC.NUBS,  KC.TAB,    KC.Q,     KC.W,     KC.E,     KC.R,     KC.T,     KC.Y,     KC.U,     KC.I,      KC.O,     KC.P,     KC.LBRC,    KC.RBRC,    KC.BSLS,   KC.PSCR,
     KC.UP,    KC.PGUP,  KC.CAPS,   KC.A,     KC.S,     KC.D,     KC.F,     KC.G,     KC.H,     KC.J,     KC.K,      KC.L,     KC.SCLN,  KC.QUOT,    KC.BSLS,    KC.LGUI,   KC.E,
     KC.HOME,  KC.MNXT,  KC.END,    KC.LSHIFT,KC.Z,     KC.X,     KC.C,     KC.V,     KC.B,     KC.N,     KC.M,      KC.COMMA, KC.DOT,   KC.SLASH,   KC.RSHIFT,  KC.ENT,    START,
     KC.MPRV,  KC.DOWN,  KC.PGDN,   KC.NO,    KC.LCTRL, KC.LALT,  KC.NO,    KC.NO,    KC.NO,    KC.SPACE, KC.MPLY,   KC.NO,    KC.NO,    KC.NO,      KC.RALT,    KC.RCTRL,  KC.NO
     ],
     [
     KC.ESC,   KC.TG(3), KC.F1,     KC.F2,    KC.F3,    KC.F4,    KC.F5,    KC.F6,    KC.F7,    KC.F8,    KC.F9,     KC.F10,   KC.F11,   KC.F12,     KC.TRNS,    KC.TRNS,   KC.TRNS,    
     KC.ESC,   KC.TG(1), KC.GRAVE,  KC.N1,    KC.N2,    KC.N3,    KC.N4,    KC.N5,    KC.N6,    KC.N7,    KC.NLCK,   KC.P0,    KC.N0,    KC.MINUS,   KC.EQUAL,   KC.BSPACE, KC.DEL,
     KC.TG(2), KC.NUBS,  KC.TAB,    KC.Q,     KC.W,     KC.E,     KC.R,     KC.T,     KC.Y,     KC.P7,    KC.P8,     KC.P9,    KC.P,     KC.LBRC,    KC.RBRC,    KC.BSLS,   KC.PSCR,
     KC.UP,    KC.PGUP,  KC.CAPS,   KC.A,     KC.S,     KC.D,     KC.F,     KC.G,     KC.H,     KC.P4,    KC.P5,     KC.P6,    KC.SCLN,  KC.QUOT,    KC.BSLS,    KC.LGUI,   KC.E,
     KC.HOME,  KC.RIGHT, KC.END,    KC.LSHIFT,KC.Z,     KC.X,     KC.C,     KC.V,     KC.B,     KC.N,     KC.P1,     KC.P2,    KC.P3,    KC.SLASH,   KC.RSHIFT,  KC.ENT,    KC.PLAY_SEQUENCE(0),
     KC.LEFT,  KC.DOWN,  KC.PGDN,   KC.NO,    KC.LCTRL, KC.LALT,  KC.NO,    KC.NO,    KC.NO,    KC.SPACE, KC.MPLY,   KC.NO,    KC.NO,    KC.NO,      KC.RALT,    KC.RCTRL,  KC.NO
     ],
     [
     KC.ESC,   KC.TG(3), KC.F1,     KC.F2,    KC.F3,    KC.F4,    KC.F5,    KC.F6,    KC.F7,    KC.F8,    KC.F9,     KC.F10,   KC.F11,   KC.F12,     KC.TRNS,    KC.TRNS,   KC.TRNS,    
     KC.ESC,   KC.TG(1), KC.GRAVE,  KC.N1,    KC.N2,    KC.N3,    KC.N4,    KC.N5,    KC.N6,    KC.N7,    KC.N8,     KC.N9,    KC.N0,    KC.MINUS,   KC.EQUAL,   KC.BSPACE, KC.DEL,
     KC.TG(2), KC.NUBS,  KC.TAB,    KC.Q,     KC.W,     KC.E,     KC.R,     KC.T,     KC.Y,     KC.U,     KC.I,      KC.O,     KC.P,     KC.LBRC,    KC.RBRC,    KC.BSLS,   KC.PSCR,
     KC.UP,    KC.PGUP,  KC.CAPS,   KC.A,     KC.S,     KC.D,     KC.F,     KC.G,     KC.H,     KC.J,     KC.K,      KC.L,     KC.SCLN,  KC.QUOT,    KC.BSLS,    KC.LGUI,   KC.E,
     KC.HOME,  KC.RIGHT, KC.END,    KC.LSHIFT,KC.Z,     KC.X,     KC.C,     KC.V,     KC.B,     KC.N,     KC.M,      KC.COMMA, KC.DOT,   KC.SLASH,   TASK,       KC.ENT,    STOP,
     KC.LEFT,  KC.DOWN,  KC.PGDN,   KC.NO,    KC.LCTRL, KC.LALT,  KC.NO,    KC.NO,    KC.NO,    KC.SPACE, KC.MPLY,   KC.NO,    KC.NO,    KC.NO,      KC.RALT,    KC.RCTRL,  KC.NO]
]

if __name__ == '__main__':
    keyboard.go()
   