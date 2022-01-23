import os
import sys
import numpy
import threading

def width(): return int(os.popen('stty size', 'r').read().split()[1])
def height(): return int(os.popen('stty size', 'r').read().split()[0]) * 2

image_height = height()

def _hide_cursor(): return "\033[?25l"
def _show_cursor(): return "\033[?25h"
def _move_cursor(x, y): return "\033[%d;%dH" % (y, x)
def _fg_color(r, g, b): return "\x1b[48;2;%d;%d;%dm" % (r, g, b)
def _bg_color(r, g, b): return "\x1b[38;2;%d;%d;%dm" % (r, g, b)
def _reset_colors(): return "\x1b[0m"
def _clear(): return "\n" * int(height() / 2)

def hide_cursor(): print(_hide_cursor(), end = "")
def show_cursor(): print(_show_cursor(), end = "")
def move_cursor(x, y): print(_move_cursor(x, y), end = "")
def fg_color(r, g, b): print(_fg_color(r, g, b), end = "")
def bg_color(r, g, b): print(_bg_color(r, g, b), end = "")
def reset_colors(): print(_reset_colors(), end = "")
def clear(): print(_clear(), end = "")
def set_image_height(height): global image_height; image_height = height

def cleanup():
	reset_colors()
	show_cursor()
	move_cursor(0, int(image_height / 2))
	print()

def draw_image(image): draw_frame(None, image)

def draw_frame(prev, current):
	instructions = ""

	nextPos = (-1, -1)
	for i in range(0, current.shape[0] - 1, 2):
		for j in range(0, current.shape[1] - 1):
			if prev is None or not (pixel_equals(prev, current, i, j) and pixel_equals(prev, current, i + 1, j)):
				instructions += _fg_color(current[i, j, 2], current[i, j, 1], current[i, j, 0])
				instructions += _bg_color(current[i + 1, j, 2], current[i + 1, j, 1], current[i + 1, j, 0])
				if not (i, j) == nextPos: instructions += _move_cursor(j + 1, i / 2 + 1)
				instructions += "▄"
				nextPos = (i, j + 1)

	sys.stdout.write(instructions)

def pixel_equals(a, b, i, j): return a[i, j, 0] == b[i, j, 0] and a[i, j, 1] == b[i, j, 1] and a[i, j, 2] == b[i, j, 2]