import serial
import csv
import time
import datetime

# open arduino, go to tools, and port
# change it to the arduino port
PORT = "COM3"  
BAUD = 115200


# Change this weight depending on cailbration 
weight = "10g"
# change this to angle that is being calibrated to
angle = "0degrees"

now = datetime.now()
timestamp = datetime(now.year, now.month, now.day, now.hour, now.minute)
tether = "tether1"
weight = "test1"
FILENAME = f"tether_{weight},{angle},{timestamp}.csv"
# Example names:
# "tether1_0g,0degrees,2023-04-01 12:00:00.csv"


ser = serial.Serial(PORT, BAUD, timeout=1)

# Opening serial often resets Arduino, so wait
time.sleep(2)

with open(FILENAME, "w", newline="") as file:
    writer = csv.writer(file)

    print(f"Recording to {FILENAME}")
    print("Press Ctrl+C to stop.")

    try:
        while True:
            line = ser.readline().decode("utf-8", errors="ignore").strip()

            if line:
                print(line)

                # only save lines that look like CSV data
                if "," in line:
                    row = line.split(",")
                    writer.writerow(row)
                    file.flush()

    except KeyboardInterrupt:
        print("Stopped recording.")

ser.close()