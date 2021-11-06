import cv2
imagen=cv2.imread('bailarina con dorado2.jpg')


scale_percent = 16 # percent of original size
width = int(imagen.shape[1] * scale_percent / 100)
height = int(imagen.shape[0] * scale_percent / 100)
dim = (width, height)
resized = cv2.resize(imagen, dim, interpolation = cv2.INTER_AREA)
grises =cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
_,umbral = cv2.threshold(grises,20,255,cv2.THRESH_BINARY) 
contorno,gerarquia = cv2.findContours(umbral,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(resized,contorno,-1,(0,255,255),1)
#Mostrar
cv2.imshow('imagen original',resized)

cv2.waitKey(0)
cv2.destroyAllWindows()