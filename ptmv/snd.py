import os
import subprocess
import tempfile
import time
import wave
import simpleaudio

def extract(file):
	ptmv_tempdir = os.path.join(tempfile.gettempdir(), "ptmv")
	if not os.path.exists(ptmv_tempdir): os.makedirs(ptmv_tempdir)
	snd_file = ptmv_tempdir + str(int(time.time())) + ".wav"
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