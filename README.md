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

# 📊 Project Report – Soccer Player Re-Identification

**Name:** MALANI GOUTHAM  
**Role:** AI Intern  
**Company:** Liat.ai  
**Task Option:** Soccer Player Detection and Re-Identification

---

## 🔍 Approach and Methodology

- **YOLOv8 Object Detection**:  
  Used the Ultralytics YOLO model to detect players, ball, and referees in each video frame.

- **DeepSORT Tracking**:  
  Implemented DeepSORT for tracking players across frames using bounding boxes and re-identification embeddings.

- **Video Processing**:  
  OpenCV was used to process and display each frame, draw detections, and export a video of tracked players.

---

## 🧪 Techniques Tried

- Tested YOLO with different confidence thresholds for optimal performance.
- Explored DeepSORT parameters (e.g., `max_age`, `n_init`) to improve ID consistency.
- Evaluated object detection results frame-by-frame with overlayed bounding boxes and IDs.

---

## ⚠️ Challenges Encountered

- **Large File Handling**: YOLOv11 model and `venv` files exceeded GitHub size limits.
- **Dependency Conflicts**: Resolved environment issues between OpenCV, Torch, and DeepSORT.
- **Realtime Performance**: Inference times were high on CPU, affecting smooth playback.

---

## 🔧 Incomplete / Future Work

- Would like to improve ID consistency during occlusion.
- Plan to fine-tune YOLOv8 for sports-specific re-identification.
- Could integrate a GUI to display analytics like ball possession and player stats.

---

## ✅ Status

- Project setup and tracking pipeline completed.
- GitHub repository submitted.
- README, `.gitignore`, and requirements fully documented.


