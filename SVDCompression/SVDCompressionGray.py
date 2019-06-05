from __future__ import division
import subprocess, time, cv2, math
import numpy as np

gui = True
imageName = "Kitten.jpeg"

def getImage(doc):
	return cv2.imread(doc)

def processImage(imageName):
	k = 0.9
	src = getImage(imageName)
	if gui:
		cv2.imshow("src", src)
	if len(src.shape) == 3:
		if src.shape[2] == 3 or src.shape[2] == 4:
			src = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
			if gui:
				cv2.imshow("gray", src)
		else:
			print "ERROR: uncompatible number of channels"
			return
	floatForm = np.float32(src)
	w, u, vt = cv2.SVDecomp(floatForm)
	zeros = np.zeros((int(round(w.size*k)), 1))
	wk = np.concatenate((w[:int(round(w.size*(1-k)))], zeros), axis=0)
	diagwk = np.diagflat(wk)
	compressedF = np.dot(u, np.dot(diagwk, vt))
	# compressedF *= 50/compressedF.max()
	compressed = np.uint8(compressedF)

	if gui:
		cv2.imshow("compressed", compressed)
		cv2.waitKey(0)

	return compressed

cv2.imwrite("Compressed" + "Gray" + imageName, processImage(imageName))
