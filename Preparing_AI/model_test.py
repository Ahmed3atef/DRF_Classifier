from tensorflow.keras.preprocessing import image
import tensorflow as tf
import numpy as np

# Function to preprocess and classify a new image
def classify_image(img_path):
    # Load the image, resize it, and convert to array
    img = image.load_img(img_path, target_size=(224, 224))
    img_array = image.img_to_array(img) / 255.0  # Normalize the image

    # Add batch dimension to match model input
    img_array = np.expand_dims(img_array, axis=0)

    # Predict the class of the image
    model = tf.keras.models.load_model('# path to the .h5 file')
    prediction = model.predict(img_array)

    # Get the class index with the highest probability
    class_index = np.argmax(prediction, axis=1)[0]
    class_names = ['cat', 'dog']  # Adjust this list if you have 'neither'

    return class_names[class_index], prediction[0][class_index]

# Test the model on a new image
img_path = "# path to the image"  # Path to the image you want to test
label, confidence = classify_image(img_path)

print(f"The image is classified as a '{label}' with a confidence of {confidence*100:.2f}%")
