import cv2
import numpy as np
import skimage
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'
# Leer la imagen
img = cv2.imread("bochido.jpg")

# Convertir a escala de grises
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Aplicar umbralización
thresh = cv2.threshold(gray, 130, 255, cv2.THRESH_BINARY_INV)[1]
# Encontrar contornos
contours, _ = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
# Definir parámetros para la detección de candidatos
license_ratio = 3.2
min_w = 150
max_w = min_w + 150
min_h = 50
max_h = min_h + 50
candidates = []

# Iterar sobre los contornos
for cnt in contours:
    x, y, w, h = cv2.boundingRect(cnt)
    aspect_ratio = float(w) / h
    
    # Condiciones para seleccionar candidatos
    if (np.isclose(aspect_ratio, license_ratio, atol=0.7) and
        (max_w > w > min_w) and
        (max_h > h > min_h)):
        candidates.append(cnt)

license = candidates[0]

# Crear un lienzo vacío del mismo tamaño que la imagen original
canvas = np.zeros_like(img)

# Dibujar contornos candidatos en el lienzo
cv2.drawContours(canvas, candidates, -1, (0, 200, 0), 1)

# Mostrar la imagen del lienzo con los contornos candidatos
# cv2.imshow("License Plate Candidates", canvas)

x,y,w,h = cv2.boundingRect(license)
cropped = img[y:y+h,x:x+w]
cv2.imshow("License2",cropped)

import skimage.io
import skimage.color
import skimage.segmentation
import matplotlib.pyplot as plt

# Cargar la imagen
imagen = cropped

# Convertir la imagen a escala de grises si es necesario
gris = skimage.color.rgb2gray(imagen) if len(imagen.shape) == 3 else imagen

# Aplicar umbralización si es necesario
umbralizada = gris > skimage.filters.threshold_otsu(gris)

# Invertir los colores
imagen_invertida = ~umbralizada  # Usamos la operación de complemento (~) para invertir los valores

# Mostrar la imagen original, la imagen binarizada y la imagen invertida
fig, axes = plt.subplots(1, 3, figsize=(15, 5))
axes[0].imshow(imagen, cmap='gray')
axes[0].set_title('Imagen Original')
axes[0].axis('off')

axes[1].imshow(umbralizada, cmap='gray')
axes[1].set_title('Imagen Binarizada')
axes[1].axis('off')

axes[2].imshow(imagen_invertida, cmap='gray')
axes[2].set_title('Imagen Invertida')
axes[2].axis('off')

plt.tight_layout()
plt.show()

gray_cropped = cv2.cvtColor(cropped,cv2.COLOR_BGR2GRAY)
thresh_cropped = cv2.adaptiveThreshold(gray_cropped, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 7, 13)
cv2.imshow("License",thresh_cropped)

borderless = skimage.segmentation.clear_border(thresh_cropped,buffer_size=0,bgval=0)
cv2.imshow("License2",borderless)

# final = cv2.bitwise_not(sin_borde)
# cv2.imshow("License Binary",final)

psm = 7
alphanumeric = "JLG520"
options = "-c tessedit_char_whitelist={}".format(alphanumeric)
options += " --psm {}".format(psm)
txt = pytesseract.image_to_string(imagen_invertida, config=options)
print(txt)


# # Esperar a que se presione una tecla y luego cerrar todas las ventanas
cv2.waitKey(0)
cv2.destroyAllWindows()

