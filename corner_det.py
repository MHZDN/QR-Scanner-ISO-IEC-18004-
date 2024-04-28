import cv2
import numpy as np

img = cv2.imread("12.png")
img =cv2.resize(img,dsize=(500,500))
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
Darkest = np.min(gray)
ret, thresh = cv2.threshold(gray,Darkest,255,cv2.THRESH_BINARY)

corners = cv2.goodFeaturesToTrack(gray, 100 , 0.01 , 10 )
corners = np.int0(corners)

for corner in corners:
    x,y =corner.ravel()
    cv2.circle(img,(x,y),5,(255,0,0),-1)

cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()