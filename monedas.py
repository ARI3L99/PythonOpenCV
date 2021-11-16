import cv2
import numpy as np
from numpy.typing import _8Bit


Gauss = 3
valor_kernel= 3
original = cv2.imread('monedas.jpg')
gris = cv2.cvtColor(original,cv2.COLOR_BGR2GRAY)
gauss = cv2.GaussianBlur(gris, (Gauss,Gauss),0)
canny = cv2.Canny(gauss,60,100)
kernel = np.ones((valor_kernel,valor_kernel), np.uint8)
closing = cv2.morphologyEx(canny, cv2.MORPH_CLOSE, kernel)
contornos,gerarquias = cv2.findContours(closing.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
print("Monedas encontradas: {}".format(len(contornos)))
cv2.drawContours(original,contornos,-1,(255,0,0),2)
#Mostrar
'''cv2.imshow("Gauss",gauss)
cv2.imshow("Gris",gris)
cv2.imshow("Canny",canny)
cv2.imshow("Closing",closing)'''
cv2.imshow("Original", original)
cv2.waitKey(0)