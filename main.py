import os
from datetime import date, time, datetime
import datetime
import random

total_day = 566 #total days back
commit_frequency = 10 #commit time per day
repo_link = "https://github.com/luckybutter322982/git_log.git"

tl = total_day #time day
ctr = 1

now = datetime.datetime.now()

f = open("commit.txt", "w")
os.system("git config user.name")
os.system("git config user.email")
os.system("git init")

pointer = random.randint(0, 10)

while tl > 0:
    # ct = commit_frequency
    ct = random.randint(0, 10)
    while ct > 0:
        f = open("commit.txt", "a+")
        l_date = now + datetime.timedelta(days=-pointer)
        formatdate = l_date.strftime("%Y-%m-%d")
        f.write(f"commit ke {ctr}: {formatdate}\n")
        f.close()
        os.system("git add .")
        os.system(f"git commit --date=\"{formatdate} 12:15:10\" -m \"commit ke {ctr}\"")
        print(f"commit ke {ctr}: {formatdate}")
        ct-=1
        ctr+=1
    pointer+=random.randint(0, 10)
    tl-=1

os.system(f"git remote add origin {repo_link}")
os.system("git branch -M main")
os.system("git push -u origin main -f")