import cv2
import mediapipe as mp
import numpy as np
import time

mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(refine_landmarks=True)

cap = cv2.VideoCapture(0)

turn_count = 0
last_turn_time = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    h, w, _ = frame.shape
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(rgb)

    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:
            # Nose tip landmark (index 1)
            nose = face_landmarks.landmark[1]
            x = int(nose.x * w)
            y = int(nose.y * h)

            # Face center reference (eyes)
            left_eye = face_landmarks.landmark[33]
            right_eye = face_landmarks.landmark[263]

            lx = int(left_eye.x * w)
            rx = int(right_eye.x * w)

            center = (lx + rx) // 2

            direction = "Forward"

            if x < center - 15:
                direction = "Looking right"
            elif x > center + 15:
                direction = "Looking left"

            cv2.putText(frame, direction, (50, 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)

            # Cheating logic
            if direction != "Forward":
                if time.time() - last_turn_time > 1:
                    turn_count += 1
                    last_turn_time = time.time()

            if turn_count >= 5:
                cv2.putText(frame, "CHEATING: HEAD TURNS",
                            (50, 100), cv2.FONT_HERSHEY_SIMPLEX,
                            1, (0,0,255), 3)

    cv2.imshow("Head Pose Monitor", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
