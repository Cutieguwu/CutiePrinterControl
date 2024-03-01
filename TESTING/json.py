import json

dictionary = {
                "G0": 
                    {
                        "Type": "Motion",
                        "ImplementationVer": "1.0.0-beta",
                        "RequiredCapabilities": "None",
                        "isExperimental": "False",
                        "Parameters":
                            {
                                "E":
                                    {
                                        "isCondition": "True",
                                        "Type": "Position",
                                        "Units": "position",
                                        "Description": "An absolute or relative coordinate on the E (extruder) axis (in current units). The E axis describes the position of the filament in terms of input to the extruder feeder."
                                    },
                                "F":
                                    {
                                        "isCondition": "True",
                                        "Type": "Rate",
                                        "Units": "rate",
                                        "Description": "The maximum movement rate of the move between the start and end point. The feedrate set here applies to subsequent moves that omit this parameter."
                                    },
                                "I":
                                    {
                                        "isCondition": "False"
                                    },
                                "J":
                                    {
                                        "isCondition": "False"
                                    },
                                "P":
                                    {
                                        "isCondition": "False"
                                    },
                                "R":
                                    {
                                        "isCondition": "False"
                                    },
                                "S":
                                    {
                                        "isImplemented": "True",
                                        "Type": "Power",
                                        "Units": "power",
                                        "Description": "Set the laser power for the move.",
                                        "ImplementationVer": "2.1.1",
                                        "RequiredCapabilities": "LASER_FEATURE"
                                    },
                                "X":
                                    {
                                        "isCondition": "True",
                                        "Type": "Position",
                                        "Units": "position",
                                        "Description": "An absolute or relative coordinate on the X axis (in current units)."
                                    },
                                "Y":
                                    {
                                        "isCondition": "True",
                                        "Type": "Position",
                                        "Units": "position",
                                        "Description": "An absolute or relative coordinate on the Y axis (in current units)."
                                    },
                                "Z":
                                    {
                                        "isCondition": "True",
                                        "Type": "Position",
                                        "Units": "position",
                                        "Description": "An absolute or relative coordinate on the Z axis (in current units)."
                                    }
                            },
                        "Description": "Add a straight line movement to the planner",
                        "Notes": []
                    },
                "G1":
                    {
                        "Type": "Motion",
                        "ImplementationVer": "1.0.0-beta",
                        "RequiredCapabilities": "None",
                        "isExperimental": "False",
                        "Parameters":
                            {
                                "E":
                                    {
                                        "isCondition": "True",
                                        "Type": "Position",
                                        "Units": "position",
                                        "Description": "An absolute or relative coordinate on the E (extruder) axis (in current units). The E axis describes the position of the filament in terms of input to the extruder feeder."
                                    },
                                "F":
                                    {
                                        "isCondition": "True",
                                        "Type": "Rate",
                                        "Units": "rate",
                                        "Description": "The maximum movement rate of the move between the start and end point. The feedrate set here applies to subsequent moves that omit this parameter."
                                    },
                                "I":
                                    {
                                        "isCondition": "False"
                                    },
                                "J":
                                    {
                                        "isCondition": "False"
                                    },
                                "P":
                                    {
                                        "isCondition": "False"
                                    },
                                "R":
                                    {
                                        "isCondition": "False"
                                    },
                                "S":
                                    {
                                        "isImplemented": "True",
                                        "Type": "Power",
                                        "Units": "power",
                                        "Description": "Set the laser power for the move.",
                                        "ImplementationVer": "2.1.1",
                                        "RequiredCapabilities": "LASER_FEATURE"
                                    },
                                "X":
                                    {
                                        "isCondition": "True",
                                        "Type": "Position",
                                        "Units": "position",
                                        "Description": "An absolute or relative coordinate on the X axis (in current units)."
                                    },
                                "Y":
                                    {
                                        "isCondition": "True",
                                        "Type": "Position",
                                        "Units": "position",
                                        "Description": "An absolute or relative coordinate on the Y axis (in current units)."
                                    },
                                "Z":
                                    {
                                        "isCondition": "True",
                                        "Type": "Position",
                                        "Units": "position",
                                        "Description": "An absolute or relative coordinate on the Z axis (in current units)."
                                    }
                            },
                        "Description": "Add a straight line movement to the planner with extrusion control",
                        "Notes": []
                    },
                "G2":
                    {
                        "Type": "Motion",
                        "ImplementationVer": "1.0.0-beta",
                        "RequiredCapabilities": "ARC_SUPPORT",
                        "isExperimental": "False",
                        "Parameters":
                            {
                                "E":
                                    {
                                        "isCondition": "True",
                                        "Type": "Position",
                                        "Units": "position",
                                        "Description": "The amount to extrude between the start point and end point"
                                    },
                                "F":
                                    {
                                        "isCondition": "True",
                                        "Type": "Rate",
                                        "Units": "rate",
                                        "Description": "The maximum rate of the move between the start and end point"
                                    },
                                "I":
                                    {
                                        "isCondition": "True",
                                        "Type": "Offset",
                                        "Units": "offset",
                                        "Description": "An offset from the current X position to use as the arc center"
                                    },
                                "J":
                                    {
                                        "isCondition": "True",
                                        "Type": "Offset",
                                        "Units": "offset",
                                        "Description": "An offset from the current Y position to use as the arc center"
                                    },
                                "P":
                                    {
                                        "isCondition": "True",
                                        "Type": "Position",
                                        "Units": "position",
                                        "Description": "Specify complete circles. (Requires ARC_P_CIRCLES)",
                                        "ImplementationVer": "None",
                                        "RequiredCapabilities": "ARC_P_CIRCLES"
                                    },
                                "R":
                                    {
                                        "isCondition": "True",
                                        "Type": "radius",
                                        "Units": "radius",
                                        "Description": "A radius from the current XY position to use as the arc center"
                                    },
                                "S":
                                    {
                                        "isImplemented": "True",
                                        "Type": "Power",
                                        "Units": "power",
                                        "Description": "Set the laser power for the move.",
                                        "ImplementationVer": "2.0.8",
                                        "RequiredCapabilities": "LASER_FEATURE"
                                    },
                                "X":
                                    {
                                        "isCondition": "True",
                                        "Type": "Position",
                                        "Units": "position",
                                        "Description": "A coordinate on the X axis"
                                    },
                                "Y":
                                    {
                                        "isCondition": "True",
                                        "Type": "Position",
                                        "Units": "position",
                                        "Description": "A coordinate on the Y axis"
                                    },
                                "Z":
                                    {
                                        "isCondition": "True",
                                        "Type": "Position",
                                        "Units": "position",
                                        "Description": "A coordinate on the Z axis"
                                    }
                            },
                        "Description": "Add an arc or circle movement to the planner, clockwise",
                        "Notes": []
                    },
                "G3":
                    {
                        "Type": "Motion",
                        "ImplementationVer": "1.0.0-beta",
                        "RequiredCapabilities": "ARC_SUPPORT",
                        "isExperimental": "False",
                        "Parameters":
                            {
                                "E":
                                    {
                                        "isCondition": "True",
                                        "Type": "Position",
                                        "Units": "position",
                                        "Description": "The amount to extrude between the start point and end point"
                                    },
                                "F":
                                    {
                                        "isCondition": "True",
                                        "Type": "Rate",
                                        "Units": "rate",
                                        "Description": "The maximum rate of the move between the start and end point"
                                    },
                                "I":
                                    {
                                        "isCondition": "True",
                                        "Type": "Offset",
                                        "Units": "offset",
                                        "Description": "An offset from the current X position to use as the arc center"
                                    },
                                "J":
                                    {
                                        "isCondition": "True",
                                        "Type": "Offset",
                                        "Units": "offset",
                                        "Description": "An offset from the current Y position to use as the arc center"
                                    },
                                "P":
                                    {
                                        "isCondition": "True",
                                        "Type": "Position",
                                        "Units": "position",
                                        "Description": "Specify complete circles. (Requires ARC_P_CIRCLES)",
                                        "ImplementationVer": "None",
                                        "RequiredCapabilities": "ARC_P_CIRCLES"
                                    },
                                "R":
                                    {
                                        "isCondition": "True",
                                        "Type": "radius",
                                        "Units": "radius",
                                        "Description": "A radius from the current XY position to use as the arc center"
                                    },
                                "S":
                                    {
                                        "isImplemented": "True",
                                        "Type": "Power",
                                        "Units": "power",
                                        "Description": "Set the laser power for the move.",
                                        "ImplementationVer": "2.0.8",
                                        "RequiredCapabilities": "LASER_FEATURE"
                                    },
                                "X":
                                    {
                                        "isCondition": "True",
                                        "Type": "Position",
                                        "Units": "position",
                                        "Description": "A coordinate on the X axis"
                                    },
                                "Y":
                                    {
                                        "isCondition": "True",
                                        "Type": "Position",
                                        "Units": "position",
                                        "Description": "A coordinate on the Y axis"
                                    },
                                "Z":
                                    {
                                        "isCondition": "True",
                                        "Type": "Position",
                                        "Units": "position",
                                        "Description": "A coordinate on the Z axis"
                                    }
                            },
                        "Description": "Add an arc or circle movement to the planner, clockwise",
                        "Notes": []
                    },
                "G4":
                    {
                        "Type": "Motion",
                        "ImplementationVer": "1.0.0-beta",
                        "RequiredCapabilities": "None",
                        "isExperimental": "False",
                        "Parameters":
                            {
                                "E":
                                    {
                                        "isCondition": "False"
                                    },
                                "F":
                                    {
                                        "isCondition": "False"
                                    },
                                "I":
                                    {
                                        "isCondition": "False"
                                    },
                                "J":
                                    {
                                        "isCondition": "False"
                                    },
                                "P":
                                    {
                                        "isCondition": "True",
                                        "Type": "Time",
                                        "Units": "ms",
                                        "Description": "Amount of time to dwell (ms).",
                                    },
                                "R":
                                    {
                                        "isCondition": "False"
                                    },
                                "S":
                                    {
                                        "isImplemented": "True",
                                        "Type": "Time",
                                        "Units": "sec",
                                        "Description": "Amount of time to dwell (sec)."
                                    },
                                "X":
                                    {
                                        "isCondition": "False"
                                    },
                                "Y":
                                    {
                                        "isCondition": "False"
                                    },
                                "Z":
                                    {
                                        "isCondition": "False"
                                    }
                            },
                        "Description": "Pause the planner.",
                        "Notes":
                            [
                                "S takes precendencce over P.",
                                "No arguments is effectively the same as M400.",
                                "M0/M1 provides an interruptible \"dwell\" (Marlin 1.1.0 and up)."
                            ]
                    }
            }

with open("./TESTING/test_json.json", "w") as outfile:
    json.dump(dictionary, outfile)