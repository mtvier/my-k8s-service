import time


cnt = 0

while 1:
    cnt += 1
    time.sleep(1)
    if cnt == 30:
        print("Alive and kicking")
        cnt = 0

