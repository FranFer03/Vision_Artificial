import cv2
import numpy as np

# Leer la imagen
img = cv2.imread("C:\GitHub\Vision_Artificial\Tutoriales\pardatio.png")

# Convertir a escala de grises
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Aplicar umbralización
thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)[1]

# Encontrar contornos
contours, _ = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

# Crear una imagen de lienzo vacía del mismo tamaño que la imagen original
canvas = np.zeros_like(img)

# Dibujar contornos en el lienzo
cv2.drawContours(canvas, contours, -1, (0, 255, 0), 2)

# Convertir thresh a color para que todas las imágenes tengan 3 canales
thresh_color = cv2.cvtColor(thresh, cv2.COLOR_GRAY2BGR)

# Alinear las imágenes verticalmente
combined_img_top = np.concatenate((cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR), thresh_color), axis=1)
combined_img_bottom = np.concatenate((canvas, np.zeros_like(canvas)), axis=1)
combined_img = np.concatenate((combined_img_top, combined_img_bottom), axis=0)

# Redimensionar la imagen combinada
scale_percent = 50  # Porcentaje de escala deseado
width = int(combined_img.shape[1] * scale_percent / 100)
height = int(combined_img.shape[0] * scale_percent / 100)
dim = (width, height)

resized_combined_img = cv2.resize(combined_img, dim, interpolation=cv2.INTER_AREA)

# Mostrar la imagen redimensionada
cv2.imshow("Gray | Thresh | Contours", resized_combined_img)

# Esperar a que se presione una tecla y luego cerrar todas las ventanas
cv2.waitKey(0)
cv2.destroyAllWindows()




