import time
import cv2

from . import console
from . import img
from . import snd

def play(file, width, height, target_fps, start_offset):
	video = cv2.VideoCapture(file)
	audio = snd.extract(file)
	if video is None: print("Could not read [%s]" % file); return

	orig_height, orig_width, _ = get_frame(video, 0).shape
	out_height, out_width, _ = img.resize(get_frame(video, 0), width, height).shape

	console.set_image_height(out_height)
	video_loop(video, audio, out_width / orig_width, out_height / orig_height, target_fps, start_offset)

def video_loop(video, audio, scale_x, scale_y, target_fps, start_offset):
	frame_count = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
	fps = int(video.get(cv2.CAP_PROP_FPS))
	dt = 1 / target_fps

	console.hide_cursor()
	snd.play(audio, start_offset)
	console.clear()

	prev_frame = None
	start_time = time.time() - start_offset
	prev_time = time.time() - dt

	while True:
		current_time = time.time()
		if current_time - prev_time > dt:
			prev_time = current_time
			current_frame = get_frame(video, int((current_time - start_time) * fps))
			if current_frame is None: break

			current_frame = cv2.resize(current_frame, (0, 0), fx = scale_x, fy = scale_y)
			console.draw_frame(prev_frame, current_frame)
			prev_frame = current_frame

def get_frame(video, frame_num):
	video.set(1, frame_num)
	return video.read()[1]