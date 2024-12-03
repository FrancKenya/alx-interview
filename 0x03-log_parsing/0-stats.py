#!/usr/bin/python3
""" """
import sys
import signal

# Initialze variables
total_file_size = 0
status_counts = {code: 0 for code in [
    200, 301, 400, 401, 403, 404, 405, 500]}
line_count = 0


def print_metrics():
    """Print the current metrics."""
    print(f"File size: {total_file_size}")
    for code in sorted(status_counts):
        if status_counts[code] > 0:
            print(f"{code}: {status_counts[code]}")


def process_line(line):
    """Parse and process a single line of log input."""
    global total_file_size

    try:
        parts = line.strip().split()
        # Ensure the line matches the expected format
        if len(parts) < 9:
            return

        # Extract relevant parts
        file_size = int(parts[-1])
        status_code = int(parts[-2])

        # Update metrics
        total_file_size += file_size
        if status_code in status_counts:
            status_counts[status_code] += 1
    except (ValueError, IndexError):
        # Ignore lines with invalid format or values
        return


def signal_handler(sig, frame):
    """Handle keyboard interruption (CTRL + C)."""
    print_metrics()
    sys.exit(0)


# Attach signal handler for graceful shutdown
signal.signal(signal.SIGINT, signal_handler)

# Read and process input
try:
    for line in sys.stdin:
        process_line(line)
        line_count += 1

        # Print metrics every 10 lines
        if line_count % 10 == 0:
            print_metrics()
except KeyboardInterrupt:
    print_metrics()
    raise
finally:
    print_metrics()
