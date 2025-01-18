import cv2
import face_recognition
import numpy as np
import os
import paho.mqtt.client as mqtt  # Import de la bibliothèque MQTT
import json

# ========= THINGSBOARD =========
# configuration thingsboard
# THINGSBOARD_HOST = "mqtt.eu.thingsboard.cloud"
# ACCESS_KEY = "rOal9beu6CtpsjXSiN5q"
#
# client = mqtt.Client()
# client.username_pw_set("mouaad","mouaad")
# client.connect(THINGSBOARD_HOST, 1883, 60)

# ========= MQTT =========
# Configuration du broker MQTT
BROKER = "localhost"  # Remplacez par l'adresse de votre broker (localhost ou IP)
PORT = 1883 # Port du broker MQTT
TOPIC = "face-detection"  # Topic sur lequel publier
# Connexion au broker MQTT
client = mqtt.Client()
client.connect(BROKER, PORT, 60)

# Charger les visages connus et leurs étiquettes
def load_known_faces_and_labels():
    known_face_encodings = []
    known_face_labels = []

    labeled_faces_dir = "labels"  # Dossier contenant les images étiquetées
    for label in os.listdir(labeled_faces_dir):
        person_dir = os.path.join(labeled_faces_dir, label)
        if not os.path.isdir(person_dir):
            continue
        for image_name in os.listdir(person_dir):
            image_path = os.path.join(person_dir, image_name)
            image = face_recognition.load_image_file(image_path)
            try:
                encoding = face_recognition.face_encodings(image)[0]
                known_face_encodings.append(encoding)
                known_face_labels.append(label)
            except IndexError:
                print(f"Warning: Aucun visage trouvé dans {image_path}. Ignoré.")

    return known_face_encodings, known_face_labels

# Initialiser les visages connus
print("Chargement des visages connus...")
known_face_encodings, known_face_labels = load_known_faces_and_labels()
print(f"{len(known_face_labels)} visages connus chargés : {known_face_labels}")

# Initialiser la webcam
video_capture = cv2.VideoCapture(0)

print("Webcam démarrée. Appuyez sur 'q' pour quitter.")

while True:
    # Lire une image depuis la webcam
    ret, frame = video_capture.read()
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Localiser les visages et encoder leurs caractéristiques
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        # Comparer le visage avec les visages connus
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding, tolerance=0.5)
        name = "Unknown"

        if True in matches:
            first_match_index = matches.index(True)
            name = known_face_labels[first_match_index]

        # ========= configuration pour mqtt ===========
        # Publier le résultat sur MQTT
        message = {"name": name}  # Exemple de message JSON
        client.publish(TOPIC, str(message))
        print(f"Message publié : {message}")

        # ========= configuration pour thingsboard ===========
        # telemetry_data = {"detected_person":name}
        # client.publish("v1/devices/me/telemetry", json.dumps(telemetry_data))
        # print(f"Données publiées : {telemetry_data} ")


        # Dessiner un rectangle autour du visage et afficher le nom
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)

    # Afficher l'image
    cv2.imshow("Face Recognition", frame)

    # Quitter avec 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libérer la webcam et fermer les fenêtres
video_capture.release()
cv2.destroyAllWindows()
