import os

print("Spark Scheduler")
try:
    # Query standard output descriptor
    terminalColumns, terminalsLines = os.get_terminal_size()
    print(f"Terminal width: {terminalColumns}")
except OSError:
    print("Not running in a standard terminal viewport.")