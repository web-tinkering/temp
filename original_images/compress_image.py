import os
from PIL import Image
from tqdm import tqdm

dir_name = "images"

if not os.path.isdir(dir_name):
	os.makedirs(dir_name)

def compress(img):
	output = os.path.abspath(dir_name + os.sep + img)
	if os.path.isfile(output):
		os.remove(output)
	img = Image.open(os.path.abspath(img))
	img.save(output, optimize=True, quality=50)

for item in tqdm(os.listdir(".")):
	if item.endswith(".jpg"):
		compress(item)