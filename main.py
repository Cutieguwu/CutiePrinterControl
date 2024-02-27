#! ./VENV/bin/python

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
    def __init__(self):
        """
        Initial variable setup and configuration for Printer class.
        """

        self.COMMPORT = "dev/ttyUSB0"
        self.COMMBAUDRATE = 115200

        ser = serial.Serial(self.COMMPORT, self.COMMBAUDRATE)

class Gcode():
    def __init__(self):
        """
        Initial variable setup and configuration for gcode commands.
        """

        self.GCODEFLAVOUR = "Marlin"
        self.GCODEFLAVOURVERSION = "2.0.8"

        # Determine printer capabilities (e.g. laser unit, implemented gcode commands)

    def home(self):
        pass
