import cv2
from ultralytics import YOLO
import time

model = YOLO("yolov8m.pt")

cap = cv2.VideoCapture(0)
phone_timer = {}

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame)[0]

    persons = []
    phones = []

    for box in results.boxes:
        cls = int(box.cls[0])
        x1, y1, x2, y2 = map(int, box.xyxy[0])

        if cls == 0:  # person
            persons.append((x1, y1, x2, y2))
        if cls == 67:  # cell phone
            phones.append((x1, y1, x2, y2))

    # Check cheating
    for i, p in enumerate(persons):
        px1, py1, px2, py2 = p

        for ph in phones:
            hx1, hy1, hx2, hy2 = ph

            if hx1 < px2 and hx2 > px1 and hy1 < py2 and hy2 > py1:
                if i not in phone_timer:
                    phone_timer[i] = time.time()

                if time.time() - phone_timer[i] > 2:
                    cv2.putText(frame, "CHEATING: PHONE DETECTED",
                                (px1, py1-10), cv2.FONT_HERSHEY_SIMPLEX,
                                0.7, (0,0,255), 2)
            else:
                phone_timer[i] = time.time()

    cv2.imshow("Exam Monitoring", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
