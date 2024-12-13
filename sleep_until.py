"""
AoC Sleeper

A simple script that blocks until the next Advent of Code puzzle unlocks
Useful when chained like ./sleep_until.py; ./fetch_input.py
"""

from time import sleep
import re

import requests

r = requests.get(
    "https://adventofcode.com",
    headers={
        "User-Agent": "https://github.com/AllanTaylor314/AdventOfCode/blob/main/sleep_until.py by allan.taylor.pi@gmail.com"
    },
)
m = int(next(re.finditer(r"server_eta = (\d+)", r.text)).group(1))
print(f"Sleeping for {m} seconds...")
sleep(m)
print("and GO!")
