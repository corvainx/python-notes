# Lesson 01: File and Directory Detection using 'os.path' and 'pathlib'
import os
from pathlib import Path

# Compute relative path to target file
base_dir = os.path.dirname(os.path.abspath(__file__))
target_path = os.path.join(base_dir, "data", "sample.txt")

print(f"Checking location: {target_path}")

if os.path.exists(target_path):
    print("Status: The target path exists.")
    if os.path.isfile(target_path):
        print("  -> It is a regular file.")
    elif os.path.isdir(target_path):
        print("  -> It is a directory.")
else:
    print("Status: Target location does not exist.")

# Modern pathlib alternative
p = Path(target_path)
print(f"Pathlib check: exists={p.exists()}, is_file={p.is_file()}")
