#!~/.pyenv/versions/3.11.6/bin/python

# Copyright (c) 2024 Cutieguwu | Olivia Brooks
#
# -*- coding:utf-8 -*-
# @Title: CutiePrinterControl/GcodeParser
# @Author: Cutieguwu | Olivia Brooks
# @Description: Gcode parsing script to determine gcode commands to prioritise the implementation of.
#
# @Script: TESTING/gcode_parser.py
# @Date Created: 1 Feb, 2024
# @Last Modified: 1 Feb, 2024
# @Last Modified by: Cutieguwu | Olivia Brooks

gcode = []

with open("./TESTING/GcodeExample.gcode", "r") as gcodeFile:                        # open gcode file for reading, close when done.
    for line in gcodeFile:
        command = ""

        for character in line:
            if character != ";":                                                    # If character isn't the start of a comment, add it to the command string.
                command = command + character
            else:                                                                   # Stop reading, as remaining characters will be comments.
                break

        if command != "":                                                           # If not a formatting space or fully commented line, add it to the commands list.
            gcode.append(command.strip())                                           # .strip method to clear leading and trailing whitespace and newlines.

print(gcode)