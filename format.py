#!/usr/bin/env python3
import glob
import os

BASE_DIR = "/workspace/fun_lines"

def add_blank_lines(filepath):
    with open(filepath, 'r') as f:
        lines = f.readlines()
    
    with open(filepath, 'w') as f:
        for i, line in enumerate(lines):
            f.write(line)
            if not line.endswith('\n'):
                f.write('\n')
            # Only add blank line if current line is non-blank AND next line is non-blank
            if i < len(lines) - 1 and line.strip() != '' and lines[i + 1].strip() != '':
                f.write('\n')
    
    print(f"Processed: {filepath}")

def main():
    pattern = os.path.join(BASE_DIR, "*/actor_assignments*.txt")
    files = glob.glob(pattern)
    
    if not files:
        print(f"No files found matching pattern: {pattern}")
        return
    
    print(f"Found {len(files)} files to process:")
    for f in sorted(files):
        print(f"  {f}")
    print()
    
    for filepath in sorted(files):
        add_blank_lines(filepath)
    
    print(f"\nDone! Processed {len(files)} files.")

if __name__ == "__main__":
    main()