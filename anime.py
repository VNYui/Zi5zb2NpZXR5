#!/usr/bin/env python3

from asciimatics.effects import Print
from asciimatics.renderers import BarChart, FigletText
from asciimatics.scene import Scene
from asciimatics.screen import Screen
from asciimatics.exceptions import ResizeScreenError
import sys
import math
import time
from random import randint


def fn():
    return randint(0, 40)


def wv(x):
    return lambda: 1 + math.sin(math.pi * (2*time.time()+x) / 5)


def demo(screen):
    scenes = []
    effects = [
    Print(screen,
          BarChart(
              7, 60, [lambda: time.time() * 10 % 101],
              gradient=[
                  (33, Screen.COLOUR_RED, Screen.COLOUR_RED),
                  (66, Screen.COLOUR_YELLOW, Screen.COLOUR_YELLOW),
                  (100, Screen.COLOUR_WHITE, Screen.COLOUR_WHITE),
              ] if screen.colours < 256 else [
                  (10, 234, 234), (20, 236, 236), (30, 238, 238),
                  (40, 240, 240), (50, 242, 242), (60, 244, 244),
                  (70, 246, 246), (80, 248, 248), (90, 250, 250),
                  (100, 252, 252)
              ],
              char=">",
              scale=100.0,
              labels=True,
              axes=BarChart.X_AXIS),
          x=int(screen.height / 2-8), y=int(screen.height / 2-8), transparent=False, speed=2),
    ]

    scenes.append(Scene(effects, -1))
    screen.play(scenes, stop_on_resize=True)

def main():
    while True:
        try:
            Screen.wrapper(demo)
            sys.exit(0)
        except ResizeScreenError:
            pass
if __name__ == '__main__':
    main()
