import serial
import csv
import time

# CHANGE THIS!!!!!
# change this to your Arduino port 
# open arduino, go to tools, and port
PORT = "COM3"  
BAUD = 115200


# Change this filename depending on your calibration condition
weight = "test1"
FILENAME = f"tether_{weight}.csv"
# Example names:
# "tether1_0g.csv"
# "tether1_100g.csv"
# "tether1_200g.csv"

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