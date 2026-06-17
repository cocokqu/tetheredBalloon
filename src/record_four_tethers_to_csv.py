import serial
import csv
import time

# CHANGE THIS
# In Arduino IDE: Tools -> Port
PORT = "COM3"
BAUD = 115200

# Change this filename depending on your test/calibration condition
test_name = "test1"
FILENAME = f"four_tether_{test_name}.csv"


def main():
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

                    # Only save lines that look like CSV data
                    if "," in line:
                        row = line.split(",")

                        # Only save rows with exactly 5 columns:
                        # time_ms, raw1, raw2, raw3, raw4
                        if len(row) == 5:
                            writer.writerow(row)
                            file.flush()

        except KeyboardInterrupt:
            print("Stopped recording.")

        finally:
            ser.close()


if __name__ == "__main__":
    main()