import mechanize
import hashlib
import urllib
import os
import time
import random

username = 'USERNAME'
password = hashlib.md5('PASSWORD') #replace with md5 hash of your pwd if you don't want to save it in plain text
minimum_delay = 10 #in minutes
maximum_delay = 45
avatar_directory = './avatars'

def login():
	parameters = {
		'vb_login_username': username,
		'vb_login_md5password': password,
		'do': 'login'
	}
	data = urllib.urlencode(parameters)
	response = browser.open('http://facepunch.com/login.php',data)
	print response.readlines()

def switch():
	browser.open('http://facepunch.com/profile.php?do=editavatar')
	browser.select_form(nr=0)
	if browser.form['vb_login_username']:
		print 'Logging in...'
		login()
		switch()
	else:
		new_avatar = random.choice(os.listdir(avatar_directory))
		browser.find_control('upload').add_file(open(new_avatar))
		browser.submit()

browser = mechanize.Browser()

while True:
	switch()
	time.sleep(random.randrange(minimum_delay, maximum_delay))
