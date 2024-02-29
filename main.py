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
# @Last Modified: 29 Feb, 2024
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

        #self.SERIAL = serial.Serial(self.COMMPORT, self.COMMBAUDRATE)

        print("\n\n")

        #self.SERIAL.write(str.encode("M115\r\n"))                                   # Return firmware information
        print("Sent M115")

        serialRead = ""
        serialRead = "FIRMWARE_NAME:Marlin 2.0.8.26F4 (Jan  9 2023 12:40:40) SOURCE_CODE_URL:github.com/MarlinFirmware/Marlin PROTOCOL_VERSION:1.0 MACHINE_TYPE:Ender-3 S1 Pro EXTRUDER_COUNT:1 UUID:cede2a2f-41a2-4748-9b12-c55c62f367ff\nCap:SERIAL_XON_XOFF:0\nCap:BINARY_FILE_TRANSFER:0\nCap:IS_PLR:0\nCap:EEPROM:1\nCap:VOLUMETRIC:1\nCap:AUTOREPORT_POS:0\nCap:AUTOREPORT_TEMP:1\nCap:PROGRESS:0\nCap:PRINT_JOB:1\nCap:AUTOLEVEL:1\nCap:RUNOUT:1\nCap:Z_PROBE:1\nCap:LEVELING_DATA:1\nCap:BUILD_PERCENT:0\nCap:SOFTWARE_POWER:0\nCap:TOGGLE_LIGHTS:0\nCap:CASE_LIGHT_BRIGHTNESS:0\nCap:EMERGENCY_PARSER:0\nCap:HOST_ACTION_COMMANDS:0\nCap:PROMPT_SUPPORT:0\nCap:SDCARD:1\nCap:REPEAT:0\nCap:SD_WRITE:1\nCap:AUTOREPORT_SD_STATUS:0\nCap:LONG_FILENAME:1\nCap:THERMAL_PROTECTION:1\nCap:MOTION_MODES:0\nCap:ARCS:1\nCap:BABYSTEPPING:1\nCap:CHAMBER_TEMPERATURE:0\nCap:COOLER_TEMPERATURE:0\nCap:MEATPACK:0\nok"
        
        while "ok" not in str(serialRead):                                          # Read serial output until M115 is done returning data.
            read = self.SERIAL.read()
            serialRead += read.decode()
        
        print("Printer returned:", serialRead)

        serialReadList = serialRead.split("\n")
        del serialReadList[-1]                                                      # remove "ok"
        serialReadFirstline = serialReadList.pop(0)                                 # Pull out first object in list.
        
        print(f'\n{serialReadFirstline}')

        # Set the following using M115

        self.FIRMWARE = ""
        self.FIRMWARE_VER = ""
        self.FIRMWARE_NAME = ""
        self.SOURCE_CODE_URL = ""
        self.PROTOCOL_VER = ""
        self.MACHINE_TYPE = ""
        self.EXTRUDER_COUNT = int()
        self.UUID = ""

        # Determine keywords in M115 first line.

        KEYWORDS = []

        currentString = ""
        for i in range(0, len(serialReadFirstline)):
            if serialReadFirstline[i].isupper() == True or serialReadFirstline[i] == "_":               # If has characteristic of a keyword argument
                currentString = currentString + serialReadFirstline[i]
            elif serialReadFirstline[i] == ":"  and serialReadFirstline[i - 1].isnumeric() == False:    # If end of keyword, add keyword and reset currentString
                KEYWORDS.append(currentString)
                currentString = ""
            else: currentString = ""                                                                    # Characters were not part of a keyword.

        positionsStart = []
        positionsEnd = []

        for i in range(0, len(KEYWORDS)):                                           # For each keyword, find its start and end indexes
            print("\nSearching for", KEYWORDS[i] + ":")

            positionStart = serialReadFirstline.find(KEYWORDS[i] + ":")
            positionEnd = positionStart + len(KEYWORDS[i]) + 1
            positionsStart.append(positionStart)
            positionsEnd.append(positionEnd)

            print(f'Found {KEYWORDS[i]} at start position {positionStart} and end position {positionEnd}\n')

        positionsStart.append(len(serialReadFirstline) + 1)

        for i in range(0, len(positionsStart) - 1):                                 # For each keyword, save the data from the end of its index to the start of the next keyword.
            position = positionsEnd[i]
            while position < len(serialReadFirstline) and position < (positionsStart[i + 1] - 1) and serialReadFirstline[position] != ("(" or "\n"):
                match KEYWORDS[i]:
                    case "FIRMWARE_NAME":
                        self.FIRMWARE_NAME = self.FIRMWARE_NAME + serialReadFirstline[position]
                    case "SOURCE_CODE_URL":
                        self.SOURCE_CODE_URL = self.SOURCE_CODE_URL + serialReadFirstline[position]
                    case "PROTOCOL_VERSION":
                        self.PROTOCOL_VER = self.PROTOCOL_VER + serialReadFirstline[position]
                    case "MACHINE_TYPE":
                        self.MACHINE_TYPE = self.MACHINE_TYPE + serialReadFirstline[position]
                    case "EXTRUDER_COUNT":
                        self.EXTRUDER_COUNT = self.EXTRUDER_COUNT + int(serialReadFirstline[position])
                    case "UUID":
                        self.UUID = self.UUID + serialReadFirstline[position]
                position = position + 1

        self.FIRMWARE_NAME.strip()                                                  # Remove whitespace from end that occurs as a result of breaking at index with "(" as whitespace
                                                                                    # cannot be used and sequence of " (" cannot be used without attempting a call an index outside of list.

        position = 0
        while self.FIRMWARE_NAME[position] != " ":
            self.FIRMWARE = self.FIRMWARE + self.FIRMWARE_NAME[position]
            position = position + 1
        position = position + 1                                                     # Skip over index with whitespace.
        while position < len(self.FIRMWARE_NAME):
            self.FIRMWARE_VER = self.FIRMWARE_VER + self.FIRMWARE_NAME[position]
            position = position + 1
        
        # Determine printer capabilities.

        self.PRINTER_CAPABILITIES = (str(serialReadList).replace("""'"[],""", ""))  # Convert remaining list back to str and clean.
        self.PRINTER_CAPABILITIES.split("Cap:")                                     # Split back into list, clearing "Cap:"

        print(f'Fetched the following:\n\nPrinter.FIRMWARE_NAME={self.FIRMWARE_NAME}\nPrinter.FIRMWARE={self.FIRMWARE}\nPrinter.FIRMWARE_VER={self.FIRMWARE_VER}\nPrinter.SOURCE_CODE_URL={self.SOURCE_CODE_URL}\nPrinter.PROTOCOL_VER={self.PROTOCOL_VER}\nPrinter.MACHINE_TYPE={self.MACHINE_TYPE}\nPrinter.EXTRUDER_COUNT={self.EXTRUDER_COUNT}\nPrinter.UUID={self.UUID}')


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