import os
from PIL import Image

# Change directory to where images are located
os.chdir('R:\\Images') 

path = "\\read path\\"
dst = "\\write path\\"
current_dir = os.getcwd()

images = os.listdir(current_dir+path)

for img in images:
    # Open image file
    im = Image.open(current_dir+path+img)

    # Resize image to 224x224 pixels
    resized_im = im.resize((224, 224))

    # Convert image to JPEG format
    jpg_im = resized_im.convert("RGB")

    # Save the converted image with the same file name
    jpg_im.save(fp=current_dir+dst+img[:-4]+'.jpg', format='jpeg')

