import time
import sys
import random

def run1():

    animation = "|/-\\"
    quote="ressources/quote.txt"

    for i in range(10):
        time.sleep(0.2)
        sys.stdout.write("\r" + animation[i % len(animation)])
        sys.stdout.flush()
        with open(quote, 'r') as f:
            x = print("     " + random.choice(f.readlines()))
        print("-------------------------------------------------------")

def run2():
    animation = "|/-\\"
    for i in range(100):
        time.sleep(0.4)
        sys.stdout.write("\r" + animation[i % len(animation)])
        sys.stdout.flush()
