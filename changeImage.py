import os
from PIL import Image
#import subprocess


def edit_images(files):
	# Verificar la extension de los archivos!!!
	images_subset = [name for name in files if ".tiff" in name]
	#images_subset = files

	# Process image files.
	for image in images_subset:
		new_name = "{}.jpeg".format(image.replace(".tiff", ""))

		im = Image.open(image)
		im = im.convert('RGB')
		im = im.resize((600,400)).save(new_name)


if __name__ == "__main__":
	# Change to images directory
	os.chdir("supplier-data/images")
	# Get file names
	files = os.listdir()

	edit_images(files)
