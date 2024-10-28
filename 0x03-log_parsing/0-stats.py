#!/usr/bin/python3
"""
0. Log parsing
"""

import sys
import re
from signal import signal, SIGINT

# Initialize counters and dictionary
total_file_size = 0
status_counts = {
    200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

# Regular expression for the log line format
log_format = re.compile(
    r"^(\S+) - \[(.*?)\] \"GET /projects/260 HTTP/1.1\" (\d{3}) (\d+)$")


def print_stats():
    """Print accumulated statistics."""
    print(f"File size: {total_file_size}")
    for code in sorted(status_counts):
        if status_counts[code] > 0:
            print(f"{code}: {status_counts[code]}")


def handle_interrupt(signal_received, frame):
    """Handle keyboard interrupt by printing stats and exiting."""
    print_stats()
    sys.exit(0)

# Register the signal handler for CTRL+C
signal(SIGINT, handle_interrupt)

# Process each line from stdin
for line in sys.stdin:
    match = log_format.match(line.strip())
    if match:
        try:
            # Extract status code and file size
            status_code = int(match.group(3))
            file_size = int(match.group(4))

            # Accumulate file size and status code count
            total_file_size += file_size
            if status_code in status_counts:
                status_counts[status_code] += 1
        except (ValueError, IndexError):
            # Skip line if there is any error in parsing to integer
            continue

        # Count and print stats every 10 lines
        line_count += 1
        if line_count % 10 == 0:
            print_stats()
    else:
        # Skip lines that do not match the required format
        continue

# Final stats printout at end of input
print_stats()
