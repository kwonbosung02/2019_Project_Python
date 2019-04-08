import cv2

from matplotlib import pyplot as plt
import numpy as np

img =cv2.imread("../img/road1.jpg", cv2.IMREAD_COLOR)
src = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

edges = cv2.Canny(img,150,620)


cv2.imshow("Grey",src)

cv2.imshow("Canny",edges)

cv2.waitKey(0)
cv2.destroyAllWindows()