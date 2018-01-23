import cv2

titulo= "Mi imagen"
path="./img/perro.jpg"

imagen= cv2.imread(path,cv2.IMREAD_COLOR)
cv2.namedWindow(titulo,cv2.WINDOW_NORMAL)
cv2.imshow(titulo,imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()