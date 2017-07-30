import sys
import os

if len(sys.argv) < 1:
    print("not enough arguments. exiting...")
    sys.exit(1)

if len(sys.argv) >= 1:
    file_name = sys.argv[1]
    if not os.path.isfile(file_name):
        with open(file_name, 'w') as f:
            f.write("kaise ho")

    
