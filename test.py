from PIL import Image
import numpy as np

# Load the image
image = Image.open("3D modeling and simulation.png")

# Convert the image to a NumPy array
image_array = np.array(image)

# Check the shape of the array
print(image_array.shape)