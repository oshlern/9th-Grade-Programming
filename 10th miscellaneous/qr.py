import cv2, copy
import numpy as np
def pxlTovVal(img):
	avg = np.average(img)
	if avg < 255 - avg:
		return 0
	else:
		return 1

def imageToQR(src, disp, pxlSize):
	shp = src.shape
	img = src[disp:shp[0]-disp, disp:shp[1]-disp]
	shp = img.shape[:2]
	num = np.ceil(np.divide(shp,pxlSize)).astype(int)
	qr = np.zeros(num)
	for i in range(num[0]):
		for j in range(num[1]):
			pxl = img[i*pxlSize:(i+1)*pxlSize, j*pxlSize:(j+1)*pxlSize]
			qr[i,j] = pxlTovVal(pxl)
	return qr

def qrToImage(qr, pxlSize=10, disp=20):
	shp = qr.shape
	img = np.ones(np.add(np.multiply(shp, pxlSize), disp*2))
	for i in range(shp[0]):
		for j in range(shp[1]):
			on = qr[i,j]
			if on:
				pxl = np.ones((pxlSize, pxlSize))
			else:
				pxl = np.zeros((pxlSize, pxlSize))
			img[disp+i*pxlSize:disp+(i+1)*pxlSize, disp+j*pxlSize:disp+(j+1)*pxlSize] = pxl
	return img


real = cv2.imread("/Users/oshlern/Downloads/randqr.png")
image = cv2.imread("/Users/oshlern/Downloads/1e07e67d356ef6aa9ec31c2dd8a970892604acef_qr2.bmp")
# cv2.imshow('image', image)
disp = 40
pxlSize = 10
qr = imageToQR(image, 40, 10)
cv2.imshow('qr', qrToImage(qr))
# print qr.shape

bigCorner = copy.deepcopy(qr[:8,:8])
smallCorner = copy.deepcopy(qr[20:25,20:25])
line = copy.deepcopy(qr[6,9:-9])
Edge1 = qr[8,:8]
Edge2 = qr[:9,8]
print Edge1, qr[-8:,8]
print Edge2, qr[8,-9:]

def setCorners(qr, bigCorner=bigCorner, smallCorner=smallCorner): #29x29
	qr[:8,:8] = bigCorner
	qr[-8:,:8] = np.flipud(bigCorner)
	qr[:8,-8:] = np.fliplr(bigCorner)
	qr[20:25,20:25] = smallCorner
	return qr

def setLines(qr, line=line):
	qr[6, 9:-9] = line
	qr[9:-9, 6] = line
	return qr

def setEdgesHard(qr, edge1=Edge1, edge2=Edge2):
	qr[8,:8] = edge1
	qr[-8:,8] = edge1[::-1]
	qr[:9,8] = edge2
	qr[8,-9:] = edge2[::-1]
	return qr

def setEdges(qr):
	edge1 = qr[8,:8]
	if all(edge1) == 1:
		edge1 = qr[-8:,8]
		qr[8,:8] = edge1[::-1]
	else:
		qr[-8:,8] = edge1[::-1]
	edge2 = qr[:9,8]
	if all(edge2[:8]) == 1:
		edge2 = qr[8,-9:]
		qr[:9,8] = edge2[::-1]
	else:
		qr[8,-9:] = edge2[::-1]
	return qr

def mask0(row,col):
	return (row + col)%2 == 0

def mask0Shift(row, col):
	return (row + col)%2 == 1

def mask1(row, col):
	return row%2 == 0

def mask1Shift(row, col):
	return row%2 == 1

def mask6(row, col):
	return ((row * col)%2 + (row * col)%3) % 2 == 0

def mask6Shift(row, col):
	row += 1
	return ((row * col)%2 + (row * col)%3) % 2 == 0

def mask7(row, col):
	return ((row+col)%2 + (row*col)%3)%2 == 0

def mask7Shift(row, col):
	row+=1
	return ((row+col)%2 + (row*col)%3)%2 == 0



