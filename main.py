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

import asyncio
import serial_asyncio

class Printer():
    """
    Determines characteristics of the connected printer.
    """

    def __init__(self):
        """
        Initial variable setup and configuration for Printer class.
        """

        self.COMMPORT = "dev/ttyUSB0"
        self.COMMBAUDRATE = 115200

        self.COMM_LOOP = asyncio.get_event_loop()                                   # Create serial communication loop.
        reader = serial_asyncio.create_serial_connection(self.COMM_LOOP, Reader, 'reader', baudrate=self.COMMBAUDRATE)   # Create serial reading coroutine.
        writer = serial_asyncio.create_serial_connection(self.COMM_LOOP, Reader, 'writer', baudrate=self.COMMBAUDRATE)   # Create serial writing coroutine.
        asyncio.ensure_future(reader)                                               # Schedule serial reader to start running async.
        print("Reader Scheduled")
        asyncio.ensure_future(writer)                                               # Schedule serial writer to start running async.
        print("Writer Scheduled")

        self.SER = serial.Serial(self.COMMPORT, self.COMMBAUDRATE)

        # Determine printer capabilities (e.g. laser unit, ARC_SUPPORT, DIRECT_STEPPING, FWRETRACT, NOZZLE_CLEAN_FEATURE implemented gcode commands)
        # M115 gcode cmd? https://marlinfw.org/docs/gcode/M115.html

        self.SER.write(str.encode("M115\r\n"))                                      # Return firmware information
        self.SER.write(str.encode("M118 E1 Done\r\n"))                              # Print a "Done" message when finished

        serRead = ""
        while "Done" not in serRead:                                                # Read serial output until M115 is done returning data.
            read = Printer.SER.read()
            serRead += read.decode()
            serRead # Convert bytes to string
        
        print(serRead)

        # Set the following using M115 as well?

        self.FIRMWARE = "Marlin"
        self.FIRMWARE_VER = "2.0.8"
        self.FIRMWARE_NAME = "Marlin 2.0.8"
        self.PROTOCOL_VER = "2.0.0"
        self.SOURCE_CODE_URL = "https://github.com/MarlinFirmware/Marlin"
        
        self.UUID = ""

        self.EXTRUDER_COUNT = 1

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