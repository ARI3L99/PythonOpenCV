import cv2 as cv
import numpy as np
captura = cv.VideoCapture(0)
if not captura.isOpened():
    print("no se encontró una camara")
    exit()
while True:
    tipo,frame=captura.read()
    gauss= 3
    valor_kernel=3
    gris = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    gauss = cv.GaussianBlur(gris, (gauss,gauss),0)
    canny = cv.Canny(gauss,60,100)
    kernel = np.ones((valor_kernel,valor_kernel), np.uint8)
    closing = cv.morphologyEx(canny, cv.MORPH_CLOSE, kernel)
    contornos,gerarquias = cv.findContours(closing.copy(),cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
    print("elementos encontrados: {}".format(len(contornos)))
    cv.drawContours(frame,contornos,-1,(255,0,0),2)
    cv.imshow("camara",frame)
    if cv.waitKey(1)==ord("q"):
        break
captura.release()
cv.destroyAllWindows()