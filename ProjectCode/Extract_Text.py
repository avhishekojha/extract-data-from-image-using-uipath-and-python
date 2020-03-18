import sys
import os

from PIL import Image

import pytesseract

from pytesseract import image_to_string

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
 
def image_without_blur(FileName):
    text = str(((image_to_string(Image.open(FileName)))))
    return text

if __name__ == '__main__':
    print(image_without_blur('New1.jpg'))