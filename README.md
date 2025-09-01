# Automatic Number Plate Recognition with YOLO

![ANPR Demo](https://raw.githubusercontent.com/ldotmithu/Automatic-number-plate-recognition-with-Yolo/main/assets/demo.gif)


Automatic Number Plate Recognition (ANPR) system built with YOLOv11 for object detection and EasyOCR for text extraction. This project can detect and recognize vehicle license plates from images in real-time.


[🎥 Demo Video (Google Drive)](https://drive.google.com/file/d/1hph2oxjHLozs1JbmNoN6VVPS2DJeKiLf/view)


## 🎯 Features

- **Real-time Detection**: Detects license plates in images using YOLOv11
- **Text Extraction**: Extracts plate numbers using EasyOCR
- **Web Interface**: Streamlit-based frontend for easy interaction
- **API Service**: FastAPI backend for processing requests
- **High Accuracy**: Trained on specialized license plate dataset

## 📁 Project Structure

```
├── backend/
│   ├── main.py              # FastAPI server implementation
│   ├── requirements.txt     # Backend dependencies
│   └── weights/
│       └── best.pt          # Pre-trained YOLO model weights
├── frontend/
│   ├── app.py               # Streamlit web application
│   └── requirements.txt     # Frontend dependencies
├── notebook/
│   └── Automatic_number_plate_recognition_with_Yolo.ipynb  # Training notebook
├── assets/                  # Demo images and gifs
├── .gitignore
└── README.md
```

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/ldotmithu/Automatic-number-plate-recognition-with-Yolo.git
   cd Automatic-number-plate-recognition-with-Yolo
   ```

2. **Install backend dependencies:**
   ```bash
   cd backend
   pip install -r requirements.txt
   cd ..
   ```

3. **Install frontend dependencies:**
   ```bash
   cd frontend
   pip install -r requirements.txt
   cd ..
   ```

### Running the Application

1. **Start the backend server:**
   ```bash
   cd backend
   uvicorn main:app --reload
   ```
   The backend API will be available at `http://127.0.0.1:8000`

2. **Start the frontend application:**
   ```bash
   cd frontend
   streamlit run app.py
   ```
   The web interface will be available at `http://localhost:8501`

3. **Use the application:**
   - Open the frontend in your browser
   - Upload an image containing a vehicle
   - Click "Detect Plate" to process the image
   - View the detected plates and extracted numbers

## 🛠️ API Endpoints

### Health Check
```
GET /health
```
Returns the status of the API service.

### Predict Plate
```
POST /predict
```
Processes an image and returns detected plates with bounding boxes.


## 🧠 How It Works

1. **Object Detection**: YOLOv8 model detects license plates in the input image
2. **Text Extraction**: EasyOCR extracts text from the detected plate regions
3. **Result Processing**: The system annotates the image with bounding boxes and plate numbers
4. **Response**: Returns both the annotated image and extracted plate numbers

## 📊 Model Training

The model was trained using the Roboflow dataset with the following specifications:
- Dataset: [ANPR2 (8th version)](https://universe.roboflow.com/arvind-kumar-wjygd/anpr2-syxl7/dataset/8#)
- Model: YOLOv11
- Epochs: 60
- Image Size: 640x640
- Training Result
- ![image](https://github.com/ldotmithu/Dataset/blob/main/Screenshot%202025-09-01%20153357.png)
- Val Result
- ![image](https://github.com/ldotmithu/Dataset/blob/main/Screenshot%202025-09-01%20152919.png)

Training details can be found in the [notebook](notebook/Automatic_number_plate_recognition_with_Yolo.ipynb).

## 📦 Dependencies

### Backend
- FastAPI - Web framework
- YOLOv8 (Ultralytics) - Object detection
- EasyOCR - Text recognition
- OpenCV - Image processing
- Pillow - Image handling
- NumPy - Numerical computations

### Frontend
- Streamlit - Web interface
- Requests - API communication
- Pillow - Image handling

## 📸 Example Results
```
![image](https://github.com/ldotmithu/Dataset/blob/main/Screenshot%202025-08-27%20141952.png)
```




## 🙏 Acknowledgements

- [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics) for object detection
- [EasyOCR](https://github.com/JaidedAI/EasyOCR) for text recognition
- [Roboflow](https://universe.roboflow.com) for the dataset
- [FastAPI](https://fastapi.tiangolo.com/) for the backend framework
- [Streamlit](https://streamlit.io/) for the frontend framework

## Contact 📧
- **Author:** L. Mithurshan  
- **Project:** Automatic Number Plate Recognition with YOLO  
- **LinkedIn:** [Connect with me](https://www.linkedin.com/in/mithurshan6)  
- **Email:** [ldotmithurshan222@gmail.com](mailto:ldotmithurshan222@gmail.com)  
- For questions or issues, please open an issue on GitHub or reach out via email.

