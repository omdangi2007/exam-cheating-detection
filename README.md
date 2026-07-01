# 🎓 AI Exam Cheating Detection System

An AI-powered online exam proctoring system that detects suspicious activities in real time using **YOLOv8**, **Computer Vision**, and **Head Pose Estimation**. The system is designed to assist invigilators by automatically monitoring students during online examinations and flagging potential cheating behavior.

---

## 📌 Features

- 👤 Real-time person detection using YOLOv8
- 📱 Mobile phone detection
- 👥 Multiple person detection
- 🎥 Live webcam monitoring
- 📂 Video file processing
- 🧠 Head pose estimation for attention monitoring
- ⚠️ Suspicious activity alerts
- ⚡ Real-time inference with OpenCV

---

## 🛠️ Tech Stack

| Category | Technologies |
|----------|--------------|
| Language | Python |
| Computer Vision | OpenCV |
| Object Detection | YOLOv8 (Ultralytics) |
| Image Processing | NumPy |
| Deep Learning | PyTorch |
| Model Training | Ultralytics YOLO |
| Development | VS Code |

---

## 📂 Project Structure

```
exam-cheating-detection/
│
├── cheating_detector.py
├── final_proctor_ai.py
├── headpose_detector.py
├── export_to_yolo.py
├── load_coco_small.py
├── reopen_dataset.py
├── requirements.txt
├── README.md
│
├── data/
├── yolo_dataset/
├── runs/
│
└── assets/
```

---

## 🚀 Installation

Clone the repository

```bash
git clone https://github.com/omdangi2007/exam-cheating-detection.git
```

Navigate to the project directory

```bash
cd exam-cheating-detection
```

Create a virtual environment

### macOS / Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Project

Run the main application

```bash
python final_proctor_ai.py
```

Or run individual modules

```bash
python cheating_detector.py
```

---

## 🧠 Detection Capabilities

The system monitors various suspicious activities during an examination, including:

- Looking away from the screen
- Presence of multiple people
- Mobile phone usage
- Head orientation changes
- Absence of the candidate
- Real-time object detection

---

## 📊 Workflow

```
Camera / Video Input
          │
          ▼
 Frame Capture (OpenCV)
          │
          ▼
 YOLOv8 Object Detection
          │
          ▼
 Head Pose Estimation
          │
          ▼
 Suspicious Activity Analysis
          │
          ▼
 Alert Generation & Display
```

---

## 📸 Demo

> **Demo videos and screenshots will be added soon.**

---

## 🔮 Future Improvements

- Eye gaze tracking
- Face recognition for candidate verification
- Mouth movement detection
- Audio-based cheating detection
- Automatic incident logging
- Web dashboard for invigilators
- Cloud deployment
- Multi-camera support

---

## 📈 Applications

- Online examinations
- University remote assessments
- Certification exams
- Corporate hiring assessments
- Government recruitment examinations

---

## 🤝 Contributing

Contributions are welcome!

If you'd like to improve the project:

1. Fork the repository
2. Create a new branch
3. Commit your changes
4. Push the branch
5. Open a Pull Request

---

## 📜 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Om Vasudeo Dangi**

B.Tech Artificial Intelligence & Machine Learning  
Vishwakarma University, Pune

GitHub: https://github.com/omdangi2007

LinkedIn: *(Add your LinkedIn profile here)*

---

⭐ If you found this project helpful, consider giving it a star!
