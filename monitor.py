import threading
from time import time, sleep
from datetime import datetime

now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

while True:
    sleep(60 - time() % 60)
    with open('apache-status.txt') as f:
        if 'failed' in f.read():
            print("[", now, "]", "Apache entered a failed state!\n")
        else:
            dot = "."
            print ("[", now, "]", dot, sep=" ", end=" ", flush=True)
