"""
AoC fetcher

Guidelines:
 - cache it
 - don't overwrite stuff
 - make it easy to use
 - don't hardcode the session key!
 - include my contact details in the useragent header
"""
from datetime import datetime
import pytz
import sys
import os
from pathlib import Path
import requests
from dotenv import load_dotenv
load_dotenv()
LOGIN_ERROR = b"Puzzle inputs differ by user.  Please log in to get your puzzle input.\n"
EARLY_ERROR = b"Please don't repeatedly request this endpoint before it unlocks! The calendar countdown is synchronized with the server time; the link will be enabled on the calendar the instant this puzzle becomes available.\n"
SESSION = os.environ["SESSION"]
BASE_PATH = Path(os.path.dirname(os.path.realpath(__file__))) # Let this be run from anywhere and act in the right place

now = datetime.now(tz=pytz.timezone('US/Eastern'))
# now = datetime(2015,12,5)
print(f"Advent of Code {now.year}")

if now.month != 12:
    print("It's not December yet!")
    sys.exit(1)
if now.day > 25:
    print("Bit late for an advent calendar now")
    sys.exit(1)

dir_year = BASE_PATH / f"./{now.year}"
if not os.path.isdir(dir_year):
    print("No directory for current year...")
    os.mkdir(dir_year)
    print("Created directory")

file_input = BASE_PATH / f"{now.year}/{now.day:02d}.txt"
url = f"https://adventofcode.com/{now.year}/day/{now.day}/input"
if os.path.isfile(file_input):
    print("Looks like you've got today's input already")
else:
    print(end="Fetching the input...")
    r = requests.get(url, cookies={"session":SESSION}, headers={"User-Agent":"https://github.com/AllanTaylor314/AdventOfCode/blob/main/fetch_input.py by allan.taylor.pi@gmail.com"})
    print("Got it!")
    if r.content == LOGIN_ERROR:
        print("Whoops - you're not logged in!")
        sys.exit(1)
    if r.content == EARLY_ERROR:
        print("Whoops - too soon!")
        sys.exit(1)
    text = r.content.decode("utf8")
    print(text[:100]+("..." if len(text)>100 else ""))
    with open(file_input, "wb") as file:
        file.write(r.content)
    print(f"Saved to {file_input}")
