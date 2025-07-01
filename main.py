from ultralytics import YOLO
import cv2

def run_detection():
    # Charger le modèle YOLOv8 (modèle léger)
    model = YOLO("yolov8n.pt")

    # Charger l’image de test
    image_path = "test_image.png"
    image = cv2.imread(image_path)

    if image is None:
        raise FileNotFoundError(f"❌ Image non trouvée à l'emplacement : {image_path}")

    # Exécuter la détection
    results = model(image)

    # Annoter l’image avec les détections
    annotated = results[0].plot()

    # Sauvegarder le résultat
    output_path = "result.jpg"
    cv2.imwrite(output_path, annotated)
    print(f"✅ Détection terminée. Image enregistrée sous : {output_path}")

if __name__ == "__main__":
    run_detection()
