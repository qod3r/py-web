import schedule
import time
from datetime import datetime


def job():
    times = datetime.now().hour % 12
    times = 12 if times == 0 else times
    print('Ку\n' * times)

schedule.every().hour.at(":43").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)