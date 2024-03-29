#!/usr/bin/python3
"""Script that reads stdin line by line and computes metrics."""

import sys


def print_statistics(total_size, status_codes):
    """Prints the statistics."""
    print("Total file size:", total_size)
    for code in sorted(status_codes.keys()):
        print(f"{code}: {status_codes[code]}")


def parse_line(line):
    """Parses a line from the input."""
    parts = line.split()
    if len(parts) >= 7 and parts[5].isdigit():
        return int(parts[5]), parts[8]
    return None, None


def main():
    """Main function."""
    total_size = 0
    status_codes = \
        {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    line_count = 0
    try:
        for line in sys.stdin:
            file_size, status_code_str = parse_line(line)
            if file_size is not None:
                total_size += file_size
                if status_code_str.isdigit():
                    status_code = int(status_code_str)
                    if status_code in status_codes:
                        status_codes[status_code] += 1
            line_count += 1
            if line_count % 10 == 0:
                print_statistics(total_size, status_codes)
    except KeyboardInterrupt:
        print_statistics(total_size, status_codes)


if __name__ == "__main__":
    main()
