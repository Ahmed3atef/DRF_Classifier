import os
import tensorflow as tf
from tensorflow.keras.preprocessing import image
from django.conf import settings
import numpy as np

# Load the model once when the server starts
MODEL_PATH = os.path.join(settings.BASE_DIR, 'models', 'cat_dog_classifier.h5')
model = tf.keras.models.load_model(MODEL_PATH)

def trained_model(image_uploaded):
    image_path = image_uploaded
    
    # Process the image and predict
    img = image.load_img(image_path, target_size=(224, 224))
    img_array = image.img_to_array(img) / 255.0 
    img_array = np.expand_dims(img_array, axis=0)

    prediction = model.predict(img_array)
    
    # Get the predicted class index and name
    class_index = np.argmax(prediction, axis=1)[0]
    class_names = ['cat', 'dog', 'other']
    classify = class_names[class_index]
    
    # Get the confidence of the prediction
    confidence = prediction[0][class_index]
    
    if confidence < 0.8 :
        # Return structured response
        result = {
            "class": "i'm Not sure",
            "confidence": f"{confidence * 100:.2f}%"
        }
    else:
        # Return structured response
        result = {
            "class": classify,
            "confidence": f"{confidence * 100:.2f}%"
        }
    return result
