from enum import Enum

class MachineCodes(Enum):
    TEST = "test"


class Machine(object):
    """Base class for machines"""

    def __init__(self):
        """"""

    def receive_signal(self, code, **args):
        """Base interface for sending signals to the machine."""

    def read_value(self, code):
        """Base interface for reading machine values."""