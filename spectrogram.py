import matplotlib.pyplot as pyplot
import numpy as numpy
import wave
import sys
import glob, os

os.chdir("audio")

for file in glob.glob("*.wav"):
	spf = wave.open(file, 'r')

	signal = spf.readframes(-1)
	signal = numpy.fromstring(signal,'Int16');

	pyplot.figure(1)
	pyplot.specgram(signal[0])
	pyplot.axis('off')
	pyplot.savefig( file + '.png', bbox_inches='tight')

