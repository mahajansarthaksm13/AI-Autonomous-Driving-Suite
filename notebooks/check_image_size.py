from PIL import Image
from pathlib import Path

img = Image.open("datasets/Images/00000000.jpg")

print("Image Size:", img.size)