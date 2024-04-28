import cv2
import numpy as np

img = cv2.imread("12.png")
img =cv2.resize(img,dsize=(500,500))
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

k_size = 7
img_median_blurr = cv2.medianBlur(img,k_size)
for _ in range(100000):
    img_median_blurr = cv2.medianBlur(img_median_blurr,k_size)
    cv2.imshow("img",img_median_blurr)
    cv2.waitKey(4)
Darkest = np.min(gray)
ret, thresh = cv2.threshold(gray,Darkest,255,cv2.THRESH_BINARY)

cv2.imshow("img",img_median_blurr)
cv2.waitKey(0)
cv2.destroyAllWindows()
