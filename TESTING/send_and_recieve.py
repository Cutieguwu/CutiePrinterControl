import serial

connection = serial.Serial("/dev/ttyUSB0", 115200)

while True:
    connection.write(str.encode(input("Enter Command: ").strip() + "\r\n"))

    serialRead = ""
    while "ok" not in str(serialRead):                                      # Read serial output until M115 is done returning data.
        read = connection.read()
        serialRead += read.decode()
    print(serialRead)