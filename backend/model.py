#Backend/model.py
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
import os

#Global variables
model = None
class_names = ['Cyst', 'Normal', 'Stone', 'Tumor']
input_size = (224, 224)

def load_model_once():
    """
    Load the trained model
    """
    global model

    #Model path
    model_path = os.path.join(os.path.dirname(__file__), '..', 'model', 'custom_cnn_kidney_model.h5')

    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Model not found at {model_path}")

    model = load_model(model_path)
    print(f"Model loaded from {model_path}")
    return model

def preprocess_image(image_array):
    """
    Preprocess image for model input
    """
    #Resize
    image = tf.image.resize(image_array, input_size)

    #Normalize to 0-1
    image = image / 255.0

    #Add batch dimension
    image = np.expand_dims(image, axis=0)
    return image

def predict(image_array):
    """
    Run prediction on image array
    """
    global model
    if model is None:
        load_model_once()

    processed = preprocess_image(image_array)
    predictions = model.predict(processed, verbose=0)[0]
    class_idx = np.argmax(predictions)
    confidence = float(predictions[class_idx])

    return {
        'prediction': class_names[class_idx],
        'confidence': confidence,
        'all_scores': {
            'Cyst': float(predictions[0]),
            'Normal': float(predictions[1]),
            'Stone': float(predictions[2]),
            'Tumor':float(predictions[3])
        }
    }
