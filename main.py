#! ~/.pyenv/versions/3.11.6/bin/python

# Copyright (c) 2024 Cutieguwu | Olivia Brooks
#
# -*- coding:utf-8 -*-
# @Title: CutiePrinterControl
# @Author: Cutieguwu | Olivia Brooks
# @Description: Serial USB printer control system.
#
# @Script: main.py
# @Date Created: 26 Feb, 2024
# @Last Modified: 27 Feb, 2024
# @Last Modified by: Cutieguwu | Olivia Brooks

import serial

class Printer():
    """
    Determines characteristics of the connected printer.
    """

    def __init__(self):
        """
        Initial variable setup and configuration for Printer class.
        """

        self.COMMPORT = "/dev/ttyUSB0"
        self.COMMBAUDRATE = 115200

        self.SERIAL = serial.Serial(self.COMMPORT, self.COMMBAUDRATE)

        # Determine printer capabilities (e.g. laser unit, ARC_SUPPORT, DIRECT_STEPPING, FWRETRACT, NOZZLE_CLEAN_FEATURE implemented gcode commands)
        # M115 gcode cmd? https://marlinfw.org/docs/gcode/M115.html

        print("\n\n")

        self.SERIAL.write(str.encode("M115\r\n"))                                   # Return firmware information
        print("Sent M115")

        serialRead = ""
        while "ok" not in serialRead:                                               # Read serial output until M115 is done returning data.
            read = self.SERIAL.read()
            serialRead += read.decode()
            serialRead # Convert bytes to string
            f = open('M115_Return.txt', 'w')
        f.write(serialRead)
        
        print(serialRead)

        # Set the following using M115

        self.FIRMWARE = ""
        self.FIRMWARE_VER = ""
        self.FIRMWARE_NAME = ""
        self.PROTOCOL_VER = ""
        self.SOURCE_CODE_URL = ""
        
        self.UUID = ""

        self.EXTRUDER_COUNT = int()

        # With EXTENDED_CAPABILITIES_REPORT enabled, Marlin reports its capabilities including the following examples:
        """
        self.EEPROM = 1
        self.AUTOREPORT_TEMP = 1
        self.PROGRESS = 0
        self.AUTOLEVEL = 1
        self.Z_PROBE = 1
        self.SOFTWARE_POWER = 0
        self.TOGGLE_LIGHTS = 0
        self.EMERGENCY_PARSER = 1
        """

class Gcode(Printer):
    """
    Determines compatible gcode commands. Takes features list from Printer class.
    """

    def __init__(self):
        """
        Initial variable setup and configuration for gcode commands.
        """
        pass
        
printer = Printer()
gcode = Gcode()