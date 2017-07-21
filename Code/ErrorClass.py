class Error(Exception):
    # Base Class for exceptions
    pass


class ConnectionError(Error):
    """ Raised if no connection to db possible """

    def __init__(self, msg):
        self.msg = msg


class LCDError(Error):
    """ Raised if LCD_Bricklet is not connected """

    def __init__(self, msg):
        self.msg = msg
