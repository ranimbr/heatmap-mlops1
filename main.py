# main.py
from ultralytics import YOLO
import cv2

def generate_heatmap(video_path, output_path="static/result.mp4"):
    model = YOLO("yolov8n.pt")
    cap = cv2.VideoCapture(video_path)

    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)

    out = cv2.VideoWriter(output_path, cv2.VideoWriter_fourcc(*'mp4v'), fps, (width, height))

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        results = model(frame)[0]
        for box in results.boxes.data.tolist():
            x1, y1, x2, y2, score, cls = box
            if int(cls) == 0:  # Personne
                cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)

        out.write(frame)

    cap.release()
    out.release()
    print("✅ Heatmap générée :", output_path)

if __name__ == "__main__":
    input_video = "test_video.mp4"       # adapte le nom si besoin
    output_video = "static/result.mp4"   # dossier static à créer si absent
    generate_heatmap(input_video, output_video)
