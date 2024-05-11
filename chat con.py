import subprocess
import sys

# Get command-line arguments
args = sys.argv[1:]  # Exclude the script name itself

# Convert arguments to a single string
inp = ' '.join(args)

# Execute the Nmap command
subprocess.call("nmap " + inp, shell=True)
