import numpy as np
import cv2


path  = '/home/debasish/NLP/Python-NLPClass/opencv/images/72.png'

# Load an color image in grayscale
imgC = cv2.imread(path, flags=cv2.IMREAD_GRAYSCALE)
print(imgC.shape)
imgG = cv2.imread(path,0)
print(imgG.shape)

# Displaying the image
cv2.imshow('Color image', imgC)
cv2.imshow('Gray image', imgG)

cv2.imwrite('Gray.png',imgG)

cv2.waitKey(0)
cv2.destroyAllWindows()

