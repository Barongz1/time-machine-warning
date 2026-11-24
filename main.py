"""Funniest Time Machine Warning Label — entry for make.fun.

Writes one line to /output/entry.txt.
The line is the funniest warning label for a time machine, at most 120 characters.
"""
import os

LINE = "WARNING: Do not meet yourself. He owes you money, and he will deny everything."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")

if __name__ == "__main__":
    main()
