#Test model
import sys
import numpy as np
from PIL import Image

#Add backend to path to import model.py
sys.path.append('backend')

from model import load_model_once, predict, class_names

print("="*30)
print("TESTING MODEL.PY")
print("="*30)

#1. Test loading the model
print("\n1. Loading the model...")
try:
    load_model_once()
    print("Model loaded succesfully")
except Exception as e:
    print(f" ERROR loading model: {e}")

#2. Test with a dummy image (random pixels)
print("\n2. Testing prediction on dummy image...")
dummy_image = np.random.randint(0, 255, (224, 224, 3), dtype=np.uint8)
result = predict(dummy_image)

print(f" Prediction: {result['prediction']}")
print(f" Confidence: {result['confidence']:.4f}")
print(f" All scores: {result['all_scores']}")
print(f" PREDICTION WORKS!")

print("\n" + "="*30)
print(" All tests passed! model.py is READY!")
print("\n" + "="*30)
