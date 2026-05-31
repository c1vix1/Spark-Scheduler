import os

print("Spark Scheduler")
try:
    # Query standard output descriptor
    terminalColumns = os.get_terminal_size()[0]
    print(f"Terminal width: {terminalColumns}")
except OSError:
    print("Not running in a standard terminal viewport.")
    terminalColumns = 10 