import os
import subprocess
import time
import wave
import simpleaudio

def extract(file):
	if not os.path.exists("/tmp/ptmv"): os.makedirs("/tmp/ptmv")
	snd_file = "/tmp/ptmv/" + str(int(time.time())) + ".wav"
	command = "ffmpeg -i " + file + " -b:a 48k -ac 1 " + snd_file
	subprocess.run(command.split(), stdout = subprocess.DEVNULL, stderr = subprocess.DEVNULL)
	return snd_file

def play(file, start_time):
	if not os.path.exists(file): return
	wave_raw = wave.open(file)
	frame_rate = wave_raw.getframerate()
	wave_raw.setpos(int(frame_rate * start_time))
	return simpleaudio.WaveObject.from_wave_read(wave_raw).play()

def stop(play_obj): play_obj.stop()