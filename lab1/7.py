import schedule
import sys
import time
from datetime import datetime


def job(text, exc=None):
    currhour = datetime.now().hour
    if exc is not None:
        start, end = map(int, exc.split('-'))
        if currhour >= start and currhour < end:
            return
    
    times = currhour % 12
    times = 12 if times == 0 else times
    print(f'{text}\n' * times)

schedule.every().hour.at(":46").do(job, text=sys.argv[1], exc=sys.argv[2])

while True:
    schedule.run_pending()
    time.sleep(1)