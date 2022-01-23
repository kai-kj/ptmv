import signal
import sys
import argparse
import mimetypes
import os
import threading

from . import console
from . import img
from . import snd
from . import vid
from . import yt

def get_args():
	doc = """
		View images and videos without leaving the console.\n
		Requires a terminal that supports truecolor and utf-8\n
		For more info visit <https://github.com/kal39/TerminalMediaViewer>
		"""

	parser = argparse.ArgumentParser(description = doc)
	parser.add_argument("FILE")
	parser.add_argument("-y", "--youtube", help = "Play video from youtube.", action = "store_true")
	parser.add_argument("--width", help = "Set output width.", type = int)
	parser.add_argument("--height", help = "Set output height.", type = int)
	parser.add_argument("--fps", help = "Set target fps; Default 15 fps.", type = int, default = 15)
	parser.add_argument("--start-time", help = "Set start time (seconds)", type = float, default = 0)
	parser.add_argument("-m", "--mute", help = "Mute audio", action = "store_true")
		
	parsed_args = parser.parse_args()
	parsed_args.FILE = os.path.expanduser(parsed_args.FILE)
	return parsed_args

def main():
	args = get_args()
	
	signal.signal(signal.SIGINT, set_exit_flag)
	threading.Thread(target = exit_flag_watcher).start()

	if args.youtube: args.FILE = yt.download(args.FILE)
	if not os.path.isfile(args.FILE):
		print("[" + args.FILE + "] does not exist"); os._exit(-1)

	if file_type(args.FILE) == "image": img.display(args.FILE, args.width, args.height)
	elif file_type(args.FILE) == "video": vid.play(args.FILE, args.width, args.height, args.fps, args.start_time)
	else: print("[" + args.FILE + "] is not a supperted file type"); os._exit(-1)

	set_exit_flag()

def file_type(file):
	mimetypes.init()
	return mimetypes.guess_type(file)[0].split('/')[0]

exit_flag = False

def set_exit_flag(*_): global exit_flag; exit_flag = True

def exit_flag_watcher():
	while True:
		if exit_flag:
			console.cleanup()
			os._exit(0)

if __name__ == "__main__": main()