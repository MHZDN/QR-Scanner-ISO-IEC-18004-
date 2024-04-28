import cv2
import numpy as np
import matplotlib.pyplot as plt


def find_intersection(line1, line2):
  """
  This function finds the intersection point of two lines represented by (rho, theta) format.

  Args:
      line1: A list containing (rho, theta) for the first line.
      line2: A list containing (rho, theta) for the second line.

  Returns:
      A tuple containing the x and y coordinates of the intersection point, 
      or None if the lines are parallel.
  """
  rho1, theta1 = line1[0]
  rho2, theta2 = line2[0]

  # Check for parallel lines (avoid division by zero)
  if np.abs(np.sin(theta1 - theta2)) < 1e-6:
    return None

  a1, b1 = np.cos(theta1), np.sin(theta1)
  a2, b2 = np.cos(theta2), np.sin(theta2)

  # Calculate the intersection point coordinates
  x = int((rho2 * b1 - rho1 * b2) / (a2 * b1 - a1 * b2))
  y = int((rho1 * a2 - rho2 * a1) / (a2 * b1 - a1 * b2))

  return (x, y)


def visualize_intersections(image, lines):
  """
  This function iterates through pairs of lines, finds their intersection, 
  and draws a red circle at the intersection point on the image.

  Args:
      image: The image where lines were detected.
      lines: A list of lines, where each line is a list containing (rho, theta).
  """
  intersections=[]
  for i in range(len(lines)):
    for j in range(i + 1, len(lines)):
      intersection = find_intersection(lines[i], lines[j])
      if intersection:
        
        x, y = intersection
        intersections.append([x,y])
        cv2.circle(image, (x, y), 2, (0, 0, 255), -1)

  return intersections
# ------------------------------------------------------------------------------
img = cv2.imread("7.png")
img =cv2.resize(img,dsize=(500,500))
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

hist = cv2.calcHist([gray], [0], None, [256], [0, 256])

plt.figure()
plt.plot(hist)
plt.xlabel("Pixel Intensity")
plt.ylabel("Number of Pixels")
plt.title("Histogram of Grayscale Image")
plt.show()

min_val, max_val, _, _ = cv2.minMaxLoc(gray)
gray = cv2.convertScaleAbs(gray, alpha=255 / (max_val - min_val), beta=-min_val * 255 / (max_val - min_val))

Darkest = np.min(gray)
ret, thresh = cv2.threshold(gray,Darkest,255,cv2.THRESH_BINARY)
# thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
#                                  cv2.THRESH_BINARY, 49, 2)

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


visualize_intersections(img,lines)

inv = 255- thresh
# contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# for cnt in contours:
#     cv2.drawContours(img,cnt,-1,(0,255,0),1)

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
