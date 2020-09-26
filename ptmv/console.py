import os
import sys


height_offset = 0


def width():
	rows, columns = os.popen('stty size', 'r').read().split()
	return int(columns)


def height():
	rows, columns = os.popen('stty size', 'r').read().split()
	return int(rows) * 2


def hide_cursor():
	print("\033[?25l", end="")


def show_cursor():
	print("\033[?25h", end="")


def move_cursor(x, y):
	print("\033[%d;%dH" % (y, x), end="")


def fg_color(r, g, b):
	print("\x1b[48;2;%d;%d;%dm" % (r, g, b), end="")


def bg_color(r, g, b):
	print("\x1b[38;2;%d;%d;%dm" % (r, g, b), end="")


def reset():
	print("\x1b[0m\033[?25h", end="")


def setup_height(image, args):
	img_height, img_width, _ = image.shape

	if args.width is None and args.height is None:
		zoom_x = min(width() / img_width, height() / img_height)
		zoom_y = zoom_x

	elif args.width is not None:
		zoom_x = args.width / img_width
		zoom_y = zoom_x

	elif args.height is not None:
		zoom_y = args.height / img_height

	else:
		zoom_y = args.height / img_height

	global height_offset
	height_offset = int(img_height * zoom_y / 2)


def cleanup(*_):
	reset()
	move_cursor(0, 0)
	print("\033[%dB" % height_offset, end="")
	sys.exit(0)
