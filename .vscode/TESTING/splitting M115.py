serRead = "FIRMWARE_NAME:Marlin 2.0.8.26F4 (Jan  9 2023 12:40:40) SOURCE_CODE_URL:github.com/MarlinFirmware/Marlin PROTOCOL_VERSION:1.0 MACHINE_TYPE:Ender-3 S1 Pro EXTRUDER_COUNT:1 UUID:cede2a2f-41a2-4748-9b12-c55c62f367ff\nCap:SERIAL_XON_XOFF:0\nCap:BINARY_FILE_TRANSFER:0\nok"

serReadList = serRead.split("\n")
del serReadList[-1]
serReadListFirstline = serReadList.pop(0)                                           # Pull out first object in list.
serReadListCapabilities = (str(serReadList).replace("""'"[],""", ""))               # Convert remaining list back to str and clean.
serReadListCapabilities.split("Cap:")                                               # Split back into list, clearing "Cap:"

print("\n\n\nInitial String:")
print(serRead)

print("\n\n\nSplit List:")
print(serReadList)

print("\n\n\nFirst Line:")
print(serReadListFirstline)

print("\n\n\nCapabilities:")
print(serReadListCapabilities)

print("\n\n")
