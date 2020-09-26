import cv2
import numpy

from ptmv import console


def resize(image, args):
	height, width, _ = image.shape

	if args.width is None and args.height is None:
		zoom_x = min(console.width() / width, console.height() / height)
		zoom_y = zoom_x

	elif args.width is not None:
		zoom_x = args.width / width
		zoom_y = zoom_x

	elif args.height is not None:
		zoom_y = args.height / height
		zoom_x = zoom_y

	else:
		zoom_x = args.width / width
		zoom_y = args.height / height

	image = cv2.resize(image, (0, 0), interpolation=cv2.INTER_AREA, fx=zoom_x, fy=zoom_y)

	return image


def draw(prev, current):
	height, width, _ = current.shape
	console.hide_cursor()

	for i in range(0, height - 1, 2):
		for j in range(0, width - 1):
			if prev is None \
					or not numpy.array_equal(prev[i, j], current[i, j]) \
					or not numpy.array_equal(prev[i + 1, j], current[i + 1, j]):
				console.fg_color(current[i, j, 2], current[i, j, 1], current[i, j, 0])
				console.bg_color(current[i + 1, j, 2], current[i + 1, j, 1], current[i + 1, j, 0])

				console.move_cursor(j + 1, i / 2 + 1)
				print("▄", end="")

	console.show_cursor()


def display(args):
	image = cv2.imread(args.FILE)

	if image is None:
		print("Could not read [%s]" % args.FILE)
		console.cleanup()

	console.setup_height(image, args)

	image = resize(image, args)
	draw(None, image)
