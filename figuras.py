import cv2
import numpy as np

fondo = np.zeros((502,502,3),np.uint8)
punto_1= (100,200)
punto_2= (250,200)
color=(255,0,255)
grosor= 10
linea = cv2.line(fondo,punto_1,punto_2,color,grosor)

# cuadrado
punto_c1= (350,450)
punto_c2=(300,400)
color= (0,255,255)
grosor=5
cuadrado= cv2.rectangle(fondo,punto_c1,punto_c2,color,grosor)

#circulo
punto_ref= (350,200)
radio=  20
color= (255,255,0)
grosor=5
cuadrado= cv2.circle(fondo,punto_ref,radio,color,grosor)

cv2.imshow("figuras",fondo)
cv2.waitKey(0)
cv2.destroyAllWindows()
