import cv2
import numpy as np 
#0 indica a la cámara a controlar
cap = cv2.VideoCapture(0)
cap.isOpened()

while True:
    ret, frame = cap.read()
    
    # print (ret)
    #'video' es nombre de la ventana y frame trae la imagen captudara
    cv2.imshow('video',frame)
    #condicion para salir de la captura
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
#release hace que la captura sea continua
cap.release()
cv2.destroyAllWindows()