import tesserocr
from PIL import Image


print(tesserocr.tesseract_version())
print(tesserocr.get_languages())

image=Image .open('code.png')
result=tesserocr .image_to_text(image ,lang='kor')
print(result )

