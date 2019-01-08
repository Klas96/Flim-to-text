#Film To text. Translates the spech in a film to text.
import speech_recognition as sr
import subprocess
import os
from os import path

timedur = 15

command = "ffmpeg -i ./Film/test.mp4 ./Film/Audio/audio.wav"
subprocess.call(command, shell=True)

command = "ffmpeg -i ./Film/Audio/audio.wav -f segment -segment_time " + str(timedur) + " -c copy ./Film/Audio/audio%d.wav"
subprocess.call(command, shell=True)

command = "rm ./Film/Audio/audio.wav"
subprocess.call(command, shell=True)

list = os.listdir('./Film/Audio/')

r = sr.Recognizer()

for i in range(0,len(list)):

	audio = "Film/Audio/audio" + str(i) + ".wav"

	#print(audio + ": ")

	AUDIO_FILE = os.path.join(path.dirname(path.realpath(__file__)), audio)

	with sr.AudioFile(AUDIO_FILE) as source:
		audioRec = r.record(source)
	try:
		print(str(i*timedur) + "-" + str((i+1)*(timedur)) + ": " + r.recognize_google(audioRec))
		#print(r.recognize_google(audioRec))
	except:
		print(str(i*timedur) + "-" + str((i+1)*(timedur)) + ": " +"...")
		#print("...")

command = "rm ./Film/Audio/*"
subprocess.call(command, shell=True)
