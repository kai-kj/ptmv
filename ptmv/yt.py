from __future__ import unicode_literals
import youtube_dl
import os
import time


def download(url):
	if not os.path.exists("/tmp/ptmv"):
		os.makedirs("/tmp/ptmv")

	yt_file = "/tmp/ptmv/" + str(int(time.time()))

	ydl_opts = {
		"quiet": True,
		"no_warnings": True,
		"outtmpl": yt_file
	}

	yt_file += ".mkv"

	with youtube_dl.YoutubeDL(ydl_opts) as ydl:
		ydl.download([url])

	return yt_file
