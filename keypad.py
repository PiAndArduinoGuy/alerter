import time

import adafruit_matrixkeypad
import board
import digitalio

from alerter_service import AlerterService


class KeyPad:
    def __init__(self, alerter_service: AlerterService):
        rows = [digitalio.DigitalInOut(x) for x in (board.D26, board.D19, board.D13, board.D6)]
        cols = [digitalio.DigitalInOut(x) for x in (board.D5, board.D20, board.D11, board.D9)]
        keys = ((1, 2, 3, "A"),
                (4, 5, 6, "B"),
                (7, 8, 9, "C"),
                ("*", 0, "#", "D"))

        self.keypad = adafruit_matrixkeypad.Matrix_Keypad(rows, cols, keys)
        self.password = '1234'
        self.alerter_service = alerter_service

    def get_entered_password(self):
        def _is_accept_key(pressed_key):
            return pressed_key == 'A'

        def _keys_not_yet_pressed(pressed_keys):
            return len(pressed_keys) == 0

        entered_keys_array = []
        print('Listening for keypad presses...')
        while True:
            if not _keys_not_yet_pressed(self.keypad.pressed_keys):
                pressed_key = self.keypad.pressed_keys[0]
                if _is_accept_key(pressed_key):
                    entered_password = ''
                    for key in entered_keys_array:
                        entered_password = entered_password + str(key)
                    print(f"Password entered: {entered_password}")
                    if entered_password == self.password:
                        print("Password confirmed. Attempting to silence alarm.")
                        self.alerter_service.stop_alert()
                    else:
                        print("Password incorrect.")
                    entered_keys_array = [] # reset entered password for repeat retries
                else:
                    entered_keys_array.append(pressed_key)
            time.sleep(0.2)




if __name__ == '__main__':
    print("Creating keypad")
    key_pad = KeyPad()
    print("Enter a password followed by 'A' to accept the keyed in password")
    print(f"Password entered: {key_pad.get_entered_password()}")
