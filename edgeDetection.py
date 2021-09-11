import cv2
import numpy as np

imagePath = "e2.jpg"

img = cv2.imread(imagePath, 0)
cv2.imwrite("edges2.jpg", cv2.Canny(img, 200, 300))
cv2.imshow("edges2", cv2.imread("edges2.jpg"))
cv2.waitKey()
cv2.destroyAllWindows()