def mask(qr, maskf):
	bigCorner = copy.deepcopy(qr[:8,:8])
	smallCorner = copy.deepcopy(qr[20:25,20:25])
	line = copy.deepcopy(qr[6,9:-9])
	e1 = copy.deepcopy(qr[8,:8])
	# if all(edge1) == 1:
	# 	edge1 = qr[-8:,8][[-1]]
	e2 = copy.deepcopy(qr[:9,8])
	# if all(edge2[:8]) == 1:
	# 	edge2 = qr[8,-9:][[-1]]
	for row in range(len(qr)):
		for col in range(len(qr[0])):
			if maskf(row, col):
				if qr[row, col]:
					qr[row, col] = 0
				else:
					qr[row, col] = 1
	setCorners(qr, bigCorner=bigCorner, smallCorner=smallCorner)
	setLines(qr, line=line)
	setEdgesHard(qr, edge1=e1, edge2=e2)
	return qr


# lines between big corners are white,black...
# lines along corner edges are the same as other edges 
# 

qrs = []
# qr[:10, :10] = np.zeros((10,10))
print qr[:,1:].shape, np.transpose([qr[:,0]]).shape
qr1 = np.concatenate((qr[1:], [qr[0]]), axis=0)
qr2 = np.concatenate((qr[:,1:], np.transpose([qr[:,0]])), axis=1)
# qrs += [np.roll(qr,1)] 
qrs += [np.roll(qr,1,axis=0)]
# qrs += [np.roll(qr,1,axis=1)]
# qrs += [np.roll(qr,-1,axis=0)]
# qrs += [np.roll(qr,-1,axis=1)]
# qrs += [np.roll(np.roll(qr,1,axis=1), 1, axis=0)]
# qrs += [np.roll(np.roll(qr,-1,axis=1), -1, axis=0)]
# qrs += [np.roll(np.roll(qr,-1,axis=1), 1, axis=0)]
# qrs += [np.roll(np.roll(qr,1,axis=1), -1, axis=0)]
# qrs += [np.roll(qr,-1)]

qrs += [np.zeros(qr.shape)]
#none work
realQR = imageToQR(real, 37, 5)
qrs += [realQR]

# print qr1.shape
# for i in range(len(qrs)):
# 	setCorners(qrs[i])
# 	setLines(qrs[i])
# 	setEdges(qrs[i])
# 	cv2.imshow('qr' + str(i), qrToImage(qrs[i]))

# qr = np.zeros(qr.shape)
setCorners(qr)
setLines(qr)
setEdgesHard(qr)
cv2.imshow('a', qrToImage(qr))
qr = mask(qr, mask6Shift)
cv2.imshow('b', qrToImage(qr))
qr = mask(qr, mask6)
cv2.imshow('c', qrToImage(qr))
# 1011010001001
# 011001000111101
# 101010000010010


cv2.waitKey(0)
cv2.destroyAllWindows()


# image = image[:,:,0]
# shp = image.shape
# for i in range(shp[0]):
# 	for j in range(shp[1]):
# 		if 40 < i < 120:
# 			if 40< j < 120 or shp[1]-40 > j > shp[1] - 120:
# 				continue
# 		elif shp[0]-40 > i > shp[0]-120 and 40 < j < 120:
# 			continue
# 		elif shp[0]-80> i > shp[0]-130 and shp[0]-80> j > shp[0]-130:
# 			continue
# 		if image[i,j] == 0:
# 			image[i,j] = 255
# 		elif image[i,j] == 255:
# 			image[i,j] = 0
# 		else:
# 			print image[i,j], i, j

# # cv2.imshow('qr',image)

# #QR
# image = cv2.imread("/Users/oshlern/Downloads/55b2063cb31834298a8ec44a518d93f5359840b7_qr1.bmp")
# shp = image.shape[:2]
# print shp

# # cv2.imshow(image)
# channels = cv2.split(image)
# r,g,b = channels[0], channels[1], channels[2]
# R,G,B = r,g,b
# # R,G,B = np.zeros(shp), np.zeros(shp), np.zeros(shp)
# index = 0
# for mat,MAT in zip([r,g,b],[R,G,B]):
# 	for i in range(shp[0]):
# 		for j in range(117) + range(shp[1]-117, shp[1]):
# 			if mat[i,j] == 1:
# 				# print i,j, "1"
# 				MAT[i,j] = 255
# 			elif mat[i,j] == 254:
# 				# print i,j
# 				MAT[i,j] = 0
# 			# if mat[i,j] != 0 and mat[i,j] != 255:
# 			# 	# print mat[i,j]
# 			# 	MAT[i,j] = 255
# 			# else:
# 			# 	MAT[i,j] = 0
# 	# MAT = cv2.cvtColor(MAT, cv2.COLOR_GRAY2BGR)
# 	# print type(MAT)
# 	# cv2.imshow(str(index), MAT)
# 	index+=1