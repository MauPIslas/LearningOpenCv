import cv2
import numpy as np

######################################Events######################################
"""
EVENT_LBUTTONDOWN
EVENT_MBUTTONDOWN
EVENT_RBUTTONDOWN
EVENT_LBUTTONUP
EVENT_MBUTTONUP
EVENT_RBUTTONUP
EVENT_LBUTTONDBCLK
EVENT_MBUTTONDBCLK
EVENT_RBUTTONDBCLK
"""

fondo = np.zeros((700,1000,4),np.uint8)
pintar= False
ix,iy= 0, 0

def dibujar(events,x,y,flags,params):
    global pintar,ix,iy
    if(events == cv2.EVENT_LBUTTONDBLCLK):
        cv2.circle(fondo,(x,y),50,(2,255,0,255),10)
    elif( events == cv2.EVENT_RBUTTONDBLCLK):
        ix,iy = x,y
        cv2.rectangle(fondo(ix-40,iy+40,(x,y),(0,255,255),5))
    elif(events == cv2.EVENT_MOUSEMOVE and pintar):
        cv2.rectangle(fondo,(x,y),(x,y),(255,0,255),5)
cv2.namedWindow("Paint")
cv2.setMouseCallback("Paint", dibujar)

while(True):
    cv2.imshow("Paint",fondo)
    k= cv2.waitKey(0) & 0xFF
    if(k == ord("p")):
            pintar = not pintar
    elif(k == cv2.waitKey(0)):
            break
    elif(k == ord("s")):
            cv2.imwrite("captura.jpg",fondo)


cv.destroyAllWindows()