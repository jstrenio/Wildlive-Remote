# return message functionality using
# Hafner, Devi, Strenio 2020


import smtplib
import re

from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

USERNAME = "wildlife.remote.r@gmail.com"
#USERNAME = "wildlive@att.net"
PASSWORD = "uV%Ku@]L8j_~'7Cg" 
#PASSWORD = "opensource2020"

ADDRESS = "wildlife.remote.r@gmail.com"

FAIL = -1

def get_picture(picture_file_name):
	picture_file = open(picture_file_name, 'rb')
	picture = picture_file.read()
	picture_file.close()
	return picture


def send_mail(picture_path, text_string):
	print("sending email")
	to_address = get_email(text_string)
	if to_address == FAIL:
		return
	picture = get_picture(picture_path)

	m = MIMEMultipart()
	m["To"] = to_address
	m["From"] = USERNAME
	m["Subject"] = "Wildlife Remote"
	m.attach(MIMEImage(picture))
	print("photo attached")

	s = smtplib.SMTP(host='smtp.gmail.com', port=587)
	#s = smtplib.SMTP(host='smtp.mail.att.net', port=465)
	s.ehlo()
	s.starttls()

	s.login(USERNAME, PASSWORD)
	print("email successfully logged in")
	s.send_message(m)
	s.quit()
	print("email sent")


def get_email(string):
	#regular expression modeled from: "https://docs.python.org/3/library/re.html" and
	#https://stackoverflow.com/questions/17681670/extract-email-sub-strings-from-large-document
	#email = re.search(r'[\w\.-]+@[\w\.-]+\.\w+', string)
	parsed_string = string.split(',')
	email = parsed_string[1]
	if email is None:
		return FAIL
	return email
