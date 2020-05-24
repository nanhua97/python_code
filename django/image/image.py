from PIL import Image
im = Image.open('QJ6676994451.jpg')
w,h = im.size
print(w,h)
im.thumbnail((w//1.5,h//1.5))
print(w//1.5,h//1.5)
im.save('test.jpg','jpeg')
