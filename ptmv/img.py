import cv2

from . import console

def display(file, user_width, user_height):
	image = cv2.imread(file)
	if image is None: print("Could not read [%s]" % file); return
	image = resize(image, user_width, user_height)
	console.set_image_height(image.shape[0])
	console.clear()
	console.draw_image(image)

def resize(image, user_width, user_height):
	image_height, image_width, _ = image.shape

	if user_width is None and user_height is None:
		scale_x = min(console.width() / image_width, console.height() / image_height)
		scale_y = scale_x
	elif user_width is not None:
		scale_x = user_width / image_width
		scale_y = scale_x
	elif user_height is not None:
		scale_y = user_height / image_height
		scale_x = scale_y
	else:
		scale_x = user_width / image_width
		scale_y = user_height / image_height

	return cv2.resize(image, (0, 0), interpolation = cv2.INTER_AREA, fx = scale_x, fy = scale_y)