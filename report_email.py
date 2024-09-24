import datetime
import os
import emails
import reports


def process_description_files(file_list):
	# The keys are: name, weight, description, image_name
	desc_list = []

	# Iterate through list of files.
	for filename in file_list:
		with open(filename, "r") as file:
			desc = {}
			desc['name'], desc['weight'], _, _ = file.read().split('\n')

		desc_list.append(desc)

	return desc_list


def main(data):
	now = datetime.datetime.now()
	title = "Processed Update on " + now.strftime("%B %d, %Y")

	fruits = ""

	for item in data:
		fruits += "name: " + item['name'] + "<br/>" + "weight: " + item['weight'] + "<br/><br/>"


	#reports.generate_report("/tmp/processed.pdf", title, )
	reports.generate_report("processed.pdf", title, fruits)


	# send the PDF report as an email attachment
	sender = "automation@example.com"
	receiver = "student@example.com"
	subject = "Upload Completed - Online Fruit Store"
	body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
	message = emails.generate_email(sender, receiver, subject, body, "/tmp/processed.pdf")
	emails.send_email(message)


if __name__ == "__main__":
	# Get list of description files.
	os.chdir("supplier-data/descriptions")
	file_list = os.listdir()

	# Process all description files.
	result = process_description_files(file_list)

	main(result)
