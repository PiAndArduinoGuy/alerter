import time

import adafruit_matrixkeypad
import board
import digitalio


class KeyPad:
    def __init__(self):
        rows = [digitalio.DigitalInOut(x) for x in (board.D26, board.D19, board.D13, board.D6)]
        cols = [digitalio.DigitalInOut(x) for x in (board.D5, board.D20, board.D11, board.D9)]
        keys = ((1, 2, 3, "A"),
                (4, 5, 6, "B"),
                (7, 8, 9, "C"),
                ("*", 0, "#", "D"))

        self.keypad = adafruit_matrixkeypad.Matrix_Keypad(rows, cols, keys)
        self.password = '1234'

    def get_entered_password(self):
        def _is_accept_key(pressed_key):
            return pressed_key != 'A'

        def _keys_not_yet_pressed(pressed_keys):
            return len(pressed_keys) == 0

        entered_password = []
        while _keys_not_yet_pressed(self.keypad.pressed_keys) or _is_accept_key(self.keypad.pressed_keys[0]):
            if not _keys_not_yet_pressed(self.keypad.pressed_keys):
                entered_password.append(self.keypad.pressed_keys[0])
            time.sleep(0.1)
        return entered_password



if __name__ == '__main__':
    print("Creating keypad")
    key_pad = KeyPad()
    print("Enter a password followed by 'A' to accept the keyed in password")
    print(f"Password entered: {key_pad.get_entered_password()}")
