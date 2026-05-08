#!/usr/bin/env python3
import os
import re
import sys
from pathlib import Path

# Ensure we are using Python 3
if sys.version_info[0] < 3:
    print("Error: TreeGen requires Python 3.x")
    sys.exit(1)

def generate_structure(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"❌ Error: File '{file_path}' not found.")
        sys.exit(1)
    except PermissionError:
        print(f"❌ Error: Permission denied when reading '{file_path}'.")
        sys.exit(1)

    path_stack = {}  
    print(f"🚀 TreeGen: Processing {file_path}...\n")

    for line_num, line in enumerate(lines, 1):
        if '#' in line:
            line = line.split('#')[0]
        line = line.rstrip()

        if not line:
            continue

        match = re.match(r'^([│├└─\s]*)(.+)$', line)
        if not match:
            continue

        prefix = match.group(1)
        name = match.group(2).strip()
        depth = len(prefix) // 4
        is_dir = name.endswith('/')
        clean_name = name.rstrip('/')

        if depth == 0:
            current_path = Path(clean_name)
        else:
            parent_path = path_stack.get(depth - 1, Path("."))
            current_path = parent_path / clean_name

        path_stack[depth] = current_path

        try:
            if is_dir:
                current_path.mkdir(parents=True, exist_ok=True)
                print(f"📁 Created: {current_path}")
            else:
                current_path.parent.mkdir(parents=True, exist_ok=True)
                current_path.touch(exist_ok=True)
                print(f"📄 Created: {current_path}")
        except PermissionError:
            print(f"⚠️  Skipped: Permission denied at '{current_path}'")
        except OSError as e:
            print(f"❌ Failed: {current_path}. Reason: {e.strerror}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: treegen <filename.txt>")
    else:
        generate_structure(sys.argv[1])
        print("\n✨ Scaffolding complete!")