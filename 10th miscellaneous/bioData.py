import numpy as np
import cv2
from matplotlib import pyplot as plt

file = '/Users/oshlern/Downloads/Pineapple Screaming.mp4'
framerate = 29.726

def recordValues():
	video = cv2.VideoCapture(file)
	colors = np.zeros((3,1))
	i = 0
	retval, image = video.read()
	while retval:
		i += 1
		if i%1000 == 0:
			print "frame: ", i
		average = np.average(image, axis=0)
		average = np.average(average, axis=0)
		average = np.transpose(np.array([average]))
		colors = np.append(colors, average, axis=1)
		retval, image = video.read()
	timestamps = [np.arange(colors.shape[1])]
	timestamps = np.true_divide(timestamps, framerate)
	colors = np.concatenate((np.array(timestamps), colors), axis=0)
	np.save('colorData.npy', colors)
	return colors

def plot(colors):
	timestamps = colors[0, :]
	plt.plot(timestamps, colors[1, :], 'b', timestamps, colors[2, :], 'g', timestamps, colors[3, :], 'r')
	plt.title("BGR Data")
	plt.ylabel("Average value across frame")
	plt.xlabel("Seconds")

colors = recordValues()
# colors = np.load('colorData.npy')
plot(colors)
plt.show()




