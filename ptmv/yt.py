from __future__ import unicode_literals
import yt_dlp as ytdl
import os
import time

def download(url):
	if not os.path.exists("/tmp/ptmv"): os.makedirs("/tmp/ptmv")
	file = "/tmp/ptmv/" + str(int(time.time()))
	
	ydl_opts = {
		"format": "worst[ext=mp4]",
		"outtmpl": file + ".%(ext)s",
		"quiet": True,
		"no_warnings": True,
	}
	
	ytdl.YoutubeDL(ydl_opts).download([url])
	return file + ".mp4"
