import serial
import csv
import time

PORT = "COM3"  # change this to your Arduino port
BAUD = 115200
#hello
# Change this filename depending on your calibration condition
FILENAME = "tether1_zero_load.csv"
# Example names:
# "tether1_zero_load.csv"
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