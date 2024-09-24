import os
import requests

def post_images(files):
	url = "http://localhost/upload/"

	images_subset = [name for name in files if ".jpeg" in name]

	# POST image files.
	for image in images_subset:
		with open(image, 'rb') as opened:
			r = requests.post(url, files={'file': opened})


if __name__ == "__main__":
	# Change to images directory
	os.chdir("supplier-data/images")
	# Get file names
	files = os.listdir()

	post_images(files)
