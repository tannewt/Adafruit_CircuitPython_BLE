# The MIT License (MIT)
#
# Copyright (c) 2019 Scott Shawcroft for Adafruit Industries
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
"""
`string`
====================================================

This module provides string characteristics.

"""

from . import Attribute
from . import Characteristic, ComplexCharacteristic
from ..uuid import VendorUUID

import _bleio

__version__ = "0.0.0-auto.0"
__repo__ = "https://github.com/adafruit/Adafruit_CircuitPython_BLE.git"

class RemoteCommand(ComplexCharacteristic):
    """Endpoint for sending commands to a media player. The value read will list all available

       commands."""
    uuid = VendorUUID("9B3C81D8-57B1-4A8A-B8DF-0E56F7CA51C2")

    def __init__(self):
        super().__init__(properties=_bleio.Characteristic.WRITE_NO_RESPONSE | _bleio.Characteristic.NOTIFY,
                         read_perm=Attribute.OPEN, write_perm=Attribute.OPEN,
                         max_length=13,
                         fixed_length=False)

class EntityUpdate(ComplexCharacteristic):
    """UTF-8 Encoded string characteristic."""
    uuid = VendorUUID("2F7CABCE-808D-411F-9A0C-BB92BA96C102")

    def __init__(self):
        super().__init__(properties=Characteristic.WRITE_NO_RESPONSE | Characteristic.NOTIFY,
                         read_perm=Attribute.OPEN, write_perm=Attribute.OPEN,
                         max_length=13,
                         fixed_length=False)

class EntityAttribute(Characteristic):
    """UTF-8 Encoded string characteristic."""
    uuid = VendorUUID("C6B2F38C-23AB-46D8-A6AB-A3A870BBD5D7")

    def __init__(self):
        super().__init__(properties=Characteristic.WRITE | Characteristic.READ,
                         read_perm=Attribute.OPEN, write_perm=Attribute.OPEN,
                         fixed_length=False)
