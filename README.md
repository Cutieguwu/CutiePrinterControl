![](./art/README_Header.png)

# CutiePrinterControl
---

## Disclaimer

I accept no liability for any harm or damage done as a result of the use of these scripts. Additionally, I do not officially support any printers not explicitly listed below including their firmware revision and modification set.

---

## About

This project's entire purpose is to facilitate 3D printing via a computer to a printer. Projects like Octoprint require a dedicated device, whereas this project aims to keep everything going from a multi-purpose system.

---

## Outlook

This project is currently just a proof-of-concept. At the end, v1 should be able to print gcode over a serial connection and nothing more. Looking forward if the project isn't abandoned, the project has the following goals, including the initial goals for v1:

#### v1 - Basic Controller
*Rose*

- [x] Printer information detection
- [ ] Printer capability detection
- [ ] Parse gcode
- [ ] Print using a gcode file
- [ ] Version documentation

###### v1.5
*Tyler*

- [ ] Automatic serial printer connection detection
- [ ] Version documentation

#### v2 - Basic Automations
*Jack*

- [ ] Basic Gcode library for Marlin
- [ ] Execute gcode commands by user request
- [ ] Version documentation

###### v2.5
*Harkness*

- [ ] Execute basic operation sequences by user request for testing purposes
- [ ] Progress bar
- [ ] Completion time estimate
- [ ] Version documentation

#### v3 - Graphical Interface
*Donna*

- [ ] Printer information panel
- [ ] Print progress panel
- [ ] Print control panel (Start, Stop, Pause)
- [ ] Version documentation

###### v3.1
*Noble*

- [ ] Asynchronous serial read
- [ ] Printer serial communication panel
- [ ] Save machine print state to resume printing after a shutdown
- [ ] Version documentation

###### v3.2
*Wilfred*

- [ ] Gcode command addition wizard
- [ ] Version Documentation

###### v3.3
*Mott*

- [ ] Gcode library panel
- [ ] Version Documentation

#### v4 - Multi Printer Control
*Martha*

- [ ] Support controlling multiple printers simultaneously
- [ ] Printer configuration editing panel
- [ ] Version documentation

###### v4.5
*Jones*

- [ ] Printer configuration saving
- [ ] Non-development logging systems
- [ ] Version documentation

#### v5 - Group Printer Control
*Amy*

- [ ] Printer grouping wizard
- [ ] Tell multiple printers/group(s) to print a common item
- [ ] Add panel for monitoring each printer in a group's status
- [ ] Version Documentation

###### v5.1
*Pond*

- [ ] Create a print queue for individual printers
- [ ] Version Documentation

###### v5.2
*Rory*

- [ ] Printer grouping library panel
- [ ] Version Documentation

###### v5.3
*Williams*

- [ ] Create a print queue for printer group(s)
- [ ] Add panel for monitoring status of a print queue. Don't replace the panel for monitoring a printer group.
- [ ] Version Documentation

###### v5.4
*River*

- [ ] Modify print queue orders after their creation and print jobs have started.
- [ ] Allow setting a number of copies of each item in print queue
- [ ] Version Documentation

###### v5.5
*Song*

- [ ] Add mass monitoring panel to view all printer's states, progress and current jobs.
- [ ] Version Documentation

##### Other

- [ ] French/Multi language support w/ system language autodetection
- [ ] Complete Marlin command support
- [ ] Error reporting system

---

## Supported Printers and Configurations

Creality Ender 3 S1 Pro
- Firmware: Ender 3 S1_Pro_HWv24S1_301_SWV2.0.8.26F4_FDM_LASER
- Chip: STM32F4
- Mods: None

---

## Credits:

Descriptions and notes in Marlin_commands.json: thinkyhead