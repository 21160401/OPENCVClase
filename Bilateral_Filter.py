#FILTRO BILATERAL PARA SUAVIZAR UNA IMAGEN MANTENIENDO EL BORDE INTACTO

import cv2 #Es la librería OpenCV, utilizada para procesar imágenes.
import numpy as np # Se usa en muchas operaciones relacionadas con matrices y datos numéricos, aunque aquí no lo usamos directamente.
import matplotlib.pyplot as plt  # Importar matplotlib para visualización

# Leer la imagen original
ruta_imagen = "cat_1.jpg"
imagen_Original = cv2.imread(ruta_imagen)# Contiene el nombre (y la ruta) de la imagen que quieres cargar.
imagen_MedianBlur = imagen_Original.copy() #Lee la imagen desde el disco y la carga en memoria como una matriz en formato BGR (azul, verde, rojo).

#Copiar la Imagen para Diferentes Técnicas de Desenfoque
imagen_GaussianBlur = imagen_Original.copy()
imagen_BilateralBlur = imagen_Original.copy()

# Aplicar diferentes técnicas de desenfoque
imagen_MedianBlur = cv2.medianBlur(imagen_MedianBlur, 9)
imagen_GaussianBlur = cv2.GaussianBlur(imagen_GaussianBlur, (9, 9), 10)
imagen_BilateralBlur = cv2.bilateralFilter(imagen_BilateralBlur, 9, 100, 75)

# Convertir las imágenes a RGB (OpenCV usa BGR por defecto)
imagen_Original = cv2.cvtColor(imagen_Original, cv2.COLOR_BGR2RGB)
imagen_MedianBlur = cv2.cvtColor(imagen_MedianBlur, cv2.COLOR_BGR2RGB)
imagen_GaussianBlur = cv2.cvtColor(imagen_GaussianBlur, cv2.COLOR_BGR2RGB)
imagen_BilateralBlur = cv2.cvtColor(imagen_BilateralBlur, cv2.COLOR_BGR2RGB)

# Crear una figura y mostrar las imágenes en subplots
plt.figure(figsize=(10, 8))

plt.subplot(2, 2, 1)
plt.imshow(imagen_Original)
plt.title("Imagen Original")
plt.axis("off")

plt.subplot(2, 2, 2)
plt.imshow(imagen_MedianBlur)
plt.title("Desenfoque Mediano")
plt.axis("off")

plt.subplot(2, 2, 3)
plt.imshow(imagen_GaussianBlur)
plt.title("Desenfoque Gaussiano")
plt.axis("off")

plt.subplot(2, 2, 4)
plt.imshow(imagen_BilateralBlur)
plt.title("Desenfoque Bilateral")
plt.axis("off")

plt.tight_layout()
plt.show()