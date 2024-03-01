#!~/.pyenv/versions/3.11.6/bin/python

# Copyright (c) 2024 Cutieguwu | Olivia Brooks
#
# -*- coding:utf-8 -*-
# @Title: CutiePrinterControl/JsonLibBuilder
# @Author: Cutieguwu | Olivia Brooks
# @Description: Script to build command json files.
#
# @Script: TESTING/json_lib_builder.py
# @Date Created: 29 Feb, 2024
# @Last Modified: 29 Feb, 2024
# @Last Modified by: Cutieguwu | Olivia Brooks

import json

data = {}

with open("./TESTING/test_json.json", "r") as inputfile:
        data = json.load(inputfile)

try:
    while True:
        entry = {}
        command = input("Enter command: ")
        type = input("Enter type: ")
        implementationVer = input("Enter implementation version: ")
        capabilities = input("Enter required capabilities: ")
        parameters = input("Enter parameters E, F, S, X, Y, Z: ")
        parametersFinal = []
        if "E" in parameters:
             