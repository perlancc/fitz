from rembg import remove
from PIL import Image
from pillow_heif import register_heif_opener

# testing the rembg library to remove the background of an image
#
#    input_path = '/Users/perla/fitz/backend/test.png'
   # output_path = '/Users/perla/fitz/backend/output.png'

   # input = Image.open('/Users/perla/fitz/backend/test.png')
  #  output = remove(input)
   # output.save('/Users/perla/fitz/backend/output.png')

# testing heic background removal using pillow-heif library
register_heif_opener()

#pil_image = Image.open("IMG_9180.HEIC")  
#output = remove(pil_image)
#output.save('output.png')

pil_image = Image.open("/Users/perla/fitz/backend/IMG_9181.HEIC")  
output = remove(pil_image)
output.save('output.png')


