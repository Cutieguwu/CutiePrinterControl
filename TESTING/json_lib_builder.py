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
             