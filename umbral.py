import cv2
import numpy as np 

gris = cv2.imread("./img/babycalamardo.jpg",cv2.IMREAD_GRAYSCALE)

t,segmentar = cv2.threshold(gris,170,255,cv2.THRESH_BINARY)
# t,segmentar = cv2.threshold(gris,170,255,cv2.THRESH_BINARY_INV)
# t,segmentar = cv2.threshold(gris,170,255,cv2.THRESH_TOZERO)
cv2.imshow("grist",gris)
cv2.imshow("segmentar",segmentar)
cv2.waitKey(0)
cv2.destroyAllWindows()