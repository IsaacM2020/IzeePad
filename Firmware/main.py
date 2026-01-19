import board

# KMK Core
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros
from kmk.modules.encoder import EncoderHandler

# OLED Imports
from kmk.extensions.oled import OLED, OledDisplayMode, OledReactionType, OledData

# Initialize Keyboard
keyboard = KMKKeyboard()

# --- 1. MODULES SETUP ---
macros = Macros()
keyboard.modules.append(macros)

encoder_handler = EncoderHandler()
keyboard.modules.append(encoder_handler)

# --- 2. PIN DEFINITIONS (From your Schematic) ---
# SW1=D0, SW2=D1, SW3=D2, SW4=D3, SW5=D10 (GPIO3/MOSI)
PINS = [board.D0, board.D1, board.D2, board.D3, board.D10]

# Encoder: A=D6, B=D7, Switch=D8
ENC_PIN_A = board.D6
ENC_PIN_B = board.D7
ENC_PIN_S = board.D8  # The built-in switch on the encoder

# --- 3. SWITCH CONFIGURATION ---
keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

# --- 4. ENCODER CONFIGURATION ---
encoder_handler.pins = (
    (ENC_PIN_A, ENC_PIN_B, ENC_PIN_S),
)

# Encoder Map: (Rotate Left, Rotate Right, Push Button)
# Currently: Volume Down, Volume Up, Mute
encoder_handler.map = [
    ((KC.VOLD, KC.VOLU, KC.MUTE),), 
]

# --- 5. OLED CONFIGURATION ---
# Note: Ensure your OLED is GND-VCC-SCL-SDA on the physical pins
oled_ext = OLED(
    OledData(
        corner_one={0:OledReactionType.STATIC,1:["Layer"]},
        corner_two={0:OledReactionType.LAYER,1:["1","2","3","4"]},
        corner_three={0:OledReactionType.STATIC,1:["KMK"]},
        corner_four={0:OledReactionType.STATIC,1:["Pad"]},
    ),
    toDisplay=OledDisplayMode.TXT,
    flip=False,
)
keyboard.extensions.append(oled_ext)


# --- 6. KEYMAP (ABCDE) ---
# Corresponding to SW1, SW2, SW3, SW4, SW5
keyboard.keymap = [
    [KC.A, KC.B, KC.C, KC.D, KC.E]
]

if __name__ == '__main__':
    keyboard.go()