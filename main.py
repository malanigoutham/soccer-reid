from ultralytics import YOLO
import cv2

# Load model
model = YOLO("models/yolov11_soccer.pt")

# Load video
cap = cv2.VideoCapture("videos/15sec_input_720p.mp4")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Detect players
    results = model(frame)

    # Visualize detections
    annotated_frame = results[0].plot()

    cv2.imshow("Detections", annotated_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
from deep_sort_realtime.deepsort_tracker import DeepSort

# Initialize tracker
tracker = DeepSort(max_age=30)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame)
    detections = []
    for box in results[0].boxes.xywh.cpu().numpy():
        x, y, w, h = box
        # Confidence threshold can be added here
        detections.append(([x, y, w, h], 0.99, 'player'))  

    tracks = tracker.update_tracks(detections, frame=frame)

    # Draw
    for track in tracks:
        if not track.is_confirmed():
            continue
        track_id = track.track_id
        ltrb = track.to_ltrb()
        x1, y1, x2, y2 = map(int, ltrb)
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0,255,0), 2)
        cv2.putText(frame, f"ID {track_id}", (x1, y1-10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,255,0), 2)

    cv2.imshow("Tracking", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('output.mp4', fourcc, 30.0, (width, height))

# Inside your loop:
out.write(frame)

# After loop:
out.release()

