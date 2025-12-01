from datetime import datetime
import pytz
now = datetime.now(tz=pytz.timezone('US/Eastern'))

BASE = R"""
cd inputs
git pull
git add .\{year}\{day:02d}.txt
git commit -m "{year} Day {day}"
lucky_commit.exe {year}D{day:02d}
# git push
cd ..
git pull
git add .\inputs\ .\{year}\{day:02d}.py
git commit -m "{year} Day {day}"
lucky_commit.exe {year}D{day:02d}
# git push
""".strip()
print(BASE.format(year=now.year,day=now.day))
