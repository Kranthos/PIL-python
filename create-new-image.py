from PIL import Image

im = Image.new(mode="RGBA", size=(2160, 1440), color=(255,255,255,255))
im.show()
im.save("blankImage.png")