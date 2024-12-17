import cv2
import matplotlib.pyplot as plt
import keyboard

face_cascade = cv2.CascadeClassifier('./Deteccion/haarcascade_frontalface_default.xml')#ubicacion del archivo 
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        print("No se pudo acceder a la cámara")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale( # Es un metodo de la clase CascadeClassifier que detecta objetos (en este caso, rostros) en la imagen.
        gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30)
    )
     # La funcion devuelve una lista de rectangulos donde se detectaron rostros. Cada rectángulo esta representado como un conjunto de 4 valores:
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2) # Estos datos son utilizados despues para dibujar rectangulos en la imagen con

    # Mostrar usando matplotlib
    plt.imshow(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    plt.axis('off')
    plt.show(block=False)
    plt.pause(0.01)
    plt.clf()

    # Detectar si se presiona la tecla 'q' para cerrar el programa
    if keyboard.is_pressed('q'):
        print("Saliendo del programa...")
        break

cap.release()
plt.close()
