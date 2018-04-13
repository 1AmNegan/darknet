from PIL import Image
import sys

if len(sys.argv) < 2:
    print ("Please provide image as argumant")
    exit(1)

try:
    f = open("bbox.txt", "r");
except FileNotFoundError:
    print ("bbox.txt File does not exist");
    exit(1)

left = int(f.readline())
top = int(f.readline())
right = int(f.readline())
bottom = int(f.readline())

img = Image.open(sys.argv[1])
img2 = img.crop((left, top, right, bottom))
# img2 = img.crop((634, 430, 698, 490))
img2.save("corpped_img.jpg")
