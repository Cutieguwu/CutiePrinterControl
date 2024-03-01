# Gcode Command Structuring in JSON

Outlines the structure of and procedure for parsing *_commands.json

###Marlin Firmware

The structure is as follows:

```
{
    [Command <str>]: {
        "Type": [Type <str>],
        "ImplementationVer": [Version <str>],
        "RequiredCapabilities": {
            [Capability <str>]: {
                "ImplementationVer": [Version <str>]
            }
        },
        "isExperimental": [Bool <str>],
        "Parameters": {
            [Parameter <str>]: {
                "isImplemented": [Bool <str>],
                "Type": [Type <str>],
                "Units": [Units <str>],
                "Description": [Description <str>],
                "ImplementationVer": [Version <str>],
                "RequiredCapabilities": {
                    [Capability <str>]: {
                        "ImplementationVer": [Version <str>]
                    }
                }
            }
        },
        "Description": [Description <str>],
        "Notes": [
            [Note <str>]
        ]
    }
}
```

Example using G0:

Please note that this does not demonstrate every aspect of the structure, and parameters may be missing at this time.

```
{
    "G0": {
        "Type": "Motion",
        "ImplementationVer": "1.0.0-beta",
        "RequiredCapabilities": {
            "None": {}
        },
        "isExperimental": "False",
        "Parameters": {
            "E": {
                "isCondition": "True",
                "Type": "Position",
                "Units": "position",
                "Description": "An absolute or relative coordinate on the E (extruder) axis (in current units). The E axis describes the position of the filament in terms of input to the extruder feeder."
            },
            "F": {
                "isCondition": "True",
                "Type": "Rate",
                "Units": "rate",
                "Description": "The maximum movement rate of the move between the start and end point. The feedrate set here applies to subsequent moves that omit this parameter."
            },
            "I": {
                "isCondition": "False"
            },
            "J": {
                "isCondition": "False"
            },
            "P": {
                "isCondition": "False"
            },
            "R": {
                "isCondition": "False"
            },
            "S": {
                "isImplemented": "True",
                "Type": "Power",
                "Units": "power",
                "Description": "Set the laser power for the move.",
                "ImplementationVer": "2.1.1",
                "RequiredCapabilities": "LASER_FEATURE"
            },
            "X": {
                "isCondition": "True",
                "Type": "Position",
                "Units": "position",
                "Description": "An absolute or relative coordinate on the X axis (in current units)."
            },
            "Y": {
                "isCondition": "True",
                "Type": "Position",
                "Units": "position",
                "Description": "An absolute or relative coordinate on the Y axis (in current units)."
            },
            "Z": {
                "isCondition": "True",
                "Type": "Position",
                "Units": "position",
                "Description": "An absolute or relative coordinate on the Z axis (in current units)."
            }
        },
        "Description": "Add a straight line movement to the planner",
        "Notes": []
    }
}
```

#####Types, Units, Version strings (Not yet scalable, but planned.)

Supported Command Types:

- Motion

Supported Parameter Types:

- count
- offset
- power
- position
- rate
- time

Supported Versions:

- None (If the command version is matching the parameter's)
- 1.0.0-beta
- 1.1.0
- 2.0.8
- 2.1.1

Supported Capabilities:

- None (If no capabilities required.)
- All; commands will call on them using their name to check if it is possible to run. The system will support all newly added capabilities so long as the commands are implemented.

#####Structure clarifications

All keys should match the pattern as shown above for readability.

All parameter letters must be given whether they are a component of the command's usage structure or not. As seen with the G0 example above, parameters `I`, `J`, `P`, and `R` as all still listed.

If a parameter has an `isCondition` key of `False`, no keys following `isCondition` in the structure will be parsed or added to the JSON.

If a `RequiredCapabilities` key is `None`, do not add an `ImplementationVer` key of `None`. Leave `RequiredCapabilities` as an empty dictionary as shown in the G0 example above.

`Notes` keys are lists. This is so it's easier to have separated notes instead of having them all jammed into a string with a bunch of newlines, etc.