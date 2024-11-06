from PIL import Image
from pytesseract import pytesseract

# Load the image from file
image = Image.open('/Users/surajkhopkar/Downloads/english/Mobile_Photos/MobPhoto_1.jpg')

# Perform OCR on the image
text = pytesseract.image_to_string(image)

# Print the extracted text
print(text)