import cv2
import numpy as np

img = cv2.imread("1.png")
img =cv2.resize(img,dsize=(500,500))
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
Darkest = np.min(gray)
ret, thresh = cv2.threshold(gray,Darkest,255,cv2.THRESH_BINARY)

edges = cv2.Canny(thresh, 50, 250)
# cv2.imshow('edges', edges)
cv2.imshow('thresh_before', thresh)

lines = cv2.HoughLines(edges, 1, np.pi / 180, 100)
# print(lines)
if lines is not None and lines.any():
    for line in lines:
        rho,theta = line[0]
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a * rho
        y0 = b * rho
        # x1 stores the rounded off value of (r * cos(theta) - 1000 * sin(theta))
        x1 = int(x0 + 1000 * (-b))
        # y1 stores the rounded off value of (r * sin(theta)+ 1000 * cos(theta))
        y1 = int(y0 + 1000 * (a))
        # x2 stores the rounded off value of (r * cos(theta)+ 1000 * sin(theta))
        x2 = int(x0 - 1000 * (-b))
        # y2 stores the rounded off value of (r * sin(theta)- 1000 * cos(theta))
        y2 = int(y0 - 1000 * (a))
        # print(line)
        cv2.line(thresh, (x1, y1), (x2, y2), (0, 0, 255), 2)
# print(gray[0])
inv = 255- thresh
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for cnt in contours:
    cv2.drawContours(img,cnt,-1,(0,255,0),1)

ret, thresh2 = cv2.threshold(gray,Darkest,255,cv2.THRESH_BINARY)

new = thresh2- thresh
cv2.imshow('Original Image', img)
cv2.imshow('GRAY', gray)
cv2.imshow('thresh', thresh)
cv2.imshow('inv', inv)
cv2.imshow('sub', new)


cv2.imwrite("cont.png",img)
cv2.imwrite('thresh.png', thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()
