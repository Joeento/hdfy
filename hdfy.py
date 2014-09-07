from PIL import Image


im = Image.open("pics/donottouch.jpg")
pixels = im.load()
print(pixels[0,0])
