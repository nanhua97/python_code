from PIL import Image,ImageFilter

im = Image.open('test.jpg')
im2 = im.filter(ImageFilter.BLUR)
im2.save('vlur.jpg','jpeg')
