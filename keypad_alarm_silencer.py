import json
import time

import adafruit_matrixkeypad
import board
import digitalio

from security_config_publisher import SecurityConfigPublisher
from security_config_subscriber import SecurityConfigSubscriber


class KeyPadAlarmSilencer:
    def __init__(self,
                 rabbitmq_host: str,
                 alerter_security_config_queue_name: str,
                 exchange_name: str,
                 security_config_subscriber: SecurityConfigSubscriber):
        rows = [digitalio.DigitalInOut(x) for x in (board.D26, board.D19, board.D13, board.D6)]
        cols = [digitalio.DigitalInOut(x) for x in (board.D5, board.D20, board.D11, board.D9)]
        keys = ((1, 2, 3, "A"),
                (4, 5, 6, "B"),
                (7, 8, 9, "C"),
                ("*", 0, "#", "D"))

        self.keypad = adafruit_matrixkeypad.Matrix_Keypad(rows, cols, keys)
        self.password = '1234'
        self.security_config_publisher = SecurityConfigPublisher(rabbitmq_host, alerter_security_config_queue_name,
                                                                 exchange_name)
        self.security_config_subscriber = security_config_subscriber

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
                    entered_keys_array = self.handle_accepted_password(entered_keys_array)
                else:
                    entered_keys_array.append(pressed_key)
            time.sleep(0.2)

    def handle_accepted_password(self, entered_keys_array):
        entered_password = ''
        for key in entered_keys_array:
            entered_password = entered_password + str(key)
        print(f"Password entered: {entered_password}")
        if entered_password == self.password:
            self.handle_correct_password()
        else:
            print("Password incorrect.")
        entered_keys_array = []  # reset entered password for repeat retries
        return entered_keys_array

    def handle_correct_password(self):
        print("Password confirmed. Attempting to silence alarm.")
        self.publish_updated_security_config()

    def publish_updated_security_config(self):
        received_security_config = self.security_config_subscriber.received_security_config
        print(
            f"The subscriber received the security config {received_security_config}. Updating the securityStatus field to SAFE before publishing.")
        new_security_config = received_security_config
        new_security_config['securityStatus'] = 'SAFE'
        new_security_config_json_string = json.dumps(received_security_config)
        print(f"Publishing {new_security_config_json_string}")
        self.security_config_publisher.send_updated_security_config(new_security_config_json_string)
