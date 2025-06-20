from ultralytics import YOLO
import cv2

def test_yolo():
    model = YOLO("yolov8n.pt")
    img = cv2.imread("test_image.jpg")
    results = model(img)
    assert results[0].boxes is not None
    print("✅ Test YOLO OK")

if __name__ == "__main__":
    test_yolo()
