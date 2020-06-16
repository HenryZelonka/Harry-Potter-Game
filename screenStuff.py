#imports
from time import sleep
import sys

#scrolly text
def scroll(string):
  for x in string:
    print(x, end = "")
    sys.stdout.flush()
    sleep(0.05)

#clearing the screen
def cls():
  print("\033[2J")
  print("\033[%d;%dH" % (0, 0))
  