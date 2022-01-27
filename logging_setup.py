import logging

class LoggingSetup():
    def __init__(self, logging_file_location: str):
        logging.basicConfig(filename=logging_file_location,
                            level=logging.INFO,
                            format='%(asctime)s:%(levelname)s:%(module)s:%(funcName)s(%(threadName)s)[%(lineno)d]:%(message)s')