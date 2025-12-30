import subprocess
from datetime import datetime
import os

from fontTools.unicodedata import script

# Open nmap path file
with open("nmap_dir.txt") as f:
    nmap = f.read().strip()

#print(nmap) Verify nmap path

# Get target from user
target = input("Enter target IP or domain: ")

# Get port and speed from user
ports = input("Enter ports to scan (0-65535, default all): ")
if not ports:
    ports = "-p-"
else:
    ports = ["-p", ports]

speed = input("Enter scan speed (0-5, default 3): ")
if not speed:
    speed = "-T3"
else:
    speed = "-T" + speed



#print(*ports) Verify ports
#print(speed) Verify speed

# Build nmap command
command = [nmap, *ports, speed]

# Get additional options from user
script = input("Enter nmap scripts to use (default none): ")

if script:
    command = [nmap, *ports, speed, "--script", script]
else:
    pass

# Generate timestamp
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
output_dir = f"scans/{target}_{timestamp}"
os.makedirs(os.path.dirname(output_dir), exist_ok=True)

# Build nmap command with output options
command.extend(["-oA", output_dir, target])

# Run nmap command
subprocess.run(command)

