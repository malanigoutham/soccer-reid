1.# Soccer Player Re-Identification

This project implements soccer player and ball detection using YOLO and player tracking using DeepSORT.

---

## 🚀 How to Set Up and Run the Code

1. **Clone this repository:**

   ```bash
   git clone https://github.com/YOUR_USERNAME/soccer-reid.git
   cd soccer-reid

2.Create and activate a virtual environment:
python -m venv venv
# On Windows:
venv\Scripts\activate


3.Install dependencies:
pip install -r requirements.txt

4.Download the YOLO model weights:
The YOLOv11 weights (yolov11_soccer.pt) are too large for GitHub.
Please download them manually from the provided link and place them in the models/ folder.

5.⚙️ Dependencies / Environment Requirements
Python >=3.8
PyTorch
Ultralytics YOLO
OpenCV
deep_sort_realtime
To install all dependencies:
pip install -r requirements.txt

6.project structure:
soccer-reid/
├── models/
│   └── yolov11_soccer.pt
├── videos/
│   └── 15sec_input_720p.mp4
├── main.py
├── requirements.txt
├── README.md





