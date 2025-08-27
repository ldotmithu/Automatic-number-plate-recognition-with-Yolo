from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from ultralytics import YOLO
import numpy as np
import cv2
import easyocr
import base64
from PIL import Image
import io

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

model = YOLO("backend/weights/best.pt")
reader = easyocr.Reader(['en'], gpu=False)

def image_to_base64(img):
    _, buf = cv2.imencode(".png", img)
    return base64.b64encode(buf).decode("utf-8")

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    img_bytes = await file.read()
    pil_img = Image.open(io.BytesIO(img_bytes)).convert("RGB")
    img = np.array(pil_img)
    img_bgr = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

    results = model(img)
    annotated = img_bgr.copy()
    plates = []

    for box in results[0].boxes:
        x1, y1, x2, y2 = map(int, box.xyxy[0])
        crop = annotated[y1:y2, x1:x2]
        text = ""
        if crop.size > 0:
            ocr = reader.readtext(crop)
            if ocr:
                text = ocr[0][1]

        cv2.rectangle(annotated, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(annotated, text, (x1, y1 - 5),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

        plates.append(text)

    return {
        "plates": plates,
        "image": image_to_base64(annotated)
    }

@app.get("/health")
def health():
    return {"status": "ok"}
