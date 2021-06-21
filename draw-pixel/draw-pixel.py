from PIL import Image

im = Image.new(mode="RGBA", size=(50,50), color=(255,255,255,255))
im.putpixel((25,25), (0,0,0,255))
im.show()
im.save("pixel.png")