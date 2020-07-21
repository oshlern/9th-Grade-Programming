import cv2, os
import numpy as np

imageNum=0
imageName = "img"
gripImageName = "contours"
def findMatchNum():
	i = 1
	while os.path.exists("match" + str(i)):
		i += 1
	return i

folder = "match" + str(findMatchNum())
# folder = "match" + str(np.random.randint(1000))

image = cv2.imread("/Users/oshlern/Downloads/train.jpg")
os.makedirs(folder)

def save(image, name=None, withGrip=False, withRand=True):
	if name != None:
		cv2.imwrite(name + ".jpg", image)
		return
	if withGrip:
		name = gripImageName
	else:
		name = imageName
	if withRand:
		name = folder + '/' + name
	global imageNum
	name += str(imageNum)
	cv2.imwrite(name + ".jpg", image)
	imageNum += 1

save(image)
save(image, withGrip=True)
save(image)
save(image)
name = folder+'/'+imageName + str(imageNum)
print name
# cv2.imwrite(name + ".jpg", image)
# cv2.imwrite("TEST.jpg", image)