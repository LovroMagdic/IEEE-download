import cv2
import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Input
from sklearn.model_selection import train_test_split

def preprocess_image(image_path):
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image = cv2.resize(image, (IMG_WIDTH, IMG_HEIGHT))
    image = image / 255.0  # Normalize pixel values to [0, 1]
    return image.reshape((IMG_HEIGHT, IMG_WIDTH, CHANNELS))

def create_cnn_model(input_shape):
    inputs = Input(shape=input_shape)

    # Convolutional layers
    x = Conv2D(128, (3, 3), activation='relu')(inputs)
    x = MaxPooling2D(pool_size=(2, 2))(x)

    x = Conv2D(64, (3, 3), activation='relu')(x)
    x = MaxPooling2D(pool_size=(2, 2))(x)

    x = Flatten()(x)

    # Two separate output layers for n1 and n2
    output_n1 = Dense(1, activation='linear', name='n1')(x)
    output_n2 = Dense(1, activation='linear', name='n2')(x)

    # Define the model
    model = Model(inputs=inputs, outputs=[output_n1, output_n2])
    return model

# Load the CSV file
data = pd.read_csv("./CNN/dataset/labels.csv", delimiter='|')
# Example: (filename, output)
# "image1.jpg", "Showing 1-25 of 3,256 res"

# Image size (height, width, channels)
IMG_HEIGHT = 50
IMG_WIDTH = 450
CHANNELS = 1

# Prepare data arrays
X = []
y_n1 = []
y_n2 = []

# Extract features and labels
for _, row in data.iterrows():
    image_path = row['path']
    text = row['label']
    
    # Preprocess image
    image = preprocess_image(image_path)
    X.append(image)
    
    # Extract the numbers from the text (e.g., "Showing 1-25 of 3,256 res")
    n1 = int(text.split(' ')[1].split('-')[1])  # Extract "25"
    n2 = int(text.split(' ')[3].replace(',', ''))  # Extract "3,256"

    y_n1.append(n1/100)
    y_n2.append(n2/10000)

# Convert to NumPy arrays
X = np.array(X)
y_n1 = np.array(y_n1)
y_n2 = np.array(y_n2)


# Create the model
input_shape = (IMG_HEIGHT, IMG_WIDTH, CHANNELS)
model = create_cnn_model(input_shape)

# Compile the model
model.compile(optimizer='adam', loss=['mae', 'mae'], metrics=[['mae'], ['mae']])

# Print model summary
model.summary()

# Split the data
X_train, X_val, y_n1_train, y_n1_val, y_n2_train, y_n2_val = train_test_split(X, y_n1, y_n2, test_size=0.2, random_state=42)

# Train the model
history = model.fit(
    X_train,
    {'n1': y_n1_train, 'n2': y_n2_train},
    validation_data=(X_val, {'n1': y_n1_val, 'n2': y_n2_val}),
    batch_size=32,
    epochs=30
)

# Evaluate the model
loss, n1_loss, n2_loss, n1_mae, n2_mae = model.evaluate(X_val, {'n1': y_n1_val, 'n2': y_n2_val})
print(f"Validation MAE for n1: {n1_mae:.2f}, n2: {n2_mae:.2f}")

# save model
model.save('my_cnn_model.keras')

# Make predictions
predictions = model.predict(X_val)

# Display some predictions
for i in range(5):
    true_n1 = y_n1_val[i] * 100  # Reverse scaling for n1
    pred_n1 = predictions[0][i][0] * 100  # Reverse scaling for predicted n1
    
    true_n2 = y_n2_val[i] * 10000  # Reverse scaling for n2
    pred_n2 = predictions[1][i][0] * 10000  # Reverse scaling for predicted n2

    print(f"True n1: {true_n1}, Predicted n1: {pred_n1:.2f}")
    print(f"True n2: {true_n2}, Predicted n2: {pred_n2:.2f}")
    print()

