import cv2
# Leer la imagen
img = cv2.imread("pardatio.png",0)
# Guardar imagen
cv2.imwrite("pardaBW.png",img)
# Mostrar imagen
cv2.imshow("Prueba de imagen",img)
cv2.waitKey(1000)
cv2.destroyAllWindows()