from PIL import Image

try:
    f = open("bbox.txt", "r");
except FileNotFoundError:
    print ("File does not exist");
    exit(1)

left = int(f.readline())
top = int(f.readline())
right = int(f.readline())
bottom = int(f.readline())

img = Image.open("predictions.png")
img2 = img.crop((left, top, right, bottom))
img2.save("corpped_img.jpg")
