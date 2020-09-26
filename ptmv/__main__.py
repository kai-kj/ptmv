import argparse
import mimetypes
import os
import signal

from ptmv import console
from ptmv import img
from ptmv import snd
from ptmv import vid
from ptmv import yt


def get_args():
	doc = """\nView images and videos without leaving the console.\n
	Requires a terminal that supports truecolor and utf-8\n
	For more info visit <https://github.com/kal39/TerminalMediaViewer>"""

	parser = argparse.ArgumentParser(description=doc)
	parser.add_argument("FILE")
	parser.add_argument("-y", "--youtube", help="Play video from youtube.", action="store_true")
	parser.add_argument("--width", help="Set output width.", type=int)
	parser.add_argument("--height", help="Set output height.", type=int)
	parser.add_argument("--fps", help="Set target fps; Default 15 fps.", type=int, default=15)
	parser.add_argument("--start-time", help="Set start time (seconds)", type=float, default=0)
	parser.add_argument("-v", "--volume", help="Set audio volume (0 ~ 1).", type=float, default=1)
	parser.add_argument("-i", "--no-info", help="Disable progress bar for videos.", action="store_true")

	return parser.parse_args()


def file_type(file):
	mimetypes.init()
	f_type = mimetypes.guess_type(file)[0]
	f_type = f_type.split('/')[0]
	return f_type


def main():
	signal.signal(signal.SIGINT, console.cleanup)

	args = get_args()

	args.FILE = os.path.expanduser(args.FILE)

	if args.youtube:
		yt_file = yt.download(args.FILE)
		args.FILE = yt_file
		vid.play(args)

	if not os.path.isfile(args.FILE):
		print("[%s] does not exist" % args.FILE)
		console.cleanup()

	if file_type(args.FILE) == "image":
		img.display(args)

	elif file_type(args.FILE) == "video":
		vid.play(args)

	elif file_type(args.FILE) == "audio":
		snd.play(args)

	else:
		print("[%s] is not an image or video file" % args.FILE)
		console.cleanup()

	console.cleanup()


if __name__ == '__main__':
	main()
