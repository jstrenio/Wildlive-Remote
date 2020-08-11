# Hafner 2020

import smtplib

import re

from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

USERNAME = "wildlife.remote.r@gmail.com"
PASSWORD = "uV%Ku@]L8j_~'7Cg"

ADDRESS = "wildlife.remote.r@gmail.com"

FAIL = -1

def get_picture(picture_file_name):
	picture_file = open(picture_file_name, 'rb')
	picture = picture_file.read()
	picture_file.close()
	return picture


def send_mail(picture_path, text_string):
	to_address = get_email(text_string)
	if to_address == FAIL:
		return
	picture = get_picture(picture_path)
	m = MIMEMultipart()
	m["To"] = to_address
	m["From"] = USERNAME
	m["Subject"] = "Wildlife Remote"
	m.attach(MIMEImage(picture))

	s = smtplib.SMTP(host='smtp.gmail.com', port=587)
	s.starttls()

	s.login(USERNAME, PASSWORD)

	s.send_message(m)
	s.quit()


def get_email(string):
	"""  decided to use regular expression instead
	using help from: "https://docs.python.org/3/library/re.html" and
	"https://stackoverflow.com/questions/17681670/extract-email-sub-strings-from-large-document"""""
	email = re.search(r'[\w\.-]+@[\w\.-]+\.\w+', string)
	if email is None:
		return FAIL
	return email[0]
