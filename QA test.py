import cv2 
import pytesseract

# this could be used for QA of annotated images

image = "3D modeling and simulation.png"
pytesseract.pytesseract.tesseract_cmd = r'/opt/homebrew/Cellar/tesseract/5.3.0_1/bin/tesseract'
string = pytesseract.image_to_string(image)

print(string)