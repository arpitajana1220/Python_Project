# Import the required libraries
import pytesseract
from PIL import Image

#Including this because tesseract is not added to the path 
pytesseract.pytesseract.tesseract_cmd = r"C:\Users\Admin\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"

# Load the image
img = Image.open(r"C:\Users\Admin\Pictures\Camera Roll\Screenshots\Screenshot (47).png")

# Convert the image to text
text = pytesseract.image_to_string(img)

# Print the extracted text
print(text)