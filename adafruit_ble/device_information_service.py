# The MIT License (MIT)
#
# Copyright (c) 2019 Dan Halbert for Adafruit Industries
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
`adafruit_ble.device_information`
====================================================

Device Information Service (DIS)

* Author(s): Dan Halbert for Adafruit Industries

"""
from _bleio import Attribute, Characteristic, Service, UUID

class DeviceInformationService:
    """This is a factory class only, and has no instances."""

    @staticmethod
    def add_to_peripheral(peripheral, *, model_number=None, serial_number=None,
                          firmware_revision=None, hardware_revision='',
                          software_revision='', manufacturer=''):
        """
        Add a Service with fixed Device Information Service characteristics to the given Peripheral.
        All values are optional.

          :param str model_number: Device model number. If None use `sys.platform`.
          :param str serial_number: Device serial number. If None use a hex representation of
             ``microcontroller.cpu.id``.
          :param str firmware_revision: Device firmware revision.
             If None use ``os.uname().version``.
          :param str hardware_revision: Device hardware revision.
          :param str software_revision: Device software revision.
          :param str manufacturer: Device manufacturer name
          :return: the created Service

        Example::

            peripheral = Peripheral()
            dis = DeviceInformationService.add_to_peripheral(
                peripheral, software_revision="1.2.4", manufacturer="Acme Corp")
        """

        # Avoid creating constants with names if not necessary. Just takes up space.
        # Device Information Service UUID = 0x180A
        # Module Number UUID = 0x2A24
        # Serial Number UUID = 0x2A25
        # Firmware Revision UUID = 0x2A26
        # Hardware Revision UUID = 0x2A27
        # Software Revision UUID = 0x2A28
        # Manufacturer Name UUID = 0x2A29

        service = Service.add_to_peripheral(peripheral, UUID(0x180A))

        if model_number is None:
            import sys
            model_number = sys.platform
        if serial_number is None:
            import microcontroller
            import binascii
            serial_number = binascii.hexlify(microcontroller.cpu.uid).decode('utf-8') # pylint: disable=no-member

        if firmware_revision is None:
            import os
            firmware_revision = os.uname().version

        # Values must correspond to UUID numbers.
        for uuid_num, value in zip(
                range(0x2A24, 0x2A29+1),
                (model_number, serial_number,
                 firmware_revision, hardware_revision, software_revision,
                 manufacturer)):

            Characteristic.add_to_service(
                service, UUID(uuid_num), properties=Characteristic.READ,
                read_perm=Attribute.OPEN, write_perm=Attribute.NO_ACCESS,
                fixed_length=True, max_length=len(value),
                initial_value=value)

        return service
