import cv2
# Leer la imagen
img = cv2.imread("C:\GitHub\Vision_Artificial\Tutoriales\pardatio.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Guardar imagen
# cv2.imwrite("pardaBW.png",img)
# Mostrar imagen
cv2.imshow("Prueba de imagen",gray)
cv2.waitKey(1000)
cv2.destroyAllWindows()
