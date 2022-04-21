import os

import cv2
import numpy as np
from cv2.cv2 import namedWindow

img = cv2.imread(r'C:\Users\Administrator\Desktop\data3\512x512\0000088.jpg')
filename = open(r'C:\Users\Administrator\Desktop\data3\512x512\0000088.txt','w')
a =[]
b = []
def on_EVENT_LBUTTONDOWN(event, x, y,flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        xy = "%d,%d" % (x, y)
        a.append(x)
        b.append(y)
        cv2.circle(img, (x, y), 1, (255, 0, 0), thickness=-1)
        cv2.putText(img, xy, (x, y), cv2.FONT_HERSHEY_PLAIN,
                    1.0, (0, 0, 0), thickness=1)

        cv2.imshow("image", img)
        # print(str(x)+","+str(y))




cv2.namedWindow("image",0)
cv2.resizeWindow("image", 1800, 1080);
cv2.setMouseCallback("image", on_EVENT_LBUTTONDOWN)
cv2.imshow("image", img)
cv2.waitKey(0)


for i,k in zip(a,b):
    print(i,k)
    filename.write(str(i) + "," + str(k)+"\n")
# img[b[0]:b[1],a[0]:a[1],:] = 0   #注意是 行，列（y轴的，X轴）
# cv2.imshow("image", img)
# cv2.waitKey(0)
# print (a,b)
filename.close()
