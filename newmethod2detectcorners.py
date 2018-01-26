import cv2
import numpy as np 

img = cv2.imread("./img/babycalamardo.jpg")
# img = cv2.imread("./img/img.jpg")
gris = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#goodFeaturesToTrack
corners = cv2.goodFeaturesToTrack(gris,140,0.01,10)
corners = np.int0(corners)

for i in corners:
    x,y= i.ravel()
    cv2.circle(img,(x,y),3,(0,255,0),-1)


cv2.imshow("gris", gris)
cv2.imshow("esquinas",img)

cv2.waitKey(0)
cv2.destroyAllWindows()
