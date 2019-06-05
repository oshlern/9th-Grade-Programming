from __future__ import division
import subprocess, time, cv2, math
import numpy as np

k = 0.9
gui = True
imageName = "Cobra.jpg"

def getImage(doc):
	return cv2.imread(doc)

def kApproximation(img, k):
	floatForm = np.float32(img)
	s, u, vt = cv2.SVDecomp(floatForm)
	zeros = np.zeros((int(round(s.size*k)), 1))
	sk = np.concatenate((s[:s.size-int(round(s.size*k))], zeros), axis=0)
	diagsk = np.diagflat(sk)
	compressedF = np.dot(u, np.dot(diagsk, vt))
	compressed = np.uint8(compressedF)
	return compressedF

def processImage(imageName, k):
	src = getImage(imageName)
	if len(src.shape) == 3:
		compressedF = np.zeros(src.shape)
		for color in range(src.shape[2]):
			compressedColor = kApproximation(src[:,:,color], k)
			compressedF[:,:,color] = compressedColor
		compressed = np.uint8(compressedF)
		if gui:
			cv2.imshow("src", src)
			cv2.imshow("compressed", compressed)
			cv2.waitKey(0)
		return compressed
	elif len(src.shape) == 2:
		compressed = kApproximation(src, k)
		if gui:
			cv2.imshow("src", src)
			cv2.imshow("compressed", compressed)
			cv2.waitKey(0)
		return compressed
	else:
		print "ERROR: incompatible image"
		return

processImage(imageName, k)
# cv2.imwrite("Compressed" + imageName, processImage(imageName, k))
