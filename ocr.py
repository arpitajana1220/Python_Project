# Import the required libraries
import pytesseract
from PIL import Image

#Including this because tesseract is not added to the path 
pytesseract.pytesseract.tesseract_cmd = r"C:\Users\Admin\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"

# Load the image
img = Image.open(r"C:\Users\Admin\Pictures\Papa hisaab dataset\1 (1).jpg")

# Convert the image to text
text = pytesseract.image_to_string(img)

# extracting text into variable
purity = text[108:129]
net_wt = text[162:165] +" : "+ text[170:177]
gross_wt = text[141:154]+ text[155:161]
voucher = text[26:43]
Date = text[55:74]

#printing extracted text 
print(Date,end = " ")
print(voucher,end = "")
print(purity,end = "")
print(gross_wt)
print()
print(net_wt)
