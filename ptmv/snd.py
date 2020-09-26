import os
import subprocess
import time
import wave

import simpleaudio


def extract(file):
	if not os.path.exists("/tmp/ptmv"):
		os.makedirs("/tmp/ptmv")

	snd_file = "/tmp/ptmv/" + str(int(time.time())) + ".wav"

	command = "ffmpeg -i %s -b:a 48k -ac 1 %s" % (file, snd_file)

	subprocess.run(command.split(), stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

	return snd_file


def stop(play_obj):
	play_obj.stop()


def start(file, location):
	wave_raw = wave.open(file)

	frame_rate = wave_raw.getframerate()

	wave_raw.setpos(int(frame_rate * location))

	wave_obj = simpleaudio.WaveObject.from_wave_read(wave_raw)

	play_obj = wave_obj.play()

	return play_obj


def play(args):
	play_obj = start(args.FILE, args.start_time)

	time.sleep(2)

	stop(play_obj)
