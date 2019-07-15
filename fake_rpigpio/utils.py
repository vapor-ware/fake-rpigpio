
import sys

from fake_rpigpio import RPi


def install():
    """This function installs fake_rpigpio as if it were RPi.GPIO.
    """

    sys.modules['RPi'] = RPi
    sys.modules['RPi.GPIO'] = RPi.GPIO
