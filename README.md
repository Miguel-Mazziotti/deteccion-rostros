# deteccion-rosrtros
-Este programa utiliza Python y OpenCV para capturar imágenes desde la cámara y detectar rostros en tiempo real utilizando el clasificador Haar Cascade. Los rostros detectados se muestran con un rectángulo en la imagen capturada.

# Requisitos
Antes de ejecutar el programa, instala los siguientes requisitos:
-pip install opencv-python matplotlib keyboard
-El archivo Haar Cascade (haarcascade_frontalface_default.xml) es necesario para la detección de rostros. Descargalo desde (https://github.com/opencv/opencv/tree/master/data/haarcascades) y guardalo en la misma carpeta que el script o en una ubicacion accesible.

# Como ejecutar el programa
1-Clona el repositorio git clone https://github.com/Miguel-Mazziotti/deteccion-rostros
cd deteccion-rostros

2-Ejecuta el script
-python app.py

3-La ventana mostrara la transmision en tiempo real de la camara.
Presiona la tecla "q" para cerrar el programa

# Descripcion del programa
Carga del Clasificador Haar Cascade: Se utiliza el archivo haarcascade_frontalface_default.xml para identificar rostros en las imagenes.

Captura de la camara: Se usa cv2.VideoCapture para acceder a la camara del dispositivo.

Procesamiento de imagenes:
La imagen capturada se convierte a escala de grises para optimizar la deteccion.
Se detectan los rostros con detectMultiScale y se dibujan rectangulos para marcarlos.

Mostrar la imagen: La imagen se muestra en tiempo real, permitiendo al usuario interactuar.
