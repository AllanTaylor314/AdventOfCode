"""
AoC fetcher

Guidelines:
 - cache it
 - don't overwrite stuff
 - make it easy to use
 - don't hardcode the session key!
 - include my contact details in the useragent header
"""
from datetime import datetime, timedelta
import pytz
import sys
import os
from pathlib import Path
import requests
from time import sleep
from dotenv import load_dotenv
load_dotenv()
LOGIN_ERROR = b"Puzzle inputs differ by user.  Please log in to get your puzzle input.\n"
EARLY_ERROR = b"Please don't repeatedly request this endpoint before it unlocks! The calendar countdown is synchronized with the server time; the link will be enabled on the calendar the instant this puzzle becomes available.\n"
SESSION = os.environ["SESSION"]
BASE_PATH = Path(os.path.dirname(os.path.realpath(__file__))) # Let this be run from anywhere and act in the right place
TEMPLATE_INPUT = "inputs/{year}/{day:02d}.txt" # Relative to this file
TEMPLATE_URL = "https://adventofcode.com/{year}/day/{day}/input"
PREVIEW_COLS = 80
PREVIEW_ROWS = 5

def fetch_input(day,year,preview=False):
    dir_year = BASE_PATH / f"inputs/{year}"
    if not os.path.isdir(dir_year):
        print(f"No directory for {year}...")
        os.mkdir(dir_year)
        print("Created directory")
    file_input = BASE_PATH / TEMPLATE_INPUT.format(day=day,year=year)
    if os.path.isfile(file_input):
        print(f"Looks like you've got the {year} Day {day} input already")
    else:
        print(end=f"Fetching the {year} Day {day} input...")
        url = TEMPLATE_URL.format(day=day,year=year)
        r = requests.get(url, cookies={"session":SESSION}, headers={"User-Agent":"https://github.com/AllanTaylor314/AdventOfCode/blob/main/fetch_input.py by allan.taylor.pi@gmail.com"})
        print("Got it!")
        if r.content == LOGIN_ERROR:
            print("Whoops - you're not logged in!")
            sys.exit(1)
        if r.content == EARLY_ERROR:
            print("Whoops - too soon!")
            return False
        if preview:
            text = r.content.decode("utf8")
            lines = text.splitlines()
            trimmed_lines = [line[:PREVIEW_COLS]+(f"... [+{len(line)-PREVIEW_COLS}]" if len(line)>PREVIEW_COLS else "") for line in lines[:PREVIEW_ROWS]]
            if len(lines)>PREVIEW_ROWS:trimmed_lines.append(f"... [{len(lines)-PREVIEW_ROWS} more lines]")
            print("\n".join(trimmed_lines))
        with open(file_input, "wb") as file:
            file.write(r.content)
        print(f"Saved to {file_input}")
        return True


now = datetime.now(tz=pytz.timezone('US/Eastern')) + timedelta(minutes=1) # because my computer is slightly out of sync
print(end="Advent of Code")
year = now.year
day = None
if len(sys.argv)==1:
    if now.month != 12:
        print("\nIt's not December yet!")
        sys.exit(1)
    elif now.day > 25:
        print("\nBit late for an advent calendar now")
        sys.exit(1)
    else:
        day = now.day
        print(f" {year}, Day {day}")
        fetch_input(day,year,preview=True)
else:print()
for val in sys.argv[1:]:
    try:
        num = int(val)
    except ValueError:
        print(f"{val!r} could not be interpreted as an integer")
        continue
    if 0<num<=25:
        day=num
        if fetch_input(day,year,preview=len(sys.argv)<5):
            print(end="Waiting 5 seconds for ratelimiting...",flush=True)
            sleep(5)
            print("OK")
    elif 2015<=num<=now.year:
        year=num
        print(f"Set year to {year}")
    else:
        print(f"{num} could not be interpreted as a day or year")
