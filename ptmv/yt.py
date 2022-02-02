from __future__ import unicode_literals
import yt_dlp as ytdl
import os
import tempfile
import time

def download(url):
	ptmv_tempdir = os.path.join(tempfile.gettempdir(), "ptmv")
	if not os.path.exists(ptmv_tempdir): os.makedirs(ptmv_tempdir)
	file = ptmv_tempdir + str(int(time.time()))
	
	ydl_opts = {
		"format": "worst[ext=mp4]",
		"outtmpl": file + ".%(ext)s",
		"quiet": True,
		"no_warnings": True,
	}
	
	ytdl.YoutubeDL(ydl_opts).download([url])
	return file + ".mp4"
