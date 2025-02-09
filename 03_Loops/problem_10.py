# Problem: Implement an exponential backoff strategy that doubles the wait time
# between retries, starting from 1 second, but stops after 5 retries.

import time

attempts = 5
retrycount = 0
wait_time = 1

while retrycount < attempts:
    print(f"Your wait time {wait_time} -- Retrying : {retrycount}")
    time.sleep(wait_time)
    retrycount += 1
    wait_time *= 2
