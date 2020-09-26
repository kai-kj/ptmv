import time

import cv2

from ptmv import console
from ptmv import img
from ptmv import snd


def read_frame(video, frame_num):
	video.set(1, frame_num)
	_, frame = video.read()

	return frame


def video_loop(video, args):
	frame_count = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
	fps = int(video.get(cv2.CAP_PROP_FPS))

	frame_time = 1 / args.fps

	prev = None
	start_time = time.time() - args.start_time
	prev_time = time.time()

	while True:
		current_time = time.time()
		if current_time - prev_time > frame_time:
			prev_time = time.time()
			frame_num = int((current_time - start_time) * fps)

			if frame_num > frame_count - 1:
				break

			current = read_frame(video, frame_num)
			current = img.resize(current, args)
			img.draw(prev, current)
			prev = current


def play(args):
	video = cv2.VideoCapture(args.FILE)

	image = read_frame(video, 1)
	console.setup_height(image, args)

	if video is None:
		print("Could not read [%s]" % args.FILE)
		console.cleanup()

	if args.volume != 0:
		snd_file = snd.extract(args.FILE)
		play_obj = snd.start(snd_file, args.start_time)

	video_loop(video, args)

	if args.volume != 0:
		snd.stop(play_obj)
