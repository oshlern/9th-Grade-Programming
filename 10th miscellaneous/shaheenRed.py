import cv2
import numpy as np
img = cv2.imread("/Users/oshlern/Downloads/shaheen.jpg")
img[:,:,2] = np.average(img, axis=2)
print img[:,:,0].shape
shp = img[:,:,1].shape
img[:,:,1] = np.zeros(shp)
img[:,:,0] = np.zeros(shp)

cv2.imshow("red", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite("RED", img)