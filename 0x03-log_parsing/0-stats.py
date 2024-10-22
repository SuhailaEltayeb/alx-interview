#!/usr/bin/python3
"""
Solving Log parsing Dialemma
"""
import sys


Line_Num = 0
total_fsize = 0
status_codes = {
    '200': 0,
    '301': 0,
    '400': 0,
    '401': 0,
    '403': 0,
    '404': 0,
    '405': 0,
    '500': 0
}


def print_status():
    """
    Function to print status
    """
    print(f"File size: {total_fsize}")

    for code, count in status_codes.items():
        if count > 0:
            print(f"{code}: {count}")


try:
    for line in sys.stdin:
        if Line_No == 10:
            print_status()
            Line_No = 0

        line = line.rstrip()
        line_parts = line.split()

        if len(line_parts) > 4:
            code = line_parts[-2]
            total_size += int(line_parts[-1])

            # Number of lines per status code
            if code in status_codes:
                status_codes[code] += 1

            # Increment the log count
            Line_No += 1
except Exception:
    pass
finally:
    print_status()
