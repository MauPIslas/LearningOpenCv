import cv2
import numpy as np 

img = cv2.imread("./img/img.jpg")
gris = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gris = np.float32(gris)

imgHarris = cv2.cornerHarris(gris,2,3,0.04)
height, width = imgHarris.shape

for y in range(0,height):
    for x in range(0,width):
        if imgHarris.item(y,x) > 0.01 * imgHarris.max():
            cv2.circle(img,(x,y),3,(0,255,0),cv2.FILLED,cv2.LINE_AA)

cv2.imshow("resultado harris", imgHarris)
cv2.imshow("esquinas",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# while True:
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
