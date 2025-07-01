from ultralytics import YOLO
import cv2
import sys

def test_yolo_video():
    model = YOLO("yolov8n.pt")

    cap = cv2.VideoCapture("test_video.mp4")
    if not cap.isOpened():
        print("❌ test_video.mp4 introuvable ou ne peut pas être ouvert.")
        sys.exit(1)

    ret, frame = cap.read()
    if not ret:
        print("❌ Impossible de lire la première frame de la vidéo.")
        sys.exit(1)

    results = model(frame)
    if results[0].boxes is None or len(results[0].boxes) == 0:
        print("❌ Aucune détection dans la première frame.")
        sys.exit(1)

    print("✅ Test YOLO sur vidéo OK")
    cap.release()

if __name__ == "__main__":
    test_yolo_video()
