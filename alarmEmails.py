import email.message
import mimetypes
import os.path
import smtplib


def generate_email(sender, recipient, subject, body):
	# Basic Email formatting
	message = email.message.EmailMessage()
	message["From"] = sender
	message["To"] = recipient
	message["Subject"] = subject
	message.set_content(body)

	return message


def send_email(message):
	#Sends the message to the configured SMTP server.
	mail_server = smtplib.SMTP('localhost')
	mail_server.send_message(message)
	mail_server.quit()
