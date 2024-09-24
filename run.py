import json
import os
import requests


def process_description_files(file_list):
	# The keys are: name, weight, description, image_name
	desc_list = []

	# Iterate through list of files.
	for filename in file_list:
		with open(filename, "r") as file:
			desc = {}
			desc['name'], desc['weight'], desc['description'], _ = file.read().split('\n')
			desc['weight'] = int(desc['weight'].replace(" lbs", ""))
			desc['image_name'] = filename.replace(".txt", ".jpeg")


		desc_list.append(desc)






	# Iterate through list of descriptions and POST everyone.
	for description in desc_list:
		# Into a JSON stream.
		json_desc = json.dumps(description)
		# json_desc = description

		print(json_desc)

		#curl -X POST -d '{"id": 37, "name": "Item7"}' -H "Content-Type: application/json" http://127.0.0.1:5000/elements

		#response = requests.post(r"http://[external-IP-address]/fruits", json=json_desc)


		#response = requests.get(r'http://34.139.22.221')

		#print("response ok: {}".format(response.ok))
		#print("response return code: {}".format(response.status_code))



if __name__ == "__main__":
	# Get list of description files.
	os.chdir("supplier-data/descriptions")
	file_list = os.listdir()

	# Process all description files.
	result = process_description_files(file_list)







student@6a887ba59018:~$ cat  ~/run.py
#! /usr/bin/env python3

import json
import os
import requests


def process_description_files(file_list):
        desc_list = []
        files_subset = [name for name in file_list if ".txt" in name]

        for filename in files_subset:
                with open(filename, "r") as file:
                        desc = {}
                        line = file.readline()
                        desc['name'] = line.strip()
                        line = file.readline()
                        desc['weight'] = int(line.strip().replace(" lbs", ""))
                        line = file.readline()
                        desc['description'] = line.strip()
                        #desc['name'], desc['weight'], desc['description'] = line.split('\n')
                        #desc['weight'] = int(desc['weight'].replace(" lbs", ""))
                        desc['image_name'] = filename.replace(".txt", ".jpeg")

                desc_list.append(desc)

        for description in desc_list:
                json_desc = json.dumps(description)

                print(json_desc)

                response = requests.post(r"http://35.233.176.36/fruits", json=json_desc)

                print("response ok: {}".format(response.ok))
                print("response return code: {}".format(response.status_code))

        return desc_list


if __name__ == "__main__":
        os.chdir("supplier-data/descriptions")
        file_list = os.listdir()

        result = process_description_files(file_list)

student@6a887ba59018:~$ 
