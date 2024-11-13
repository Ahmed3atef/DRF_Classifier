import tensorflow as tf

# Load the trained model from the .h5 file
model = tf.keras.models.load_model('cat_dog_classifier.h5')

# Verify that the model is loaded
model.summary()

