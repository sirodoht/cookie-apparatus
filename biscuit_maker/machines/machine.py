from enum import Enum

class MachineCodes(Enum):
    ON = "ON"
    OFF = "OFF"
    PAUSE = "PAUSE"


class Machine():
    """Base class for machines"""

    def __init__(self):
        """"""
        self._state = MachineCodes.OFF

    def send_signal(self, code):
        """Base interface for sending signals to the machine."""
        pass

    def read_value(self):
        """Base interface for reading machine values."""
        return self._state
