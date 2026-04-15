#backend/main.py
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import numpy as np
from PIL import Image
import io
import sys
import os

#Path to import model.py
sys.path.append(os.path.dirname(__file__))

#Import the model functions
from model import load_model_once, predict, class_names

#Create the FastAPI app
app = FastAPI(
    title = "Kidney CT Detection API",
    description = "Detect cysts, tumors, and stones from kidney CT scans",
    version = "1.0.0"
)

#Add CORS so streamlit can call this API
app.add_middleware(CORSMiddleware,
                   allow_origins = ["*"],
                   allow_credentials = True,
                   allow_methods = ["*"],
                   allow_headers = ["*"],
                   )

#To load the model once the API starts and avoid loading everytime a prediction is made
@app.on_event("startup")
async def startup_event():
    load_model_once()
    print ("API ready!")

 #To check if the API is running
@app.get("/health")
def health():
    return{"status": "healthy"}

#Prediction Endpoint
@app.post("/predict")
async def predict_endpoint(file: UploadFile = File(...)):
    #Step 1: Validate it's an image
    if not file.content_type.startswith("image/"):
        raise HTTPException(400, "File must be an image")

    #Step 2: Read and upload file
    contents = await file.read()
    image = Image.open(io.BytesIO(contents))

    #Step 3: Convert to RGB (just in case)
    if image.mode != 'RGB':
        image = image.convert('RGB')

    #Step 4: Convert to numpy array for the model
    image_array = np.array(image)

    #Step 5: Get prediction from the model
    result = predict(image_array)

    #Step 6: Return the result as JSON
    return JSONResponse(content = result)
