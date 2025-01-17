import * as faceapi from './face-api.js';

// Charger les modèles de face-api.js
async function loadModels() {
    const statusElement = document.getElementById('status');
    statusElement.textContent = "Chargement des modèles...";
    try {
        await faceapi.nets.ssdMobilenetv1.loadFromUri('./models');  // Détection des visages
        await faceapi.nets.faceLandmark68Net.loadFromUri('./models');  // Repères faciaux (yeux, nez, bouche)
        await faceapi.nets.faceRecognitionNet.loadFromUri('./models');  // Reconnaissance des visages
        await faceapi.nets.faceExpressionNet.loadFromUri('./models');  // Expressions faciales (joie, colère, etc.)
        statusElement.textContent = "Modèles chargés. Vous pouvez démarrer la détection.";
    } catch (error) {
        console.error("Erreur lors du chargement des modèles :", error);
        statusElement.textContent = "Erreur : Impossible de charger les modèles.";
    }
}

async function startCamera() {
    const videoElement = document.getElementById('video');
    const statusElement = document.getElementById('status');

    try {
        // Accès à la webcam
        const stream = await navigator.mediaDevices.getUserMedia({ video: true });
        videoElement.srcObject = stream;
        statusElement.textContent = "Caméra activée. Flux vidéo en cours...";
    } catch (error) {
        console.error("Erreur lors de l'accès à la webcam :", error);
        statusElement.textContent = "Erreur : Impossible d'accéder à la webcam.";
    }
}

async function detectFaces() {
    const videoElement = document.getElementById('video')
    // const canvas = faceapi.createCanvasFromMedia(videoElement);
    document.body.append(canvas);

    const displaySize = { width: videoElement.width, height: videoElement.height };
    faceapi.matchDimensions(canvas, displaySize);

    setInterval(async () => {
        const detections = await faceapi.detectAllFaces(videoElement)
            .withFaceLandmarks()
            .withFaceExpressions()  // Ajout des expressions
            .withFaceDescriptors();  // Descripteurs pour reconnaissance

        canvas.getContext('2d').clearRect(0, 0, canvas.width, canvas.height);
        const resizedDetections = faceapi.resizeResults(detections, displaySize);

        // Dessiner les rectangles autour des visages et afficher les repères
        faceapi.draw.drawDetections(canvas, resizedDetections);
        faceapi.draw.drawFaceLandmarks(canvas, resizedDetections);
        faceapi.draw.drawFaceExpressions(canvas, resizedDetections);
    }, 200);  // Fréquence de détection en millisecondes
}

document.getElementById('startButton').addEventListener('click', async () => {
    await loadModels();  // Charger les modèles
    await startCamera(); // Activer la caméra
    detectFaces();       // Démarrer la détection faciale
});
