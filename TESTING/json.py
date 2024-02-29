import json

dictionary = {
                "G0": 
                    {
                        "Type": "Motion",
                        "ImplementationVer": "1.0.0-beta",
                        "RequiredCapabilities": "None",
                        "Parameters":
                            [
                                "E",
                                "F",
                                "S",
                                "X",
                                "Y",
                                "Z"
                            ],
                        "Description": "Add a straight line movement to the planner"
                    },
                "G1":
                    {
                        "Type": "Motion",
                        "ImplementationVer": "1.0.0-beta",
                        "RequiredCapabilities": "None",
                        "Parameters":
                            [
                                "E",
                                "F",
                                "S",
                                "X",
                                "Y",
                                "Z"
                            ],
                        "Description": "Add a straight line movement to the planner with extrusion control"
                    }
            }

with open("./TESTING/test_json.json", "w") as outfile:
    json.dump(dictionary, outfile)