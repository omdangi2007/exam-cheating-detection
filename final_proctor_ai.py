import cv2
import mediapipe as mp
import time
from ultralytics import YOLO

# ---------------- LOAD MODELS ----------------
yolo = YOLO("yolov8m.pt")

mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(refine_landmarks=True)

# ------------- VIDEO SOURCE ------------------
#cap = cv2.VideoCapture(0)   # Webcam

# For video:
cap = cv2.VideoCapture("demo1.mp4")

# Reduce resolution for speed
cap.set(3, 640)
cap.set(4, 480)

# ------------- VARIABLES ---------------------
turn_count = 0
last_turn_time = 0
phone_timer = {}

frame_skip = 2
frame_count = 0

# ------------- MAIN LOOP ---------------------
while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame_count += 1
    if frame_count % frame_skip != 0:
        continue

    h, w, _ = frame.shape

    # -------- YOLO DETECTION --------
    results = yolo(frame)[0]
    persons, phones = [], []

    for box in results.boxes:
        cls = int(box.cls[0])
        x1, y1, x2, y2 = map(int, box.xyxy[0])

        if cls == 0:  # PERSON
            persons.append((x1, y1, x2, y2))
            cv2.rectangle(frame, (x1,y1), (x2,y2), (255,0,0), 2)
            cv2.putText(frame, "Person", (x1,y1-5),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,0,0), 2)

        if cls == 67:  # PHONE
            phones.append((x1, y1, x2, y2))
            cv2.rectangle(frame, (x1,y1), (x2,y2), (0,255,0), 2)
            cv2.putText(frame, "Phone", (x1,y1-5),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 2)

    # -------- HEAD POSE --------
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    face_results = face_mesh.process(rgb)

    head_alert = False

    if face_results.multi_face_landmarks:
        for face_landmarks in face_results.multi_face_landmarks:
            nose = face_landmarks.landmark[1]
            left_eye = face_landmarks.landmark[33]
            right_eye = face_landmarks.landmark[263]

            nx = int(nose.x * w)
            lx = int(left_eye.x * w)
            rx = int(right_eye.x * w)

            center = (lx + rx) // 2

            direction = "Forward"
            if nx < center - 15:
                direction = "Right"
            elif nx > center + 15:
                direction = "Left"

            cv2.putText(frame, direction, (50, 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)

            if direction != "Forward":
                if time.time() - last_turn_time > 1:
                    turn_count += 1
                    last_turn_time = time.time()

            if turn_count >= 5:
                head_alert = True

    # -------- PHONE CHEATING LOGIC --------
    phone_alert = False
    for i, p in enumerate(persons):
        px1, py1, px2, py2 = p
        for ph in phones:
            hx1, hy1, hx2, hy2 = ph
            if hx1 < px2 and hx2 > px1 and hy1 < py2 and hy2 > py1:
                if i not in phone_timer:
                    phone_timer[i] = time.time()
                if time.time() - phone_timer[i] > 2:
                    phone_alert = True
            else:
                phone_timer[i] = time.time()

    # -------- FINAL ALERT (Centered Top) --------
    if phone_alert or head_alert:
        cv2.putText(frame, "CHEATING DETECTED",
                    (w//4, 40), cv2.FONT_HERSHEY_SIMPLEX,
                    1, (0,0,255), 3)

    cv2.imshow("AI Exam Proctor", frame)

    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
